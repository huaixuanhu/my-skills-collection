# Critique and Verification

Evaluate the rendered artifact before reading its design rationale. A convincing explanation cannot repair a weak or broken result.

## Artifact-First Pass

Record what the artifact itself shows. Separate direct observations, reviewer predictions, and actual user feedback:

- predicted first visual focus, reading path, and places where competing emphasis interrupts continuity;
- whether the primary task or claim is immediately available;
- transitions from entry to supporting information, action or conclusion, feedback, and the next step, as applicable;
- semantic fit between content relationship and visual form;
- whether scale, whitespace, alignment, shape, and boundaries establish coherent groups and priority across the whole composition;
- interaction discoverability and state clarity;
- responsive behavior and real-data density;
- unmotivated containers, accents, icons, motion, or repetition;
- context specificity and fidelity to approved references;
- narrative continuity for a deck;
- diagram legibility and truthful relationship encoding;
- accessibility and export defects visible in the artifact.

Only after this pass compare the artifact with the intent, state, and visual contracts and the accepted project baseline. A walkthrough can reveal likely interruption or ambiguity; it does not prove users' gaze or attention. Preserve the distinction between intended path, reviewer inference, and observed behavior.

## Diagnose Before Restyling

Classify the likely source of a finding before choosing a repair:

- **Task or content:** the artifact solves the wrong job, omits a required fact, or uses unsupported content; return to the brief and sources.
- **Information structure:** comparison needs memory across distant regions, related information is separated, or everything competes as a peer; revisit grouping, sequence, and content-to-form choices.
- **Interaction or state:** the next action, result, recovery, or context continuity is unclear; repair the flow and state model.
- **Composition or language:** the task structure is sound but emphasis, rhythm, shape roles, or transitions conflict; repair their relationships across the composition and compare with the accepted baseline.
- **Local craft or implementation:** the intended relationship is correct but spacing, type, rendering, behavior, or export is defective; repair the affected implementation.

These are hypotheses, not automatic diagnoses. Record the visible evidence, task consequence, probable cause, and smallest useful verification. Quote or summarize user feedback separately from your explanation of it. A preference may guide an authorized direction change without proving a usability failure.

Return to the earliest relevant decision when the evidence warrants it. Recoloring repeated containers will not repair a missing hierarchy or an interrupted task. Equally, a valid card collection needs no structural replacement merely because it contains rectangles.

## Acceptance Comparison

Assess three distinct dimensions against the agreed scope:

- **Task and experience:** the intended task, comparison, narrative, or explanation works through its relevant states and transitions.
- **Visual direction:** the rendered artifact expresses the approved attention hierarchy, composition, and language; justified contextual variation is coherent.
- **Implementation and integrity:** behavior, accessibility requirements, content truth, supported layouts, and output fidelity meet the applicable checks.

When a baseline exists, compare representative accepted and revised renders with equivalent content, viewport or output format, and state where practical. Explain any unavoidable difference that limits the comparison. Check whether local feedback improved its target while shared roles and conventions stayed coherent; make intentional evolution explicit using [project-design-context.md](project-design-context.md). Do not preserve a demonstrated defect solely for visual consistency.

Passing package tests or writing a persuasive rationale cannot establish visual quality. Record what was rendered, exercised, or observed and what remains unverified. Match the depth of comparison to the impact; do not require a new study, fixed number of critique rounds, or extra approval for every bounded repair.

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
- test long text and representative real data;
- trace the intended attention and action sequence through the changed flow, checking that feedback, overlays, density changes, and responsive reflow preserve context and a discoverable next step.

Slides:

- follow [slides.md](slides.md) to select full-deck review for new work or a whole-deck redesign, and affected-page plus relevant-neighbor review for a local edit;
- broaden integrity checks when shared styles, saving, or export can affect other pages; retain applicable title flow, transition, viewing-distance, and fidelity checks within that scope;
- check that affected pages preserve the deck's visual language and attention sequence while allowing purposeful differences between slide roles.

Diagram:

- inspect at reduced scale and in grayscale;
- trace every claimed direction, boundary, sequence, and category back to the source;
- verify that changed emphasis and visual grammar preserve the intended explanation without inventing relationships.

Fix the artifact, render it again, and recheck only the affected claims and permanent quality requirements.
