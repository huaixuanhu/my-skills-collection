---
name: design-authorship
description: Direct, critique, redesign, and verify context-specific visual and interaction design for user interfaces, presentation slides, presentation-like HTML, and explanatory diagrams. Use for layout, hierarchy, typography, color, imagery, motion, responsive behavior, interaction states, narrative flow, visual form, AI-like structural repetition, concept-image calibration, or rendered visual review. Pair it with the appropriate format-specific build skill or tool for code, PPTX, images, and diagrams.
---

# Design Authorship

Skill version: `0.1.0`

## Purpose

Create artifacts whose major design decisions follow from the subject, audience, task, content relationships, interaction states, narrative, or real technical and accessibility constraints.

This skill owns design direction, interaction alignment, content-to-form choices, critique, and visual acceptance. It does not replace the skill or tool that constructs the actual website, PPTX, image, document, or diagram. It does not grant permission to change product behavior, factual content, brand identity, private assets, deployment, or publication.

## Route the Work

Choose the smallest useful route before loading references:

- Work mode: `shape`, `build`, `redesign`, `audit`, or `verify`.
- Artifact mode: `ui`, `slides`, or `diagram`.
- Project state: `established`, `greenfield`, or `replacement`.
- Evidence state: source only, rendered artifact, or live interactive artifact.

Use one primary artifact mode. Load a secondary mode only for a real embedded surface, such as a diagram inside a deck. Route linear presentation-like HTML through `slides`; route interactive HTML through `ui`.

## Core Workflow

1. Inspect the existing world.
   - Read the brief, real content, project instructions, design system, tokens, components, templates, screenshots, and durable user decisions that actually exist.
   - Preserve an established visual and interaction system unless the user requests replacement.

2. Align the human design contract.
   - Establish the audience, artifact job, primary task or claim, desired emotional register, truth constraints, technical constraints, and what the result should not resemble.
   - For a new UI, material redesign, or new interaction pattern, obtain human confirmation or explicit delegation for the target desktop and mobile surfaces plus relevant `selected`, `hover`, `focus`, `pressed`, `disabled`, `empty`, `loading`, `error`, and success states before implementation.
   - Present inferred existing behavior and ask only about material gaps. For a bounded repair, align only the affected viewport, input method, and states.
   - Read [intent-and-reference.md](references/intent-and-reference.md) for the compact contract and reference-analysis method.

3. Decide whether visual concept images add information.
   - For a greenfield UI or material visual replacement, actively offer concept-image calibration when layout, atmosphere, imagery, material, or brand character would otherwise be carried mainly through words.
   - For slides or presentation-like HTML, offer it only when original imagery, visual world, or composition would materially improve the story. Skip it for small refinements, strict templates, exact product-state documentation, or evidence-heavy pages where generated imagery could mislead.
   - Read [concept-image-calibration.md](references/concept-image-calibration.md) before recommending or using GPT Image 2 or another approved image-generation capability.

4. Set direction proportionally.
   - For greenfield or replacement work, compare two or three directions that differ in reading path, spatial composition, density, imagery relationship, or interaction model. Do not present color swaps as separate directions.
   - For established-system extensions and small refinements, use one coherent direction inside the current system.
   - Classify major content relationships before choosing visual forms. Read [content-to-form.md](references/content-to-form.md).

5. Build through the artifact's format workflow.
   - Read [ui-interaction.md](references/ui-interaction.md), [slides.md](references/slides.md), or [diagrams.md](references/diagrams.md) for the primary mode.
   - Use the available format-specific skill or tool for construction. Keep real content, behavior, and accessibility ahead of decorative novelty.

6. Critique the artifact, then verify it.
   - Render the actual artifact at the relevant sizes and states. Judge screenshots, exports, or the live result before consulting its design rationale.
   - Address findings within the agreed scope and verify affected claims again. Read [critique-and-verification.md](references/critique-and-verification.md).

7. Persist only durable approved decisions.
   - Prefer existing design-system and project documents. Do not create `.design-memory/` or cross-project fingerprint logs by default.
   - Read [project-design-context.md](references/project-design-context.md) only when a long-lived project needs a durable design-context owner.

## Decision Rules

- Treat anti-default observations as prompts for contextual review, not bans. A familiar font, card, color, grid, or animation remains valid when it serves the artifact.
- Do not add aesthetic lint scripts, fixed style recipes, or numerical taste gates without evidence of a recurring mechanical failure that a deterministic check can actually detect.
- Use containers for interaction, state, persistent boundary, or direct comparison. Otherwise consider alignment, whitespace, rules, axes, bands, annotation, or the content itself.
- Spend the strongest visual emphasis in one intentional place unless the brief establishes a different system.
- Do not let a concept image decide exact copy, data, component semantics, responsive behavior, or interaction states. Treat it as calibration evidence, then implement and verify the real artifact.
- Preserve factual content and uncertainty. Generated imagery must not create fake evidence, product states, metrics, testimonials, or source material.

## Composition Boundaries

Use `human-ai-governance` only when project-wide planning, approval, authority, evidence, or durable collaboration rules are in scope. Use research scaffolding only when the task also needs research-task architecture. Skill availability and automatic invocation depend on the current platform installation and the skill description; a repository catalog can help routing and management but cannot activate a missing installation or grant authority.
