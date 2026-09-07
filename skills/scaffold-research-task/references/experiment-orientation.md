# Experiment Orientation

Use this reference when a model experiment's design dimensions or current comparison are difficult to track. The reader should be able to answer: what can vary in the whole study, where are we now, what are we comparing, and over what scope does the result hold?

## One Owner, Two Views

Keep the full dimension map and current slice in the existing protocol, experiment registry, or design notes. Use a section of `RESEARCH_ARCHITECTURE.md` for a new standard scaffold. For a small study, a short table in its existing task notes is enough. Link to authoritative configuration, data, evaluation, and run records instead of copying them into another plan.

If a separate document becomes useful, start it with its source plan or protocol, its derived status and scope, and the owner of current experiment state. Preserve existing plan numbering. A derived map is a navigation aid; accepted protocols and observed evidence remain authoritative in their respective roles.

The full map explains the available design. A compact orientation card explains the active slice of that design. Each report or result retains its own slice identity, even after the active slice changes.

## Build the Dimension Map

Open with the number and names of tracked setting groups and the settings currently being changed. State the counting convention: a configuration bundle, its component choices, and its nested arms are different levels of description. Keep dimension count, levels per dimension, and valid experimental combinations distinct. Give an independent-factor count only when the mappings support it; otherwise report the grouped inventory and unresolved dependencies. A training-run total does not answer how many design dimensions are in play.

Inspect effective configurations and protocols, not just filenames or a configuration ID. Expand a configuration or arm label into the settings it controls when they matter to the comparison. Record these fields using existing project names:

| Field | What to record |
| --- | --- |
| Dimension and source | Stable name, meaning, and the configuration or protocol field that owns it |
| Values and scope | Allowed or observed levels; distinguish planned, executed, deferred, and unknown coverage |
| Role | Model or training choice, population or data grouping, replication, evaluation, artifact selection, or execution setting |
| Relationships | Independently crossed, nested within another dimension, derived from a bundle, or restricted to listed combinations |
| Current treatment | Compared, fixed at a value, reported separately, aggregated by a named rule, deferred, not applicable, or unresolved |

Treat role and current treatment as separate questions. A state can identify a separately trained model, a reporting group within one shared model, or both. A seed can be fixed in one slice and repeated then averaged in another. A reporting group can have both separate results and an explicitly weighted summary.

Inventory every material axis, including fixed and deferred ones. Check whether data version and split, features or architecture, training budget and stopping rule, seed or fold, checkpoint selection, metric, and horizon affect this study. Use the task's actual dimensions; do not create unused axes from this list. Changing a previously fixed setting opens a new comparison condition.

Distinguish a readable group of choices from independently variable factors. A configuration may bundle several model choices. An arm may already select a learning-rate policy and loss. Keep those settings visible without counting them a second time as freely crossed factors. Record the exact configuration-to-arm mapping when arm meaning or availability depends on configuration.

### Six Setting Groups in a Forecasting Study

This is an illustrative interpretation of the user's categories, not a verified inventory or current state of any project.

| Setting group | Clarification needed |
| --- | --- |
| Model configuration | Which architecture, feature, and other choices are inside each ID; which can actually vary independently? |
| Arm within a configuration | Which arms exist for each configuration, and which settings does each arm change? |
| State | Separate training per state, grouping at evaluation, or both? Which states are eligible? |
| Learning-rate policy | Initial value, schedule, and adaptation rule; independently selected or already determined by the arm? |
| Training loss | Exact loss and options; independently selected or determined by the configuration or arm? |
| Prediction scoring view | Day 1, final day, or mean across days; what exact horizon, metric, and averaging order? |

These are six setting groups. The independent-factor count depends on their mappings. The three scoring views are levels of an evaluation choice, and can often reuse one prediction artifact. Confirm reuse from the task rather than assuming three additional training runs. If prediction horizon changes the trained model or target, expose that training choice separately from the scoring view.

### Count the Work Without Double Counting

Count distinct valid training identities from the accepted run manifest or configuration-to-arm mapping. A product of level counts is valid only when the protocol actually crosses all those choices. Use an explicit set or sum for nested arms, restricted combinations, and adaptive selections. Report the training choices, repeated seeds or folds, and resulting total separately.

Keep logical training runs, retries or resumed attempts, checkpoints, prediction artifacts, and score rows distinct. Multiple score views of the same predictions are not independent experimental replications. A scheduler job can also contain several runs; use the actual execution mapping before estimating job counts.

For a synthetic example, configuration `cfg1` has two arms and `cfg2` has one. Each permitted configuration-arm pair is trained for two states and two seeds. That is `(2 + 1) × 2 × 2 = 12` logical training runs. Three scoring views for each run would yield up to 36 score rows, not 36 training runs. An arm-defined learning-rate policy or loss adds no further multiplier. These counts describe the planned complete design; missing or ineligible results change observed coverage.

## One-Line Experiment-Design Summary

Begin every experiment-design proposal and design or slice change with one visible logical line in the user's language. Keep these five fields in the same order; natural screen wrapping does not change the format:

Keep this line compact: use short field labels and English dimension names without parenthetical Chinese translations. Established aliases such as `config`, `LR`, `arms`, `loss`, and `score` are suitable when their meanings are clear in the map. Preserve exact IDs, comparison values, weights, learning-rate policy, and scoring horizon. Put any needed terminology explanation outside the line.

```text
Total design dimensions: {registered dimensions and relevant levels} | Current varied: {comparison dimensions and candidate values} | Current marginalized: {averaged dimensions and eligible levels} | Marginalization rule: {support, weights and reduction order} | Current fixed: {dimension=value pairs}
```

Use the current study's full registered design space for the first field, including dimensions held fixed in this slice. List the names, not only a count. In Chinese, retain the user's label `总自由维度`; annotate a grouped inventory as `按设置分组` when bundled or nested choices prevent an independent-factor count. A range such as C01–C10 gives ten levels of one configuration group.

`Current varied` identifies the intended comparison. A population axis traversed only to form an average belongs under `Current marginalized`; do not silently treat it as another target comparison. Give actual fixed values, baseline and candidate values, the eligible population, and averaging weights. When several axes are averaged, include their reduction order. Use `none` for an empty set and `unresolved` for missing information. If the full map contains axes that are deferred or only reported separately, append their treatment briefly rather than mislabeling them as fixed or marginalized.

Illustrative Chinese example only: assume the protocol allows loss to vary independently within arm1; arm1 does not itself select the loss. No capstone configuration or current experiment is asserted here.

> 总自由维度：{config=C01–C10; LR; arms; loss; score; states} | 变动：{loss=MSE→Huber} | marginal：{states} | 规则：预定n州等权1/n | 固定：{config=C03; LR=1e-3 constant; arms=arm1; score=MAE@t+7}

If an actual arm also determines loss or learning rate, expose that dependency and the effective changed settings in the line. Never describe an arm as fixed while changing a setting that defines its identity. Keep the line derived from the same map and protocol; it is a display of current position, not another state record.

## Default Compact Orientation Card

Use the design summary line above as the minimum compact card when proposing or changing an experiment. Add only the question, evidence, scoring detail, or comparability information needed beyond that line; do not repeat its fields in a second unchanged card. For other experiment-facing updates, use a small paragraph or card in the user's language. Preserve exact IDs and explain specialist terms when needed outside the compact line. Include decision-relevant values inline and link the full map for the rest. Unknown values stay explicit; never fill them from memory or a suggestive arm name.

```text
Current: [stage / slice ID; planning, running, or interpreting; question]
Compare: [baseline -> candidate(s); settings actually changed]
Fixed: [claim-relevant settings and values; source for remaining controls]
Separate / aggregate: [dimensions retained; dimensions averaged, support and weights, or none]
Score: [data/split; metric; prediction day/window and averaging rule; checkpoint rule]
Change since previous slice: [only on a switch; old -> new and comparability impact]
Evidence: [relevant plan/run/result pointers; coverage or uncertainty when material]
```

The expanded card's headings and length are flexible; retain the five-field summary line for design proposals and changes. Combine additional fields for a simple study. Use the card for experiment-facing plans, progress, result interpretation, restarts, and handoffs; routine command progress does not need another unchanged card. Expand the map when requested, when its dimensions or dependencies change, or when the compact view no longer resolves confusion.

The card must explain what the agent is doing now, not merely recite all possible settings. If only the scoring view changes, state whether existing predictions can be rescored and whether earlier comparisons retain their meaning. Do not imply a new training campaign from an evaluation-only switch.

## Say What a Comparison Means

Replace an ambiguous phrase such as "marginal to X" with explicit treatments of the relevant dimensions:

- **Conditional comparison:** compare the named candidates at specified values of the other dimensions. A difference measured at one loss or state does not establish the same difference at other losses or states.
- **Marginal summary or contrast:** average over named dimensions using a stated population, support, and weights, while retaining the named fixed conditions. A marginal score summarizes one candidate; a marginal contrast compares candidates on the same defined support. Say which one is being reported.
- **Separate results:** retain a dimension in rows, panels, or individual statements. Separate state results are not a cross-state average. Report reversals or material heterogeneity when an average would hide them.

For example, if `M(candidate, state)` already uses one fixed scoring rule and the agreed within-state seed reduction, a state-averaged contrast can be written as:

```text
delta = sum over eligible states s of w(s) * [M(candidate, s) - M(baseline, s)]
```

State the sign convention and metric direction, and how `w(s)` is normalized. Equal state weights and sample-count weights answer different questions. Keep the same eligible states and agreed pairing or reduction for both candidates, or label a changed-support comparison and its limitation. Record missing, failed, or excluded runs and the accepted handling rule; do not silently average whichever runs happened to succeed. If weights or eligibility are unspecified, show separate results and keep the aggregate conclusion unresolved while continuing supported work.

A single-factor claim needs an appropriate matched comparison or an explicitly justified analysis. When an arm changes both learning rate and loss, call it a comparison of that bundle. Differences across independently tuned candidates describe the selected configurations under their selection rule; they do not isolate one setting's effect. Ranking by best observed score or choosing a checkpoint is selection, not marginalization. Preserve the selection rule and the split that supported it.

## Keep Scoring Semantics Visible

Training loss and evaluation metric are separate fields. Also separate prediction length, the scored day or window, and the rule that combines errors. For a seven-day forecast:

- Day 1 scores predictions at `t+1`.
- Day 7 scores predictions at `t+7` only.
- A seven-day mean score combines the defined daily scores across `t+1` through `t+7`.

Define the metric, units, valid-observation mask, day weights, population weights, and reduction order when they can affect the answer. A mean of daily errors and an error of averaged predictions are different operations. A label such as `h7` alone does not establish which rule is implemented; inspect the evaluation owner.

Keep the evaluation split, checkpoint selection metric and horizon, and scoring metric and horizon explicit. Rescoring an existing checkpoint does not retroactively change how it was selected. If results use different budgets, stopping rules, checkpoints, populations, or score definitions, name that difference before drawing a comparative conclusion. Preserve the host's test-access and model-selection boundaries.

## Preserve Position Through Changes and Restarts

1. At the start or restart, read the current state owner, relevant dimension map, accepted slice, and evidence needed for the current claim. Resolve source disagreements before making the affected decision; continue independent work supported by known settings.
2. At a design or slice change, record changed dimensions, retained controls, reason, source plan or protocol, and predecessor slice. Retain deferred axes and earlier result identities. A new score, population, or checkpoint rule changes the scope of comparison even if the model code is unchanged.
3. After execution, reconcile planned training identities with observed receipts and result coverage. Record deviations as observed facts rather than silently rewriting the accepted design to fit the run.
4. At result reporting and handoff, save the current slice and next comparison in the same owner, and attach conclusions to their original settings, aggregation, score definition, and eligible evidence. Explain whether the next step reuses artifacts or requires new training.

Keep this proportional. No new service, experiment database, tracking dependency, JSON schema, automatic training action, or generic preflight gate is required to keep a dimension map and orientation card useful.
