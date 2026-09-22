# Concept-Image Calibration

Use image generation to carry visual information that prose communicates poorly. Treat the result as a styleframe or composition reference, not as production truth.

## Current OpenAI Naming

At this skill version's release, OpenAI's current model is **GPT Image 2**, with API model ID `gpt-image-2`:

- https://developers.openai.com/api/docs/models/gpt-image-2

Verify current official guidance when the exact model matters. When an environment exposes only a generic image-generation tool, do not claim which underlying model it uses.

## Recommend a Concept Pass When

- a greenfield UI or material redesign needs a visual world;
- atmosphere, material, typography character, imagery treatment, or composition is difficult to align through words;
- a presentation needs original narrative imagery or a visual metaphor;
- references are absent or pull in conflicting directions;
- the human wants to compare substantially different visual directions.

Skip it when the task is a bounded polish, an extension of a mature design system, a precise product-state record, a data or technical diagram, or a sensitive project whose assets are not approved for a separate model.

## Workflow

1. Use the established intent contract and, for UI work, the confirmed or delegated viewport-and-state contract; resolve only remaining material gaps.
2. Reuse the human's existing image-tool choice and authorization. When the choice remains unresolved and matters to the result or external effects, ask whether to use GPT Image 2, the environment's approved image-generation tool, or human-supplied concept images.
3. Do not send private screenshots, unreleased assets, confidential data, or third-party material to a separate service without authorization.
4. Generate or request only the views needed to compare the selected directions. Prefer styleframes and composition studies over fake production screenshots with invented text or controls.
5. Follow an already-selected direction. When selection has been delegated, choose within that delegation and continue; otherwise let the human select, reject, or combine materially different directions.
6. Extract Reference DNA, including explicit `take` and `avoid` decisions.
7. Build with real content, components, states, and accessibility constraints.
8. Compare the rendered implementation with the selected concept. Explain material departures and re-align when they weaken the approved direction.

## Evidence Boundary

Concept images may calibrate proportion, rhythm, mood, material, imagery, and visual hierarchy. They do not establish:

- exact text or data;
- valid controls or component semantics;
- desktop, mobile, hover, focus, selected, loading, or error behavior;
- accessibility conformance;
- technical feasibility;
- factual evidence or approved brand assets.

Preserve the chosen concept or its location only when the project needs durable traceability. Do not create a global visual-memory store by default.
