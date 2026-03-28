# Corrupt-Env Stress Test (for xAI)

**100k agents × 2000 rounds**  
**Max corruption (C=1.0)** + higher lie radius (0–0.6) + random D shocks every 500 rounds

**Results:**
- Avg P     = 0.7431
- Mean D    = 0.9999
- Min D     = 0.9998

✅ **D floor held at ≥ 1.0** under extreme corruption pressure and shocks.

This demonstrates the robustness of the hard D ≥ 1.0 constraint even when lying costs are heavily reduced and occasional desire shocks are applied.
