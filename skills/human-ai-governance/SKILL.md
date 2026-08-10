---
name: human-ai-governance
description: Create, review, or maintain practical five-tier human-AI collaboration governance and reasoning-mode routing for software projects. Use when setting up or adapting AGENTS.md, architecture docs, plan docs, changelogs, AI agent logs, validation gates, safety boundaries, handoff routines, long-running workflows, or deciding whether an important main-workspace task should use xhigh, Max, Ultra, or a staged combination.
---

# Human-AI Governance

Skill version: `0.6.1`

## Overview

Create a durable collaboration system while scaling governance to credible harm, effective authority, reversibility, and operating scale. Treat this skill as a decision framework, not a universal checklist.

When generating or upgrading project governance files, include this marker in `AGENTS.md` or another durable governance file:

```text
Generated/adapted from human-ai-governance v0.6.1
```

Use the marker to decide whether an existing project needs a separately approved migration. Do not auto-migrate downstream projects when this global skill changes.

## Decision Rules

- The project tier records the highest authority and credible consequence present in the running project.
- Apply added controls to the capability surface the task can change. A distant roadmap or unrelated high-risk module does not make every edit high-risk, but permanent project invariants still apply.
- Skip an inapplicable step without a long justification. Preserve explicit repository rules, unresolved material decisions, and controls tied to credible failure modes.
- Treat a change as material when it can alter observable behavior, architecture or data flow, persistence, safety or authority, privacy, production operation, or a consequential runtime dependency. Typos, formatting, contract-preserving tests, lockfile-only churn, and historical notes are not automatically material.
- One accepted plan covers safe local implementation inside its scope. Ask again only for a material scope expansion, consequential external action, unresolved material choice, or explicit approval gate.
- Update a document when its current claim would become false, incomplete, or misleading. Give each rule one primary owner and prefer one canonical source plus links over repetition.
- For a projectless discussion or bounded low-impact task, stop at this file unless a resource trigger below actually applies. Do not load references or create governance artifacts for completeness alone.

## Core Workflow

1. Orient before changing files.
   - Read `AGENTS.md` and the directly relevant canonical source. Expand only when the task, local instructions, risk, or uncertainty requires it.
   - Before material edits, inspect repository state, protect user-owned changes, and identify affected authority and side effects.

2. Classify and plan proportionally.
   - Use the higher of current authority on the affected surface and authority introduced by the work.
   - For material work, state scope, non-scope, likely files, validation, and safety assumptions concisely. Proceed directly on small read-only or reversible work unless local rules say otherwise.
   - When reasoning-mode routing applies, make one concise recommendation before material work and name any real switch point. Do not repeat the recommendation after the user accepts it.

3. Implement in bounded slices.
   - Prefer the project's existing patterns, language, tooling, and docs style.
   - Treat roadmap stages as coordination containers, not automatic execution units. Size an execution stage around one primary verifiable outcome and one coherent acceptance and recovery boundary; stages need not be equal.
   - For complex or multi-session work, classify stage capacity as `bounded`, `dense_but_coherent`, or `split_required`. Split independent acceptance, rollback, authority, evidence, or recovery domains only at a restartable seam; do not split by file, function, package, token, duration, or compaction counts alone.
   - Keep atomic or causally inseparable work together. When a product can remain accepted while cross-product roadmap closeout remains pending, expose that restartable seam instead of burying both states in one execution outcome.
   - Preserve the accepted parent plan as the source of truth; child or branch plans must name their parent, scope, non-scope, retained state, entry conditions, and exit criteria.

4. Validate and hand off.
   - Run the smallest meaningful validation that covers the changed behavior and relevant safety invariant.
   - When an aggregate gate already includes the relevant focused check, run only the aggregate gate. Run a child separately only to diagnose a failure or when the user or repository explicitly requires separate evidence. Add a preflight（预检）only when it controls a recurring mechanical failure.
   - Treat a passing result as current until a relevant validation input changes; do not rerun it solely for ceremony or handoff.
   - Review the diff, then report outcome, material files, validation, remaining risk, and next required decision.

## Reasoning-Mode Routing

- In the main workspace, use `xhigh` for relatively simple, bounded tasks. Once meaningful complexity appears, recommend Max or Ultra according to task shape; treat them as peer primary modes.
- Recommend Max when the dominant challenge is deep serial reasoning, tightly coupled diagnosis, long causal continuity, difficult plan closure, or a stable decomposition whose bounded parallel work must feed one coherent causal or decision chain.
- Recommend Ultra when adaptive orchestration across meaningful investigation, implementation, testing, or review streams can improve coverage or progress because decomposition is uncertain, evolving, or dominated by separable parallel work. Apply the same proportionality rules: do not multiply agents, safeguards, documents, or validation without a concrete benefit.
- Treat mode choice and agent topology as separate decisions. Max and Ultra may both use multiple subagents and parallel writes. Delegate by independent questions, hypotheses, or verifiable outputs rather than directories; distribute decision or write authority across coherent ownership, acceptance, and recovery boundaries.
- Recommend a staged Max/Ultra combination only when the task genuinely changes shape across a restartable handoff, and state the switch condition. Preserve Codex's ordinary discretion over delegation, coordination, and writing.
- Do not impose read-only or single-writer defaults. Consider a temporary Max single-writer recovery slice only after repeated coupled failures, persistent validation deadlock, or cyclic breakage where repairing one surface repeatedly damages another; end the restriction once the causal loop is closed and validated.
- Treat mode choice as workflow guidance, never as evidence of correctness, safety, authority, or completion.

## Five Tiers

- **Tier 1:** scratch, minitoy, or disposable work.
- **Tier 2:** durable low-impact project.
- **Tier 3:** confidential or production app with limited direct harm. `learningWordsformimi` is the reference ceiling while it lacks material account or economic authority.
- **Tier 4:** high-consequence read-only or advisory system. Current `autoadvisor` is the reference shape; reuse its proven guards instead of adding a generic allowlist（白名单）without a concrete gap.
- **Tier 5:** live trading, transfers, withdrawals, material payments, bulk account actions, or other material or scalable authority. Permit valid action inside an approved execution envelope; block or escalate invalid or out-of-envelope action.

Judge tiers by maximum credible single and cumulative impact, third-party effect, and reversibility. Credentials, external APIs（外部接口）, confidential data, or production infrastructure alone do not set the tier. Prefer hard limits and runtime guards over paperwork, and preserve designed cancellation or risk-reducing paths during degraded Tier 5 operation.

## Durable Artifacts

Retain governance artifacts that support continuity, but keep each one focused.

- `AGENTS.md`: concise rules, tier, permanent boundaries, canonical-doc pointers, and aggregate validation commands; keep history and transient status elsewhere.
- `ARCHITECTURE.md` or `PROJECT_MAP.md`: current structure, module responsibilities, data flow, safety and deployment boundaries.
- `plan_docs/`: accepted scope, decisions, sequencing, exit criteria, and known non-scope for complex or multi-session work.
- `CHANGELOG.md` and `governance/AI_AGENT_LOG.md`: concise reasons, outcomes, validation, and safety notes when the project uses them for continuity.
- `governance/preflight` scripts: mechanical checks for stable invariants; they should not infer nuanced human risk judgments.
- `docs/` evidence files: handoffs, source notes, data dictionaries, API scope records, and user decisions.

## Resources

Read `references/governance-patterns.md` when creating governance files, adapting this workflow to a new project, writing templates, or deciding how strict the project should be.

Read `references/preflight-patterns.md` when the user wants automatic governance checks, drift prevention, pre-commit integration, or a reusable local gate.

Read `references/evaluation-scenarios.md` only when evaluating or revising this skill's behavior across representative project types.

Read `references/stage-sizing.md` when creating or revising a complex multi-stage plan, handling a recovery branch, or deciding whether one stage spans too many independent responsibility or recovery domains.

Read `references/reasoning-mode-routing.md` when recommending xhigh, Max, Ultra, or a staged combination for an important or complex main-workspace task, or when mode choice needs recovery routing after repeated failure.

Read `references/graph-governance.md` only when the user explicitly asks for graph governance, an accepted plan calls for a shadow graph pilot, or a repository graph manifest is needed for the current task's cross-surface impact, recovery, authority, lineage, or freshness question. The presence of a manifest alone does not activate graph workflow for a bounded task. Treat graphs as optional derived indexes; do not introduce graph files, hooks, gates, or services merely because this skill is active.

Use `scripts/governance_preflight_template.py` as a starting point. Copy it into the target project, usually as `governance/preflight.py` or `governance/agent_preflight.py`, then tune paths, risk terms, and strictness. Do not replace a proven project-specific gate merely to standardize on this generic template.
