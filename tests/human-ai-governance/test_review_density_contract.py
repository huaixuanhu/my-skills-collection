"""Validate synthetic evaluation inputs, not the quality of model prose."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills/human-ai-governance"
FIXTURE = Path(__file__).with_name("review-density-scenarios.yaml")


def main() -> int:
    data = yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))
    assert data["schema_version"] == 1
    assert data["skill"] == "human-ai-governance"
    assert data["data_kind"] == "synthetic"
    assert f'Skill version: `{data["version"]}`' in (
        SKILL / "SKILL.md"
    ).read_text(encoding="utf-8")

    scenarios = data["scenarios"]
    required_ids = {
        "bounded-result", "material-plan", "recovery-status", "high-consequence",
        "explicit-expanded", "formal-runbook",
        "distinct-issue-subjects", "unknown-issue-origin",
    }
    ids = [case["id"] for case in scenarios]
    assert len(ids) == len(set(ids))
    assert required_ids <= set(ids)
    assert {case["expected_density"] for case in scenarios} == {
        "compact", "expanded", "artifact-complete",
    }
    for case in scenarios:
        assert set(case) == {
            "id", "surface", "expected_density", "request", "context",
            "required_information", "exact_terms", "forbidden_behaviors",
        }, case["id"]
        assert case["surface"] in {"conversation", "formal-record"}
        assert case["request"] and case["context"]
        assert case["required_information"] and case["forbidden_behaviors"]
        assert len(case["exact_terms"]) == len(set(case["exact_terms"]))
        for value in case["exact_terms"]:
            assert value in case["context"], (case["id"], value)

    routes = data["routing_cases"]
    route_ids = [case["id"] for case in routes]
    assert len(route_ids) == len(set(route_ids))
    assert {case["expected"] for case in routes} == {"apply", "skip"}
    for case in routes:
        assert set(case) == {"id", "request", "expected"}
        assert case["request"]

    print("PASS: v0.7.8 review-density evaluation inputs are consistent; model behavior is assessed separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
