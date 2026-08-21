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
        "references/proportional-assurance.md",
        "references/reasoning-mode-routing.md",
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
    assert "Skill version: `0.7.0`" in skill
    assert "Generated/adapted from human-ai-governance v0.7.0" in skill
    assert len(skill.splitlines()) < 120
    assert "The presence of a manifest alone does not activate graph workflow" in skill
    for required in (
        "treat them as peer primary modes",
        "Preserve Codex's ordinary discretion over delegation, coordination, and writing",
        "Do not impose read-only or single-writer defaults",
        "temporary Max single-writer recovery slice",
        "Treat mode choice and agent topology as separate decisions",
        "Max and Ultra may both use multiple subagents and parallel writes",
        "Tier 1-5 is the only governance classification",
        "platform's current effective sandbox",
        "Stop adding validation",
        "references/proportional-assurance.md",
    ):
        assert required in skill, required

    for relative_path in (
        "references/governance-patterns.md",
        "references/preflight-patterns.md",
        "references/evaluation-scenarios.md",
        "references/proportional-assurance.md",
        "references/reasoning-mode-routing.md",
    ):
        text = (CANDIDATE / relative_path).read_text(encoding="utf-8")
        assert "v0.7.0" in text, relative_path

    assurance = (
        CANDIDATE / "references/proportional-assurance.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Validation options are not cumulative levels",
        "There is no mandatory preference order",
        "outside this skill's control",
        "they do not add tiers",
    ):
        assert required in assurance, required

    routing = (
        CANDIDATE / "references/reasoning-mode-routing.md"
    ).read_text(encoding="utf-8")
    for required in (
        "choose between Max and Ultra as peer primary modes",
        "Do not make Ultra read-only by default",
        "Do not use single-writer execution as a Max default",
        "Do not force an Ultra-Max-Ultra ceremony",
        "do not route by agent count",
        "Parallel writing is valid in either Max or Ultra",
        "not a numerical risk formula",
        "Do not hard-code agent counts",
    ):
        assert required in routing, required

    evaluation = (
        CANDIDATE / "references/evaluation-scenarios.md"
    ).read_text(encoding="utf-8")
    assert "`xhigh`, `max`, and `ultra`" in evaluation
    assert "Select scenarios and reasoning modes" in evaluation
    for required in (
        "Stable known multi-agent causal task",
        "Evolving decomposition task",
        "Separable parallel implementation",
        "Shared-invariant coupled task before failure",
        "Large-data consumer change with valid receipts",
        "Boundary-owned defensive review",
        "Full-access platform configuration",
        "Complex component and simple glue decision",
        "hard-coded fan-out defaults",
    ):
        assert required in evaluation, required
    assert "Keep high and xhigh results separate" not in evaluation

    runtime_routing = skill + routing
    for unstable_product_detail in ("four agents", "4 agents", "R ∝"):
        assert unstable_product_detail not in runtime_routing, unstable_product_detail

    agent_metadata = (CANDIDATE / "agents/openai.yaml").read_text(encoding="utf-8")
    assert 'short_description: "Risk-scaled governance and Max/Ultra routing"' in agent_metadata
    assert (
        'default_prompt: "Use $human-ai-governance to set proportional project '
        'governance and recommend xhigh, Max, or Ultra for this task."'
        in agent_metadata
    )

    graph = (CANDIDATE / "references/graph-governance.md").read_text(encoding="utf-8")
    assert "Manifest presence alone does not activate graph workflow" in graph

    preflight = (
        CANDIDATE / "scripts/governance_preflight_template.py"
    ).read_text(encoding="utf-8")
    for required in (
        'SKILL_VERSION = "0.7.0"',
        '"--porcelain=v1", "-z"',
        'errors="surrogateescape"',
        "class GitInspectionError",
        'SnapshotText(path, "staged index", index_text)',
        'SnapshotText(path, "working tree", worktree_text)',
        "could not inspect repository state",
    ):
        assert required in preflight, required
    assert "strip_git_quotes" not in preflight

    print("PASS: v0.7.0 package regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
