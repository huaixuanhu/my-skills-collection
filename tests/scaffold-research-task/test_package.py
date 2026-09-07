from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "skills/scaffold-research-task"


def main() -> int:
    expected_files = {
        "SKILL.md",
        "agents/openai.yaml",
        "assets/templates/base/README.md.tmpl",
        "assets/templates/base/RESEARCH_TASK.md.tmpl",
        "assets/templates/base/evidence/README.md.tmpl",
        "assets/templates/base/reports/README.md.tmpl",
        "assets/templates/base/sources/README.md.tmpl",
        "assets/templates/model-research/RESEARCH_ARCHITECTURE.md.tmpl",
        "assets/templates/model-research/configs/README.md.tmpl",
        "assets/templates/model-research/data_contracts/README.md.tmpl",
        "assets/templates/model-research/environment/README.md.tmpl",
        "assets/templates/model-research/notebooks/README.md.tmpl",
        "assets/templates/model-research/research_artifacts/README.md.tmpl",
        "assets/templates/model-research/running_logs/README.md.tmpl",
        "assets/templates/model-research/scripts/README.md.tmpl",
        "assets/templates/model-research/src/{{package_name}}/__init__.py.tmpl",
        "assets/templates/model-research/tests/README.md.tmpl",
        "assets/templates/remote-compute/{{compute_dir}}/README.md.tmpl",
        "assets/templates/remote-compute/{{compute_dir}}/job_templates/README.md.tmpl",
        "assets/templates/remote-compute/{{compute_dir}}/run_receipts/README.md.tmpl",
        "assets/templates/third-party-source/THIRD_PARTY.md.tmpl",
        "references/decision-matrix.md",
        "references/experiment-orientation.md",
        "references/host-adaptation.md",
        "references/profiles.md",
        "references/research-governance.md",
        "references/research-lifecycle.md",
        "scripts/scaffold_research_task.py",
        "scripts/validate_research_scaffold.py",
    }
    actual_files = {
        str(path.relative_to(CANDIDATE))
        for path in CANDIDATE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    assert actual_files == expected_files, sorted(actual_files ^ expected_files)

    skill = (CANDIDATE / "SKILL.md").read_text(encoding="utf-8")
    assert "Skill version: `0.1.2`" in skill
    assert "Build the smallest useful scaffold for one research task" in skill
    assert "It is not a project-wide base governance system" in skill
    assert "`governance-connect`" in skill
    assert "creates no generic governance files by itself" in skill
    assert "Do not impose Model 5 SONNET's source-ingestion stop" in skill
    assert "`local-governance`" not in skill
    assert "research-workspace-scaffolder" not in skill
    assert "WORKSPACE_PROFILE" not in skill
    assert len(skill.splitlines()) < 180

    frontmatter = skill.split("---", 2)[1]
    assert "name: scaffold-research-task" in frontmatter
    assert "task-scoped research scaffold" in frontmatter
    assert "workspace" not in frontmatter.lower()

    agent_metadata = (CANDIDATE / "agents/openai.yaml").read_text(encoding="utf-8")
    assert 'display_name: "Scaffold Research Task"' in agent_metadata
    assert (
        'short_description: "Scaffold research and clarify experiment scope"'
        in agent_metadata
    )
    assert "$scaffold-research-task" in agent_metadata

    source = (CANDIDATE / "scripts/scaffold_research_task.py").read_text(
        encoding="utf-8"
    )
    for required in (
        'SKILL_VERSION = "0.1.2"',
        '"governance-connect"',
        '"no-automatic-root-changes"',
        'parser.add_argument("--apply", action="store_true")',
        'parser.add_argument("--allow-repository-root", action="store_true")',
        'with destination.open("x"',
    ):
        assert required in source, required

    template_paths = {
        path.relative_to(CANDIDATE).as_posix()
        for path in (CANDIDATE / "assets/templates").rglob("*.tmpl")
    }
    assert not any(path.endswith("AGENTS.md.tmpl") for path in template_paths)
    assert not any("preflight" in path.lower() for path in template_paths)
    assert not any("AI_AGENT_LOG" in path for path in template_paths)

    governance = (CANDIDATE / "references/research-governance.md").read_text(
        encoding="utf-8"
    )
    for required in (
        "Level 1: cite or summarize",
        "Level 2: inspect or execute locally",
        "Level 3: incorporate or redistribute",
        "Do not promote a Level 3 hard stop",
        "may use any host-approved location",
        "Invoke or adapt `human-ai-governance` only for a real project-level gap",
    ):
        assert required in governance, required

    print("PASS: scaffold-research-task v0.1.2 package checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
