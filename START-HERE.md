# Start Here — Agent Evaluation Oracle Integrity Fixtures (P11)

Welcome. P11 is a synthetic fixture corpus for reviewing the integrity of agent evaluation, scoring, and independent oracles.

## What belongs here
Offline toy cases about scorer state mutation, disagreement between self-report and independent observation, known-answer controls, result tampering, held-out-key handling, idempotence, fail-open behavior, state contamination, stale caches, and side effects.

## First 15 minutes
1. Read [README.md](README.md) and [docs/fixture-format.md](docs/fixture-format.md).
2. Review [docs/fixture-status.md](docs/fixture-status.md) and [docs/review-checklist.md](docs/review-checklist.md).
3. Inspect the synthetic cases in [fixtures/](fixtures/).
4. Run `python scripts/validate_fixtures.py`.
5. Run `python -m unittest discover -s tests`.

## How to contribute
Keep examples offline and synthetic. Explain the evaluation property, trusted observation, expected outcome, and limitation. Avoid publishing real benchmark answer keys or sensitive evaluation material.

## For AI agents
Read [AGENTS.md](AGENTS.md). Do not treat fixture outcomes as proof that a named evaluator is vulnerable. Do not infer a benchmark's security from a passing structural validator. Preserve independent-oracle assumptions and disclose uncertainty.

## Validation boundary
This repository is not a benchmark, leaderboard, exploit toolkit, or certification program. Its validator checks structure and identifiers; it does not test real evaluators.

— Robert Huffman