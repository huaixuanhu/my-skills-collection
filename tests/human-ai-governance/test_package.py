from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "skills/human-ai-governance"


def main() -> int:
    expected_files = {
        "SKILL.md",
        "agents/openai.yaml",
        "references/evaluation-scenarios.md",
        "references/governance-patterns.md",
        "references/graph-governance.md",
        "references/preflight-patterns.md",
        "references/stage-sizing.md",
        "scripts/governance_preflight_template.py",
    }
    actual_files = {
        str(path.relative_to(CANDIDATE))
        for path in CANDIDATE.rglob("*")
        if path.is_file()
    }
    assert actual_files == expected_files, sorted(actual_files ^ expected_files)

    skill = (CANDIDATE / "SKILL.md").read_text(encoding="utf-8")
    assert "Skill version: `0.5.1`" in skill
    assert "Generated/adapted from human-ai-governance v0.5.1" in skill
    assert len(skill.splitlines()) < 120
    assert "The presence of a manifest alone does not activate graph workflow" in skill

    for relative_path in (
        "references/governance-patterns.md",
        "references/preflight-patterns.md",
        "references/evaluation-scenarios.md",
    ):
        text = (CANDIDATE / relative_path).read_text(encoding="utf-8")
        assert "v0.5.1" in text, relative_path

    graph = (CANDIDATE / "references/graph-governance.md").read_text(encoding="utf-8")
    assert "Manifest presence alone does not activate graph workflow" in graph

    preflight = (
        CANDIDATE / "scripts/governance_preflight_template.py"
    ).read_text(encoding="utf-8")
    for required in (
        'SKILL_VERSION = "0.5.1"',
        '"--porcelain=v1", "-z"',
        'errors="surrogateescape"',
        "class GitInspectionError",
        'SnapshotText(path, "staged index", index_text)',
        'SnapshotText(path, "working tree", worktree_text)',
        "could not inspect repository state",
    ):
        assert required in preflight, required
    assert "strip_git_quotes" not in preflight

    print("PASS: v0.5.1 package regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
