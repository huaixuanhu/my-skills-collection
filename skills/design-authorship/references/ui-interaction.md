# UI and Interaction Mode

Use this reference for interactive products, pages, dashboards, tools, and presentation-like artifacts whose user can change state.

## Human Alignment Gate

For a new UI, material redesign, or new interaction pattern, establish a compact viewport-and-state contract and obtain confirmation or explicit delegation before implementation. Reuse an existing confirmed or delegated contract; resolve only material gaps for supported surfaces, including when the new product supports only one platform.

Confirm the applicable items:

- desktop width or window range;
- mobile width or device class;
- intermediate responsive behavior;
- pointer, touch, keyboard, and assistive-technology input;
- default, hover, focus, pressed or active, selected, and disabled states;
- empty, loading, error, partial, success, and stale-data states;
- long text, dense real data, and overflow behavior;
- navigation persistence and state continuity;
- motion and reduced-motion behavior.

Mark a state `not applicable` when it truly does not exist. Do not invent hover as a mobile interaction or rely on hover for necessary information. For an established product, show the behavior inferred from current code and screens, then ask only about material conflicts or gaps. For a bounded repair, limit alignment to affected surfaces.

## Interaction Contract

Define:

1. Entry: what the user sees and knows on arrival.
2. Primary task: the shortest understandable path to the intended outcome.
3. Feedback: how the interface acknowledges input, progress, and completion.
4. Recovery: how users correct errors, cancel, undo, retry, or resume safely.
5. Exit and continuity: what state persists and what the next screen communicates.

Use stable action names across controls, progress messages, confirmations, and errors. Keep destructive or irreversible actions distinguishable and proportionate to their consequence.

## Attention Across Space and State

Design a coherent intended path, allowing scanning, comparison, and return visits rather than forcing every user through one sequence. For the current task, identify the useful entry focus, related information, local action, resulting feedback, and next meaningful step. A short annotation can suffice; do not create an attention-map deliverable for every edit.

- Connect related regions through alignment, proximity, scale, shared labels, or restrained contrast. Avoid a series of equally loud islands that make each section restart orientation.
- Keep the current object, selection, filters, and navigation context recognizable when a panel opens, a result arrives, or a user returns. Introduce emphasis where the new state needs explanation without making every update compete for attention.
- Place feedback in a perceivable relationship to the action and affected object. Persistent status and transient messages need different treatment; animation is optional, not a substitute for clear state.
- At narrower widths, preserve the information relationships and meaningful order, not just the desktop component list. Verify that necessary comparison or context remains available.
- Keep visual emphasis, DOM reading order, and keyboard focus individually meaningful. Do not move focus simply to enforce an imagined gaze path; use appropriate interaction semantics and restore focus when the interaction calls for it.

Treat this path as a hypothesis until actual observation supports it. A screenshot can reveal competing emphasis but cannot establish a user's eye movements, task success, or post-action continuity. Execute the task and inspect the changed states; distinguish reviewer inference from supplied user feedback.

## Visual and Responsive Rules

- Let real tasks and real data establish hierarchy and density.
- Reuse components when repetition lowers learning cost; vary structure only when the task relationship changes.
- Give each screen one primary focal task unless the product explicitly requires a command-center layout.
- Preserve content priority across breakpoints instead of merely stacking desktop columns.
- Use motion for feedback, state, continuity, or spatial relationship, and provide a reduced-motion path.
- Keep color from being the only carrier of state or meaning.

## Accessibility and Verification

Prefer native semantics and established platform patterns. Verify keyboard operation, visible and predictable focus, labels, reading order, contrast, target size, error identification, and status communication for changed interactions. Use WCAG 2.2 as the normative web accessibility baseline and WAI-ARIA Authoring Practices as informative pattern guidance when custom widgets are necessary:

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/ARIA/apg/

Render representative applicable layouts and every materially changed state within the confirmed or delegated contract. Broaden checks when shared components or styles can affect other supported surfaces; do not add an unsupported platform solely for verification. Exercise the changed interaction rather than judging source code alone. Compare entry, action, feedback, and return states against the accepted task and design language, including long content and interruptions relevant to the change.
