import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_fixtures.py"
SPEC = importlib.util.spec_from_file_location("fixture_validator", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidatorTests(unittest.TestCase):
    def test_repository_fixtures_validate(self):
        errors, count = MODULE.validate()
        self.assertGreater(count, 0)
        self.assertEqual(errors, [])

    def test_required_fields_are_defined(self):
        self.assertIn("id", MODULE.REQUIRED)
        self.assertIn("expected_observation", MODULE.REQUIRED)


if __name__ == "__main__":
    unittest.main()
