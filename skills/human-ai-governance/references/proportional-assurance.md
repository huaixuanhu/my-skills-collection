# Proportional Assurance

Current skill version: `human-ai-governance v0.7.9`

Use this reference when considering an additional safeguard, validation is expensive, prior evidence may still be valid, architecture or authority boundaries are involved, defensive controls may overlap, platform permissions need to be separated from project authorization, or a complex capability may reuse an existing component.

## One Tier Model, Contextual Questions

Tier 1-5 remains the only governance classification. Choose it from effective authority, credible consequence, reversibility, cumulative impact, and third-party effect.

Use the following as contextual questions without assigning levels, scores, or a second taxonomy:

- Which behavioral, data, safety, or operational claim can this change affect?
- Does the change cross a trust, authority, representation, persistence, or irreversibility boundary?
- Which existing evidence is still bound to the same subject and relevant inputs?
- Does the next action remain local and inside the accepted scope, or does it require project approval or a platform approval?

Complexity, data volume, cloud infrastructure, and long task duration can increase orientation and evidence-management needs. They do not determine the tier by themselves.

## Bind Evidence to Claims

Useful validation evidence identifies enough of the following to decide whether it remains current:

- the claim proved and its acceptance rule;
- the code, artifact, configuration, or service version being evaluated;
- the relevant input, dataset, manifest, partition set, or source snapshot;
- the interface, schema（数据结构约定）, unit, time, null, ordering, and other semantic contracts involved;
- the validator, test, query, review procedure, or policy version;
- the environment facts that can change the result, including freshness for mutable external state.

Exact hashes are useful for immutable artifacts but are not mandatory for every claim. A stable release identifier, dataset manifest, partition inventory, migration version, or deployment identity can be the cheaper binding when it is strong enough for the stated conclusion.

Reuse passing evidence while every element relevant to its claim remains unchanged. When one element changes, invalidate that claim and its affected dependants rather than unrelated evidence. A failed or inconclusive result is not passing evidence.

Examples:

- A consumer-only code change can reuse an accepted upstream dataset receipt and validate the changed consumer.
- A schema, unit, timezone, missing-value, ordering, or upstream transformation change reopens the affected contract and downstream claims.
- A documentation or UI change does not invalidate data-quality evidence unless it changes the meaning presented to a user or the acceptance claim.
- A source snapshot can remain reproducible while its statement about current live conditions expires; keep reproducibility and freshness as separate claims.

## Select Sufficient Validation

Choose validation from the affected claim and boundary. Validation options are not cumulative levels.

Exercise the behavior relevant to the claim and, for a repair, check whether the original problem is resolved. Intermediate observations and test doubles support only the behavior they actually establish; state what remains unverified. This does not require a full production workflow for every change.

| Change shape | Sufficient evidence direction |
| --- | --- |
| Local contract-preserving edit | Focused syntax, unit, or smoke evidence for the changed behavior |
| Shared interface or schema change | Contract and round-trip evidence plus affected consumers |
| Data-source or transformation change | Source identity, semantic and integrity checks, then affected downstream claims |
| Auth, credential, network, persistence, or deployment boundary | Boundary tests, failure behavior, rollback or recovery evidence, and required approval |
| Live material-action capability | Execution-envelope, hard-limit, degraded-mode, monitoring, and controlled activation evidence |

For large datasets:

- Use manifests, partition identities, stratified samples, invariants, and stage receipts when they prove the required claim without rescanning every record.
- Run a full scan, rebuild, replay, or expensive backfill when the affected claim truly depends on complete coverage, relevant upstream bytes or semantics changed, or an explicit acceptance gate requires it.
- State the ceiling of sample-based, synthetic, offline, or design-only evidence. Do not promote it to full-data, live, production, performance, or training authority.
- Let downstream stages consume accepted upstream evidence and validate their own transformation or decision logic.

An assurance slice is complete when every affected acceptance claim and permanent safety invariant has current sufficient evidence, the diff and side effects are understood, and no unresolved required approval remains. More checks need a new affected claim, invalidation trigger, failed evidence, or explicit repository requirement.

## Place Defensive Controls at Their Owners

A control earns its place by naming the failure it owns and the boundary where it can prevent or contain that failure.

Common control-owning boundaries include:

- external or untrusted input entering a trusted component;
- advice becoming an account, payment, deployment, or trading action;
- one representation becoming another, such as API payload to domain object or source data to derived feature;
- transient state becoming durable or externally visible;
- a reversible workflow crossing into an irreversible or costly action.

Within one boundary, prefer one canonical validator, normalizer, retry policy, or guard. Independent layers remain appropriate when they control different failures or one layer must contain the failure of another. For example, a Tier 5 preflight can review an order path while a runtime limit still constrains each live order.

During review, ask:

- Which plausible failure becomes less controlled if this branch, guard, retry, fallback, or compatibility path is removed?
- Does an upstream contract already guarantee the same condition within the same trust boundary?
- Does this layer fail visibly and preserve the correct claim ceiling, or can it silently convert an error into misleading success?
- Is the duplication independent defense-in-depth（纵深防御）, or the same check repeated without a separate owner?

## Human Choice Before Added Safeguards

A safeguard can address a plausible failure and still be an unresolved design trade-off. Before implementing an additional mechanism that introduces system paths, operating burden, or ongoing maintenance beyond the accepted design, present the choice and wait for the user's decision. This includes proposed retry or fallback machinery, compatibility branches, repeated validation, backup systems, background recovery, and extra approval steps when they add those obligations. Judge the added behavior and cost, not line count, model identity, or a tier label alone. Several individually small additions can form one material expansion.

Give a concise, concrete account of:

- the failure being addressed, the evidence or uncertainty, and its credible impact on this project's affected surface;
- existing protections, the remaining gap, and the exact owner rule if a safeguard is claimed to be required;
- the proposed addition and its behavior, operating, testing, dependency, and maintenance costs;
- the simplest acceptable alternative, the residual risk with each choice, and a recommendation. Keeping the current design or deferring an optional addition can be valid choices.

An announcement, silence, or a general request to make something robust is not agreement to an undisclosed expansion. Wait before implementing or scaffolding the proposed addition, while continuing independent work inside the accepted scope. Once the user chooses, carry that choice forward without asking again unless the relevant facts or scope materially change. If an optional addition is declined, preserve the agreed simpler design; do not treat that choice as a failed acceptance check or repeatedly propose the same layer without new evidence. Record a consequential choice in the existing plan or design owner when continuity needs it, without creating another approval registry.

Ordinary error handling that preserves the intended contract, explicitly required controls, and implementation of already-approved safeguards do not need a new choice. For example, a clear save-error message can remain an ordinary repair; adding a durable retry queue and recovery worker introduces a design decision. Reusing an accepted backup procedure does not authorize building a new backup subsystem. Calling added machinery an error handler does not exempt it from the decision.

Preserve existing safety invariants and the platform's effective restrictions. Name a concrete governing requirement when one makes a control mandatory; “safer” or “best practice” alone does not do so. If a newly discovered gap prevents safe completion within the agreed design, pause only the affected operation and explain the smallest viable remedy or scope reduction. Do not silently build a larger protection system, offer bypassing a mandatory boundary, or remove existing controls to make the project simpler.

Keep this as a design conversation. Do not add safeguard counters, keyword checks, risk scores, or another preflight gate to automate the judgment.

## Reuse or Build

For a complex, shared, security-sensitive, infrastructure, protocol, or maintenance-heavy capability, inspect suitable existing project capabilities, platform services, standard-library support, and maintained open-source components before building it from scratch.

There is no mandatory preference order. Compare:

- functional and operational fit;
- maintenance health and upgrade path;
- security, provenance（来源）and supply-chain exposure;
- licence and redistribution constraints;
- integration, observability, migration, and exit cost;
- the amount of custom glue still required.

Simple local glue, narrow domain logic, or a small well-tested transformation may be safer and cheaper to implement directly than adding a dependency. Record the choice only when it is material to architecture, maintenance, safety, or future handoff.

## Platform Permission and Project Authorization

The platform's current effective sandbox（沙盒）, approval policy（审批策略）, connector（连接器）, and access configuration is authoritative and outside this skill's control.

- If the platform requires approval, wait for it. An accepted project plan does not bypass that gate.
- If the platform configuration permits an action without approval, do not create a pause solely to imitate a stricter platform configuration.
- Platform-granted technical capability is not blanket task authorization. Preserve the user's scope and project-specific gates for consequential external actions such as push, deployment, production mutation, cutover, retirement, live trading, or material cost.
- One accepted plan covers ordinary local implementation decisions inside its scope. Reopen human agreement for material scope expansion, unresolved choices that change the result, consequential external action, or an explicit project gate.

## Persistent Completion and Recovery

When the user explicitly asks the agent to continue until a verifiable outcome succeeds, keep the accepted objective and safe in-scope recovery active after a failed attempt. Separate ordinary diagnosis, repair, validation, checkpointing, resume, and preparation from the next action that can create material consequences.

Classify a retry by whether it changes maximum credible single or cumulative impact, authority, accepted state, success criteria, cost, external side effects, or the execution envelope. Attempt number alone is not a new approval boundary. Even when another live or destructive run needs renewed authority, continue safe recovery up to that exact boundary. Read `persistent-completion.md` for the full route and recording pattern.

## Keep Presentation and Control Placement Separate

Audience-facing expression may place a necessary caveat close to the claim it qualifies and remove repeated prose that adds no new reader protection. This editorial placement applies only to the presentation layer.

Operational sources of truth retain constraints wherever independent execution, reproduction, review, approval, or recovery depends on them. A style revision is never evidence that a control, validation, disclosure, or authorization boundary is redundant. Judge those elements by their owned failure mode and functional entry point.

## Representative Project Shapes

| Project shape | Low-friction path | Boundary that retains stronger assurance |
| --- | --- | --- |
| Large research or data pipeline | Reuse immutable stage receipts and validate affected consumers | Source semantics, schema, lineage（数据血缘）, publication, remote write, or expensive recomputation |
| Read-only financial or other high-consequence advisory system | Preserve proven read-only guards and one aggregate gate | New account authority, private action endpoints, consequential calibration, or misleading evidence |
| Personal cloud or trading infrastructure | Continue approved local code, documentation, simulation, and focused tests | Credentials, public exposure, remote service mutation, single-writer change, cutover, retirement, or live action |
| Production web application | Keep visual, copy, and local component work focused | Auth, privacy, schema migration, backup or restore, payment, and production deployment |
| Institutional workflow | Keep learning material and bounded internal prototypes proportionate | Confidential client data, external submission, delegated business decisions, payments, or legal execution |
| Shared model-training package | Keep richer controls local to the owned package and consume frozen data evidence | Shared contracts, dependency installation, cloud writes, costly training, and activation of executable stages |

These shapes guide reasoning; they do not add tiers or replace the target repository's current facts and rules.
