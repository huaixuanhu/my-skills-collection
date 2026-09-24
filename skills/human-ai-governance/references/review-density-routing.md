# Review-Density Routing

Current skill version: `human-ai-governance v0.7.9`

Use this reference when a user-facing engineering update must balance review effort with completeness, when shorter wording might hide a material fact, or when one deliverable contains both conversation and formal engineering records.

## Choose the Presentation

Review density has two choices, independent of writing mode, terminology, reasoning effort, and governance tier:

| Choice | Use |
| --- | --- |
| `compact` | Default for conversational engineering plans, progress updates, evidence, results, and handoffs. Use concise, contextual prose rather than the shortest possible answer; retain everything needed for the current judgment or action. |
| `expanded` | When the user requests detail, or when a decision, explanation, safe execution, or reproducibility requires it. Expand only the parts that need it. |

Do not ask the user to select a mode on every turn. A request for “all details,” a causal walkthrough, or exact reproduction takes precedence over the compact default. High risk requires complete disclosure, not an automatically long report. A complex task can still have a short status update.

Apply this default while the skill is in use. Installation and discovery do not guarantee invocation in every task. When adapting project governance under an approved migration, include the short communication rule in the project's existing collaboration section. Do not silently rewrite global instructions or downstream projects to make a preference persistent.

## Ground Each Issue in Its Subject

When introducing a problem or switching to another one, name the affected feature, component, file, service, or operation; describe what happened to it; then state what has been done or what remains needed. Prefer complete, natural sentences over fragments such as “fixed locally,” “checks passed,” or “approval needed” when the reader would have to infer their subject. Include enough context to understand the problem without reconstructing it from earlier messages, even when this makes the answer moderately longer.

For next actions and approval requests, identify who would act or approve, what action is proposed, and which problem it addresses when those facts are known. The affected system and the responsible person are different facts: do not invent an owner, cause, affected scope, or completion state to fill a sentence. If the precise source is unknown, name the observed surface and state what remains unidentified.

Once the subject is established, use natural pronouns or leave it implicit only when the reference remains clear. Reintroduce the subject when switching between problems with different evidence, states, or permissions. Do not require every sentence to repeat the same noun, add grammar quotas, or turn the answer into a fixed “subject / phenomenon / status” form.

Illustrative wording: “The export tool omitted the final row from generated files. I have corrected the local code, but the full test suite has not run.” This preserves the affected feature, observed problem, actor, and limited state without a process diary. A real answer must use only the facts and authority available for its task.

## Preserve the Decision

Lead with the answer, conclusion, or current state. Then select the applicable information in this order:

1. Evidence needed to support or limit that conclusion, including what was checked and what remains unverified.
2. Material risks, uncertainty, contrary evidence, exceptions, and consequential limits near the claim they qualify.
3. Any decision or authorization needed from the user, with the consequence of the choice.
4. The next action or remaining blocker, if one exists.

This is a priority order, not a fixed set of headings. Omit empty sections and “none” fields. Use a paragraph, short list, or compact table only when it makes the actual decision easier to understand.

Keep statuses exact: inspected, changed, validated, committed, pushed, deployed, and activated are different claims. A passing local test does not establish live readiness. A prepared candidate does not mean it has been installed or published. Preserve denominators, time windows, units, thresholds, and missing evidence when they affect interpretation.

Retain exact identifiers, commands, paths, configuration keys, error text, formulas, and contract wording when needed to identify, execute, reproduce, verify, or stop safely. Compact reporting does not justify replacing specific diagnostic errors with generic failures or discarding useful context; apply the entrypoint's diagnostic-retention rule to the underlying evidence. Do not flood an update with every path or log line simply because it exists. Link the relevant source for secondary detail; keep decision-changing caveats in the response itself. Never invent a source link or claim that an unwritten report holds the omitted evidence.

In a repair or implementation handoff, preserve the provided material changed-file pointer so the reader can inspect the reported change. A clear feature name supplies the subject, while a short file link preserves that review entrypoint; do not replace it with a long list of incidental files or invent a path that was not supplied or verified.

## Remove Lower-Value Detail First

- Remove repeated background, a replay of tool calls, generic reassurance, and explanations of routine steps that do not affect the decision.
- Combine facts sharing the same conclusion; avoid repeating a risk or approval boundary in several sections of one response.
- Explain behavior with concrete subjects and verbs. Do not replace a longer clear sentence with a dense chain of specialist nouns, acronyms, slashes, or unexplained shorthand.
- In progress updates, report meaningful changes, new evidence, current blockers, and next work; avoid replaying the full plan. The final handoff must still stand alone because progress messages may be hidden.
- Put optional implementation detail in the existing engineering record when continuity requires it. Do not create extra reports or appendices solely to make the chat shorter.

Use no fixed word count, line limit, terminology quota, readability score, or required shortening percentage. Brevity is useful only after correctness and decision completeness are preserved. Do not print an editorial checklist or a routine announcement of the selected mode.

## Compose with Technical Language

`compact` does not select `plain`. Honor explicit terminology choices from the current request or standing user/project instructions without asking again. If none exists, retain `default` terminology under the existing rules.

When `plain` is selected, prefer a common exact substitute for unfamiliar terminology. Keep and briefly explain a necessary term when substitution would be ambiguous; follow the user's language and bilingual conventions. Do not append a tutorial to every term or remove domain distinctions to save words. Plain language can require more words.

Read `technical-language-routing.md` when terminology selection or exact meaning needs review. A request to simplify implementation language does not authorize approximating scientific methods, formulas, or other specialist content the user needs precisely.

## Keep Formal Records Complete

This route controls user-visible conversation, not the amount of engineering work performed or stored. Formal plans, architecture, specifications, schemas, runbooks, migration steps, tests, evidence records, and authorization contracts retain their full operational requirements. A compact conversational summary can accompany a complete artifact; it cannot replace an explicitly requested complete artifact.

For mixed deliverables, identify the function of each content unit. Preserve the audience-facing voice of an article or presentation and the precision of its technical sections. Do not apply a conversational checklist or short-answer limit to the artifact itself. `expanded` does not change writing mode, terminology choice, permission, or the completion criteria.

## Review Before Sending

Check the actual meaning rather than matching phrases:

- Would the reader reach the same supported decision, know what is unverified, and understand the same next action and authority boundary after compression?
- Can the reader distinguish work performed from plans, recommendations, and untested claims?
- Can the reader identify which subject has which problem, evidence, handling state, and next action, without guessing or assigning an unknown owner?
- Did any shorter wording erase a condition, quantity, exception, contrary result, or dependency that changes that decision?
- Are exact operational details and source pointers recoverable without guessing?
- Did the answer reduce reading effort without forcing dense shorthand or hiding necessary detail behind a link?

If a check fails, restore or explain the missing information and expand that part. Keep reasoning, investigation, implementation, validation, evidence, safety, recovery, and completion requirements unchanged. Do not add a generic preflight or style-lint gate for review density.
