# Custom Skill Index

This human-readable view is derived from `SKILLS_INDEX.yaml` and the version markers in each `SKILL.md`. Run `.venv/bin/python scripts/manage_skills.py catalog --check` to detect drift.

The catalog routes and explains repository-owned skills. It does not install a skill, force platform invocation, or grant task authority. Runtime availability depends on the current installation; implicit invocation depends on each skill's metadata and semantic match.

| Skill | Version | Routing class | Lifecycle | Invocation |
| --- | --- | --- | --- | --- |
| `design-authorship` | `0.1.0` | `task-specific` | `maintained` | `implicit` |
| `human-ai-governance` | `0.7.5` | `cross-cutting` | `maintained` | `implicit` |
| `scaffold-research-task` | `0.1.0` | `task-specific` | `maintained` | `implicit` |

## `design-authorship`

Direct, critique, redesign, and verify context-specific visual and interaction design for user interfaces, presentation slides, presentation-like HTML, and explanatory diagrams. Use for layout, hierarchy, typography, color, imagery, motion, responsive behavior, interaction states, narrative flow, visual form, AI-like structural repetition, concept-image calibration, or rendered visual review. Pair it with the appropriate format-specific build skill or tool for code, PPTX, images, and diagrams.

- Source: `skills/design-authorship/SKILL.md`
- Use when:
  - A UI, interaction, responsive state, slide, presentation-like HTML, or explanatory diagram needs design direction, redesign, critique, or visual verification.
  - Visual intent would benefit from references, content-to-form reasoning, or concept-image calibration before engineering implementation.
- Do not route for:
  - Pure backend, data, prose, or infrastructure work with no material visual or interaction decision.
  - Standalone image generation whose requested result is the image itself rather than calibration for a designed artifact.
- Common composition: `human-ai-governance`, `scaffold-research-task`

## `human-ai-governance`

Guide engineering plans, progress updates, evidence, results, and handoffs with concise, decision-complete human review. Also create, review, or maintain proportional five-tier human-AI governance, AGENTS.md, architecture and plan documents, plan indexes, validation and safety boundaries, persistent recovery, reasoning-mode routing, audience-facing writing, and explicit default/plain technical language. Use for user-facing engineering communication, including bounded tasks, and for long-running or consequential technical workflows. Keep ordinary communication lightweight; do not use for general chat, simple translation, or unrelated prose, or replace a task-specific implementation, research, or design workflow.

- Source: `skills/human-ai-governance/SKILL.md`
- Use when:
  - User-facing engineering plans, progress, evidence, results, or handoffs need concise, decision-complete communication, including ordinary bounded tasks.
  - Project-wide planning, authority, evidence, recovery, validation, handoff, writing-mode, or technical-language rules need to be created, reviewed, or maintained.
  - A long-running or consequential workflow needs proportional human-AI collaboration boundaries across task types.
- Do not route for:
  - General chat, simple translation, or unrelated prose without an engineering review or governance need.
  - Replacing a task-specific design, research, presentation, data, or implementation workflow.
- Common composition: `design-authorship`, `scaffold-research-task`

## `scaffold-research-task`

Derive, create, adapt, or validate a task-scoped research scaffold with proportional architecture and research governance. Use when a literature review, data study, ML or model investigation, third-party source study, reproducible experiment, or local or remote research task needs a clear folder structure, lifecycle, source and data boundaries, configuration and environment separation, artifact and evidence handling, or connection to existing project governance.

- Source: `skills/scaffold-research-task/SKILL.md`
- Use when:
  - A literature review, data study, model investigation, reproducible experiment, or remote research task needs a task-scoped workspace structure.
  - Research inputs, code, data, environments, artifacts, evidence, or host-governance connections need proportional separation.
- Do not route for:
  - Ordinary implementation work that does not need a new research-task architecture.
  - Creating a second project-wide governance base inside an already governed repository.
- Common composition: `human-ai-governance`, `design-authorship`

## Live Installation State

Installation is deliberately not stored in this index because it can change independently of Git. Inspect it with:

```bash
.venv/bin/python scripts/manage_skills.py list
```
