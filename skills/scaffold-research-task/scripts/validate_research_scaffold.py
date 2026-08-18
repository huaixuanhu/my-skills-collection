#!/usr/bin/env python3
"""Validate a scaffold generated for one research task."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import scaffold_research_task as scaffold


class ValidationError(RuntimeError):
    """Raised when a generated research scaffold violates its manifest contract."""


def read_manifest(target: Path) -> dict[str, object]:
    path = target / scaffold.PROFILE_FILENAME
    if path.is_symlink() or not path.is_file():
        raise ValidationError(f"missing regular manifest file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot parse {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError("manifest must contain a JSON object")
    return payload


def require_exact_keys(payload: dict[str, object]) -> None:
    expected = {
        "schema_version",
        "generated_by",
        "task_name",
        "profile",
        "modules",
        "package_name",
        "compute_dir",
        "governance_connect",
        "root_policy",
    }
    if set(payload) != expected:
        missing = sorted(expected.difference(payload))
        extra = sorted(set(payload).difference(expected))
        raise ValidationError(f"manifest keys differ; missing={missing}, extra={extra}")


def options_from_manifest(target: Path, payload: dict[str, object]) -> scaffold.BuildOptions:
    require_exact_keys(payload)
    if payload["schema_version"] != scaffold.SCHEMA_VERSION:
        raise ValidationError("unsupported manifest schema version")
    expected_generator = {
        "skill": scaffold.SKILL_NAME,
        "version": scaffold.SKILL_VERSION,
    }
    if payload["generated_by"] != expected_generator:
        raise ValidationError("manifest generator identity does not match this skill")
    if payload["root_policy"] != scaffold.ROOT_POLICY:
        raise ValidationError("manifest root policy is invalid")

    task_name = payload["task_name"]
    profile = payload["profile"]
    modules = payload["modules"]
    if not isinstance(task_name, str) or not isinstance(profile, str):
        raise ValidationError("manifest task_name and profile must be strings")
    if profile not in scaffold.PROFILE_MODULES:
        raise ValidationError(f"unknown manifest profile: {profile}")
    if not isinstance(modules, list) or not all(
        isinstance(module, str) for module in modules
    ):
        raise ValidationError("manifest modules must be a list of strings")
    try:
        ordered = scaffold.ordered_modules(modules)
    except scaffold.ScaffoldError as exc:
        raise ValidationError(str(exc)) from exc
    if list(ordered) != modules:
        raise ValidationError("manifest modules are duplicated or out of canonical order")
    required_by_profile = set(scaffold.PROFILE_MODULES[profile])
    if not required_by_profile.issubset(ordered):
        raise ValidationError("manifest modules do not satisfy the named profile")

    package_value = payload["package_name"]
    if "model-research" in ordered:
        if not isinstance(package_value, str):
            raise ValidationError("model-research requires package_name")
        try:
            package_name = scaffold.validate_package_name(package_value)
        except scaffold.ScaffoldError as exc:
            raise ValidationError(str(exc)) from exc
    else:
        if package_value is not None:
            raise ValidationError("package_name must be null without model-research")
        package_name = scaffold.derive_package_name(task_name)

    compute_value = payload["compute_dir"]
    if "remote-compute" in ordered:
        if not isinstance(compute_value, str):
            raise ValidationError("remote-compute requires compute_dir")
        try:
            compute_dir = scaffold.validate_compute_dir(compute_value)
        except scaffold.ScaffoldError as exc:
            raise ValidationError(str(exc)) from exc
    else:
        if compute_value is not None:
            raise ValidationError("compute_dir must be null without remote-compute")
        compute_dir = "remote_compute"

    expected_connect = "governance-connect" in ordered
    if payload["governance_connect"] is not expected_connect:
        raise ValidationError("governance_connect does not match selected modules")

    try:
        clean_task_name = scaffold.validate_task_name(task_name)
    except scaffold.ScaffoldError as exc:
        raise ValidationError(str(exc)) from exc
    return scaffold.BuildOptions(
        target=target,
        task_name=clean_task_name,
        profile=profile,
        modules=ordered,
        package_name=package_name,
        compute_dir=compute_dir,
    )


def required_marker_paths(options: scaffold.BuildOptions) -> set[Path]:
    paths = {Path("README.md"), Path("RESEARCH_TASK.md")}
    if "model-research" in options.modules:
        paths.add(Path("RESEARCH_ARCHITECTURE.md"))
    if "third-party-source" in options.modules:
        paths.add(Path("THIRD_PARTY.md"))
    if "remote-compute" in options.modules:
        paths.add(Path(options.compute_dir) / "README.md")
    return paths


def validate_files(options: scaffold.BuildOptions) -> int:
    expected = scaffold.expected_relative_paths(options)
    marker = f"Generated by {scaffold.SKILL_NAME} v{scaffold.SKILL_VERSION}"
    marker_paths = required_marker_paths(options)
    validated = 0
    for relative in expected:
        path = options.target / relative
        component_conflict = scaffold.path_component_conflict(
            options.target, relative
        )
        if component_conflict is not None:
            _, detail = component_conflict
            raise ValidationError(f"unsafe required path {relative}: {detail}")
        if not path.is_file():
            raise ValidationError(f"missing required file: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise ValidationError(f"cannot read {relative}: {exc}") from exc
        if "{{" in text or "}}" in text:
            raise ValidationError(f"unresolved template token in {relative}")
        if relative in marker_paths and marker not in text:
            raise ValidationError(f"missing generator marker in {relative}")
        validated += 1
    return validated


def validate_target(value: Path) -> tuple[scaffold.BuildOptions, int]:
    try:
        target = scaffold.normalize_target(value)
    except scaffold.ScaffoldError as exc:
        raise ValidationError(str(exc)) from exc
    if not target.is_dir():
        raise ValidationError(f"target directory does not exist: {target}")
    payload = read_manifest(target)
    options = options_from_manifest(target, payload)
    return options, validate_files(options)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        options, count = validate_target(args.target)
        print(
            f"PASS: validated {count} scaffold file(s) for {options.profile}; "
            f"modules={','.join(options.modules)}"
        )
        return 0
    except (OSError, ValidationError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
