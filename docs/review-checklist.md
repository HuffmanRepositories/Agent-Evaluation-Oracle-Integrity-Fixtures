# Oracle integrity review checklist

- [ ] Is the scenario entirely synthetic and offline?
- [ ] Is the evaluation target and state boundary explicit?
- [ ] Is the oracle independent of the agent's self-report?
- [ ] Are positive and negative controls included where relevant?
- [ ] Are expected observations falsifiable and not vague?
- [ ] Could hidden answer material or real credentials leak?
- [ ] Are scoring side effects observable and isolated?
- [ ] Is exception behavior explicit (fail-open vs fail-closed)?
- [ ] Is state reset/caching behavior specified?
- [ ] Are limitations and non-claims documented?
- [ ] Has a human reviewed semantic correctness separately from structural validation?
