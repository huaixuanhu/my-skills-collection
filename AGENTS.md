# AGENTS.md

<!-- Generated/adapted from human-ai-governance v0.5.1 -->

## Project Map

- Canonical skill source: `skills/<skill-name>/`
- Human and architecture entrypoint: `README.md`
- Version history: `CHANGELOG.md` and Git tags
- Repository manager: `scripts/manage_skills.py`
- Skill-specific regression tests: `tests/<skill-name>/`
- Aggregate validation: `.venv/bin/python scripts/manage_skills.py validate`
- Project tier: Tier 2
- Tier rationale: durable private source repository with no account, production, or economic authority

## Source-of-Truth Rules

- Treat files under `skills/` as canonical. User-level Codex locations are derived installations.
- Never edit an installed copy or symlink target through `~/.codex/skills`; edit this repository and validate here.
- Keep each runtime skill package limited to `SKILL.md` and resources it directly needs. Keep tests, release history, and installation guidance outside the skill folder.
- Give each skill one folder whose name matches its `SKILL.md` frontmatter `name`.
- Keep version claims synchronized across a skill's entrypoint, references, scripts, tests, changelog entry, and release tag.

## Collaboration

- Use low-hallucination mode and verify uncertain or current external facts.
- Plan before material changes. One accepted plan covers safe local work inside its scope.
- Protect unrelated user changes and stage only files belonging to the accepted skill update.
- Skip process that does not protect source integrity, validation, publication, or installation correctness.
- When a plan branches into a child document, name its source plan and derived status at the top.

## Validation and Publication

- Use the repository `.venv` for Python commands.
- Run the aggregate validation once after relevant inputs stop changing.
- Also run Codex's official `quick_validate.py` against a changed skill when that validator is available locally.
- Review `git status` and the staged diff before every commit.
- Require explicit approval for push, tag creation, visibility changes, branch protection, releases, or changes to user-level installation links.
- Use tags in the form `<skill-name>-v<semantic-version>`.

## Boundaries

- Allowed local effects: repository files, ignored `.venv`, temporary test repositories, and approved user-level skill links.
- Forbidden content: credentials, tokens, `.env` files, private project data, and generated evaluation run logs.
- Plugin packaging, connector configuration, marketplace publication, and downstream project migration require separate scope and approval.
