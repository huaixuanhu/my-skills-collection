# Built-In Profiles and Generated Paths

Profiles are convenience compositions, not universal project types. Add a module only when the decision matrix identifies a real responsibility.

## Profiles

| Profile | Modules | Typical use |
| --- | --- | --- |
| `literature-review` | `base` | Literature review, desk research, source-backed synthesis |
| `local-ml` | `base`, `model-research` | Local data analysis, ML experiment, maintained modelling code |
| `third-party-remote` | `base`, `model-research`, `third-party-source`, `remote-compute`, `governance-connect` | External model or code with remote execution inside a governed task |
| `existing-repository` | `base`, `governance-connect` | A bounded research package inside a mature repository; add substantive modules as needed |

`governance-connect` creates no files. It records the connection in `RESEARCH_TASK_PROFILE.json` and requires the agent to inspect and preserve host governance.

## Base Paths

```text
README.md
RESEARCH_TASK.md
RESEARCH_TASK_PROFILE.json
sources/README.md
evidence/README.md
reports/README.md
```

## Model-Research Paths

```text
RESEARCH_ARCHITECTURE.md
configs/README.md
data_contracts/README.md
environment/README.md
notebooks/README.md
research_artifacts/README.md
running_logs/README.md
scripts/README.md
src/<package_name>/__init__.py
tests/README.md
```

The scaffold creates contracts and policy placeholders, not datasets, dependencies, notebooks, experiments, or model implementations.

## Third-Party-Source Paths

```text
THIRD_PARTY.md
```

Use the register proportionally. A citation-only source needs less detail than incorporated or redistributed code.

## Remote-Compute Paths

Default:

```text
remote_compute/README.md
remote_compute/job_templates/README.md
remote_compute/run_receipts/README.md
```

Use `--compute-dir hpc`, `--compute-dir cloud`, or an established safe relative name to adapt the directory without changing the module contract.

## Script Options

- `--target`: required explicit task path.
- `--task-name`: required human-readable task name.
- `--profile`: one built-in profile.
- `--add-module`: repeat to add a justified module to a profile.
- `--package-name`: Python package name; derived safely from the task name when omitted.
- `--compute-dir`: safe relative directory for remote-compute files; defaults to `remote_compute`.
- `--apply`: write after a conflict-free preview; omitted means dry-run.
- `--allow-repository-root`: permit an explicitly accepted target containing `.git`.

The script never removes a profile module because doing so can make the named profile misleading. Choose a smaller profile and add modules when a custom composition is needed.

## Manifest Contract

`RESEARCH_TASK_PROFILE.json` records schema version, generating skill and version, task name, selected profile, modules, package name when applicable, compute directory when applicable, and `no-automatic-root-changes` policy. It contains no timestamp so identical inputs remain deterministic.

The validator allows extra user files. It checks only the selected module contract, path safety, generated markers, and unresolved template tokens.
