# Preflight Patterns

Current skill version: `human-ai-governance v0.7.7`

Use this reference when a project needs automatic checks to prevent governance drift. The bundled `scripts/governance_preflight_template.py` is a starting scaffold, not a universal law. Copy it into the target repository and tune it to the project's tier（层级）, filenames, architecture docs, and credible side effects. Preserve a stronger proven project-specific gate instead of replacing it for consistency alone.

## Contents

- [What Preflight Should Catch](#what-preflight-should-catch)
- [Material and Architecture Boundaries](#material-and-architecture-boundaries)
- [Recommended Installation](#recommended-installation)
- [Tier Guidance](#tier-guidance)
- [Strict Side-Effect Scanning](#strict-side-effect-scanning)
- [Pre-Commit Wrappers](#pre-commit-wrappers)
- [Upgrade Routine](#upgrade-routine)

## What Preflight Should Catch

Use tier-aware checks:

- every tier: accidental `.env` tracking and likely token/private-key patterns in changed staged-index, unstaged, and untracked content
- Tier 2 through Tier 5: changed material files without the configured changelog update, when the project maintains a changelog
- Tier 3 through Tier 5: changed material files with a missing or stale AI log, incomplete latest log entry, module-topology or migration changes without architecture sync, or child plans without `Source plan` / `Derived from`
- optional strict mode: project-specific risky side effects in executable runtime paths
- optional indexed-plan mode: project-specific checks for unique plan IDs and paths, valid state values, resolvable parent and status-owner links, and lineage cycles after the repository adopts a stable index contract
- marker mode: missing or stale `Generated/adapted from human-ai-governance vX.Y.Z` marker
- advisory only: a changed root `AGENTS.md` that is approaching or exceeds the common project-document byte budget

Keep automatic checks mechanical. Do not ask a generic script to infer whether an economic limit is appropriate, whether a trade thesis is sound, or whether confidential exposure is materially harmful. Record those judgments in project governance and test the resulting technical limits.

Do not require a plan index in every repository or infer `complete`, `consumed`, or `evidence_only` from file contents. The generic preflight template does not enforce plan-index lifecycle. Add a project-specific index check only after routing ambiguity is recurring, the project has adopted stable fields and state values, and the check can validate structure without deciding semantic completion or authority.

Do not turn audience-facing style or technical-language choice into a generic preflight gate. Phrase or jargon counts, word blacklists, reading-level scores, regular expressions for constructions such as “not X, but Y,” punctuation or list quotas, and AI-detector scores cannot reliably decide whether prose fits its audience, whether `plain` preserved meaning, or whether an engineering constraint is necessary. Use semantic review and, for presentations, inspect the rendered artifact. Enforce a mechanical format requirement only when the target project has an explicit stable contract for it.

Do not make the generic preflight infer completion persistence, retry equivalence, cumulative consequence, exhausted recovery authority, or whether another attempt is authorized. Attempt numbers and words such as `retry` or `attempt` do not prove risk. Keep this classification semantic and enforce only explicit project-specific execution limits that have a stable machine-readable contract.

Review density is also semantic. Do not add word-count, line-count, jargon-quota, required-heading, or shortening-percentage gates for `compact` or `expanded`. Check that decision-relevant information survives; exact artifact formats remain governed by their own contracts.

Fail when Git repository state cannot be inspected. Use NUL-delimited status records so Unicode, whitespace, rename, and copy paths remain exact. When staged and working-tree content differ, validate each changed snapshot without printing matched secret values.

## Material and Architecture Boundaries

The v0.5 line deliberately narrows generic enforcement:

- Runtime source, migrations, deployment or infrastructure files, governance rules, root manifests, and plan docs are material by default.
- README, ordinary docs, tests, lockfile-only churn, architecture docs themselves, changelogs, and AI logs are not automatically material.
- Secret and strict side-effect scanning cover every changed readable staged-index, unstaged, and untracked snapshot, including non-material files for secret scanning.
- Architecture sync is triggered by added, deleted, renamed, or copied runtime modules and by migration changes. A modification inside an existing source file is not automatically structural because a generic script cannot infer semantic responsibility.
- Root or master plans do not need a parent marker. Child and branch plans do.

These are scaffold defaults. Expand `MATERIAL_*` or structure constants when a repository has a known contract that requires it. Keep semantic doc-drift judgment in the model and project review: update a document whenever its current claim would otherwise become false or incomplete.

## Recommended Installation

1. Copy `scripts/governance_preflight_template.py` into the target project, commonly as:

```text
governance/preflight.py
```

2. Tune the project-specific constants:

- `CHANGELOG`
- `AI_AGENT_LOG`
- `ARCHITECTURE_CANDIDATES`
- `PLAN_DOC_PREFIXES`
- `MATERIAL_EXACT` and `MATERIAL_PREFIXES`
- `STRUCTURE_TOPOLOGY_PREFIXES` and `STRUCTURE_ALWAYS_PREFIXES`
- `RISK_SCAN_PREFIXES`
- `RISKY_SIDE_EFFECT_PATTERNS`

3. Add an explicit tier to the project command. Use the project virtual environment（虚拟环境）interpreter when one exists:

```bash
.venv/bin/python governance/preflight.py --tier 3 --require-skill-marker
```

4. Add strict side-effect scanning only after tuning its runtime paths and patterns to the project's credible risks:

```bash
.venv/bin/python governance/preflight.py --tier 5 --strict-side-effects --require-skill-marker
```

When strict mode finds an expected action path, review the current diff and acknowledge that path explicitly:

```bash
.venv/bin/python governance/preflight.py \
  --tier 5 \
  --strict-side-effects \
  --reviewed-side-effect-path src/execution/order_router.py \
  --require-skill-marker
```

`--reviewed-side-effect-path` records code-review acknowledgement only. It does not authorize a live order, replace the execution envelope, or belong as a permanent bypass in an always-on wrapper.

The template deliberately requires `--tier`; it does not silently choose a governance level.

## Tier Guidance

### Tier 1

- Usually skip a dedicated script.
- Run one smoke command or manual check when useful.

### Tier 2

- Use `--tier 2` when a durable project maintains a changelog or benefits from a repeatable light gate.
- Avoid requiring an AI log by default.

### Tier 3

- Use `--tier 3 --require-skill-marker` when a confidential or production app benefits from mechanical plan, log, secret, or topology checks.
- Keep risky-operation scanning optional unless the project has identified a concrete executable risk.

### Tier 4

- Use `--tier 4 --require-skill-marker` alongside the project's existing read-only guard, redaction, connector tests, and final gate.
- Current `autoadvisor` is the reference strength: preserve its project-specific checks and do not add a second generic allowlist（白名单）or repeated approval flow without a demonstrated gap.
- Enable strict scanning only when its patterns add value beyond the existing guard and tests.

### Tier 5

- Use `--tier 5 --strict-side-effects --require-skill-marker` after tuning the scan to executable paths and real action terms.
- A reviewed live-action implementation can pass with one or more `--reviewed-side-effect-path` arguments; unreviewed findings still fail.
- Add project tests for the approved execution envelope（执行范围）, per-action and cumulative limits, degraded-mode cancellation or risk reduction, monitoring, and emergency stop.
- Keep preflight outside the latency-sensitive order path. It validates code and configuration before launch or handoff; runtime guards enforce each live action without preventing valid in-envelope orders.

## Strict Side-Effect Scanning

The generic scanner is intentionally opt-in.

- Scan executable runtime paths such as `src/`, `app/`, `api/`, `lib/`, and `server/` by default.
- Do not scan documentation or tests merely because they mention forbidden operations.
- Do not classify HTTP method alone as authority. Some valid read-only account endpoints use `POST`; evaluate the exact service action or existing project boundary.
- Remove patterns that generate routine false positives.
- Add patterns only for credible operations the project must review, such as live order placement, transfers, withdrawals, payments, or destructive production data actions.
- Treat strict-scan output as a code-review gate. A reviewed path may be acknowledged for the current diff; runtime execution remains governed by the project's permission and limit controls.

## Pre-Commit Wrappers

For a Python project, a small `governance/pre_commit.py` can wrap the configured preflight and tests:

```python
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    py = sys.executable
    steps = (
        ("governance preflight", [py, "governance/preflight.py", "--tier", "3"]),
        ("unit tests", [py, "-m", "unittest", "discover", "-s", "tests"]),
    )
    for label, command in steps:
        result = subprocess.run(command, cwd=root, check=False)
        if result.returncode != 0:
            print(f"FAIL: {label}")
            return result.returncode
    print("PASS: local pre-commit checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

For JavaScript / TypeScript projects, wrap the same preflight with package scripts and point the command at the available Python virtual environment when practical:

```json
{
  "scripts": {
    "governance:preflight": "python governance/preflight.py --tier 3 --require-skill-marker",
    "check": "npm run governance:preflight && npm test"
  }
}
```

Expose the wrapper as the aggregate local gate and run it once. Do not separately rerun its preflight and test children unless a failure needs diagnosis or separate evidence is required.

## Upgrade Routine

When `human-ai-governance` changes version:

1. Read the target project's existing marker and governance files.
2. Compare the marker with the current skill version.
3. Inspect only the changed capability area and current effective authority.
4. Explain a migration plan and wait for agreement before editing the project.
5. Update project governance files, copied preflight code, and local commands together.
6. Record the upgrade in the target project's changelog or AI log and rerun the final local gate.

For a `v0.3.0` to `v0.4.0` migration, the five-tier classification normally stays unchanged. Review the narrowed material and topology defaults, identify the project's aggregate validation command, exempt genuine root plans from parent markers, and decide whether strict findings need a project-specific rule or current-diff acknowledgement.

For a `v0.4.0` to `v0.5.0` migration, the five-tier classification and mechanical preflight defaults remain unchanged. Review only the new semantic stage-sizing guidance and optional graph-governance protocol. Do not require graph files, add graph checks, or copy a generic graph implementation merely to update the marker. Migrate a project's copied preflight and marker only after its own read-only inspection, plan, and approval.

For a `v0.5.0` to `v0.5.1` migration, the governance model remains unchanged. The generic preflight now fails when Git inspection fails, parses exact NUL-delimited paths, and checks changed staged-index plus working-tree snapshots. Review project-specific staged-content logic before replacing it; retain a stronger local implementation when one already exists.

For a `v0.5.1` to `v0.6.0` migration, the five-tier model and mechanical preflight behavior remain unchanged. Review the new main-workspace reasoning-mode routing separately: `xhigh` serves relatively simple work, while meaningful complexity routes to Max or Ultra by task shape. Do not add preflight checks for model choice, agent count, read-only operation, or single-writer execution. Temporary single-writer recovery remains a model judgment after concrete repeated-failure evidence, not a mechanical repository invariant.

For a `v0.6.0` to `v0.6.1` migration, the five-tier model and mechanical preflight behavior remain unchanged. The routing reference now separates task-topology certainty from agent and authority topology. Do not add preflight checks for mode, agent count, delegation boundaries, parallel writing, authority distribution, or single-writer recovery; these remain contextual workflow judgments.

For a `v0.6.1` to `v0.7.0` migration, Tier 1-5 remains the only classification and the generic preflight behavior remains unchanged apart from the version marker. Review the new proportional-assurance guidance for evidence reuse, claim-scoped invalidation, boundary-owned controls, platform-permission deference, and conditional component reuse. Keep these as contextual judgments: do not add generic script checks for validation density, defensive-programming style, platform access mode, dependency choice, or evidence sufficiency.

For a `v0.7.0` to `v0.7.1` migration, the five-tier model, authority boundaries, and generic preflight behavior remain unchanged apart from the version marker. Review the new writing-mode route only where the project produces audience-facing prose or presentations. Keep functional engineering documents under engineering governance, route mixed deliverables by content unit, and do not add phrase bans, punctuation quotas, or AI-detector gates.

For a `v0.7.1` to `v0.7.2` migration, the writing-mode route, five-tier model, authority boundaries, and generic preflight behavior remain unchanged apart from the version marker. Review the new explicit `default` / `plain` technical-language choice only where users need control over unexplained terminology. Keep it independent from writing mode and engineering capability; do not add jargon counts, word blacklists, reading-level scores, regular expressions, or detector gates.

For a `v0.7.2` to `v0.7.3` migration, the five-tier model, writing and terminology routes, authority boundaries, and generic preflight behavior remain unchanged apart from the version marker. Review plan-index routing only where nested, parallel, multi-session, or retained historical plans make the current entry ambiguous. Keep the index a compact routing read model, preserve evidence-bound paths, and add a mechanical index checker only when the target repository has an explicit stable contract for it.

For a `v0.7.3` to `v0.7.4` migration, the five-tier model, plan-index route, writing and terminology routes, and generic preflight behavior remain unchanged apart from the version marker. Review any rule that treats a new attempt as automatically requiring approval. Keep safe diagnosis, repair, validation, and preparation active under an explicit persistent-completion request; retain renewed approval only for consequence-bearing execution outside its accepted single or cumulative envelope. Do not add generic attempt-count, retry-word, or persistence-mode checks to preflight.

For a `v0.7.4` to `v0.7.5` migration, keep the five-tier model, reasoning and writing routes, explicit terminology choice, plan routing, recovery authority, and generic preflight behavior unchanged apart from the version marker. Add the compact conversational review rule to the existing collaboration instructions under a separately approved project migration, while retaining full formal records and exact evidence and authorization boundaries. Honor existing standing plain-language preferences. Do not introduce length, jargon, heading, or review-density script gates, and do not infer that a new global skill version updated existing project adapters.

For a `v0.7.5` to `v0.7.6` migration, review active-task continuity and any fixed graph-rebuild status wording. Preserve in-scope progress across side questions, reconcile already-started operations on cancellation or replacement, and report rebuild authority and results from actual evidence. Keep the existing governance model and generic preflight behavior unchanged apart from the version marker; no new script gate or downstream migration follows from this global update.

For a `v0.7.6` to `v0.7.7` migration, carry valid existing agreement and external-action authorization into later steps. In copied templates, qualify renewed approval by an out-of-envelope action or an unsatisfied approval or renewal condition. Preserve one-shot limits, expiry, cumulative limits, and platform gates. The generic preflight changes only its version marker; update a project's marker after its actual rules have been synchronized, not as a substitute for that migration.

Under the accepted reference classifications, `learningWordsformimi` remains Tier 3 while it lacks material economic or account authority, current read-only `autoadvisor` remains Tier 4, and a future live-trading quant system is Tier 5.

Do not auto-migrate existing projects merely because the global skill changed. Each project needs its own read-only inspection, tier decision, plan, and approval.
