from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "skills/design-authorship"


def main() -> int:
    expected_files = {
        "SKILL.md",
        "agents/openai.yaml",
        "references/concept-image-calibration.md",
        "references/content-to-form.md",
        "references/critique-and-verification.md",
        "references/diagrams.md",
        "references/intent-and-reference.md",
        "references/product-structure.md",
        "references/project-design-context.md",
        "references/slides.md",
        "references/ui-interaction.md",
    }
    actual_files = {
        path.relative_to(CANDIDATE).as_posix()
        for path in CANDIDATE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    assert actual_files == expected_files, sorted(actual_files ^ expected_files)

    skill = (CANDIDATE / "SKILL.md").read_text(encoding="utf-8")
    assert "Skill version: `0.2.0`" in skill
    assert len(skill.splitlines()) < 120
    frontmatter = skill.split("---", 2)[1]
    for required in (
        "name: design-authorship",
        "user interfaces",
        "presentation slides",
        "presentation-like HTML",
        "explanatory diagrams",
        "interaction states",
        "concept-image calibration",
        "rendered visual review",
    ):
        assert required in frontmatter, required

    for required in (
        "obtain human confirmation or explicit delegation",
        "supported surfaces and input methods",
        "`selected`, `hover`, `focus`, `pressed`, `disabled`, `empty`, `loading`, `error`, and success states",
        "actively offer concept-image calibration",
        "offer it only when original imagery, visual world, or composition would materially improve the story",
        "Do not add aesthetic lint scripts",
        "numerical taste gates",
        "Treat anti-default observations as prompts for contextual review, not bans",
        "a repository catalog can help routing and management but cannot activate a missing installation or grant authority",
    ):
        assert required in skill, required

    agent_metadata = (CANDIDATE / "agents/openai.yaml").read_text(encoding="utf-8")
    assert 'display_name: "Design Authorship"' in agent_metadata
    assert "$design-authorship" in agent_metadata
    assert "allow_implicit_invocation: true" in agent_metadata

    ui = (CANDIDATE / "references/ui-interaction.md").read_text(encoding="utf-8")
    for required in (
        "obtain confirmation or explicit delegation before implementation",
        "desktop width or window range",
        "mobile width or device class",
        "empty, loading, error, partial, success, and stale-data states",
        "Do not invent hover as a mobile interaction",
        "For a bounded repair, limit alignment to affected surfaces",
    ):
        assert required in ui, required

    concept = (CANDIDATE / "references/concept-image-calibration.md").read_text(
        encoding="utf-8"
    )
    for required in (
        "do not claim which underlying model it uses",
        "Do not send private screenshots",
        "styleframe or composition reference, not as production truth",
        "accessibility conformance",
    ):
        assert required in concept, required

    critique = (CANDIDATE / "references/critique-and-verification.md").read_text(
        encoding="utf-8"
    )
    assert "Do not calculate a taste score" in critique
    assert "require every subjective axis to exceed a number" in critique
    assert "derive a universal completion condition" in critique
    assert "task's agreed acceptance criteria" in critique

    assert not (CANDIDATE / "scripts").exists()
    assert not (CANDIDATE / "assets").exists()

    # Every runtime reference must be reachable from the entrypoint. This checks
    # discoverability and missing files, not whether the instructions are good.
    pending = [CANDIDATE / "SKILL.md"]
    visited = set()
    while pending:
        page = pending.pop().resolve()
        if page in visited:
            continue
        visited.add(page)
        for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "#")):
                continue
            resolved = (page.parent / target.split("#", 1)[0]).resolve()
            assert resolved.is_relative_to(CANDIDATE.resolve()), target
            assert resolved.is_file(), (page, target)
            if resolved.suffix == ".md":
                pending.append(resolved)
    assert {path.resolve() for path in (CANDIDATE / "references").glob("*.md")} <= visited

    print("PASS: design-authorship v0.2.0 package and reference-link checks passed; design behavior is assessed separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
