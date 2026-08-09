# Reasoning-Mode Routing

Current skill version: `human-ai-governance v0.6.0`

Use this reference for important or complex work in the main workspace. Keep reasoning-mode choice separate from governance tier: tier controls authority and credible harm, while mode routing responds to the task's reasoning shape.

## Routing Sequence

1. Use `xhigh` when the task is relatively simple, bounded to one clear responsibility surface, and has direct validation.
2. Once meaningful complexity appears, choose between Max and Ultra as peer primary modes.
3. Prefer Max when depth dominates: a long causal chain, tightly coupled state, difficult root-cause closure, ordering-sensitive changes, or hard plan closure.
4. Prefer Ultra when parallelism dominates: several meaningful investigation, implementation, testing, comparison, or review directions can progress with useful independence.
5. Use a staged combination only when the dominant task shape changes across a restartable handoff. Name the evidence or checkpoint that triggers the switch instead of prescribing a fixed sequence.

Do not create a numerical score. File count, token count, duration, repository size, or project tier can inform inspection but do not decide the mode by themselves.

## Model Discretion and Proportionality

- Preserve Codex's ordinary discretion over delegation, agent count, coordination, and writing unless a concrete failure requires a temporary recovery constraint.
- Do not make Ultra read-only by default. Parallel implementation is acceptable when the accepted scope, ownership, validation, and recovery boundary remain coherent.
- Apply existing proportionality rules in every mode. Avoid speculative guards, defensive abstractions, duplicate tests, extra documents, repeated approval pauses, or additional agents without a credible benefit.
- Respect the user's explicit mode choice. Raise a mismatch once only when another mode would materially improve the task, explain why, and continue after the user decides.
- If the relevant mode is unavailable, use the closest available main-workspace mode without claiming the unavailable capability was active.

## Temporary Single-Writer Recovery

Do not use single-writer execution as a Max default. Consider a temporary Max single-writer recovery slice only when evidence shows one or more of these conditions:

- a high-coupling change has failed repeatedly;
- required validation remains blocked after bounded repair attempts;
- concurrent changes repeatedly overwrite or invalidate one another;
- repairing surface A damages B, repairing B damages C, and repairing C damages A;
- competing local explanations cannot close one shared causal model.

Bound the recovery slice to the failing causal chain, state its validation and stop conditions, and restore normal Codex discretion after the loop is closed. Do not turn a local recovery tactic into a permanent repository-wide policy.

## Recommendation Shape

Give one compact recommendation during planning:

```text
Recommended mode: <xhigh | Max | Ultra> - <dominant task shape and concrete reason>.
Switch point, if any: <verified handoff condition or none>.
```

For a staged combination, name only the modes and handoff that current evidence supports. Do not force an Ultra-Max-Ultra ceremony around every complex task.

## Validation

Mode selection changes how work is organized, not what counts as correct. Preserve the accepted scope, project safety boundaries, relevant tests, aggregate gate, evidence ceiling, and recovery conditions in every mode.
