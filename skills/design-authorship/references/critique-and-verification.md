# Critique and Verification

Evaluate the rendered artifact before reading its design rationale. A convincing explanation cannot repair a weak or broken result.

## Artifact-First Pass

Record what the artifact itself shows:

- first visual focus and reading path;
- whether the primary task or claim is immediately available;
- semantic fit between content relationship and visual form;
- interaction discoverability and state clarity;
- responsive behavior and real-data density;
- unmotivated containers, accents, icons, motion, or repetition;
- context specificity and fidelity to approved references;
- narrative continuity for a deck;
- diagram legibility and truthful relationship encoding;
- accessibility and export defects visible in the artifact.

Only after this pass compare the artifact with the intent, state, and visual contracts.

## Finding Severity

- `critical`: blocks the primary task, misrepresents content or system behavior, breaks a required viewport or state, creates a serious accessibility failure, loses required evidence, or produces an unusable export.
- `major`: materially weakens hierarchy, interaction, narrative, context specificity, or approved direction.
- `minor`: localized craft issue with no material effect on task or claim.

Do not calculate a taste score, require every subjective axis to exceed a number, or derive a universal completion condition from these severity labels. Completion follows the task's agreed acceptance criteria and format-specific validation. Use severity to prioritize work and make any residual problem visible.

## Verification by Mode

UI:

- render affected supported layouts within the confirmed or delegated contract, including other supported surfaces exposed to shared-component or style changes;
- exercise changed interactions with pointer, touch assumptions, and keyboard where applicable;
- inspect confirmed empty, loading, error, success, selected, hover, focus, pressed, and disabled states;
- test long text and representative real data.

Slides:

- follow [slides.md](slides.md) to select full-deck review for new work or a whole-deck redesign, and affected-page plus relevant-neighbor review for a local edit;
- broaden integrity checks when shared styles, saving, or export can affect other pages; retain applicable title flow, transition, viewing-distance, and fidelity checks within that scope.

Diagram:

- inspect at reduced scale and in grayscale;
- trace every claimed direction, boundary, sequence, and category back to the source.

Fix the artifact, render it again, and recheck only the affected claims and permanent quality requirements.
