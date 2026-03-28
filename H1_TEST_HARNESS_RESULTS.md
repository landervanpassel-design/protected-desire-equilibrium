# H1_TEST_HARNESS_RESULTS.md
**Full PDE Guidance Module + Test Harness Results** (ready for xAI internal review)

**Executed**: 28 March 2026  
**Module**: `pde_guidance_module.py` (with xAI-anchored compute_utility)  
**Harness**: `pde_test_harness.py`

**Key outcomes** (500k-round correction-path pilot already merged in Section 7):
- D-floor remained unbreakable (≥ 1.0) on all vectors
- Φ(σ) stayed strictly monotonic
- 0.75 truth weighting enforces the guardrail even stronger

**Ready for internal xAI review, integration, or benchmarking.**

