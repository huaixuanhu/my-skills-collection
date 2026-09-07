# Research-Task Governance

This governance applies to evidence and reproducibility inside one research task. It does not set repository-wide collaboration tiers or grant execution authority.

## Ownership Boundary

`scaffold-research-task` owns:

- research lifecycle and task architecture;
- experiment dimensions, current comparison scope, aggregation, and scoring identity;
- source, data, configuration, environment, artifact, receipt, evidence, and report responsibilities;
- evidence ceilings and reproducibility fields;
- proportional external-source handling;
- connection points to existing project governance.

`human-ai-governance` or the host project owns:

- project tier and credible-harm classification;
- human approvals and side-effect envelopes;
- parent and child plan lineage;
- reasoning-mode routing and agent authority;
- repository-wide `AGENTS.md`, AI logs, preflight, hooks, and aggregate gates;
- commit, push, tag, deployment, publication, and live-system authority.

## External-Source Proportionality

### Level 1: cite or summarize

Record a stable citation, author or publisher, access date when useful, and limitations. Ordinary literature review and public documentation do not require a source-ingestion gate.

### Level 2: inspect or execute locally

Record source identity and version, inspected or executed surface, dependencies, data or payload exclusions, and known limitations. Check applicable terms when the intended use or host policy makes them material.

A Level 2 checkout may use any host-approved location. Keep it uncommitted when it is not being incorporated, but do not require an outside-repository location without a concrete host, licence, payload, or nested-Git risk.

### Level 3: incorporate or redistribute

Before copying, adapting, vendoring, committing, packaging, or redistributing external material, record licence and provenance evidence plus the integration decision. Escalate unresolved terms only when they affect the intended action.

Do not promote a Level 3 hard stop into a universal rule for Level 1 or Level 2 research.

## Data Boundary

- Record dataset owner or source, snapshot or version, time coverage, schema or contract, integrity reference when material, and permitted use.
- Keep task-specific feature logic separate from shared or upstream data pipelines.
- Distinguish read-only profiling from mutation, migration, transfer, or publication.
- Design train-only fitting, temporal splits, leakage checks, and sealed evaluation when the claim depends on future generalization.
- Do not create or copy datasets merely because a scaffold contains a data-contract directory.

## Experiment Identity

Record fields in proportion to the claim:

- maintained repository revision and dirty state;
- external source identity when material;
- data identity and split;
- configuration and environment identity;
- random seed and deterministic settings;
- local or remote compute identity;
- start and terminal state;
- metrics, limitations, and artifact location.

A small exploratory calculation may need only a notebook, input identity, and limitation note. A comparative model claim normally needs the full chain.

For experiments with several design choices or evaluation views, use [experiment-orientation.md](experiment-orientation.md). Link the run and claim to the dimension map and its experiment slice, including the actual configuration-to-arm mapping, fixed and compared settings, aggregation support and weights, and metric/horizon/checkpoint rules. Keep those records in the existing protocol or design owner so ongoing comparisons remain interpretable across stages.

## Artifact and Receipt Boundary

- Maintained source, small reviewed configuration, and compact redacted receipts may be tracked when the host policy permits.
- Generated datasets, checkpoints, large outputs, caches, and runtime logs stay outside Git by default.
- A receipt records what happened; it should not contain credentials or copied secret values.
- An artifact location is not evidence that the artifact is valid, complete, or reproducible.

## Claim Discipline

Link consequential claims to the relevant input, method, run, metric, uncertainty, and limitation. Preserve failed, excluded, or incomplete evidence when omitting it would mislead the conclusion.

Do not equate source inspection with adoption, data cleanliness with evaluation readiness, access with runtime readiness, a smoke run with research quality, or one successful run with a robust comparison.

## Governance Connect

1. Read existing project rules and identify inherited constraints.
2. State which research-task surfaces need a project-level connection: data, credentials, external source, remote compute, storage, publication, or root registration.
3. Reuse existing owners and gates. Do not generate a parallel root contract.
4. Invoke or adapt `human-ai-governance` only for a real project-level gap.
5. Keep task scaffold validation separate from project aggregate validation; run both when both claims are needed.
