---
name: scaffold-research-task
description: Derive, create, adapt, or validate a task-scoped research scaffold with proportional architecture and research governance. Use when a literature review, data study, ML or model investigation, third-party source study, reproducible experiment, or local or remote research task needs a clear folder structure, lifecycle, source and data boundaries, configuration and environment separation, artifact and evidence handling, or connection to existing project governance.
---

# Scaffold Research Task

Skill version: `0.1.0`

## Purpose

Build the smallest useful scaffold for one research task. Derive the structure from the task's evidence, code, data, compute, and reproducibility needs instead of copying a reference project tree.

This skill owns research-task architecture and research-specific evidence rules. It is not a project-wide base governance system. Use `human-ai-governance` for project tiers, human approval, plan lineage, reasoning-mode routing, AI logs, preflight gates, or durable repository-wide collaboration rules.

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
   - Read `references/decision-matrix.md` for ambiguous selections and `references/profiles.md` before generating files.

3. Propose before writing.
   - State scope, non-scope, selected modules, intended target, likely files, root integration, validation, and external side effects.
   - Explain which structure is task-specific and which rule is inherited from the host project.
   - Obtain agreement before material scaffold creation when local instructions or the task require plan-first work.

4. Preview and create safely.
   - Use `scripts/scaffold_research_task.py`; its default is dry-run.
   - Require an explicit target. Do not infer or edit the repository root.
   - Review every proposed path before using `--apply`.
   - Treat a different existing file, a symlinked path, path traversal, or an unapproved repository-root target as a conflict. Do not overwrite it.
   - Keep root registration, dependency installation, network access, remote actions, Git commits, pushes, tags, and installation links outside the scaffold command.

5. Validate and hand off.
   - Run `scripts/validate_research_scaffold.py --target <target>` after creation.
   - Run the host project's focused or aggregate gate when the scaffold becomes part of that project.
   - Report created and unchanged files, selected modules, evidence ceiling, inherited governance, validation, and unresolved decisions.

## Module Boundaries

- `base`: task identity, scope, sources, evidence, and reports. Keep it suitable for a small literature or desk-research task.
- `model-research`: research architecture, source package, data contracts, configurations, environment, scripts, notebooks, tests, logs, and generated artifacts.
- `third-party-source`: proportional external-source records. Citation-only use remains light; local execution records identity and limitations; copying, adapting, or redistributing requires stronger licence and provenance evidence.
- `remote-compute`: host-adapted compute guidance, inert job templates, and redacted run receipts. Access evidence does not prove environment or research readiness.
- `governance-connect`: inherit existing rules and expose task-specific gaps. Invoke or adapt `human-ai-governance` only when project-level governance work is actually needed.

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

The generated `RESEARCH_TASK_PROFILE.json` is a task-scoped scaffold manifest. It records the selected profile and modules; it does not establish project governance or execution authority.

## Scripts

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
- `references/host-adaptation.md`: existing repository, package-local, remote host, and root-integration adaptation.
- `references/profiles.md`: built-in profiles, generated paths, and script options.
- `assets/templates/`: files copied and rendered by the scaffold script; do not load all templates merely to advise on structure.
