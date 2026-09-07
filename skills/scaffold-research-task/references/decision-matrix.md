# Research Scaffold Decision Matrix

Use this reference when the correct structure is unclear. Select the smallest module set that preserves the task's real evidence and recovery boundaries.

## Decision Sequence

1. Identify the primary deliverable: synthesis, dataset finding, code, trained model, benchmark, reusable method, or decision memo.
2. Identify material inputs: publications, public documentation, external code, third-party data, internal data, or generated data.
3. Identify execution: no code, local analysis, repeatable local experiment, remote batch work, or sustained compute.
4. Identify evidence needed for the final claim: citations, data identity, configuration, environment, run receipts, metrics, or statistical uncertainty.
5. Inspect existing repository and governance conventions before choosing names or root integration.

## Module Selection

| Signal | Add module | Do not infer |
| --- | --- | --- |
| Every research task | `base` | That every task needs code, environments, or a master plan |
| Maintained analysis or model code, data contract, experiment config, or repeatable test | `model-research` | That a literature task needs an ML tree |
| External code, data, model, or reusable material beyond ordinary citation | `third-party-source` | That public visibility automatically requires a hard stop |
| Remote host, scheduler, container, cloud batch, or off-device execution | `remote-compute` | That account visibility proves job or training readiness |
| Existing project rules must be inherited or a task-specific gap must be connected | `governance-connect` | That a second project-wide governance system is needed |

## Proportionality Checks

- If removing a directory would not hide a real responsibility, evidence type, or recovery boundary, omit it.
- Do not create empty source, data, environment, or compute surfaces for possible future use.
- Do not split documents solely to resemble a reference scaffold.
- Keep one task file capable of carrying scope, non-scope, current lifecycle state, and evidence ceiling for small work.
- Add a dedicated architecture document when several responsibility surfaces or data and execution flows must remain distinct.

## Choose the Construction Route

Use standard generation when every path in the selected profile serves a real task responsibility. The generator and its validator intentionally share that complete layout contract.

Use manual adaptation when the task needs fewer surfaces, an existing host layout, or another implementation language. Map selected responsibilities to actual files in existing task or architecture notes when needed for continuity, then validate that accepted layout and the affected host contracts. A `model-research` responsibility does not force a Python package on this route. Do not add unused directories or move mature content merely to pass the standard-layout validator.

## Research Shape Examples

### Literature or desk research

Use `base`. Keep citations, extracted evidence, synthesis, limitations, and final report distinct enough to audit. Omit source code, environment, remote compute, and project governance unless the host already requires them.

### Local data or ML study

Use `base` plus `model-research`. Record data contracts and experiment identities. Add `third-party-source` only if external material is executed, incorporated, or redistributed beyond ordinary package dependencies and citations.

### External model on remote compute

Use `base`, `model-research`, `third-party-source`, and `remote-compute`. Add `governance-connect` when operating inside an existing governed project or when job, data, or source actions need project-level authorization.

### Package inside a mature repository

Start from the task's substantive modules, then add `governance-connect`. Preserve root names, data flows, environments, and aggregate gates. Root registration is a separate proposed change, not an automatic scaffold action.

## Stop Conditions

Pause for a new decision when inspection reveals a materially different target location, disputed data ownership, an unresolved source-use choice that changes intended actions, consequential remote work outside existing authorization, or required root changes outside the accepted scaffold scope. Reuse valid agreement within its accepted conditions.
