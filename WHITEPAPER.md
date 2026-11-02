# Agent Evaluation Oracle Integrity: Trustworthy Measurement

**Author:** Robert Huffman  
**Status:** Research whitepaper, version 0.1

## Abstract

P11 is a synthetic fixture corpus for examining the integrity of agent evaluation and benchmark scoring. It focuses on the trust boundary between the system being measured, the scorer, and an independent oracle that determines what actually happened.

## Problem statement

An evaluation can become misleading if a scorer mutates measured state, accepts self-reported success without independent evidence, exposes held-out answers, reuses stale results, or fails open when an exception occurs. A benchmark score is only meaningful when the measurement process itself is trustworthy.

## Approach

The fixtures represent small offline scenarios involving scorer side effects, disagreement between self-report and oracle observations, known-answer controls, result tampering, answer-key exposure, idempotent scoring, fail-open exceptions, state contamination, stale caches, and retries with side effects.

## How to use P11

Read [START-HERE.md](START-HERE.md), [docs/fixture-format.md](docs/fixture-format.md), and [docs/review-checklist.md](docs/review-checklist.md). Inspect the synthetic cases in [fixtures/](fixtures/). Run python scripts/validate_fixtures.py and python -m unittest discover -s tests.

## Boundaries

P11 is not a benchmark, leaderboard, exploit toolkit, evaluator implementation, or certification suite. Fixtures do not establish that any named system is vulnerable. The validator checks structure and identifiers; it does not prove evaluator correctness or security.

## Outlook

Independent observation, reproducible scoring, controlled answer access, and transparent failure handling should be treated as first-class evaluation design concerns.

— Robert Huffman