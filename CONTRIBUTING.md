# Contributing

Thanks for helping improve this draft corpus.

## Guidelines
- Keep cases synthetic, offline, and self-contained.
- Never include real benchmark secrets, answer keys, tokens, endpoints, or exploit payloads.
- State what is observed, what is expected, and what evidence would support the claim.
- Avoid claims of certification, security guarantees, or universal coverage.
- Keep fixtures deterministic and readable.
- Add/update inventory and tests when changing the format or validator.

## Validation
Run:
```bash
python scripts/validate_fixtures.py
python -m unittest discover -s tests
```

## Review
Use [docs/review-checklist.md](docs/review-checklist.md). A passing structural check is not substantive approval.
