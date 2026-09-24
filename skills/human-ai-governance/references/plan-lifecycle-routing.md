# Plan-Index and Lifecycle Routing

Current skill version: `human-ai-governance v0.7.9`

Use this reference when a project has nested or parallel plans, multi-session continuation, completed plans retained for evidence, or enough plan history that finding the current execution source otherwise requires broad searching.

## Decide Whether an Index Is Needed

Keep a single clear plan direct. Add a plan index when one or more of these conditions make routing ambiguous:

- child plans have their own children or recovery branches;
- more than one branch can be active, blocked, conditional, or independently resumed;
- work continues across tasks or sessions and the current entry cannot be inferred safely from one canonical plan;
- completed or superseded plans must remain at stable paths for evidence, receipts, links, or historical reconstruction;
- agents repeatedly search or read several plan files before identifying the current one.

Do not use a fixed plan-count threshold. Do not create an index merely because a project is important, high tier, or long-lived.

## Keep the Index a Routing Read Model

Use `PLAN_INDEX.yaml`, `PLAN_INDEX.md`, or an existing project registry. Point to it from `AGENTS.md` or the project's normal orientation entrypoint.

The index helps an agent find what to read. It cannot grant scope, implementation authority, runtime authority, approval, or completion. Confirm material claims against their owner sources: current plans, contracts, receipts, code, tests, authorization records, and Git evidence.

A minimum useful entry records:

- stable `plan_id` and `path`;
- parent or source plan;
- responsibility surface, workstream, or other task-matching field;
- `lifecycle_status`, `authority_state`, and `load_policy`;
- `status_owner`, plus a successor or consumer when one exists;
- path binding when moving or editing the plan could invalidate a digest, receipt, contract, or compatibility route.

Keep the index compact. Put detailed decisions, history, evidence, and explanations in their owner documents rather than copying them into routing metadata.

## Separate the Three State Axes

| Axis | Values | Meaning |
| --- | --- | --- |
| `lifecycle_status` | `active`, `blocked`, `complete`, `superseded` | Whether the planned work is open, paused, finished, or replaced. |
| `authority_state` | `current`, `consumed` | Whether the plan still directs new work or its retained result has been absorbed elsewhere. |
| `load_policy` | `default`, `conditional`, `evidence_only` | Whether the plan is normally loaded for a matched task, loaded only when material, or retained for on-demand evidence. |

Use the axes independently. Common combinations include:

- `active + current + default`: the normal current execution plan;
- `blocked + current + default` or `conditional`: still authoritative, but continuation depends on a recorded condition;
- `complete + current + default`: execution has closed, while the plan remains the canonical baseline or status owner;
- `complete + consumed + evidence_only`: work is complete, its result is represented by a newer owner source, and the plan is read only for recovery, audit, receipt verification, or history;
- `superseded + consumed + evidence_only`: a replacement governs new work and the older plan remains trace evidence.

Do not infer `load_policy` from `lifecycle_status` alone. Completion does not prove that another source now carries the plan's current contract.

## Apply Load Policy Before Opening Plan Bodies

For material work in an indexed plan tree:

1. Read the applicable `AGENTS.md` and query the plan index.
2. Match the task to the smallest relevant responsibility surface or workstream.
3. Resolve the workstream entry and current plan, then inspect their state metadata.
4. Apply `load_policy` before opening the referenced plan body.
5. Load `default` plans for the matched workstream. Load `conditional` plans only when their scope, stage, lineage, authority, or recovery condition affects the task.
6. Load `evidence_only` plans only for recovery, audit, receipt verification, source conflict, or historical reconstruction.
7. Expand only to the parent chain, status owner, contracts, and evidence needed to establish the affected claim.

Do not recursively read all plans, all siblings, or every ancestor by default. File presence, recent modification time, folder name, and an in-file heading do not establish current authority.

If the index conflicts with a newer owner source, treat the index as stale, use the owner source for the factual state, and repair the index inside an accepted scope. Do not let stale routing metadata silently override evidence or authorization.

## Close a Plan Without Losing Evidence

At a verified closeout:

1. Confirm the plan's exit claim and current evidence ceiling.
2. Identify which source now owns the retained result and which plan, if any, governs the next work.
3. Set the three state axes and record `status_owner`, consumer, and successor.
4. Update the parent or current plan's retained state and next-entry condition when those claims changed.
5. Update the index and any mutable plan-header mirror in the same change.

For a mutable child plan in an indexed project, a concise header mirror can use:

```markdown
Lifecycle status: complete
Authority state: consumed
Load policy: evidence_only
Status owner: `<path/to/current-status-or-receipt>`
Consumed by: `<path/to/parent-or-canonical-successor>`
Successor: `<path/to/next-plan-or-none>`
```

Do not edit an immutable, signed, digest-bound, receipt-bound, or append-only plan merely to refresh its header. Keep its execution-time text intact and record current routing state in the index and named `status_owner`.

`evidence_only` means retained and read on demand. It does not mean obsolete, safe to delete, or irrelevant to every future claim.

## Keep Routing Cheap as the Index Grows

An index-first design does not require loading the whole index into model context. Keep the root index limited to workstream routing and current entrypoints. When it becomes large, use one or both of these patterns:

- a small root index that points to responsibility- or workstream-specific indexes;
- a deterministic selector that returns only matched entries and their required parent or owner links.

Validate mechanical facts such as unique IDs, valid paths, valid state values, parent existence, and cycles only when the project has adopted a stable index contract and recurring drift justifies a check. Keep semantic judgments about completion, authority, and evidence with the model and owner sources.

Keep paths stable when receipts, hashes, code, or governance checks bind them. Store lifecycle in metadata rather than renaming or moving folders whenever status changes.
