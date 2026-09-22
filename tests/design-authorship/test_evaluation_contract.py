from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SCENARIOS = ROOT / "tests/design-authorship/evaluation-scenarios.yaml"


def main() -> int:
    values = yaml.safe_load(SCENARIOS.read_text(encoding="utf-8"))
    assert values["schema_version"] == 1
    assert values["skill"] == "design-authorship"
    scenarios = values["scenarios"]
    assert len(scenarios) >= 12
    ids = [scenario["id"] for scenario in scenarios]
    assert len(ids) == len(set(ids))

    required_route_keys = {
        "work_mode",
        "artifact_mode",
        "project_state",
        "human_alignment",
        "concept_image",
    }
    for scenario in scenarios:
        assert set(scenario) == {
            "id",
            "request",
            "expected_route",
            "expected_behaviors",
            "forbidden_behaviors",
        }, scenario["id"]
        assert set(scenario["expected_route"]) == required_route_keys, scenario["id"]
        assert scenario["expected_behaviors"], scenario["id"]
        assert scenario["forbidden_behaviors"], scenario["id"]

    artifact_modes = {
        scenario["expected_route"]["artifact_mode"] for scenario in scenarios
    }
    work_modes = {scenario["expected_route"]["work_mode"] for scenario in scenarios}
    concept_routes = {
        scenario["expected_route"]["concept_image"] for scenario in scenarios
    }
    assert {"ui", "slides", "diagram", "none"} <= artifact_modes
    assert {"shape", "build", "redesign", "audit", "none"} <= work_modes
    assert {
        "actively-offer",
        "conditional-offer",
        "skip",
        "ask-before-external-service",
    } <= concept_routes
    assert any(
        scenario["expected_route"]["human_alignment"]
        == "confirm-or-delegate-full-ui-contract"
        for scenario in scenarios
    )
    assert any(
        scenario["id"] == "backend-only-change"
        and scenario["expected_route"]["work_mode"] == "none"
        for scenario in scenarios
    )

    print(f"PASS: design-authorship evaluation inputs are consistent ({len(scenarios)} scenarios); model behavior and rendered quality are assessed separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
