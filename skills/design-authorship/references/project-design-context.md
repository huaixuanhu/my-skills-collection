# Durable Project Design Context

Use this reference when a long-lived project needs design decisions to survive across tasks, including when an existing design owner needs to guide an extension, critique, or repair.

## Prefer Existing Owners

Inspect `DESIGN.md`, design-system documentation, tokens, component stories, product briefs, brand guidance, templates, and representative accepted artifacts before proposing a new file. Reuse the established owner and link to supporting sources instead of copying them. Resolve material conflicts against the project's source-of-truth rules; do not treat the newest screenshot or the current code as automatically approved.

## Accepted Design Baseline

A maintainable language needs the relationships that make the design coherent, as well as tokens and components. In the existing owner, retain only the durable decisions needed to guide future work:

- product or subject world;
- audience and recurring task priorities;
- intended attention path, composition, hierarchy, and spatial rhythm;
- typography, color, imagery, and motion roles, including how emphasis is allocated;
- shape and boundary meanings, such as what a panel, card, divider, or open region signifies;
- interaction, responsive, and state conventions, including continuity of context and next steps;
- approved signature elements and where they belong;
- rejected patterns with the reason they fail this project;
- representative accepted renders linked to their source revision or other reproducible identity, relevant viewport or output format, and state;
- unresolved decisions and their owner.

Keep the record proportional: link to existing evidence and describe meaningful relationships instead of cataloging every property. If no owner exists and a durable gap matters, use the project's authorized documentation scope to establish one concise owner such as `DESIGN.md`; do not create a parallel design authority. For a deck this may be its approved master, narrative and composition conventions; for a diagram it may be its visual grammar and source constraints.

Distinguish these statuses explicitly when they could otherwise be confused:

- **Durable intent:** approved priorities and relationships to preserve, with their reasons.
- **Allowed flexibility:** details that may change within that intent, such as spacing adjustments for real content.
- **Contextual variation:** deliberate differences for another task, density, viewport, state, slide role, or diagram relationship; record the reason and scope when reusable.
- **Approved or delegated evolution:** a deliberate change to the baseline within current authority, subject to validation of its affected claims.
- **Temporary experiment:** a candidate direction or trial whose result has not entered the accepted baseline.
- **Incidental implementation:** current code or one-off styling without a durable design decision behind it.

An intended attention path remains an intention until observed. Label user feedback, observed behavior, and reviewer inference separately; a screenshot alone cannot establish where users actually look.

## Maintain Through the Feedback Cycle

1. Start each relevant revision from the task and accepted baseline. Identify what should improve, what relationships must hold, and what variation the scope allows.
2. Keep the user's feedback in its own terms, then state the inferred cause separately. Use [critique-and-verification.md](critique-and-verification.md) to choose the upstream layer to repair instead of accumulating cosmetic patches.
3. Revise within existing confirmation or delegation. When evidence exposes a flawed baseline, make the proposed change and its reason explicit; preserve valid intent without freezing defects or treating every preference as a new system rule.
4. Verify the affected task, rendered design, and shared effects against the baseline and the new acceptance criteria. A local improvement must not quietly rewrite unrelated emphasis, boundary meanings, or responsive conventions.
5. Update the durable owner only after relevant validation is complete, for a change that is accepted or covered by explicit delegation. Identify the replaced decision or evidence as superseded and link its replacement, rather than leaving competing current baselines. Describe remaining uncertainty honestly.

Do not add an approval round where existing authority covers the change. Keep temporary directions, generated-image candidates, per-run critique, and speculative preferences outside the durable record unless the project explicitly needs them. A rendered implementation does not become approved merely because it now exists.

## Boundaries

- Do not create `.design-memory/`, cross-project fingerprints, or global preference files by default.
- Do not turn one accepted artifact into a universal template.
- Do not record private project material in a global memory system without explicit authorization.
- Update the durable owner when an accepted or delegated, validated change makes its current claim false or incomplete; do not canonize accidental drift.
