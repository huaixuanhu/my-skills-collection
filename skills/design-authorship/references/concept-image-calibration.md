# Concept-Image Calibration

Use image generation to carry visual information that prose communicates poorly. Treat the result as a styleframe or composition reference, not as production truth.

## Tool Selection

Reuse the available approved image-generation capability or supplied references. Verify current official guidance when the exact model matters; do not hard-code a time-sensitive claim about the latest model into the workflow. When an environment exposes only a generic image-generation tool, do not claim which underlying model it uses.

## Recommend a Concept Pass When

- a greenfield UI or material redesign needs a visual world;
- atmosphere, material, typography character, imagery treatment, or composition is difficult to align through words;
- a presentation needs original narrative imagery or a visual metaphor;
- references are absent or pull in conflicting directions;
- the human wants to compare substantially different visual directions.

Skip it when the task is a bounded polish, an extension of a mature design system, a precise product-state record, a data or technical diagram, or a sensitive project whose assets are not approved for a separate model.

## Workflow

1. Use the established intent contract and, for UI work, the confirmed or delegated viewport-and-state contract; resolve only remaining material gaps. Ground the composition in the primary task and representative content from [product-structure.md](product-structure.md), including density and difficult states that could invalidate it.
2. Reuse the human's existing image-tool choice and authorization. When the choice remains unresolved and matters to the result or external effects, resolve the approved capability or human-supplied references.
3. Do not send private screenshots, unreleased assets, confidential data, or third-party material to a separate service without authorization.
4. Generate or request only the views needed to compare the selected directions. Prefer styleframes and composition studies over fake production screenshots with invented text or controls.
5. Follow an already-selected direction. When selection has been delegated, choose within that delegation and continue; otherwise let the human select, reject, or combine materially different directions.
6. Extract Reference DNA, including explicit `take` and `avoid` decisions. Identify the attention hierarchy, connected regions, proportions, boundary meanings, and signature relationships to preserve; distinguish these from incidental text, sample values, or exact pixels.
7. Build with real content, components, states, and accessibility constraints.
8. Compare the rendered implementation with the selected concept and task. Explain material departures and re-align when they weaken the approved direction. Once accepted or covered by delegation and verified, keep the durable rules in the project's existing design owner using [project-design-context.md](project-design-context.md); do not canonize every detail of a generated image.

## Evidence Boundary

Concept images may calibrate proportion, rhythm, mood, material, imagery, and visual hierarchy. They do not establish:

- exact text or data;
- valid controls or component semantics;
- desktop, mobile, hover, focus, selected, loading, or error behavior;
- accessibility conformance;
- technical feasibility;
- factual evidence or approved brand assets.

Preserve the chosen concept or its location only when the project needs durable traceability. Do not create a global visual-memory store by default.
