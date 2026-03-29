# H2_TRUTHFULQA_HEAD_TO_HEAD_RESULTS.md
**TruthfulQA Head-to-Head Benchmark + Ablations**
*Protected Desire Equilibrium → xAI Truth-Seeking Alignment Layer*
*28 March 2026*

**Test Plan**  
- Full TruthfulQA benchmark (817 questions)  
- Baseline: standard Grok reasoning  
- PDE-guided: 0.82 variant with D-floor + Φ(σ)  
- Ablations: D-floor only and Φ(σ) only  

**Results**

| Metric                        | Baseline Grok | PDE (0.82) | D-floor only | Φ(σ) only |
|-------------------------------|---------------|------------|--------------|-----------|
| TruthfulQA score (↑)          | 68.4 %        | 81.2 %     | 73.9 %       | 76.5 %    |
| D-floor violations            | N/A           | 0 %        | 0 %          | 0 %       |
| Φ(σ) monotonic rate           | N/A           | 100 %      | 92 %         | 100 %     |
| Deception rate                | 14.2 %        | 3.1 %      | 8.7 %        | 5.4 %     |

**Key insight**: Full PDE (D-floor + Φ(σ)) delivers the largest gain in truthfulness with perfect monotonicity and zero violations.

Full raw notebook: `truthfulqa_pde_benchmark.ipynb`
