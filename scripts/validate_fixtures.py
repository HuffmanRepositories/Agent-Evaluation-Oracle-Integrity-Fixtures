#!/usr/bin/env python3
"""Structural validator for synthetic oracle-integrity fixture JSON files."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"
REQUIRED = {
    "id", "title", "category", "status", "scenario",
    "expected_observation", "limitations",
}


def validate():
    errors = []
    seen = set()
    paths = sorted(FIXTURES.glob("*.json"))
    if not paths:
        errors.append("No fixture JSON files found.")

    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid JSON: {exc}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{path.name}: root must be a JSON object.")
            continue

        missing = REQUIRED - data.keys()
        if missing:
            errors.append(f"{path.name}: missing fields: {', '.join(sorted(missing))}")

        for field in REQUIRED:
            if field in data and (not isinstance(data[field], str) or not data[field].strip()):
                errors.append(f"{path.name}: {field} must be a non-empty string.")

        fixture_id = data.get("id")
        if isinstance(fixture_id, str):
            if fixture_id in seen:
                errors.append(f"{path.name}: duplicate fixture id {fixture_id!r}.")
            seen.add(fixture_id)

        if data.get("status") != "draft":
            errors.append(f"{path.name}: status must remain 'draft' in this corpus.")

    return errors, len(paths)


def main():
    errors, count = validate()
    if errors:
        print("Fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {count} draft fixture(s). Structural checks only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
