from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "skills/human-ai-governance"


def main() -> int:
    expected_files = {
        "SKILL.md",
        "agents/openai.yaml",
        "references/audience-facing-writing.md",
        "references/evaluation-scenarios.md",
        "references/governance-patterns.md",
        "references/graph-governance.md",
        "references/plan-lifecycle-routing.md",
        "references/persistent-completion.md",
        "references/preflight-patterns.md",
        "references/proportional-assurance.md",
        "references/reasoning-mode-routing.md",
        "references/review-density-routing.md",
        "references/stage-sizing.md",
        "references/technical-language-routing.md",
        "scripts/governance_preflight_template.py",
    }
    actual_files = {
        str(path.relative_to(CANDIDATE))
        for path in CANDIDATE.rglob("*")
        if path.is_file()
    }
    assert actual_files == expected_files, sorted(actual_files ^ expected_files)

    skill = (CANDIDATE / "SKILL.md").read_text(encoding="utf-8")
    assert "Skill version: `0.7.5`" in skill
    assert "Generated/adapted from human-ai-governance v0.7.5" in skill
    assert len(skill.splitlines()) < 145
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
        "Engineering-governance writing is the default",
        "File extension, document length, or a request for polish alone does not decide the mode",
        "Expression mode changes prose and organization only",
        "references/audience-facing-writing.md",
        "Treat technical-language routing as an explicit axis independent of writing mode",
        "add no terminology transformation beyond current Codex and governing instructions",
        "must not activate, deactivate, replace, weaken, or reshape",
        "It must not change reasoning, planning, implementation, tool use, validation, evidence, safety controls, authorization, or completion criteria",
        "references/technical-language-routing.md",
        "route through a compact plan index before opening plan bodies",
        "Do not recursively load a plan directory to discover which document is current",
        "Use an index when child-of-child plans, parallel branches, multi-session continuation, or retained historical plans make task routing ambiguous",
        "`complete + consumed + evidence_only`",
        "A stale index yields to its owner sources",
        "references/plan-lifecycle-routing.md",
        "explicitly asks to continue until a verifiable outcome succeeds",
        "Route retries by credible single and cumulative consequence, not attempt number",
        "attempt count alone is not an approval boundary",
        "references/persistent-completion.md",
        "references/review-density-routing.md",
    ):
        assert required in skill, required

    for relative_path in (
        "references/governance-patterns.md",
        "references/preflight-patterns.md",
        "references/evaluation-scenarios.md",
        "references/proportional-assurance.md",
        "references/reasoning-mode-routing.md",
        "references/audience-facing-writing.md",
        "references/technical-language-routing.md",
        "references/plan-lifecycle-routing.md",
        "references/persistent-completion.md",
        "references/review-density-routing.md",
    ):
        text = (CANDIDATE / relative_path).read_text(encoding="utf-8")
        assert "v0.7.5" in text, relative_path

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

    preflight_patterns = (
        CANDIDATE / "references/preflight-patterns.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Attempt numbers and words such as `retry` or `attempt` do not prove risk",
        "Do not add generic attempt-count, retry-word, or persistence-mode checks to preflight",
    ):
        assert required in preflight_patterns, required

    persistent = (
        CANDIDATE / "references/persistent-completion.md"
    ).read_text(encoding="utf-8")
    for required in (
        "completion objective",
        "safe recovery",
        "consequence-bearing execution",
        "Attempt numbers are audit metadata",
        "Do not stop at “attempt 1 used”",
        "Do not use a universal retry count",
        "A plan index may point to that owner",
    ):
        assert required in persistent, required

    writing = (
        CANDIDATE / "references/audience-facing-writing.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Engineering records remain the default",
        "Minimize repeated self-justification, process defense, and irrelevant boundary statements",
        "Route each section, page, slide, note, or appendix by its own function",
        "not X, but Y",
        "Do not use phrase counts, regular expressions, AI-detector scores",
        "natural-sounding prose never justifies removing an operational invariant",
        "Do not fill an unspecified trigger, fallback condition, threshold, or authorization step",
        "Do not repeat the full boundary list in the conclusion",
        "After one clear negative contrast, phrase later points affirmatively",
        "Technical-language choice is a separate axis",
        "cannot activate, deactivate, or reshape audience-facing expression",
    ):
        assert required in writing, required
    for banned in (
        "Never use not X, but Y",
        "Never use em dashes",
        "AI-detector score must",
    ):
        assert banned not in writing, banned

    terminology = (
        CANDIDATE / "references/technical-language-routing.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Use `default` when the user does not make an explicit choice",
        "Technical-language routing is orthogonal to writing-mode routing",
        "Audience-facing expression does not imply `plain`",
        "Plain language does not mean a shorter or less complete answer",
        "reasoning effort, reasoning route, or agent topology",
        "Keep exact identifiers, code, commands, paths, configuration keys, API fields, error text, formulas, standards",
        "Would `default` and `plain` lead to the same engineering decision, implementation, validation, evidence, risk, and next action?",
        "Do not use jargon counts, word blacklists, reading-level scores, regular expressions, or AI-detector scores",
    ):
        assert required in terminology, required

    plan_routing = (
        CANDIDATE / "references/plan-lifecycle-routing.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Do not use a fixed plan-count threshold",
        "The index helps an agent find what to read",
        "It cannot grant scope, implementation authority, runtime authority, approval, or completion",
        "`lifecycle_status` | `active`, `blocked`, `complete`, `superseded`",
        "`authority_state` | `current`, `consumed`",
        "`load_policy` | `default`, `conditional`, `evidence_only`",
        "Completion does not prove that another source now carries the plan's current contract",
        "Apply `load_policy` before opening the referenced plan body",
        "Do not recursively read all plans, all siblings, or every ancestor by default",
        "Do not edit an immutable, signed, digest-bound, receipt-bound, or append-only plan",
        "It does not mean obsolete, safe to delete, or irrelevant to every future claim",
        "An index-first design does not require loading the whole index into model context",
        "Store lifecycle in metadata rather than renaming or moving folders whenever status changes",
    ):
        assert required in plan_routing, required

    stage_sizing = (
        CANDIDATE / "references/stage-sizing.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Plan closeout and context release",
        "Do not infer `evidence_only` from completion alone",
        "preserve its original text and carry current lifecycle and loading state in the index",
        "attempt count alone is not a decision boundary",
        "An exhausted runtime attempt does not exhaust recovery authority",
    ):
        assert required in stage_sizing, required

    governance = (
        CANDIDATE / "references/governance-patterns.md"
    ).read_text(encoding="utf-8")
    for required in (
        "Plan Index and Lifecycle Routing",
        "Plan index / active status entrypoint",
        "Lifecycle status: active",
        "Authority state: current",
        "Load policy: default",
        "Consumed by: none",
        "Persistent Completion and Recovery",
        "Completion directive: persistent",
        "route any new execution by consequence rather than attempt number",
    ):
        assert required in governance, required

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
        "Long engineering plan with a request for polish",
        "Leadership presentation",
        "Technical design presentation",
        "High-consequence audience memo",
        "No terminology choice",
        "Plain engineering explanation",
        "Audience-facing default terminology",
        "Audience-facing plain terminology",
        "Plain high-consequence handoff",
        "Simple project with one clear plan",
        "Nested plan tree with consumed history",
        "Completed current baseline",
        "Immutable evidence-bound plan closeout",
        "Stale plan index conflict",
        "Large plan index",
        "Persistent local validation failure",
        "Authorized non-force push transport failure",
        "Production activation no-go",
        "Pre-authorized multi-attempt execution envelope",
        "Ambiguous non-idempotent external result",
        "Accepted artifact under recovery",
    ):
        assert required in evaluation, required
    assert "Keep high and xhigh results separate" not in evaluation

    runtime_routing = skill + routing
    for unstable_product_detail in ("four agents", "4 agents", "R ∝"):
        assert unstable_product_detail not in runtime_routing, unstable_product_detail

    agent_metadata = yaml.safe_load(
        (CANDIDATE / "agents/openai.yaml").read_text(encoding="utf-8")
    )
    interface = agent_metadata["interface"]
    assert interface["display_name"] == "Human-AI Governance"
    assert 25 <= len(interface["short_description"]) <= 64
    assert "$human-ai-governance" in interface["default_prompt"]
    assert agent_metadata.get("policy", {}).get("allow_implicit_invocation", True)

    graph = (CANDIDATE / "references/graph-governance.md").read_text(encoding="utf-8")
    assert "Manifest presence alone does not activate graph workflow" in graph

    preflight = (
        CANDIDATE / "scripts/governance_preflight_template.py"
    ).read_text(encoding="utf-8")
    for required in (
        'SKILL_VERSION = "0.7.5"',
        '"--porcelain=v1", "-z"',
        'errors="surrogateescape"',
        "class GitInspectionError",
        'SnapshotText(path, "staged index", index_text)',
        'SnapshotText(path, "working tree", worktree_text)',
        "could not inspect repository state",
    ):
        assert required in preflight, required
    assert "strip_git_quotes" not in preflight
    assert "PLAN_INDEX" not in preflight

    print("PASS: v0.7.5 package regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
