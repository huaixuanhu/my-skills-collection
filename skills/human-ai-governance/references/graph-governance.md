# Optional Graph Governance

Use graph governance only when the user explicitly requests it, an accepted plan authorizes a shadow pilot, or the current task needs an existing repository graph manifest to answer a cross-surface impact, recovery, authority, lineage, or freshness question. Manifest presence alone does not activate graph workflow. Keep projectless conversations, bounded tasks, and ordinary low-complexity work graph-free.

## Authority model

Treat the graph as a derived read model, never a parallel source of truth.

- Plans own intent, scope, sequencing, and human decisions.
- Rule indexes and rule bodies own governance policy.
- Contracts, registries, authorizations, receipts, and runtime evidence own identity and observed state.
- Code and tests own executable behavior.
- Git owns version and selected-snapshot state.

Every material graph claim must point to one owner source. Prefer `unknown` or `unresolved` over an inferred edge without evidence.

## Minimal projections

Use only the projections required by the task:

- repository projection: surfaces, modules, contracts, products, consumers, tests, and gates;
- execution projection: roadmap stages, execution stages, attempts, checkpoints, branches, failures, supersessions, and next-entry conditions;
- evidence and authority overlay: plans, approvals, authorizations, limits, receipts, and retained or exhausted authority.

Do not force a repository dependency graph into a DAG. Keep execution snapshots acyclic where immutable event and supersession identities allow it.

## Provenance and freshness

For each material node or edge, retain the smallest useful provenance:

- source path and field, heading, or stable locator;
- content digest, Git identity, or selected snapshot when available;
- extraction class: `declared`, `derived`, `observed`, or `unresolved`;
- observation time or snapshot identity;
- freshness state and builder version when generated.

Before use, verify the graph's bound sources or declared freshness contract. When a newer authoritative source conflicts with the graph, mark the graph stale, use the authoritative source, block invalid downstream continuation, and include one concise handoff field: `Rebuild status: <projection> requires rebuild; not authorized or performed in this task.` Do not silently smooth the conflict.

## Shadow-first lifecycle

Adopt graph governance progressively:

1. `external_compare`: build outside the repository and compare against human-verified source truth.
2. `retain_as_shadow`: permit read-only context and query use while all decisions still verify back to owner sources.
3. `report_only`: surface impact, drift, boundary, lineage, and recovery findings without failing existing gates.
4. `selective_enforcement`: after repeated validated use, enforce only exact mechanical invariants already accepted by the project.

Do not move between states based on one successful output alone. Preserve the previous state and evaluation evidence for rollback.

## Context manifest

Give Codex a bounded context manifest instead of the whole graph. Include only:

- current objective and execution frontier;
- source plan and frozen decisions;
- required owner sources and source snapshot;
- retained products and failed attempts;
- authority ceiling, forbidden scope, and unresolved facts;
- validation evidence and exact next-entry conditions.

Verify material claims against owner sources before consequential work. A context manifest reduces source loading; it does not authorize execution.

In a task handoff, report only the bounded manifest, material freshness conflicts, owner-source closure, and exact next entry. Do not restate the graph lifecycle or full governance protocol unless the task is deciding adoption.

## Proportionality and side effects

- Do not introduce a graph database, third-party graph tool, network call, hook, watcher, CI step, or preflight check without a demonstrated project-local gap and separate approval.
- Do not copy project-specific paths, confidential artifacts, or raw runtime data into this global skill.
- Do not create graph files or stage-capacity paperwork for Tier 1 through Tier 3 solely because this skill is active.
- Tier 4 may use a shadow graph for complex evidence and recovery work while preserving existing read-only guards and aggregate gates.
- Future Tier 5 systems may use prevalidated authority and evidence projections, but graph queries must stay outside the latency-sensitive live-action path. Preserve explicitly designed cancellation and risk-reducing operations during degraded graph or governance availability.

Do not auto-migrate downstream projects when this global skill adds or changes graph guidance. Each project needs its own inspection, plan, approval, validation, and rollback route.
