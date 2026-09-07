from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills/scaffold-research-task/scripts/scaffold_research_task.py"


def run_scaffold(
    *arguments: object, script: Path = SCRIPT
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *(str(argument) for argument in arguments)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def expected_base() -> set[str]:
    return {
        "README.md",
        "RESEARCH_TASK.md",
        "RESEARCH_TASK_PROFILE.json",
        "evidence/README.md",
        "reports/README.md",
        "sources/README.md",
    }


def files_under(target: Path) -> set[str]:
    return {
        path.relative_to(target).as_posix()
        for path in target.rglob("*")
        if path.is_file()
    }


def test_dry_run_creates_nothing(root: Path) -> None:
    target = root / "preview"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Policy literature review",
        "--profile",
        "literature-review",
    )
    assert result.returncode == 0, result.stderr
    assert "DRY-RUN" in result.stdout
    assert "Modules: base" in result.stdout
    assert "no files were written" in result.stdout
    assert not target.exists()


def test_literature_profile_is_lightweight(root: Path) -> None:
    target = root / "literature"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Policy literature review",
        "--profile",
        "literature-review",
        "--apply",
    )
    assert result.returncode == 0, result.stderr
    assert files_under(target) == expected_base()
    manifest = json.loads(
        (target / "RESEARCH_TASK_PROFILE.json").read_text(encoding="utf-8")
    )
    assert manifest["modules"] == ["base"]
    assert manifest["package_name"] is None
    assert manifest["compute_dir"] is None
    assert not manifest["governance_connect"]
    assert not (target / "src").exists()
    assert not (target / "environment").exists()
    assert not (target / "remote_compute").exists()


def test_local_ml_profile_adds_model_contracts(root: Path) -> None:
    target = root / "local_ml"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Local Forecast Pilot",
        "--profile",
        "local-ml",
        "--apply",
    )
    assert result.returncode == 0, result.stderr
    actual = files_under(target)
    assert expected_base().issubset(actual)
    assert "RESEARCH_ARCHITECTURE.md" in actual
    assert "data_contracts/README.md" in actual
    assert "environment/README.md" in actual
    assert "src/local_forecast_pilot/__init__.py" in actual
    assert "tests/README.md" in actual
    assert "THIRD_PARTY.md" not in actual
    assert not any(path.startswith("remote_compute/") for path in actual)


def test_third_party_remote_is_host_adaptable(root: Path) -> None:
    target = root / "remote_model"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "External Climate Model",
        "--profile",
        "third-party-remote",
        "--package-name",
        "climate_model",
        "--compute-dir",
        "hpc",
        "--apply",
    )
    assert result.returncode == 0, result.stderr
    actual = files_under(target)
    assert "THIRD_PARTY.md" in actual
    assert "hpc/README.md" in actual
    assert "hpc/job_templates/README.md" in actual
    assert "hpc/run_receipts/README.md" in actual
    assert "src/climate_model/__init__.py" in actual
    assert "AGENTS.md" not in actual
    assert not any("preflight" in path.lower() for path in actual)
    manifest = json.loads(
        (target / "RESEARCH_TASK_PROFILE.json").read_text(encoding="utf-8")
    )
    assert manifest["governance_connect"]
    assert manifest["compute_dir"] == "hpc"


def test_repository_root_requires_explicit_flag(root: Path) -> None:
    repository = root / "repo"
    (repository / ".git").mkdir(parents=True)
    result = run_scaffold(
        "--target",
        repository,
        "--task-name",
        "Repository research",
        "--profile",
        "existing-repository",
        "--apply",
    )
    assert result.returncode == 2
    assert "--allow-repository-root" in result.stderr
    assert not (repository / "README.md").exists()

    package = repository / "research_tasks" / "bounded_study"
    result = run_scaffold(
        "--target",
        package,
        "--task-name",
        "Bounded study",
        "--profile",
        "existing-repository",
        "--apply",
    )
    assert result.returncode == 0, result.stderr
    assert (package / "README.md").is_file()
    assert not (repository / "README.md").exists()
    assert not (package / "AGENTS.md").exists()


def test_conflict_prevents_all_writes(root: Path) -> None:
    target = root / "conflict"
    target.mkdir()
    existing = "user-owned content\n"
    (target / "README.md").write_text(existing, encoding="utf-8")
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Conflict study",
        "--profile",
        "local-ml",
        "--apply",
    )
    assert result.returncode == 2
    assert "different existing content" in result.stdout
    assert "no files were written" in result.stderr
    assert files_under(target) == {"README.md"}
    assert (target / "README.md").read_text(encoding="utf-8") == existing


def test_ancestor_file_conflict_prevents_all_writes(root: Path) -> None:
    target = root / "ancestor_conflict"
    target.mkdir()
    (target / "src").write_text("user-owned file\n", encoding="utf-8")
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Ancestor conflict study",
        "--profile",
        "local-ml",
        "--apply",
    )
    assert result.returncode == 2
    assert "ancestor is not a directory" in result.stdout
    assert files_under(target) == {"src"}


def test_symlink_conflict_prevents_all_writes(root: Path) -> None:
    target = root / "symlink_conflict"
    external = root / "external_evidence"
    target.mkdir()
    external.mkdir()
    (target / "evidence").symlink_to(external, target_is_directory=True)
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Symlink conflict study",
        "--profile",
        "literature-review",
        "--apply",
    )
    assert result.returncode == 2
    assert "symlinked path" in result.stdout
    assert not any(path.is_file() for path in target.rglob("*"))
    assert not any(external.iterdir())


def test_repeat_apply_is_idempotent(root: Path) -> None:
    target = root / "repeat"
    arguments = (
        "--target",
        target,
        "--task-name",
        "Repeat study",
        "--profile",
        "literature-review",
        "--apply",
    )
    first = run_scaffold(*arguments)
    assert first.returncode == 0, first.stderr
    before = {
        path: path.read_bytes() for path in target.rglob("*") if path.is_file()
    }
    second = run_scaffold(*arguments)
    assert second.returncode == 0, second.stderr
    assert "created 0 file(s); 6 unchanged" in second.stdout
    after = {path: path.read_bytes() for path in target.rglob("*") if path.is_file()}
    assert before == after


def test_unsafe_compute_path_fails_closed(root: Path) -> None:
    target = root / "unsafe"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        "Unsafe path study",
        "--profile",
        "third-party-remote",
        "--compute-dir",
        "../escape",
        "--apply",
    )
    assert result.returncode == 2
    assert "safe relative path" in result.stderr
    assert not target.exists()


def test_task_name_cannot_break_generated_python(root: Path) -> None:
    target = root / "unsafe_title"
    result = run_scaffold(
        "--target",
        target,
        "--task-name",
        'Broken \"\"\" title',
        "--profile",
        "local-ml",
        "--apply",
    )
    assert result.returncode == 2
    assert "triple-double-quote" in result.stderr
    assert not target.exists()


def test_template_json_is_preserved_and_unknown_tokens_fail(root: Path) -> None:
    skill_copy = root / "template_fixture"
    shutil.copytree(SCRIPT.parents[1], skill_copy, ignore=shutil.ignore_patterns("__pycache__"))
    script = skill_copy / "scripts/scaffold_research_task.py"
    template = skill_copy / "assets/templates/model-research/configs/README.md.tmpl"
    original = template.read_text(encoding="utf-8")
    template.write_text(
        original + '\n{"analysis": {"name": "{{task_name}}", "seed": 7}}\n',
        encoding="utf-8",
    )
    target = root / "generated_json"
    result = run_scaffold(
        "--target", target,
        "--task-name", "JSON study",
        "--profile", "local-ml",
        "--apply",
        script=script,
    )
    assert result.returncode == 0, result.stderr
    text = (target / "configs/README.md").read_text(encoding="utf-8")
    assert json.loads(text.splitlines()[-1]) == {"analysis": {"name": "JSON study", "seed": 7}}

    template.write_text(original + "\n{{unknown_field}}\n", encoding="utf-8")
    blocked_target = root / "unknown_token"
    result = run_scaffold(
        "--target", blocked_target,
        "--task-name", "Unknown field study",
        "--profile", "local-ml",
        "--apply",
        script=script,
    )
    assert result.returncode == 2
    assert "unknown template token" in result.stderr
    assert not blocked_target.exists()


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="scaffold-research-task-") as directory:
        root = Path(directory)
        test_dry_run_creates_nothing(root)
        test_literature_profile_is_lightweight(root)
        test_local_ml_profile_adds_model_contracts(root)
        test_third_party_remote_is_host_adaptable(root)
        test_repository_root_requires_explicit_flag(root)
        test_conflict_prevents_all_writes(root)
        test_ancestor_file_conflict_prevents_all_writes(root)
        test_symlink_conflict_prevents_all_writes(root)
        test_repeat_apply_is_idempotent(root)
        test_unsafe_compute_path_fails_closed(root)
        test_task_name_cannot_break_generated_python(root)
        test_template_json_is_preserved_and_unknown_tokens_fail(root)
    print("PASS: scaffold generation behavior checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
