# Audience-Facing Writing

Current skill version: `human-ai-governance v0.7.3`

Use this reference after `SKILL.md` routes a deliverable or one of its content units into audience-facing expression mode. This mode governs presentation and prose. It does not change project tier, engineering controls, evidence requirements, or authorization.

Technical-language choice is a separate axis. `default` and `plain` cannot activate, deactivate, or reshape audience-facing expression. When the user explicitly selects `plain`, preserve the chosen voice, narrative, organization, rhythm, genre, and presentation logic while adapting only terminology under `technical-language-routing.md`.

## Route by Content Function

Engineering records remain the default. Activate audience-facing expression when the primary job of a content unit is to help a defined audience understand, remember, evaluate, or act on an idea through presentation, explanation, narrative, or persuasion.

| Content function | Writing mode |
| --- | --- |
| Execute, reproduce, configure, authorize, validate, audit, or preserve project truth | Engineering-governance writing |
| Present, explain, narrate, persuade, or support a reader decision | Audience-facing expression |
| Serve both functions in one deliverable | Route each section, page, slide, note, or appendix by its own function |

Strong expression signals include an explicit audience and genre, such as an article, speech, public copy, executive narrative, client-facing explanation, or presentation story. File extension, length, visual polish, or the presence of readers is insufficient by itself. A technical review deck, operational handbook, or `.docx` runbook can remain wholly or partly engineering-governed.

Infer the mode when purpose and audience are clear. If ambiguity would materially change the deliverable and the surrounding task does not resolve it, ask one concise question. Otherwise retain the engineering default.

## Preserve Engineering Function

Plans, architecture records, specifications, schemas, API contracts, runbooks, migrations, incident records, test and validation reports, evidence receipts, audit logs, and authorization boundaries retain engineering precision. Keep constraints where operators, reviewers, or later agents need them to execute, reproduce, verify, or stop work correctly.

When restating a functional contract, preserve its named conditions and leave unresolved gaps visible. Do not fill an unspecified trigger, fallback condition, threshold, or authorization step with a plausible operational assumption merely to make the narrative smoother.

An independently consumed entry point may need its own critical precondition even when another document states the same condition. Treat that as functional control placement, not stylistic repetition. Concision may improve an engineering record, but natural-sounding prose never justifies removing an operational invariant.

Expression mode cannot soften facts, invent support, hide material uncertainty, paraphrase wording that must remain exact, or reduce required legal, compliance, safety, privacy, source, approval, or risk disclosure. It also cannot convert sampled, synthetic, offline, or design-only evidence into a stronger claim.

## Write for the Intended Audience

- Lead with the idea, outcome, tension, or decision the audience needs. Keep agent process and governance narration out of the finished piece unless the method itself matters to that audience.
- Minimize repeated self-justification, process defense, and irrelevant boundary statements. Give a rationale once at the point where it helps the reader.
- In one continuously read piece, state a scope or authorization boundary once near the decision it governs. Do not repeat the full boundary list in the conclusion unless exact wording is required or the closing can be consumed independently.
- Place a necessary caveat close to the claim it qualifies. Repeat it only when a separately consumed page, slide, or section would otherwise become materially misleading or unsafe.
- Prefer concrete nouns and verbs, natural paragraph movement, and sentence lengths that fit the thought. Preserve the author's requested voice rather than substituting a generic polished assistant voice.
- Use paragraphs for connected reasoning and lists for genuinely parallel items. Let headings, bold text, tables, and summary lines earn their place through reader need.
- Remove empty intensifiers, inflated abstractions, ceremonial introductions, conclusions that only restate the opening, and transitions that announce structure without advancing the idea.
- Never fabricate quotations, reader reactions, personal experience, or emotional certainty to make prose feel human.

Treat recurring patterns as revision signals rather than forbidden forms. Repeated negative parallelism such as “not X, but Y,” identical paragraph shapes, stacked three-part lists, excessive em dashes, bold fragments, and repeated conclusion statements can make prose feel templated. Keep an individual use when it expresses a real distinction or improves rhythm. After one clear negative contrast, phrase later points affirmatively when the meaning remains intact; revise any pattern that becomes the default skeleton.

## Adapt to the Deliverable

### Long-Form Prose

Build continuity across paragraphs instead of translating every thought into headings and bullets. Let evidence support the narrative where it becomes relevant. Avoid repeatedly explaining why the structure, scope, or cautious wording was chosen.

### Presentations

Give each slide a clear audience job and let its title carry a real message when the genre allows. Keep visible copy concise enough to read at presentation distance. Put supporting detail in notes or an appendix only when the main audience does not need it on the slide; do not bury a material limitation.

Technical appendices, methodology, source notes, risk disclosures, operating instructions, and approval conditions keep engineering precision. Render and inspect the actual deck because natural prose cannot compensate for dense, clipped, or visually incoherent slides.

### Executive and Client-Facing Reports

Lead with the answer, implication, or decision. Explain evidence and uncertainty in terms the intended reader can use. Keep internal agent workflow, validation narration, and defensive caveats out of the main story unless they change the reader's decision or confidence.

## Hybrid Examples

| Deliverable | Expression layer | Engineering layer |
| --- | --- | --- |
| Leadership system deck | Main storyline, transitions, audience takeaway | Architecture details, source notes, risk gates, operating limits |
| Research report | Abstract, introduction, discussion, executive summary | Methods, data definitions, result tables, reproducibility and evidence limits |
| Product proposal | User problem, value, decision narrative | Security constraints, migration contract, acceptance criteria, rollout gates |
| Incident briefing | Reader-oriented chronology and impact summary | Exact timestamps, evidence, unresolved facts, remediation owners and runbook changes |

## Revision Diagnostics

Before handing off audience-facing work, check:

- Does each explanation help this audience, or does it defend the writer's process?
- Does every repeated caveat protect a separately encountered claim or decision?
- Have code-like lists and headings displaced prose that needs continuity?
- Does a contrast, em dash, bold fragment, or three-part pattern recur from habit?
- Does the opening reach the subject promptly, and does the ending add a consequence rather than another summary?
- Does the ending repeat a complete scope, authorization, or caveat list already stated for the same continuous reading path?
- Are facts, sources, uncertainty, required wording, and engineering boundaries still exact?

Do not use phrase counts, regular expressions, AI-detector scores, or forced sentence variation as acceptance gates. They can reward superficial evasion and penalize legitimate style. Judge the complete artifact against its audience, genre, truthfulness, and functional boundaries.
