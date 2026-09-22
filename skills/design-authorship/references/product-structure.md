# Product Structure and Prototype Choice

Use for a new UI, material structural redesign, or a new task or interaction pattern. For a bounded repair, reuse the established task and structure and inspect only the affected relationships. Keep the reasoning in the current brief or plan; this reference does not require a new document.

## Establish the Situated Task

Use available evidence to establish:

- who acts, their familiarity, and whether the task is occasional or repeated;
- the situation that starts the task, including interruptions and relevant device or input constraints;
- the outcome they need, the decisions they must make, and observable signs of completion;
- representative real content and the cost of mistakes, delay, or lost context;
- established behavior and design decisions that the change must preserve.

Distinguish source facts, working assumptions, and accepted decisions using [intent-and-reference.md](intent-and-reference.md). Do not invent user research or require a fresh questionnaire when existing evidence is sufficient.

## Derive Structure from the Work

Start with the task outcome, then identify the minimum useful model:

1. **Objects:** what the user examines or changes, such as an application, experiment, or exercise.
2. **Properties:** which attributes identify the object and support the current decision.
3. **Relations:** what belongs together, must be compared, depends on another object, or provides evidence.
4. **Actions:** what the user can do, with prerequisites, consequences, and reversible or recovery paths.
5. **States:** what changes before, during, and after those actions, including incomplete and failed outcomes.

Express the primary task as a short sequence: starting context, decision, action, feedback, completion or recovery. Add branches only when they change the design. A sketch linking screens and state changes can suffice.

Do not turn this inventory directly into a component menu. An object's properties may belong in one shared working area; an action may change that area without requiring a new screen or card.

## Organize Information before Components

Decide:

- what must be visible together to avoid cross-screen memory or repeated navigation;
- what defines the primary working area and what provides supporting context;
- which objects need independent navigation, and which are attributes, evidence, or states of the current object;
- what should remain stable during repeated actions, and what can appear progressively;
- how the user returns to the same object, selection, comparison, or unfinished step.

Then choose visual forms with [content-to-form.md](content-to-form.md). A container is an implementation choice whose visible boundary needs a purpose; the number of features does not determine the number of boxes.

## Distinguish the Three Paths

| Path | Design question | Useful evidence |
| --- | --- | --- |
| Task flow | Can the user reach the outcome and recover from relevant failures? | Execute the task and its affected branches. |
| Intended attention sequence | Does emphasis guide the reader from orientation through relevant evidence to the next decision or action? | Inspect the rendered hierarchy, grouping, and transitions; actual gaze requires observation. |
| Operation path | Can pointer, touch, and keyboard users act and continue without losing their place? | Exercise the supported input methods, focus changes, and repeated actions. |

These paths should support each other, but they are not interchangeable. A drawn attention arrow expresses design intent; it is not eye-tracking evidence. A short pointer route does not establish comprehension. A successful click sequence does not establish a coherent reading experience.

At selection, expansion, submission, failure, and return, check what the user is now attending to, what feedback connects to the action, and where they can continue. Use [ui-interaction.md](ui-interaction.md) for viewport, state, and input verification.

## Explore with Representative Content

Establish the task and representative content structure before concept exploration that depends on them. Include relevant long labels, dense records, missing values, or empty states so attractive placeholders do not conceal structural failure. Label synthetic examples explicitly.

When structure remains unresolved, compare materially different arrangements using the same key content, task, constraints, and state. Assess the primary working area, simultaneous comparison, supporting context, reveal order, and space allocation. Use [intent-and-reference.md](intent-and-reference.md) to compare visual directions separately where useful.

Follow an already-approved direction. A new project does not require a fixed number of alternatives. Wireframe rectangles mark occupied space; they do not commit the final artifact to backgrounds, borders, or cards.

## Match Prototype Fidelity to the Uncertainty

| Unresolved question | Smallest useful prototype |
| --- | --- |
| What belongs together, or what appears first? | Content arrangement or linked wireframes with representative labels and values. |
| Does the composition or visual language express the agreed intent? | A representative rendered composition, style study, or concept image when useful. |
| Can the user complete, repeat, or recover from the action? | An interactive prototype containing the relevant states and input behavior. |
| Does the implemented artifact hold up with real content and supported viewports? | The actual artifact at the affected sizes and states. |

Use an available format workflow. Increase fidelity only when the next unresolved question needs it. A concept image cannot establish interaction behavior; a prototype cannot establish production readiness.

When feedback changes the structure, identify which assumption or accepted decision it challenges. Preserve unaffected intent and route durable changes through [project-design-context.md](project-design-context.md), rather than treating each revision as a fresh design brief.
