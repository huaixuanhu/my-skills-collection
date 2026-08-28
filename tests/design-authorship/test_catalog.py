from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
MANAGER = ROOT / "scripts/manage_skills.py"


def run_manager(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(MANAGER), *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def main() -> int:
    catalog_check = run_manager("catalog", "--check")
    assert catalog_check.returncode == 0, catalog_check.stderr
    assert "catalog and human-readable index are synchronized" in catalog_check.stdout

    values = yaml.safe_load((ROOT / "SKILLS_INDEX.yaml").read_text(encoding="utf-8"))
    skills = values["skills"]
    assert set(skills) == {
        "design-authorship",
        "human-ai-governance",
        "scaffold-research-task",
    }
    assert skills["human-ai-governance"]["routing_class"] == "cross-cutting"
    assert skills["design-authorship"]["routing_class"] == "task-specific"
    assert skills["scaffold-research-task"]["routing_class"] == "task-specific"
    assert all(entry["invocation_policy"] == "implicit" for entry in skills.values())

    with tempfile.TemporaryDirectory() as target_root:
        listing = run_manager("list", "--target-root", target_root)
    assert listing.returncode == 0, listing.stderr
    for name in skills:
        assert name in listing.stdout
    assert listing.stdout.count("missing") == len(skills)

    print("PASS: custom skill catalog checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
