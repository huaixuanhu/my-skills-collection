from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREFLIGHT = (
    Path(sys.argv[1]).resolve()
    if len(sys.argv) > 1
    else ROOT / "skills/human-ai-governance/scripts/governance_preflight_template.py"
)


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=False, text=True, capture_output=True)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def assignment_secret(suffix: str) -> str:
    return "real_" + "secret_value_" + suffix


def token_secret(suffix: str) -> str:
    return "sk-" + ("a" * 24) + suffix


def api_key_assignment(value: str, *, quoted: bool = False) -> str:
    rendered = f'"{value}"' if quoted else value
    return "api_" + "key = " + rendered + "\n"


def commit_all(root: Path, message: str) -> None:
    run(["git", "add", "."], root)
    result = run(["git", "commit", "-qm", message], root)
    assert result.returncode == 0, result.stderr


def init_repo(root: Path, marker: str = "0.7.8") -> None:
    run(["git", "init", "-q"], root)
    run(["git", "config", "user.email", "test@example.invalid"], root)
    run(["git", "config", "user.name", "Governance Test"], root)
    write(root / "AGENTS.md", f"Generated/adapted from human-ai-governance v{marker}\n")
    write(root / "ARCHITECTURE.md", "# Architecture\n\nInitial.\n")
    write(root / "CHANGELOG.md", "## 2026-07-10 10:00 AEST\n\n- Initial.\n- Reason: fixture.\n")
    write(
        root / "governance/AI_AGENT_LOG.md",
        "## 2026-07-10 10:00 AEST\n\n"
        "- Task: initial fixture.\n"
        "- Plan agreed: yes.\n"
        "- Changed files: fixture.\n"
        "- Reason: fixture.\n"
        "- Validation: passed.\n"
        "- Safety notes: local only.\n",
    )
    commit_all(root, "initial")


def preflight(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return run([sys.executable, str(PREFLIGHT), "--repo-root", str(root), *args], root)


def update_trace(root: Path, *, architecture: bool = False, changed: str = "runtime") -> None:
    if architecture:
        write(root / "ARCHITECTURE.md", f"# Architecture\n\nUpdated for {changed}.\n")
    write(
        root / "CHANGELOG.md",
        "## 2026-07-11 10:00 AEST\n\n"
        f"- Changed {changed}.\n"
        "- Reason: test v0.7.8 behavior.\n\n"
        "## 2026-07-10 10:00 AEST\n\n"
        "- Initial.\n"
        "- Reason: fixture.\n",
    )
    write(
        root / "governance/AI_AGENT_LOG.md",
        "## 2026-07-11 10:00 AEST\n\n"
        f"- Task: test {changed}.\n"
        "- Plan agreed: yes.\n"
        f"- Changed files: {changed}.\n"
        "- Reason: test v0.7.8 behavior.\n"
        "- Validation: passed.\n"
        "- Safety notes: fixture only.\n\n"
        "## 2026-07-10 10:00 AEST\n\n"
        "- Task: initial fixture.\n"
        "- Plan agreed: yes.\n"
        "- Changed files: fixture.\n"
        "- Reason: fixture.\n"
        "- Validation: passed.\n"
        "- Safety notes: local only.\n",
    )


def assert_pass(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, result.stdout + result.stderr


def main() -> int:
    assert PREFLIGHT.exists(), PREFLIGHT

    missing_tier = run([sys.executable, str(PREFLIGHT)], ROOT)
    assert missing_tier.returncode == 2
    assert "--tier" in missing_tier.stderr

    with tempfile.TemporaryDirectory(prefix="governance-v074-") as temp:
        base = Path(temp)

        not_repo = base / "not-repo"
        not_repo.mkdir()
        result = preflight(not_repo, "--tier", "1")
        assert result.returncode == 1
        assert "could not inspect repository state" in result.stdout
        assert "no staged, unstaged, or untracked changes" not in result.stdout

        clean = base / "clean"
        clean.mkdir()
        init_repo(clean)
        for tier in range(1, 6):
            assert_pass(preflight(clean, "--tier", str(tier), "--require-skill-marker"))

        stale = base / "stale"
        stale.mkdir()
        init_repo(stale, marker="0.3.0")
        result = preflight(stale, "--tier", "3", "--require-skill-marker")
        assert result.returncode == 1
        assert "skill marker is stale" in result.stdout

        tier_one = base / "tier-one"
        tier_one.mkdir()
        init_repo(tier_one)
        write(tier_one / "src/local.py", "value = 1\n")
        assert_pass(preflight(tier_one, "--tier", "1", "--require-skill-marker"))

        tier_two = base / "tier-two"
        tier_two.mkdir()
        init_repo(tier_two)
        write(tier_two / "src/local.py", "value = 2\n")
        result = preflight(tier_two, "--tier", "2", "--require-skill-marker")
        assert result.returncode == 1
        assert "CHANGELOG.md was not updated" in result.stdout

        for name, path, content in (
            ("readme-only", "README.md", "# Updated wording\n"),
            ("test-only", "tests/test_app.py", "def test_fixture():\n    assert True\n"),
            ("lockfile-only", "package-lock.json", '{"lockfileVersion": 3}\n'),
        ):
            repo = base / name
            repo.mkdir()
            init_repo(repo)
            write(repo / path, content)
            assert_pass(preflight(repo, "--tier", "3", "--require-skill-marker"))

        secret_in_readme = base / "secret-in-readme"
        secret_in_readme.mkdir()
        init_repo(secret_in_readme)
        readme_secret = assignment_secret("123")
        write(secret_in_readme / "README.md", api_key_assignment(readme_secret))
        result = preflight(
            secret_in_readme,
            "--tier",
            "1",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert "real secret assignment" in result.stdout
        assert readme_secret not in result.stdout

        unicode_secret = base / "unicode-secret"
        unicode_secret.mkdir()
        init_repo(unicode_secret)
        unicode_path = unicode_secret / "src/秘密.py"
        unicode_secret_value = assignment_secret("456")
        write(unicode_path, api_key_assignment(unicode_secret_value))
        run(["git", "add", "src/秘密.py"], unicode_secret)
        write(unicode_path, api_key_assignment("placeholder"))
        result = preflight(
            unicode_secret,
            "--tier",
            "1",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert "src/秘密.py" in result.stdout
        assert "real secret assignment" in result.stdout
        assert "staged index" in result.stdout
        assert unicode_secret_value not in result.stdout

        trailing_space_secret = base / "trailing-space-secret"
        trailing_space_secret.mkdir()
        init_repo(trailing_space_secret)
        trailing_secret_value = assignment_secret("789")
        write(
            trailing_space_secret / "src/trailing.py ",
            api_key_assignment(trailing_secret_value),
        )
        result = preflight(
            trailing_space_secret,
            "--tier",
            "1",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert '"src/trailing.py "' in result.stdout
        assert "real secret assignment" in result.stdout
        assert trailing_secret_value not in result.stdout

        renamed_unicode = base / "renamed-unicode"
        renamed_unicode.mkdir()
        init_repo(renamed_unicode)
        write(renamed_unicode / "src/old.py", "value = 1\n")
        commit_all(renamed_unicode, "add rename source")
        run(["git", "mv", "src/old.py", "src/新 name.py"], renamed_unicode)
        renamed_secret_value = assignment_secret("987")
        write(
            renamed_unicode / "src/新 name.py",
            api_key_assignment(renamed_secret_value),
        )
        result = preflight(
            renamed_unicode,
            "--tier",
            "1",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert "src/新 name.py" in result.stdout
        assert "working tree" in result.stdout
        assert renamed_secret_value not in result.stdout

        renamed_out_of_source = base / "renamed-out-of-source"
        renamed_out_of_source.mkdir()
        init_repo(renamed_out_of_source)
        write(renamed_out_of_source / "src/old.py", "value = 1\n")
        commit_all(renamed_out_of_source, "add source module")
        (renamed_out_of_source / "archive").mkdir()
        run(
            ["git", "mv", "src/old.py", "archive/old.py"],
            renamed_out_of_source,
        )
        update_trace(renamed_out_of_source, changed="source module removal")
        result = preflight(
            renamed_out_of_source,
            "--tier",
            "3",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert "module-topology or migration changes detected" in result.stdout
        update_trace(
            renamed_out_of_source,
            architecture=True,
            changed="source module removal",
        )
        assert_pass(
            preflight(
                renamed_out_of_source,
                "--tier",
                "3",
                "--require-skill-marker",
            )
        )

        trailing_root = base / "repository-with-trailing-space "
        trailing_root.mkdir()
        init_repo(trailing_root)
        write(trailing_root / "src/local.py", "value = 1\n")
        assert_pass(preflight(trailing_root, "--tier", "1", "--require-skill-marker"))

        staged_secret = base / "staged-secret"
        staged_secret.mkdir()
        init_repo(staged_secret)
        staged_path = staged_secret / "src/config.py"
        staged_token = token_secret("123456")
        write(staged_path, api_key_assignment(staged_token, quoted=True))
        run(["git", "add", "src/config.py"], staged_secret)
        write(staged_path, api_key_assignment("placeholder", quoted=True))
        result = preflight(staged_secret, "--tier", "1", "--require-skill-marker")
        assert result.returncode == 1
        assert "token/private-key pattern in staged index" in result.stdout
        assert staged_token not in result.stdout

        working_secret = base / "working-secret"
        working_secret.mkdir()
        init_repo(working_secret)
        working_path = working_secret / "src/config.py"
        write(working_path, api_key_assignment("placeholder", quoted=True))
        run(["git", "add", "src/config.py"], working_secret)
        working_token = token_secret("654321")
        write(working_path, api_key_assignment(working_token, quoted=True))
        result = preflight(working_secret, "--tier", "1", "--require-skill-marker")
        assert result.returncode == 1
        assert "token/private-key pattern in working tree" in result.stdout
        assert working_token not in result.stdout

        staged_side_effect = base / "staged-side-effect"
        staged_side_effect.mkdir()
        init_repo(staged_side_effect)
        side_effect_path = staged_side_effect / "src/action.py"
        write(side_effect_path, "def place_order():\n    return 'fixture'\n")
        run(["git", "add", "src/action.py"], staged_side_effect)
        write(side_effect_path, "def safe_action():\n    return 'fixture'\n")
        result = preflight(
            staged_side_effect,
            "--tier",
            "1",
            "--strict-side-effects",
            "--require-skill-marker",
        )
        assert result.returncode == 1
        assert "side-effect term needing review: place_order in staged index" in result.stdout

        staged_plan = base / "staged-plan"
        staged_plan.mkdir()
        init_repo(staged_plan)
        staged_plan_path = staged_plan / "plan_docs/PLAN_V1_STAGE2.md"
        write(staged_plan_path, "# Stage 2\n")
        update_trace(staged_plan, changed="staged plan")
        run(["git", "add", "."], staged_plan)
        write(
            staged_plan_path,
            "# Stage 2\n\n"
            "Source plan: `plan_docs/PLAN_V1_MASTER.md`\n\n"
            "Derived from: the accepted master plan\n",
        )
        result = preflight(staged_plan, "--tier", "3", "--require-skill-marker")
        assert result.returncode == 1
        assert "should declare Source plan" in result.stdout
        assert "staged index" in result.stdout

        staged_marker = base / "staged-marker"
        staged_marker.mkdir()
        init_repo(staged_marker)
        write(
            staged_marker / "AGENTS.md",
            "Generated/adapted from human-ai-governance v0.5.0\n",
        )
        run(["git", "add", "AGENTS.md"], staged_marker)
        write(
            staged_marker / "AGENTS.md",
            "Generated/adapted from human-ai-governance v0.7.8\n",
        )
        result = preflight(staged_marker, "--tier", "1", "--require-skill-marker")
        assert result.returncode == 1
        assert "skill marker is stale in AGENTS.md in staged index" in result.stdout

        staged_env_deletion = base / "staged-env-deletion"
        staged_env_deletion.mkdir()
        init_repo(staged_env_deletion)
        write(staged_env_deletion / ".env", "placeholder=true\n")
        commit_all(staged_env_deletion, "add legacy env fixture")
        (staged_env_deletion / ".env").unlink()
        run(["git", "add", "-u", ".env"], staged_env_deletion)
        assert_pass(
            preflight(
                staged_env_deletion,
                "--tier",
                "1",
                "--require-skill-marker",
            )
        )

        existing_module = base / "existing-module"
        existing_module.mkdir()
        init_repo(existing_module)
        write(existing_module / "src/action.py", "VALUE = 1\n")
        commit_all(existing_module, "add existing module")
        write(existing_module / "src/action.py", "VALUE = 2\n")
        update_trace(existing_module, changed="existing module")
        assert_pass(
            preflight(existing_module, "--tier", "3", "--require-skill-marker")
        )

        added_module = base / "added-module"
        added_module.mkdir()
        init_repo(added_module)
        write(added_module / "src/new_module.py", "VALUE = 1\n")
        update_trace(added_module, changed="new module")
        result = preflight(added_module, "--tier", "3", "--require-skill-marker")
        assert result.returncode == 1
        assert "module-topology or migration changes detected" in result.stdout
        update_trace(added_module, architecture=True, changed="new module")
        assert_pass(preflight(added_module, "--tier", "3", "--require-skill-marker"))

        root_plan = base / "root-plan"
        root_plan.mkdir()
        init_repo(root_plan)
        write(root_plan / "plan_docs/PLAN_V1_MASTER.md", "# Master Plan\n")
        update_trace(root_plan, changed="root plan")
        assert_pass(preflight(root_plan, "--tier", "3", "--require-skill-marker"))

        content_root_plan = base / "content-root-plan"
        content_root_plan.mkdir()
        init_repo(content_root_plan)
        write(
            content_root_plan / "plan_docs/ROADMAP.md",
            "# Roadmap\n\nDocument nature: master plan\n",
        )
        update_trace(content_root_plan, changed="content-marked root plan")
        assert_pass(
            preflight(content_root_plan, "--tier", "3", "--require-skill-marker")
        )

        child_plan = base / "child-plan"
        child_plan.mkdir()
        init_repo(child_plan)
        path = child_plan / "plan_docs/PLAN_V1_STAGE2.md"
        write(path, "# Stage 2\n")
        update_trace(child_plan, changed="child plan")
        result = preflight(child_plan, "--tier", "3", "--require-skill-marker")
        assert result.returncode == 1
        assert "should declare Source plan" in result.stdout
        write(
            path,
            "# Stage 2\n\n"
            "Source plan: `plan_docs/PLAN_V1_MASTER.md`\n\n"
            "Derived from: the accepted master plan\n",
        )
        assert_pass(preflight(child_plan, "--tier", "3", "--require-skill-marker"))

        tier_four = base / "tier-four"
        tier_four.mkdir()
        init_repo(tier_four)
        write(tier_four / "src/action.py", "def place_order():\n    return 'fixture'\n")
        update_trace(tier_four, architecture=True, changed="order action")
        assert_pass(preflight(tier_four, "--tier", "4", "--require-skill-marker"))
        strict = preflight(
            tier_four,
            "--tier",
            "4",
            "--strict-side-effects",
            "--require-skill-marker",
        )
        assert strict.returncode == 1
        assert "side-effect term needing review: place_order" in strict.stdout

        tier_five = base / "tier-five"
        tier_five.mkdir()
        init_repo(tier_five)
        write(
            tier_five / "src/execution/order_router.py",
            "def submit_order():\n    return 'in-envelope fixture'\n",
        )
        update_trace(tier_five, architecture=True, changed="Tier 5 order router")
        reviewed = preflight(
            tier_five,
            "--tier",
            "5",
            "--strict-side-effects",
            "--reviewed-side-effect-path",
            "src/execution/order_router.py",
            "--require-skill-marker",
        )
        assert_pass(reviewed)
        assert "current diff acknowledged" in reviewed.stdout
        assert "runtime authorization still applies" in reviewed.stdout

        risk_reducing = base / "risk-reducing"
        risk_reducing.mkdir()
        init_repo(risk_reducing)
        write(
            risk_reducing / "src/action.py",
            "HTTP_METHOD = 'POST'\n\n"
            "def cancel_order():\n"
            "    return 'risk-reducing fixture'\n",
        )
        update_trace(risk_reducing, architecture=True, changed="risk-reducing action")
        assert_pass(
            preflight(
                risk_reducing,
                "--tier",
                "5",
                "--strict-side-effects",
                "--require-skill-marker",
            )
        )

        large_agents = base / "large-agents"
        large_agents.mkdir()
        init_repo(large_agents)
        write(
            large_agents / "AGENTS.md",
            "Generated/adapted from human-ai-governance v0.7.8\n" + ("x" * 33_000),
        )
        result = preflight(
            large_agents,
            "--tier",
            "1",
            "--require-skill-marker",
        )
        assert_pass(result)
        assert "exceeds the common 32 KiB project-doc budget" in result.stdout

    print("PASS: v0.7.8 preflight behavior tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
