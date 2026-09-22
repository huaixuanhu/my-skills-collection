# Technical-Language Routing

Current skill version: `human-ai-governance v0.7.7`

Use this reference when the user explicitly selects plain technical language, when a technical explanation is intended for a non-specialist, or when reviewing the independence of terminology, writing mode, and engineering capability.

## Select the Terminology Mode

Technical-language mode has two choices:

| Choice | Behavior |
| --- | --- |
| `default` | Add no terminology transformation beyond current Codex behavior and other governing instructions. |
| `plain` | Reduce unexplained specialist terminology in the selected content while preserving exact meaning and every engineering requirement. |

Use `default` when the user does not make an explicit choice. Do not ask the user to select a terminology mode for every task. An explicit request such as “plain technical language,” “plain version,” “explain for a non-specialist,” “use less jargon,” or an equivalent request in the user's language activates `plain`.

Apply an explicit choice to the current task, deliverable, or named content unit unless the user sets a broader scope. A later explicit choice replaces it for the newly named scope. The skill does not create a persistent cross-project preference by itself.

A standing user or project instruction requesting ordinary, non-specialist, or low-jargon language is already an explicit choice. Honor its domain and audience scope without requiring the user to repeat it in every message. Do not mistake an existing choice for an omitted choice just because the latest task does not restate it.

`default` means this skill adds no extra terminology adjustment. Platform instructions, repository rules, and the user's other current instructions still apply.

## Keep Writing Mode Independent

Technical-language routing is orthogonal to writing-mode routing. Determine engineering-governance writing or audience-facing expression from content function first, then apply the selected terminology choice inside that writing mode.

| Writing mode | `default` | `plain` |
| --- | --- | --- |
| Engineering-governance writing | Preserve the existing precise engineering form. | Preserve the same contract and operational detail while making surrounding explanations easier for a non-specialist to follow. |
| Audience-facing expression | Preserve the existing audience-facing voice, narrative, organization, rhythm, genre, and presentation logic. | Preserve those same expression choices while explaining or reducing only the terminology that would block the intended reader. |

Neither terminology choice may activate, deactivate, replace, weaken, or reshape a writing mode. Audience-facing expression does not imply `plain`, and `plain` does not imply audience-facing expression.

In audience-facing `plain` content, do not flatten prose into an engineering checklist, replace the author's voice with tutorial language, or remove useful narrative, rhetorical, or presentation choices merely because they are not technical.

## Preserve Engineering Capability

Terminology choice controls wording only. It must not change:

- reasoning effort, reasoning route, or agent topology;
- investigation, planning, implementation, code, or tool use;
- tests, validation coverage, evidence, or claim ceilings;
- facts, sources, uncertainty, thresholds, required disclosures, or unresolved gaps;
- safety controls, project tier, authorization, approval, or completion criteria.

Plain language does not mean a shorter or less complete answer. Review density is a separate choice: conversational engineering updates default to `compact`, and expand when needed, as described in `review-density-routing.md`. Neither density choice changes terminology activation. Remove or explain jargon only after preserving the information needed to execute, reproduce, verify, decide, or stop safely.

Keep exact identifiers, code, commands, paths, configuration keys, API fields, error text, formulas, standards, and wording that functions as a contract. If replacing a technical term would introduce ambiguity, keep the term and give a short explanation in the user's language. Define a recurring term once when one explanation remains visible to the same continuous reader.

Prefer a common exact substitute before introducing specialist terminology. For example, “the operation is idempotent” may become “repeating the operation does not create an additional change”; retain and briefly explain `idempotent` when that exact property is needed to discuss the contract. Do not invent an analogy, causal explanation, or simplified rule that the evidence does not support. Avoid compact chains of unfamiliar terms and preserve precise scientific or domain terminology outside the requested simplification scope.

## Apply by Content Unit

Use `plain` for user-facing explanations, progress updates, handoffs, summaries, and requested reader-facing sections inside its selected scope. A precise engineering document may add a plain summary while retaining exact specifications, runbook steps, validation conditions, and authorization rules.

For mixed deliverables, route each section, page, slide, note, or appendix by content function, then apply the selected terminology choice without moving content between writing modes.

## Review the Result

Before handing off `plain` technical content, check:

- Would `default` and `plain` lead to the same engineering decision, implementation, validation, evidence, risk, and next action?
- Are exact identifiers and operational conditions still recoverable without guessing?
- Did the terminology change leave the selected writing mode's voice, structure, and purpose intact?
- Did any shorter phrase weaken a fact, limit, uncertainty, disclosure, or authorization boundary?
- Where ordinary wording became ambiguous, was the exact technical term retained and explained?

Treat these as semantic review questions. Do not use jargon counts, word blacklists, reading-level scores, regular expressions, or AI-detector scores as acceptance gates.
