# Semantic Stage Sizing

Use this reference for complex multi-stage or recovery-prone work. Skip it for small bounded tasks. The goal is reconstructable execution, not equal stage size or additional ceremony.

## Stage roles

- `roadmap stage`: a coordination container that may describe several products or outcomes; it is not automatically one execution batch or one Codex task.
- `execution stage`: a restartable unit with one primary verifiable outcome and one coherent acceptance and recovery boundary.
- `work package`: a bounded slice inside an execution stage. Create a derived child plan only when durable recovery or a separate task needs it.

Use numeric hierarchy such as `Stage 2.1.3`. Reserve letter suffixes for explicit addenda, not ordinary sequence.

For a plan-only response, state only the minimum useful structure: stage identifier, primary outcome, entry evidence, exit claim, retained state, and recovery or next-entry condition. Do not restate the whole project packet or every permanent invariant.

## Capacity classification

For a complex or multi-session execution stage, record at most one concise classification:

- `bounded`: one coherent outcome, authority envelope, validation claim, and recovery boundary.
- `dense_but_coherent`: substantial or cross-package work that remains one atomic contract, causal chain, or recovery unit.
- `split_required`: independently acceptable, deferrable, reversible, authorized, or retainable outcomes have been combined.

Do not create a score. Inspect the stage's outcome, responsibility surfaces, authority transitions, validation claims, durable outputs, branches, unknowns, and recovery domains. File, function, package, line, token, duration, and compaction counts are diagnostic signals only.

## Split triggers

Split, or state briefly why the work remains coherent, when:

- two results can be accepted, deferred, rolled back, or retained independently;
- discovery determines a materially different dependent implementation route;
- local design moves into migration, external calibration, publication, deployment, or live activation and changes authority or evidence ceiling;
- responsibility surfaces have distinct consumers, validation gates, or failure handling;
- a partial failure should preserve an already completed product or evidence claim;
- an accepted product can remain valid while cross-product roadmap reconciliation and closure are still pending;
- a recovery, supersession, or conditional branch makes the linear stage state misleading;
- the next slice requires a different primary domain model and a substantially different source closure.

Crossing packages alone is not a split trigger. Keep a narrow vertical contract together when it has one outcome and one recovery boundary.

## Restartable seam

Split only where all relevant conditions hold:

1. Upstream work produces a durable output, receipt, decision, or verified checkpoint.
2. Downstream work can verify that input and begin without reconstructing unrelated upstream context.
3. Downstream failure does not automatically invalidate upstream success.
4. The authority, side effects, validation, and failure behavior on both sides remain explicit.

Do not split an atomic transaction, a causally inseparable implementation, or an intermediate state that cannot be safely retained and verified. Do not create separate stages solely for code, tests, documentation, or validation when they support the same acceptance claim. A bounded closeout stage is appropriate when it reconciles several independently retained outcomes and owns the roadmap's final status; if it only documents one still-open acceptance claim, keep it inside that execution stage.

## Restart checkpoint

At a high-load stage close, pause, failure, or task switch, persist the smallest sufficient recovery truth in the current plan, machine receipt, or existing handoff surface:

- status and primary outcome;
- source plan and frozen decisions;
- input evidence or source snapshot;
- retained products, changed contracts, and owned paths;
- validation result and evidence ceiling;
- failed attempts, unresolved risks, and forbidden retries;
- exact next-stage entry conditions.

Do not create a new report when existing receipts and plan links already provide this truth.

## Plan closeout and context release

When a project uses a plan index, close a stage by recording both the execution result and how future agents should load its plan:

- set `lifecycle_status` from verified exit evidence;
- set `authority_state` according to whether the plan still directs new work or its retained result has been consumed by another owner source;
- set `load_policy` only after identifying the current status owner and future retrieval need;
- record the consumer or successor and the exact next-entry condition.

Do not infer `evidence_only` from completion alone. A completed plan may remain the current baseline, while a consumed plan may still be required for a specific audit or recovery claim.

Update a mutable plan header and its index entry together. When the plan is immutable, digest-bound, receipt-bound, signed, or append-only, preserve its original text and carry current lifecycle and loading state in the index plus the named status owner. Do not create another closeout document merely to say that an existing plan is complete.

## Mid-stage overload

When a stage becomes overloaded during execution:

1. stop at the last verified durable boundary;
2. preserve completed valid state and append-only failure evidence;
3. derive the remaining work from the accepted parent plan instead of rewriting history;
4. keep ordinary in-scope decomposition under the accepted plan;
5. request a new decision only for material scope expansion, consequential external action, a new one-shot or runtime attempt, changed authority, or an explicit local approval gate.

Use a completed checkpoint as a low-cost task-switch point when the next execution stage changes the primary responsibility surface, authority, or evidence type. Do not switch tasks mechanically in the middle of atomic work.

## Graph assistance

When an explicitly enabled fresh governance graph exists, use it to project responsibility surfaces, independent products, authority transitions, validation edges, recovery branches, and the minimum source closure for each execution stage. Treat graph-based split suggestions as advisory semantic evidence; never let a graph automatically rewrite the accepted plan.
