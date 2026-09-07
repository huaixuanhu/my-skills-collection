# Host Adaptation

Adapt the scaffold to its containing project and compute environment. Preserve established contracts before introducing new names.

## New Standalone Research Task

- An explicit task directory may become the repository root only with user agreement.
- Start with `base`; add modules from actual requirements.
- Do not initialize Git, install dependencies, or create publication settings through the scaffold script.

## Package Inside an Existing Repository

- Read root instructions, architecture, environment, data flow, storage policy, and aggregate validation.
- Prefer one bounded package or task directory.
- Reuse the root virtual environment for lightweight checks only when the host project says to do so.
- Keep root registration as a separately reviewed change.
- Do not create a second data pipeline, environment, or governance gate when the existing owner already covers the task.
- Select manual adaptation when established names, shared owners, or the implementation language differ from the complete standard layout. Preserve the host's real responsibilities and validate the affected contracts without adding filler paths.

## Existing Research Task

- Treat existing files as user-owned.
- Use dry-run only when the standard layout is a suitable candidate; otherwise inspect the accepted paths directly.
- Exact generated content may be reported unchanged; different existing files are generator conflicts and may be adapted manually within the accepted edit scope.
- Do not force the generated manifest into an existing task unless the user accepts that migration.
- For manual adaptation, review the responsibility-to-file mapping and meaningful host checks. Record that evidence honestly; the standard-layout validator is not its acceptance gate.
- For experiment-orientation work, extend the existing protocol or design notes with the dimension map and current slice. Keep the current state owner, plan lineage, configuration IDs, and result history; use the orientation route without generating a new scaffold or parallel plan. Read [experiment-orientation.md](experiment-orientation.md) for the map and compact card.

## Mature Governed Repository

- Select `governance-connect` and record inherited boundaries.
- Keep package-specific complexity inside the task boundary when the shared root should remain simple.
- Propose the smallest root pointer or aggregate-gate registration only when required.
- Never weaken a stronger project-specific control to match a generic template.

## Local Compute

- Reuse the host project's environment convention when it exists.
- Separate maintained code, configuration, data identity, generated artifacts, and logs.
- Do not install dependencies as part of scaffold creation.

## Slurm or HPC

- Preserve an established directory such as `hpc/` by passing `--compute-dir hpc`.
- Separate login or account checks, environment checks, allocation tests, smoke jobs, and research runs.
- Follow scheduler and login-node policies; generated job templates remain inert until separately reviewed and submitted.

## Cloud or Generic Remote Compute

- Use an established host-specific directory when one exists; otherwise keep `remote_compute/`.
- Separate credentials, data transfer, environment build, job execution, artifact storage, and result retrieval.
- Access or inventory evidence does not authorize mutation, spending, deployment, or sustained execution.

## Root-Target Protection

The scaffold script refuses `--apply` to a directory containing `.git` unless `--allow-repository-root` is provided. This flag confirms the target location only. It does not approve root governance changes, commits, pushes, dependency installation, or external actions.
