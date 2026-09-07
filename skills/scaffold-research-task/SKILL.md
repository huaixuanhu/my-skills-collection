---
name: scaffold-research-task
description: Derive, create, adapt, or validate a task-scoped research scaffold with proportional architecture and research governance. Use when a literature review, data study, ML or model investigation, third-party source study, reproducible experiment, or local or remote research task needs a clear folder structure, lifecycle, source and data boundaries, configuration and environment separation, artifact and evidence handling, or connection to existing project governance. Also use when ongoing model experiments need an explicit map of design dimensions, current comparisons, fixed conditions, aggregation, and scoring scope.
---

# Scaffold Research Task

Skill version: `0.1.2`

## Purpose

Build the smallest useful scaffold for one research task. Derive the structure from the task's evidence, code, data, compute, and reproducibility needs instead of copying a reference project tree.

This skill owns research-task architecture and research-specific evidence rules. It is not a project-wide base governance system. Use `human-ai-governance` for project tiers, human approval, plan lineage, reasoning-mode routing, AI logs, preflight gates, or durable repository-wide collaboration rules.

For an existing experiment that only needs orientation, use **Experiment Orientation** below directly. Inspect its current protocol, configurations, and relevant evidence; keep its established layout and continue the accepted task without running the scaffold generator.

## Core Workflow

1. Inspect before proposing.
   - Read the target repository's `AGENTS.md` and directly relevant architecture, plan, data, source, and validation files.
   - Inspect the target tree and Git state. Distinguish a new standalone task, a package inside an existing repository, and an existing research task that needs repair.
   - Identify the research question, intended deliverables, data ownership, external sources, compute location, artifact scale, reproducibility expectation, and existing governance.

2. Derive the smallest module set.
   - Always start from `base`.
   - Add `model-research` only when code, data contracts, configurations, environments, or experiments are real task surfaces.
   - Add `third-party-source` when external code, data, models, or other reusable material needs more than ordinary citation.
   - Add `remote-compute` only when the task actually uses or prepares for remote execution.
   - Add `governance-connect` when the task must inherit or extend existing project governance. This module creates no generic governance files by itself.
   - Treat modules as responsibility and evidence areas. Use the standard generator only when its complete selected layout fits; choose manual adaptation for omitted surfaces, established paths, or a non-Python implementation. Read `references/decision-matrix.md` for ambiguous selections and `references/profiles.md` to assess the standard layout.

3. Propose before writing.
   - State scope, non-scope, selected modules, standard-generation or manual-adaptation route, intended target, likely files, root integration, validation, and external side effects.
   - Explain which structure is task-specific and which rule is inherited from the host project.
   - Obtain agreement before material scaffold creation when local instructions or the task require plan-first work.

4. Create or adapt within the accepted layout.
   - Require an explicit target and review proposed paths. Repository-root changes need accepted root-level scope; preserve existing user content and avoid unsafe or symlinked write paths.
   - For standard generation, use `scripts/scaffold_research_task.py`; its default is dry-run. Review the preview before `--apply`. Different existing content is a conflict that the generator must not overwrite.
   - For manual adaptation, use the accepted task and host structure, omit unused surfaces, and edit only agreed files. Do not generate filler directories, a Python package, or a generator manifest merely to satisfy the standard-layout validator. Explicitly approved edits may adapt existing files without treating them as disposable template output.
   - Keep root registration, dependency installation, network access, remote actions, Git commits, pushes, tags, and installation links outside the scaffold command.

5. Validate and hand off.
   - For the standard layout, run `scripts/validate_research_scaffold.py --target <target>`. It checks the generator contract, not every valid research architecture.
   - For a manually adapted layout, verify the accepted responsibility-to-file mapping, relevant links, source/data/evidence boundaries, and affected host contracts. Use the host's meaningful checks; do not claim the standard-layout validator passed or require unused paths to make it pass.
   - Run the host project's applicable focused or aggregate gate when the scaffold becomes part of that project; if it includes a required check, avoid running that check twice without a distinct reason.
   - Report created and unchanged files, selected modules, evidence ceiling, inherited governance, validation, and unresolved decisions.

## Module Boundaries

- `base`: task identity, scope, sources, evidence, and reports. Keep it suitable for a small literature or desk-research task.
- `model-research`: research architecture, source package, data contracts, configurations, environment, scripts, notebooks, tests, logs, and generated artifacts.
- `third-party-source`: proportional external-source records. Citation-only use remains light; local execution records identity and limitations; copying, adapting, or redistributing requires stronger licence and provenance evidence.
- `remote-compute`: host-adapted compute guidance, inert job templates, and redacted run receipts. Access evidence does not prove environment or research readiness.
- `governance-connect`: inherit existing rules and expose task-specific gaps. Invoke or adapt `human-ai-governance` only when project-level governance work is actually needed.

## Experiment Orientation

For model experiments with several design choices, nested arms, populations, or scoring views, read `references/experiment-orientation.md`. Keep the experiment's full design space and current position visible through planning, execution, interpretation, and handoff.

- Maintain one dimension map in the existing protocol or experiment-design owner. Summarize the tracked setting groups and how many settings the current comparison changes, distinguishing dimensions, levels, and valid combinations. Record material axes, values, dependencies, source pointers, and training versus evaluation roles; retain deferred dimensions so a narrow current comparison does not erase the larger design.
- Begin each experiment-design proposal or design/slice change with one visible summary line, in this order: total design dimensions; current varied dimensions; current marginalized dimensions; marginalization rule; current fixed dimensions and values. Use short labels and English dimension names without parenthetical Chinese translations in this line; preserve exact IDs and meaningful values. Follow the format in `references/experiment-orientation.md`; screen wrapping is fine. Keep the full registered design space visible even when the current comparison varies only one setting.
- In experiment-facing progress and result updates, default to a compact orientation card: current question and compared levels, fixed conditions, dimensions kept separate or aggregated with weights, and scoring scope. At a switch, add what changed from the previous slice and which earlier results remain comparable. Show the full map on request or when the design changes; do not repeat it for routine tool progress with no experiment change.
- Distinguish independent factors from configuration bundles and nested arms. Count valid training combinations separately from repeats, execution attempts, and score views. Never turn a list of setting categories into an unsupported count of independent dimensions or jobs.
- State whether a result is conditional on fixed settings or averaged over named dimensions. Preserve comparison support, metric and horizon, checkpoint rule, and evidence identity. Several simultaneous setting changes support a bundle comparison unless the design supplies a justified separate effect estimate.
- Use the same map and slice identity at restart and handoff. Reconcile accepted settings with actual run evidence, mark unresolved fields, and keep each completed result tied to its original slice. A map or card summarizes its owner sources; it cannot alter a protocol or grant execution authority.

## Research-Governance Rules

- Separate source notes, data identity, protocol, implementation, execution receipts, metrics, reports, and final claims when those surfaces exist.
- Preserve an explicit evidence ceiling. A citation, source inspection, data profile, import test, access check, smoke run, and accepted research result are different claims.
- Record enough identity to reconstruct consequential experiments: code, source, data, configuration, environment, seed, compute, terminal state, metrics, limitations, and artifact location.
- Keep generated data, large artifacts, checkpoints, and runtime logs out of Git by default; follow the host repository's storage policy.
- Scale external-source checks to intended use. Do not impose Model 5 SONNET's source-ingestion stop on citation-only or ordinary public-source research.
- For inspection or local execution, follow the host project's checkout and ignore policy; do not require an external checkout to live outside the repository unless a concrete host, licence, payload, or nested-Git risk calls for it.
- Never let the scaffold grant permission to copy source, access data, install dependencies, submit jobs, deploy, publish, commit, or push.

Read `references/research-governance.md` when defining evidence, reproducibility, source, data, artifact, or claim rules. Read `references/research-lifecycle.md` when the task needs staged research or evidence gates.

## Host Adaptation

Preserve established names and responsibilities when they already satisfy the selected modules. Prefer adding a bounded task package over changing a mature shared root. Read `references/host-adaptation.md` for existing repositories, team roots, HPC or cloud conventions, and root-integration decisions.

The generated `RESEARCH_TASK_PROFILE.json` is a task-scoped standard-layout manifest. A manually adapted task can use its existing task or architecture notes instead; it need not adopt this manifest or generator markers. Neither form establishes execution authority.

## Scripts

These commands apply to the standard-generation route. Use the manual route above when the complete generated layout does not fit the accepted task.

Preview:

```bash
python <skill-root>/scripts/scaffold_research_task.py \
  --target <task-path> \
  --task-name "<task name>" \
  --profile <profile>
```

Apply only after reviewing the preview:

```bash
python <skill-root>/scripts/scaffold_research_task.py \
  --target <task-path> \
  --task-name "<task name>" \
  --profile <profile> \
  --apply
```

Use `--package-name` for model code, `--compute-dir` to preserve an established remote-compute directory name, and repeat `--add-module` only for a justified addition. Use `--allow-repository-root` only after the user explicitly accepts root-level creation.

Validate:

```bash
python <skill-root>/scripts/validate_research_scaffold.py --target <task-path>
```

## Resource Routing

- `references/decision-matrix.md`: ambiguous module selection or scope sizing.
- `references/research-lifecycle.md`: staged research and evidence transitions.
- `references/research-governance.md`: research-specific source, data, experiment, artifact, and claim rules plus the governance connection.
- `references/experiment-orientation.md`: dimension maps, compact current-experiment cards, conditional and marginal comparisons, scoring scope, and continuity across experiment switches.
- `references/host-adaptation.md`: existing repository, package-local, remote host, and root-integration adaptation.
- `references/profiles.md`: built-in profiles, generated paths, and script options.
- `assets/templates/`: files copied and rendered by the scaffold script; do not load all templates merely to advise on structure.
