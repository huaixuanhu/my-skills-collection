#!/usr/bin/env python3
"""Preview or create a proportional scaffold for one research task."""

from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKILL_NAME = "scaffold-research-task"
SKILL_VERSION = "0.1.0"
SCHEMA_VERSION = 1
SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "templates"
PROFILE_FILENAME = "RESEARCH_TASK_PROFILE.json"
ROOT_POLICY = "no-automatic-root-changes"

MODULE_ORDER = (
    "base",
    "model-research",
    "third-party-source",
    "remote-compute",
    "governance-connect",
)
PROFILE_MODULES = {
    "literature-review": ("base",),
    "local-ml": ("base", "model-research"),
    "third-party-remote": MODULE_ORDER,
    "existing-repository": ("base", "governance-connect"),
}

PACKAGE_RE = re.compile(r"^[a-z][a-z0-9_]*$")
SAFE_RELATIVE_RE = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*(?:/[A-Za-z0-9][A-Za-z0-9._-]*)*$"
)
TOKEN_RE = re.compile(r"\{\{([a-z_]+)\}\}")


class ScaffoldError(RuntimeError):
    """Raised when a scaffold request is unsafe or internally inconsistent."""


@dataclass(frozen=True, slots=True)
class BuildOptions:
    target: Path
    task_name: str
    profile: str
    modules: tuple[str, ...]
    package_name: str
    compute_dir: str


@dataclass(frozen=True, slots=True)
class OutputStatus:
    relative: str
    state: str
    detail: str = ""


def validate_task_name(value: str) -> str:
    value = value.strip()
    if not value:
        raise ScaffoldError("task name must not be empty")
    if len(value) > 120:
        raise ScaffoldError("task name must be 120 characters or fewer")
    if any(ord(character) < 32 for character in value):
        raise ScaffoldError("task name must not contain control characters")
    if "{{" in value or "}}" in value:
        raise ScaffoldError("task name must not contain template delimiters")
    if '\"\"\"' in value:
        raise ScaffoldError("task name must not contain a triple-double-quote sequence")
    return value


def derive_package_name(task_name: str) -> str:
    candidate = re.sub(r"[^a-z0-9]+", "_", task_name.lower()).strip("_")
    if not candidate:
        candidate = "research_task"
    if not candidate[0].isalpha():
        candidate = f"research_{candidate}"
    if keyword.iskeyword(candidate):
        candidate = f"{candidate}_research"
    return candidate


def validate_package_name(value: str) -> str:
    if not PACKAGE_RE.fullmatch(value) or keyword.iskeyword(value):
        raise ScaffoldError(
            "package name must be a lowercase Python identifier beginning with a letter"
        )
    return value


def validate_compute_dir(value: str) -> str:
    if not SAFE_RELATIVE_RE.fullmatch(value):
        raise ScaffoldError(
            "compute directory must be a safe relative path without dot or parent segments"
        )
    parts = Path(value).parts
    if any(part in {".", ".."} for part in parts):
        raise ScaffoldError("compute directory must not contain dot or parent segments")
    return Path(*parts).as_posix()


def ordered_modules(values: Iterable[str]) -> tuple[str, ...]:
    selected = set(values)
    unknown = selected.difference(MODULE_ORDER)
    if unknown:
        raise ScaffoldError(f"unknown module(s): {', '.join(sorted(unknown))}")
    selected.add("base")
    return tuple(module for module in MODULE_ORDER if module in selected)


def select_modules(profile: str, additions: Iterable[str]) -> tuple[str, ...]:
    if profile not in PROFILE_MODULES:
        raise ScaffoldError(f"unknown profile: {profile}")
    return ordered_modules((*PROFILE_MODULES[profile], *additions))


def normalize_target(value: Path) -> Path:
    target = value.expanduser()
    if not target.is_absolute():
        target = Path.cwd() / target
    target = Path(str(target.absolute()))
    if target == Path(target.anchor):
        raise ScaffoldError("filesystem root is not a valid scaffold target")
    if target == Path.home().absolute():
        raise ScaffoldError("home directory is not a valid scaffold target")
    if target.is_symlink():
        raise ScaffoldError("scaffold target must not be a symlink")
    if target.exists() and not target.is_dir():
        raise ScaffoldError("scaffold target exists and is not a directory")
    return target


def make_options(
    *,
    target: Path,
    task_name: str,
    profile: str,
    additions: Iterable[str] = (),
    package_name: str | None = None,
    compute_dir: str = "remote_compute",
) -> BuildOptions:
    clean_task_name = validate_task_name(task_name)
    modules = select_modules(profile, additions)
    clean_package_name = validate_package_name(
        package_name or derive_package_name(clean_task_name)
    )
    clean_compute_dir = validate_compute_dir(compute_dir)
    return BuildOptions(
        target=normalize_target(target),
        task_name=clean_task_name,
        profile=profile,
        modules=modules,
        package_name=clean_package_name,
        compute_dir=clean_compute_dir,
    )


def template_context(options: BuildOptions) -> dict[str, str]:
    return {
        "task_name": options.task_name,
        "package_name": options.package_name,
        "compute_dir": options.compute_dir,
        "profile": options.profile,
        "module_summary": ", ".join(options.modules),
        "skill_name": SKILL_NAME,
        "skill_version": SKILL_VERSION,
    }


def render_tokens(value: str, context: dict[str, str]) -> str:
    unknown = sorted(set(TOKEN_RE.findall(value)).difference(context))
    if unknown:
        raise ScaffoldError(f"unknown template token(s): {', '.join(unknown)}")
    rendered = TOKEN_RE.sub(lambda match: context[match.group(1)], value)
    if "{{" in rendered or "}}" in rendered:
        raise ScaffoldError("unresolved template delimiter")
    return rendered


def safe_relative_path(value: str) -> Path:
    relative = Path(value)
    if relative.is_absolute() or not relative.parts:
        raise ScaffoldError(f"unsafe generated path: {value}")
    if any(part in {"", ".", ".."} for part in relative.parts):
        raise ScaffoldError(f"unsafe generated path: {value}")
    return relative


def module_template_files(module: str) -> list[Path]:
    if module == "governance-connect":
        return []
    root = TEMPLATE_ROOT / module
    if not root.is_dir():
        raise ScaffoldError(f"missing template module: {module}")
    templates = sorted(path for path in root.rglob("*.tmpl") if path.is_file())
    if not templates:
        raise ScaffoldError(f"template module is empty: {module}")
    return templates


def expected_relative_paths(options: BuildOptions) -> tuple[Path, ...]:
    context = template_context(options)
    paths: set[Path] = {Path(PROFILE_FILENAME)}
    for module in options.modules:
        for template in module_template_files(module):
            relative_template = template.relative_to(TEMPLATE_ROOT / module).as_posix()
            if not relative_template.endswith(".tmpl"):
                raise ScaffoldError(f"unexpected template extension: {template}")
            rendered = render_tokens(relative_template[:-5], context)
            relative = safe_relative_path(rendered)
            if relative in paths:
                raise ScaffoldError(f"duplicate generated path: {relative}")
            paths.add(relative)
    return tuple(sorted(paths, key=lambda path: path.as_posix()))


def manifest_payload(options: BuildOptions) -> dict[str, object]:
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_by": {"skill": SKILL_NAME, "version": SKILL_VERSION},
        "task_name": options.task_name,
        "profile": options.profile,
        "modules": list(options.modules),
        "package_name": (
            options.package_name if "model-research" in options.modules else None
        ),
        "compute_dir": (
            options.compute_dir if "remote-compute" in options.modules else None
        ),
        "governance_connect": "governance-connect" in options.modules,
        "root_policy": ROOT_POLICY,
    }


def build_outputs(options: BuildOptions) -> dict[Path, str]:
    context = template_context(options)
    outputs: dict[Path, str] = {
        Path(PROFILE_FILENAME): json.dumps(
            manifest_payload(options), ensure_ascii=False, indent=2
        )
        + "\n"
    }
    for module in options.modules:
        for template in module_template_files(module):
            relative_template = template.relative_to(TEMPLATE_ROOT / module).as_posix()
            relative = safe_relative_path(
                render_tokens(relative_template[:-5], context)
            )
            if relative in outputs:
                raise ScaffoldError(f"duplicate generated path: {relative}")
            try:
                template_text = template.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                raise ScaffoldError(f"cannot read template {template}: {exc}") from exc
            outputs[relative] = render_tokens(template_text, context)
    return dict(sorted(outputs.items(), key=lambda item: item[0].as_posix()))


def path_component_conflict(target: Path, relative: Path) -> tuple[Path, str] | None:
    current = target
    for part in relative.parts[:-1]:
        current = current / part
        if current.is_symlink():
            return current, "symlinked path"
        if current.exists() and not current.is_dir():
            return current, "ancestor is not a directory"
    destination = target / relative
    if destination.is_symlink():
        return destination, "symlinked path"
    return None


def inspect_outputs(options: BuildOptions, outputs: dict[Path, str]) -> list[OutputStatus]:
    statuses: list[OutputStatus] = []
    for relative, content in outputs.items():
        component_conflict = path_component_conflict(options.target, relative)
        if component_conflict is not None:
            _, detail = component_conflict
            statuses.append(
                OutputStatus(relative.as_posix(), "CONFLICT", detail)
            )
            continue
        destination = options.target / relative
        if not destination.exists():
            statuses.append(OutputStatus(relative.as_posix(), "CREATE"))
            continue
        if not destination.is_file():
            statuses.append(
                OutputStatus(relative.as_posix(), "CONFLICT", "not a regular file")
            )
            continue
        try:
            existing = destination.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            statuses.append(
                OutputStatus(relative.as_posix(), "CONFLICT", f"cannot read: {exc}")
            )
            continue
        state = "UNCHANGED" if existing == content else "CONFLICT"
        detail = "" if state == "UNCHANGED" else "different existing content"
        statuses.append(OutputStatus(relative.as_posix(), state, detail))
    return statuses


def print_plan(options: BuildOptions, statuses: list[OutputStatus], apply: bool) -> None:
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"{mode}: {SKILL_NAME} v{SKILL_VERSION}")
    print(f"Target: {options.target}")
    print(f"Profile: {options.profile}")
    print(f"Modules: {', '.join(options.modules)}")
    for status in statuses:
        suffix = f" - {status.detail}" if status.detail else ""
        print(f"{status.state}: {status.relative}{suffix}")


def apply_outputs(
    options: BuildOptions,
    outputs: dict[Path, str],
    statuses: list[OutputStatus],
) -> tuple[int, int]:
    if any(status.state == "CONFLICT" for status in statuses):
        raise ScaffoldError("conflicts detected; no files were written")

    create_paths = {
        status.relative for status in statuses if status.state == "CREATE"
    }
    created = 0
    for relative, content in outputs.items():
        if relative.as_posix() not in create_paths:
            continue
        destination = options.target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        except FileExistsError as exc:
            raise ScaffoldError(
                f"path appeared after conflict inspection: {relative}"
            ) from exc
        created += 1
    unchanged = sum(status.state == "UNCHANGED" for status in statuses)
    return created, unchanged


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--task-name", required=True)
    parser.add_argument("--profile", choices=sorted(PROFILE_MODULES), required=True)
    parser.add_argument(
        "--add-module",
        action="append",
        default=[],
        choices=MODULE_ORDER,
        help="add a justified module; may be repeated",
    )
    parser.add_argument("--package-name")
    parser.add_argument("--compute-dir", default="remote_compute")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--allow-repository-root", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        options = make_options(
            target=args.target,
            task_name=args.task_name,
            profile=args.profile,
            additions=args.add_module,
            package_name=args.package_name,
            compute_dir=args.compute_dir,
        )
        if (
            args.apply
            and (options.target / ".git").exists()
            and not args.allow_repository_root
        ):
            raise ScaffoldError(
                "target appears to be a repository root; review the plan and rerun with "
                "--allow-repository-root only after explicit agreement"
            )
        outputs = build_outputs(options)
        statuses = inspect_outputs(options, outputs)
        print_plan(options, statuses, args.apply)
        if any(status.state == "CONFLICT" for status in statuses):
            raise ScaffoldError("conflicts detected; no files were written")
        if not args.apply:
            print("PASS: preview complete; no files were written")
            return 0
        created, unchanged = apply_outputs(options, outputs, statuses)
        print(f"PASS: created {created} file(s); {unchanged} unchanged")
        return 0
    except (OSError, ScaffoldError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
