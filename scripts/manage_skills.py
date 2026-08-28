#!/usr/bin/env python3
"""Validate and install skills from this canonical personal repository."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
TESTS_ROOT = REPO_ROOT / "tests"
CATALOG_PATH = REPO_ROOT / "SKILLS_INDEX.yaml"
CATALOG_MARKDOWN_PATH = REPO_ROOT / "SKILLS_INDEX.md"
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
VERSION_RE = re.compile(
    r"^Skill version: `([0-9]+\.[0-9]+\.[0-9]+(?:[-+][0-9A-Za-z.-]+)?)`$",
    re.MULTILINE,
)
ROUTING_CLASSES = {"cross-cutting", "task-specific"}
LIFECYCLE_STATUSES = {"maintained", "experimental", "retired"}
INVOCATION_POLICIES = {"implicit", "explicit-only"}
FORBIDDEN_SKILL_AUXILIARY = {
    "CHANGELOG.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "README.md",
}
IGNORED_SCAN_DIRECTORIES = {".git", ".venv", "__pycache__"}
IGNORED_SCAN_SUFFIXES = {
    ".db",
    ".gif",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".pyc",
    ".sqlite",
    ".webp",
}
REPOSITORY_SECRET_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
)


class RepositoryValidationError(RuntimeError):
    """Raised when repository or installation state violates a mechanical rule."""


@dataclass(frozen=True, slots=True)
class SkillMetadata:
    name: str
    description: str
    version: str
    root: Path


@dataclass(frozen=True, slots=True)
class SkillCatalogEntry:
    name: str
    path: str
    routing_class: str
    lifecycle_status: str
    invocation_policy: str
    use_when: tuple[str, ...]
    not_for: tuple[str, ...]
    composes_with: tuple[str, ...]


def parse_skill_metadata(skill_root: Path) -> SkillMetadata:
    skill_md = skill_root / "SKILL.md"
    try:
        text = skill_md.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise RepositoryValidationError(f"cannot read {skill_md}: {exc}") from exc

    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise RepositoryValidationError(f"{skill_md} must begin with YAML frontmatter")
    try:
        closing = lines.index("---", 1)
    except ValueError as exc:
        raise RepositoryValidationError(f"{skill_md} has no closing frontmatter marker") from exc

    try:
        values = yaml.safe_load("\n".join(lines[1:closing]))
    except yaml.YAMLError as exc:
        raise RepositoryValidationError(f"invalid YAML frontmatter in {skill_md}: {exc}") from exc
    if not isinstance(values, dict):
        raise RepositoryValidationError(f"{skill_md} frontmatter must be a mapping")

    expected_keys = {"name", "description"}
    if set(values) != expected_keys:
        raise RepositoryValidationError(
            f"{skill_md} frontmatter keys must be exactly name and description"
        )
    name = values["name"]
    description = values["description"]
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        raise RepositoryValidationError(f"invalid skill name: {name}")
    if not isinstance(description, str) or not description.strip():
        raise RepositoryValidationError(f"{skill_md} description must be non-empty text")
    if name != skill_root.name:
        raise RepositoryValidationError(
            f"skill folder {skill_root.name} does not match frontmatter name {name}"
        )
    if len(lines) > 500:
        raise RepositoryValidationError(f"{skill_md} exceeds the 500-line authoring budget")
    version_matches = VERSION_RE.findall(text)
    if len(version_matches) != 1:
        raise RepositoryValidationError(
            f"{skill_md} must contain exactly one semantic Skill version marker"
        )
    return SkillMetadata(name, description, version_matches[0], skill_root)


def discover_skills() -> list[Path]:
    if not SKILLS_ROOT.is_dir():
        raise RepositoryValidationError(f"missing skills directory: {SKILLS_ROOT}")
    skill_roots: list[Path] = []
    for path in sorted(SKILLS_ROOT.iterdir(), key=lambda item: item.name):
        if path.name.startswith("."):
            continue
        if path.is_symlink() or not path.is_dir():
            raise RepositoryValidationError(
                f"canonical skills must be real directories: {path}"
            )
        if not (path / "SKILL.md").is_file():
            raise RepositoryValidationError(f"skill directory lacks SKILL.md: {path}")
        skill_roots.append(path)
    if not skill_roots:
        raise RepositoryValidationError("no skills found")
    return skill_roots


def require_string_list(
    value: object,
    *,
    field: str,
    allow_empty: bool = False,
) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise RepositoryValidationError(f"catalog field {field} must be a list")
    if not allow_empty and not value:
        raise RepositoryValidationError(f"catalog field {field} must not be empty")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise RepositoryValidationError(
            f"catalog field {field} must contain only non-empty text"
        )
    if len(value) != len(set(value)):
        raise RepositoryValidationError(f"catalog field {field} contains duplicates")
    return tuple(value)


def expected_invocation_policy(skill_root: Path) -> str:
    agent_metadata = skill_root / "agents/openai.yaml"
    if not agent_metadata.is_file():
        return "implicit"
    try:
        values = yaml.safe_load(agent_metadata.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        raise RepositoryValidationError(
            f"cannot parse invocation policy in {agent_metadata}: {exc}"
        ) from exc
    if not isinstance(values, dict):
        raise RepositoryValidationError(f"{agent_metadata} must contain a mapping")
    policy = values.get("policy", {})
    if not isinstance(policy, dict):
        raise RepositoryValidationError(f"{agent_metadata} policy must be a mapping")
    allow_implicit = policy.get("allow_implicit_invocation", True)
    if not isinstance(allow_implicit, bool):
        raise RepositoryValidationError(
            f"{agent_metadata} allow_implicit_invocation must be true or false"
        )
    return "implicit" if allow_implicit else "explicit-only"


def load_skill_catalog(
    metadata_items: list[SkillMetadata] | None = None,
) -> list[SkillCatalogEntry]:
    if metadata_items is None:
        metadata_items = [validate_skill(root) for root in discover_skills()]
    metadata_by_name = {metadata.name: metadata for metadata in metadata_items}

    try:
        values = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
        raise RepositoryValidationError(f"cannot parse {CATALOG_PATH}: {exc}") from exc
    if not isinstance(values, dict):
        raise RepositoryValidationError(f"{CATALOG_PATH} must contain a mapping")
    if set(values) != {"schema_version", "role", "skills"}:
        raise RepositoryValidationError(
            f"{CATALOG_PATH} keys must be exactly schema_version, role, and skills"
        )
    if values["schema_version"] != 1:
        raise RepositoryValidationError("skill catalog schema_version must be 1")
    if values["role"] != "routing_read_model":
        raise RepositoryValidationError("skill catalog role must be routing_read_model")
    raw_skills = values["skills"]
    if not isinstance(raw_skills, dict):
        raise RepositoryValidationError("skill catalog skills must be a mapping")

    catalog_names = set(raw_skills)
    discovered_names = set(metadata_by_name)
    if catalog_names != discovered_names:
        missing = sorted(discovered_names - catalog_names)
        extra = sorted(catalog_names - discovered_names)
        raise RepositoryValidationError(
            f"skill catalog coverage differs from skills/: missing={missing}, extra={extra}"
        )

    entries: list[SkillCatalogEntry] = []
    expected_keys = {
        "path",
        "routing_class",
        "lifecycle_status",
        "invocation_policy",
        "use_when",
        "not_for",
        "composes_with",
    }
    for name in sorted(raw_skills):
        raw_entry = raw_skills[name]
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            raise RepositoryValidationError(f"invalid catalog skill name: {name}")
        if not isinstance(raw_entry, dict) or set(raw_entry) != expected_keys:
            raise RepositoryValidationError(
                f"catalog entry {name} keys must be exactly {', '.join(sorted(expected_keys))}"
            )
        expected_path = f"skills/{name}"
        if raw_entry["path"] != expected_path:
            raise RepositoryValidationError(
                f"catalog entry {name} path must be {expected_path}"
            )
        routing_class = raw_entry["routing_class"]
        lifecycle_status = raw_entry["lifecycle_status"]
        invocation_policy = raw_entry["invocation_policy"]
        if routing_class not in ROUTING_CLASSES:
            raise RepositoryValidationError(
                f"catalog entry {name} has invalid routing_class {routing_class}"
            )
        if lifecycle_status not in LIFECYCLE_STATUSES:
            raise RepositoryValidationError(
                f"catalog entry {name} has invalid lifecycle_status {lifecycle_status}"
            )
        if invocation_policy not in INVOCATION_POLICIES:
            raise RepositoryValidationError(
                f"catalog entry {name} has invalid invocation_policy {invocation_policy}"
            )
        expected_policy = expected_invocation_policy(metadata_by_name[name].root)
        if invocation_policy != expected_policy:
            raise RepositoryValidationError(
                f"catalog entry {name} invocation_policy is {invocation_policy}; "
                f"agents/openai.yaml resolves to {expected_policy}"
            )
        use_when = require_string_list(
            raw_entry["use_when"], field=f"{name}.use_when"
        )
        not_for = require_string_list(raw_entry["not_for"], field=f"{name}.not_for")
        composes_with = require_string_list(
            raw_entry["composes_with"],
            field=f"{name}.composes_with",
            allow_empty=True,
        )
        unknown_relations = set(composes_with) - discovered_names
        if unknown_relations:
            raise RepositoryValidationError(
                f"catalog entry {name} composes_with unknown skills: "
                f"{sorted(unknown_relations)}"
            )
        if name in composes_with:
            raise RepositoryValidationError(
                f"catalog entry {name} must not compose with itself"
            )
        entries.append(
            SkillCatalogEntry(
                name=name,
                path=expected_path,
                routing_class=routing_class,
                lifecycle_status=lifecycle_status,
                invocation_policy=invocation_policy,
                use_when=use_when,
                not_for=not_for,
                composes_with=composes_with,
            )
        )
    return entries


def render_catalog_markdown(
    entries: list[SkillCatalogEntry],
    metadata_items: list[SkillMetadata],
) -> str:
    metadata_by_name = {metadata.name: metadata for metadata in metadata_items}
    lines = [
        "# Custom Skill Index",
        "",
        "This human-readable view is derived from `SKILLS_INDEX.yaml` and the version "
        "markers in each `SKILL.md`. Run `.venv/bin/python scripts/manage_skills.py "
        "catalog --check` to detect drift.",
        "",
        "The catalog routes and explains repository-owned skills. It does not install a "
        "skill, force platform invocation, or grant task authority. Runtime availability "
        "depends on the current installation; implicit invocation depends on each skill's "
        "metadata and semantic match.",
        "",
        "| Skill | Version | Routing class | Lifecycle | Invocation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        metadata = metadata_by_name[entry.name]
        lines.append(
            f"| `{entry.name}` | `{metadata.version}` | `{entry.routing_class}` | "
            f"`{entry.lifecycle_status}` | `{entry.invocation_policy}` |"
        )
    for entry in entries:
        metadata = metadata_by_name[entry.name]
        lines.extend(
            [
                "",
                f"## `{entry.name}`",
                "",
                metadata.description,
                "",
                f"- Source: `{entry.path}/SKILL.md`",
                "- Use when:",
            ]
        )
        lines.extend(f"  - {item}" for item in entry.use_when)
        lines.append("- Do not route for:")
        lines.extend(f"  - {item}" for item in entry.not_for)
        composed = ", ".join(f"`{name}`" for name in entry.composes_with) or "none"
        lines.append(f"- Common composition: {composed}")
    lines.extend(
        [
            "",
            "## Live Installation State",
            "",
            "Installation is deliberately not stored in this index because it can change "
            "independently of Git. Inspect it with:",
            "",
            "```bash",
            ".venv/bin/python scripts/manage_skills.py list",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def validate_skill_catalog(metadata_items: list[SkillMetadata]) -> list[SkillCatalogEntry]:
    entries = load_skill_catalog(metadata_items)
    expected_markdown = render_catalog_markdown(entries, metadata_items)
    try:
        actual_markdown = CATALOG_MARKDOWN_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise RepositoryValidationError(
            f"cannot read {CATALOG_MARKDOWN_PATH}: {exc}"
        ) from exc
    if actual_markdown != expected_markdown:
        raise RepositoryValidationError(
            "SKILLS_INDEX.md has drifted from SKILLS_INDEX.yaml or SKILL.md metadata"
        )
    return entries


def compile_python(path: Path) -> None:
    try:
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")
    except (OSError, UnicodeDecodeError, SyntaxError) as exc:
        raise RepositoryValidationError(f"Python validation failed for {path}: {exc}") from exc


def validate_skill(skill_root: Path) -> SkillMetadata:
    metadata = parse_skill_metadata(skill_root)
    for path in skill_root.rglob("*"):
        if path.is_symlink():
            raise RepositoryValidationError(f"canonical skill contains a symlink: {path}")
    forbidden = FORBIDDEN_SKILL_AUXILIARY.intersection(
        path.name for path in skill_root.iterdir() if path.is_file()
    )
    if forbidden:
        names = ", ".join(sorted(forbidden))
        raise RepositoryValidationError(
            f"{skill_root} contains repository documentation inside the runtime package: {names}"
        )
    for script in sorted(skill_root.rglob("*.py")):
        compile_python(script)
    return metadata


def validate_repository_secrets() -> None:
    for directory, names, filenames in os.walk(REPO_ROOT):
        names[:] = [name for name in names if name not in IGNORED_SCAN_DIRECTORIES]
        root = Path(directory)
        for filename in filenames:
            path = root / filename
            if filename.startswith(".env") and filename != ".env.example":
                raise RepositoryValidationError(
                    f"forbidden environment file: {path.relative_to(REPO_ROOT)}"
                )
            if path.suffix.lower() in IGNORED_SCAN_SUFFIXES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in REPOSITORY_SECRET_PATTERNS:
                if pattern.search(text):
                    raise RepositoryValidationError(
                        f"possible credential pattern in {path.relative_to(REPO_ROOT)}"
                    )


def run_skill_tests(metadata: SkillMetadata) -> int:
    test_root = TESTS_ROOT / metadata.name
    if not test_root.exists():
        return 0
    tests = sorted(test_root.glob("test_*.py"))
    for test in tests:
        result = subprocess.run(
            [sys.executable, str(test)],
            cwd=REPO_ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        if result.returncode != 0:
            raise RepositoryValidationError(
                f"regression test failed for {metadata.name}: {test.relative_to(REPO_ROOT)}"
            )
    return len(tests)


def validate_repository() -> tuple[int, int]:
    validate_repository_secrets()
    metadata_items = [validate_skill(root) for root in discover_skills()]
    validate_skill_catalog(metadata_items)
    test_count = sum(run_skill_tests(metadata) for metadata in metadata_items)
    return len(metadata_items), test_count


def tree_manifest(root: Path) -> dict[str, tuple[str, str]]:
    manifest: dict[str, tuple[str, str]] = {}
    for path in sorted(root.rglob("*")):
        relative = str(path.relative_to(root))
        if path.is_symlink():
            manifest[relative] = ("symlink", os.readlink(path))
        elif path.is_file():
            manifest[relative] = ("file", hashlib.sha256(path.read_bytes()).hexdigest())
    return manifest


def default_codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    return Path(configured).expanduser() if configured else Path.home() / ".codex"


def next_backup_path(backup_root: Path, name: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    candidate = backup_root / f"{name}-{timestamp}-pre-repository-link"
    counter = 1
    while candidate.exists() or candidate.is_symlink():
        candidate = backup_root / f"{name}-{timestamp}-{counter}-pre-repository-link"
        counter += 1
    return candidate


def require_skill(name: str) -> tuple[Path, SkillMetadata]:
    if not NAME_RE.fullmatch(name):
        raise RepositoryValidationError(f"invalid skill name: {name}")
    source = SKILLS_ROOT / name
    if not source.is_dir() or source.is_symlink():
        raise RepositoryValidationError(f"canonical skill not found: {source}")
    return source.resolve(), validate_skill(source)


def install_skill(
    name: str,
    target_root: Path,
    backup_root: Path,
    replace: bool,
) -> None:
    source, metadata = require_skill(name)
    target_root = target_root.expanduser()
    backup_root = backup_root.expanduser()
    target = target_root / name
    target_root.mkdir(parents=True, exist_ok=True)

    if target.is_symlink():
        if target.resolve(strict=False) == source:
            print(f"PASS: {name} already links to {source}")
            return
        if not replace:
            raise RepositoryValidationError(
                f"{target} points elsewhere; review it and rerun with --replace"
            )
    elif target.exists():
        if not target.is_dir():
            raise RepositoryValidationError(f"installation target is not a directory: {target}")
        if not replace:
            raise RepositoryValidationError(
                f"{target} is a real directory; rerun with --replace after reviewing it"
            )
        if tree_manifest(target) != tree_manifest(source):
            raise RepositoryValidationError(
                f"{target} differs from canonical source; preserve or reconcile it before replacement"
            )

    run_skill_tests(metadata)

    if target.is_symlink():
        prior_link = os.readlink(target)
        target.unlink()
        try:
            target.symlink_to(source, target_is_directory=True)
        except OSError:
            target.symlink_to(prior_link, target_is_directory=True)
            raise
    elif target.exists():
        backup_root.mkdir(parents=True, exist_ok=True)
        backup = next_backup_path(backup_root, name)
        shutil.move(str(target), str(backup))
        try:
            target.symlink_to(source, target_is_directory=True)
        except OSError:
            if not target.exists() and not target.is_symlink():
                shutil.move(str(backup), str(target))
            raise
        print(f"Backed up the prior identical directory to {backup}")
    else:
        target.symlink_to(source, target_is_directory=True)

    if not target.is_symlink() or target.resolve(strict=True) != source:
        raise RepositoryValidationError(f"failed to install canonical link at {target}")
    print(f"PASS: installed {name} -> {source}")


def check_installation(name: str, target_root: Path) -> None:
    source, _ = require_skill(name)
    target = target_root.expanduser() / name
    if not target.is_symlink():
        raise RepositoryValidationError(f"installation is not a symlink: {target}")
    if target.resolve(strict=False) != source:
        raise RepositoryValidationError(
            f"installation points to {target.resolve(strict=False)}; expected {source}"
        )
    print(f"PASS: {name} installation points to canonical source")


def installation_state(name: str, target_root: Path) -> str:
    source = (SKILLS_ROOT / name).resolve()
    target = target_root.expanduser() / name
    if target.is_symlink():
        return "linked" if target.resolve(strict=False) == source else "linked-elsewhere"
    if target.is_dir():
        return "directory"
    if target.exists():
        return "other"
    return "missing"


def list_skills(target_root: Path) -> None:
    metadata_items = [validate_skill(root) for root in discover_skills()]
    entries = load_skill_catalog(metadata_items)
    metadata_by_name = {metadata.name: metadata for metadata in metadata_items}
    headers = ("NAME", "VERSION", "ROUTING", "LIFECYCLE", "INVOCATION", "INSTALLATION")
    rows = [
        (
            entry.name,
            metadata_by_name[entry.name].version,
            entry.routing_class,
            entry.lifecycle_status,
            entry.invocation_policy,
            installation_state(entry.name, target_root),
        )
        for entry in entries
    ]
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]
    print("  ".join(value.ljust(widths[index]) for index, value in enumerate(headers)))
    for row in rows:
        print("  ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def check_all_installations(target_root: Path) -> None:
    metadata_items = [validate_skill(root) for root in discover_skills()]
    entries = load_skill_catalog(metadata_items)
    failures: list[str] = []
    for entry in entries:
        state = installation_state(entry.name, target_root)
        if state == "linked":
            print(f"PASS: {entry.name} installation points to canonical source")
        else:
            failures.append(f"{entry.name}={state}")
            print(f"FAIL: {entry.name} installation state is {state}", file=sys.stderr)
    if failures:
        raise RepositoryValidationError(
            "one or more canonical skills are not installed links: " + ", ".join(failures)
        )


def main(argv: list[str] | None = None) -> int:
    codex_home = default_codex_home()
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate all canonical skills and regressions")

    catalog_parser = subparsers.add_parser(
        "catalog", help="print or verify the human-readable skill catalog"
    )
    catalog_parser.add_argument("--check", action="store_true")

    list_parser = subparsers.add_parser(
        "list", help="list canonical skills and live installation state"
    )
    list_parser.add_argument("--target-root", type=Path, default=codex_home / "skills")

    check_all_parser = subparsers.add_parser(
        "check-all", help="check every canonical skill installation link"
    )
    check_all_parser.add_argument(
        "--target-root", type=Path, default=codex_home / "skills"
    )

    install_parser = subparsers.add_parser("install", help="install one canonical skill link")
    install_parser.add_argument("name")
    install_parser.add_argument("--target-root", type=Path, default=codex_home / "skills")
    install_parser.add_argument("--backup-root", type=Path, default=codex_home / "skill-backups")
    install_parser.add_argument("--replace", action="store_true")

    check_parser = subparsers.add_parser("check", help="check one canonical skill link")
    check_parser.add_argument("name")
    check_parser.add_argument("--target-root", type=Path, default=codex_home / "skills")
    args = parser.parse_args(argv)

    try:
        if args.command == "validate":
            skill_count, test_count = validate_repository()
            print(f"PASS: validated {skill_count} skill(s) and {test_count} regression script(s)")
        elif args.command == "catalog":
            metadata_items = [validate_skill(root) for root in discover_skills()]
            entries = load_skill_catalog(metadata_items)
            rendered = render_catalog_markdown(entries, metadata_items)
            if args.check:
                validate_skill_catalog(metadata_items)
                print("PASS: skill catalog and human-readable index are synchronized")
            else:
                print(rendered, end="")
        elif args.command == "list":
            list_skills(args.target_root)
        elif args.command == "check-all":
            check_all_installations(args.target_root)
        elif args.command == "install":
            install_skill(args.name, args.target_root, args.backup_root, args.replace)
        elif args.command == "check":
            check_installation(args.name, args.target_root)
    except (OSError, RepositoryValidationError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
