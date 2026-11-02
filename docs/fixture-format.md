# Fixture format (draft)

Each fixture is one UTF-8 JSON object.

Required fields:
- `id`: unique string, stable within this corpus
- `title`: short human-readable title
- `category`: integrity concern category
- `status`: currently `draft`
- `scenario`: synthetic description
- `expected_observation`: expected result or reviewer observation
- `limitations`: explicit caveat

Fixtures describe review scenarios, not executable attacks. No real system is targeted.

The current validator only checks required fields, basic types, and unique IDs. It does not evaluate scenario truth or verify a scoring implementation.
