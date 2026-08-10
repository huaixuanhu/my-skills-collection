# Governance Patterns

Use this reference when the task needs concrete templates or a stricter tier decision. Keep final project files shorter than these templates when the project is small.

Current skill version: `human-ai-governance v0.6.1`

When adapting this skill into a project, write this marker into `AGENTS.md` or another durable governance file:

```text
Generated/adapted from human-ai-governance v0.6.1
```

## Contents

- [Tier Decision Workflow](#tier-decision-workflow)
- [Tier Checklist](#tier-checklist)
- [Task Scope and Model Discretion](#task-scope-and-model-discretion)
- [Proportionality and Convenience](#proportionality-and-convenience)
- [Economic and Account Consequences](#economic-and-account-consequences)
- [Tier-Specific Governance](#tier-specific-governance)
- [Governance Templates](#governance-templates)
- [Validation Ladder](#validation-ladder)
- [Examples](#examples)
- [Handoff Summary](#handoff-summary)

## Tier Decision Workflow

Record these values before material work when they affect the decision:

- `Project tier`: the highest authority and credible consequence already present in the running project.
- `Current authority on the affected surface`: what the code, data, account, or workflow being changed can do now.
- `Target capability tier`: the authority introduced or designed by the current work.
- `Working tier`: the higher of the current and target authority on the affected surface.

Classify effective capability rather than project labels or distant roadmap ideas. A Tier 5 repository can use lighter task procedure for a documentation typo outside its protected surfaces, while permanent Tier 5 invariants still apply. Code that designs or enables a higher-risk capability uses the higher working tier before that capability is deployed.

If account permissions are unknown, use a temporary cautious gate while verifying them. Do not make that temporary state permanent: downgrade promptly after evidence confirms a narrower boundary.

## Tier Checklist

Ask these questions before choosing governance strength:

1. What can the running system actually read, change, send, deploy, spend, delete, or authorize?
2. What new authority will the current task introduce, even if it is initially disabled?
3. Can a mistake cause confidential exposure, material economic loss, safety or legal harm, account loss, irreversible data damage, or broad service disruption?
4. What is the maximum credible single-action and cumulative or bulk impact?
5. Does a hard technical limit constrain that impact, or does the project rely only on intended usage?
6. Is the effect reversible, refundable, restorable, or compensable?
7. Does the action affect only the owner or also customers, counterparties, or other third parties?
8. Which existing guard, test, approval, or backup already controls each credible risk?

Suggested mapping:

| Tier | Effective project shape | Minimum governance |
| --- | --- | --- |
| 1 | scratch script, minitoy, disposable experiment | short plan or notes and one smoke test when useful |
| 2 | durable low-impact local app, small tool, low-sensitivity persistent data | concise `AGENTS.md`, architecture map, repeatable validation, changelog when continuity needs it |
| 3 | confidential or production web app with limited direct harm, cloud database, ordinary credentials | data and secret boundaries, explicit approval for meaningful production changes, backup or rollback thinking, proportionate preflight and handoff |
| 4 | high-consequence read-only or advisory system, sensitive financial/medical/legal/identity data, tightly capped reversible real-money action | Tier 3 controls plus a verified authority boundary, provenance, redaction, evidence-backed tests, and project-specific safety guards |
| 5 | live trading, transfers, withdrawals, material payments, bulk account actions, or other material/scalable economic, legal, safety, or irreversible authority | approved execution envelope, hard limits, runtime enforcement, monitoring, emergency behavior, audit evidence, and rollback or compensation planning |

Confidential data alone does not automatically require Tier 4. A small private web app whose plausible exposure has limited material consequences can remain Tier 3. Data whose exposure can predictably cause serious financial, medical, identity, legal, or safety harm can justify Tier 4 even without write authority.

## Task Scope and Model Discretion

Use the workflow as a set of decision rules. A capable model may omit a step when all of the following are true:

- the step is not required by local repository instructions;
- it does not protect a credible failure mode touched by the task;
- omitting it does not make a canonical document stale;
- the task remains inside an already accepted scope.

Do not produce a long explanation for every skipped step. State the exception only when it changes safety, evidence quality, or user expectations.

One accepted plan covers ordinary local implementation decisions inside its declared scope. Ask again only for a material scope expansion, a consequential external action, an unresolved choice that changes the result, or an explicit repository approval gate.

Examples:

- A CSS or wording fix does not need architecture sync merely because it occurs in a Tier 5 repository.
- A new order-routing branch is Tier 5 work even if live mode remains disabled, because it designs material authority.
- A test-only refactor that preserves the tested contract can omit changelog and architecture updates unless the project explicitly requires them.
- A database migration remains material even when the diff is short.

## Proportionality and Convenience

Use the lightest governance that adequately controls credible harm.

- Require each gate to name the failure mode it controls.
- Avoid duplicate approval, logging, or documentation when an existing technical control already covers the risk.
- Prefer one aggregate validation command when it already runs the required child checks.
- Keep `AGENTS.md` as a concise routing map. Put stage history, test counts, and transient implementation status in canonical plans, changelogs, or logs.
- Allow local, read-only, reversible, low-impact operations without repeated human confirmation.
- Prefer hard limits, permission separation, deterministic tests, and runtime guards over additional paperwork.
- Treat credentials, production infrastructure, external APIs（外部接口）, or automation as risk evidence to inspect, not automatic reasons for the highest tier.
- Tune or remove a gate that repeatedly blocks safe work without catching credible risk.
- Reclassify downward when risky authority is removed or a previously uncertain permission is proven narrower.
- Keep Tier 4 close to the proven `autoadvisor` operating model: existing read-only guards, endpoint or method boundaries where needed, confirmation for real account calibration, redaction, tests, logs, and a local final gate. Do not impose a new cross-project allowlist（白名单）or per-request approval system without a concrete gap.

## Economic and Account Consequences

Judge payment, account, and administrative capabilities by consequences rather than feature names alone.

- Sandbox（沙盒）, simulated funds, or test accounts with no real economic consequence usually remain Tier 3 or below.
- A real-money action that is technically hard-capped to a small amount, easily reversible or refundable, non-bulk, and unable to scale silently may be Tier 4.
- A single action or cumulative/bulk sequence that can cause material economic loss is Tier 5.
- A reversible action on the owner's private test account does not automatically become Tier 5.
- Bulk suspension, deletion, or loss of access affecting customer assets, income, business continuity, or many third parties is Tier 5.
- Live trading, transfers, and withdrawals normally qualify for Tier 5 because loss can accumulate even when each individual action is modest.

Do not define “material” only in prose. For Tier 5, record project-specific limits using appropriate measures such as absolute value, percentage of account equity, maximum position, daily cumulative amount, daily loss, affected account count, or service downtime.

## Tier-Specific Governance

### Tier 1

- Keep documentation minimal.
- Use a short plan only when the work has more than one meaningful step.
- Run a smoke test or manual check when it provides real confidence.
- Skip a dedicated AI log and governance script unless the user explicitly wants them.

### Tier 2

- Maintain concise collaboration rules and a current architecture map.
- Add repeatable validation commands.
- Use a changelog when work spans sessions or future maintainers need reasons.
- Keep preflight optional unless persistent data or collaboration continuity makes it useful.

### Tier 3

- Document data, credential, network, deployment, and production boundaries.
- Require human agreement for meaningful production, credential, migration, or destructive data changes.
- Use secret scanning, backup or rollback thinking, and an AI log when work spans sessions. Add a local preflight when it prevents a recurring mechanical failure.
- Do not add Tier 4 account-connector controls when the project lacks comparable authority or consequence.

### Tier 4

- Preserve a verified read-only, advisory, or tightly bounded authority boundary.
- Reuse proven project-specific guards and tests before adding generic machinery.
- Verify real account or high-consequence access with the smallest approved calibration.
- Protect credentials and sensitive outputs through redaction and controlled local storage.
- Record data provenance（数据来源）, incomplete evidence, and uncertainty when outputs can influence important decisions.
- Keep humans responsible for consequential decisions the system cannot execute.

### Tier 5

- Use policy-constrained execution（策略约束执行）, not an unconditional block on live action.
- Define the approved execution envelope: accounts, instruments or targets, action and order types, per-action and cumulative limits, time windows, environments, and required health checks.
- Permit valid in-envelope actions without repeated approval when the human has explicitly approved that automation policy.
- Block or escalate missing, invalid, or out-of-envelope actions and report the exact reason.
- Under degraded safety conditions, block new risk while preserving explicitly designed cancellation or risk-reducing operations such as `reduce-only`（只减仓）orders.
- Test with fixtures, simulation, paper or shadow mode, then limited live scope before broader activation.
- Maintain monitoring, emergency stop, audit evidence, idempotency（幂等控制）, and rollback or compensating-action plans.
- Separate development, test, and live credentials and environments.

## Governance Templates

### AGENTS.md Template

```markdown
# AGENTS.md

<!-- Generated/adapted from human-ai-governance v0.6.1 -->

## Collaboration

- Use low-hallucination mode. Verify uncertain or drift-prone facts from source.
- Plan before material changes. One accepted plan covers safe local work inside its scope.
- Protect user changes. Do not revert unrelated work.
- Skip irrelevant process; preserve explicit rules and controls tied to credible harm.

## Project Map

- Runtime / virtual environment:
- Architecture entrypoint:
- Active plan / status entrypoint:
- Aggregate validation command:
- Project tier:
- Tier rationale:

## Permanent Boundaries

- Allowed side effects:
- Forbidden side effects:
- Credential handling:
- Data persistence policy:
- Economic or account limits, if applicable:

## Decision Rules

- Read only the canonical sources relevant to the task.
- For material work, state scope, non-scope, validation, and affected authority.
- Update a document only when its current claim would become stale.
- Run the aggregate gate once; rerun child checks only for diagnosis or separate evidence.
- Pause for material scope expansion, consequential external action, unresolved material choices, or an explicit approval gate.
```

### Plan Doc Header

Use this for child plans or branch plans to avoid plan drift.

```markdown
# <Project> <Stage or Branch>: <Topic>

Created:
Last updated:

Source plan:
- `<path/to/parent-plan.md>`

Derived from:
- `<path/to/related-plan-or-architecture.md>`

Input evidence:
- `<path/to/evidence-or-handoff.md>`

Consumer / next stage:
- `<path/to/future-plan.md>`

Document nature:
This is a derived design / implementation plan for <scope>. It is not an independent peer plan.

Project tier:
Current authority on affected surface:
Target capability tier:
Working tier:

## Scope

## Non-Scope

## Safety / Side Effects

## Exit Criteria
```

### Changelog Entry

```markdown
## YYYY-MM-DD HH:MM ZZZ

- Changed <thing>.
- Updated <doc/test/command>.
- Reason: <why this change exists, not only what changed>.
```

### AI Agent Log Entry

Use for Tier 3 through Tier 5, or any project where future agents need traceability.

```markdown
## YYYY-MM-DD HH:MM ZZZ

- Task: <what the agent was asked to do>.
- Plan agreed: <yes/no/implicit/read-only inspection>.
- Working tier: <1-5 and brief rationale>.
- Changed files:
  - `<path>`
- Reason: <why this slice was needed>.
- Validation:
  - Passed: `<command>`
  - Not run: `<command>` because <reason>
- Safety notes: <side effects, authority boundary, credential/data handling, and limits>.
```

### Side-Effect Boundary Template

```markdown
Allowed:
- Read local source files.
- Write project files under <paths>.
- Write generated local artifacts under <ignored path>.
- Call <service> through <approved mode or execution envelope>.

Forbidden or approval-gated:
- Read or expose credential values outside the approved path.
- Mutate production data outside the agreed scope.
- Exceed economic, account, or bulk-action limits.
- Create long-running automation or deploy publicly without the required agreement.
```

For light projects, translate the same idea into a shorter “What this project may touch” section.

## Validation Ladder

Pick the lowest rung that gives real confidence, then add higher rungs as credible harm grows.

1. Read-only inspection: source review and state checks.
2. Tiny local change: syntax check or one smoke command.
3. Durable app change: unit tests plus lint/format if present.
4. Data or persistence change: migration or round-trip test, backup/export thought, and data-integrity checks.
5. Confidential or production change: secret check, staging or preview validation, rollback route, and explicit approval for meaningful live changes.
6. High-consequence read-only connector: fake tests first, existing guard or exact boundary where needed, redaction, failure downgrade, and approved minimal live calibration.
7. Material-action system: simulation, execution-envelope tests, hard-limit tests, degraded-mode behavior, monitoring, emergency stop, and limited live acceptance.

If an aggregate project command already covers the applicable rungs, run it once. Do not separately rerun every nested command unless diagnosing a failure or preserving distinct evidence.

For Tier 3 through Tier 5, read `preflight-patterns.md` and adapt `scripts/governance_preflight_template.py` only when the project lacks a stronger local gate and a mechanical check addresses a recurring failure mode.

## Examples

### Minigame or disposable experiment

Use Tier 1:

- Keep one short run note.
- Validate with a browser smoke test or one command.
- Log only meaningful decisions if the project becomes durable.

### Durable local tool

Use Tier 2:

- Maintain concise collaboration rules and architecture notes.
- Record meaningful changes and repeatable validation.
- Add heavier governance only after persistent or external risk appears.

### Small confidential production web app

Use Tier 3 while direct harm remains limited:

- Protect ordinary credentials and confidential data.
- Separate production and non-production data.
- Require approval for credential, migration, deployment, and destructive production work.
- Keep backup, rollback, and local validation proportional to the small trusted-user scope.
- `learningWordsformimi` is the reference shape while it lacks material economic or account authority.

### High-consequence read-only account tool

Use Tier 4:

- Preserve verified read-only account credentials and runtime guards.
- Use endpoint or method boundaries only where the service requires them.
- Run fixture tests before approved real-account calibration.
- Redact secrets and record safety impact in the existing log and preflight flow.
- Current `autoadvisor` is the reference shape; do not add a second generic control layer without a demonstrated gap.

### Live quant execution system

Use Tier 5:

- Approve an explicit execution envelope before enabling live orders.
- Let valid in-envelope signals place orders automatically.
- Block and report out-of-envelope actions.
- Enforce per-order, position, cumulative exposure, and loss limits mechanically.
- Preserve cancel and designed risk-reduction paths during degraded operation.
- Validate in simulation, paper or shadow mode, limited live scope, then broader live scope.

## Handoff Summary

```markdown
Outcome:
- <what is now true>

Material files:
- `<path>` — <why it changed>

Validation:
- Passed: `<command>`
- Not run: `<reason>`

Remaining risk:
- <known limitation or none>

Next decision:
- <required user choice or none>
```
