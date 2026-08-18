# Research Lifecycle

Use these stages as semantic checkpoints. Rename or combine them to fit the host project; do not create equal-sized stages or documents for ceremony.

## stage1 Framing

Define the research question, decision consumer, intended output, non-scope, constraints, and acceptable evidence. Record the current evidence ceiling.

Exit claim: the question and evaluation target are clear enough to investigate.

## stage2 Source and Data Feasibility

Inspect publications, documentation, external material, available data, data provenance, feature availability, quality, and known limitations. Separate inspection permission from incorporation or execution permission.

Exit claim: the relevant inputs and material unknowns are identified. This does not authorize implementation or remote work.

## stage3 Protocol and Contract

Freeze the data contract, evaluation split, baselines, metrics, comparison rules, stopping rules, reproducibility fields, and invalidation conditions that matter for the task.

Exit claim: implementation can be judged against a reviewable protocol.

## stage4 Implementation

Build the smallest code, configuration, environment, or analysis path needed by the accepted protocol. Keep generated artifacts separate from maintained source.

Exit claim: focused deterministic checks pass; no research-quality claim follows automatically.

## stage5 Smoke and Calibration

Test imports, tiny fixtures, one bounded local or remote path, resource assumptions, and receipt capture. Treat access, imports, and smoke runs as engineering evidence.

Exit claim: the selected execution path works within the tested boundary.

## stage6 Approved Research Runs

Run the accepted protocol inside the separately authorized compute and data boundary. Preserve code, source, data, config, environment, seed, compute, terminal state, metrics, and artifact identity.

Exit claim: eligible run evidence exists for evaluation.

## stage7 Evaluation and Closeout

Evaluate only eligible runs, preserve negative and incomplete evidence, state uncertainty and limitations, reconcile the task status, and identify the next decision.

Exit claim: the report's claims match the recorded evidence ceiling.

## Restartable Seams

Split work where an upstream product remains useful if the downstream stage is delayed or fails. Common seams include source feasibility before incorporation, protocol before implementation, implementation before remote execution, smoke evidence before expensive runs, and accepted runs before comparative claims.

Do not split an atomic data transformation or an intermediate state that cannot be safely retained and verified.

## Evidence Ceiling Examples

- Citation collected: source identity exists.
- Source inspected: relevant behavior or content was reviewed.
- Data profiled: the inspected snapshot has recorded properties.
- Import passed: a narrow engineering path loaded.
- Access checked: the account or host was visible within the checked boundary.
- Smoke passed: one bounded execution path completed.
- Protocol run completed: an eligible experiment receipt exists.
- Result accepted: metrics and limitations support the stated research claim.
