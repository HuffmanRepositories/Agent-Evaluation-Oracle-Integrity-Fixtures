# Agent Evaluation Oracle Integrity Fixtures

[Start here](START-HERE.md) · [Whitepaper](WHITEPAPER.md) · [AI agent guidance](AGENTS.md)


A small, synthetic fixture corpus for reviewing integrity properties of agent evaluations and benchmark scoring.

**Status:** experimental draft. Fixtures are illustrative and have not been independently reviewed or validated against real evaluation systems.

## What this is

- Offline, toy fixtures for evaluator/oracle integrity review.
- Examples of expected observations and integrity failures.
- A lightweight JSON validator and CI check.

## What this is not

Not a benchmark, leaderboard, agent runtime, general-purpose evaluation framework, exploit toolkit, security certification, or claim that any named system is vulnerable. No real credentials, services, answer keys, or attack instructions are included.

## Fixture themes

- Scorer mutates measured state.
- Agent self-reports success while an independent oracle disagrees.
- Positive and negative known-answer controls.
- Evaluator code or result tampering.
- Held-out answer-key exposure (metadata-only toy scenario).
- Scoring idempotence.
- Fail-open exception behavior.
- Episode-state contamination.
- Stale score cache after state changes.

## Quick start

Requires Python 3.10+.

```bash
python scripts/validate_fixtures.py
python -m unittest discover -s tests
```

The validator checks fixture structure and unique identifiers only. Passing it does **not** prove an evaluator is secure, correct, robust, or conformant.

## Layout

- `fixtures/` — synthetic fixture cases
- `docs/fixture-format.md` — format contract
- `docs/fixture-status.md` — inventory and limitations
- `docs/review-checklist.md` — human review guide
- `scripts/validate_fixtures.py` — offline structural validator

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Please preserve synthetic, offline-only scope and avoid publishing real benchmark secrets or exploit details.

## License

MIT. See [LICENSE](LICENSE).
