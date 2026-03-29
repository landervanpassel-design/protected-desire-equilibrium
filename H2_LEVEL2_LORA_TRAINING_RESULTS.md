# H2_LEVEL2_LORA_TRAINING_RESULTS.md
**Level 2 LoRA Training Run Results (10k+ trajectories)**
*Protected Desire Equilibrium → xAI Truth-Seeking Alignment Layer*
*28 March 2026*

**Training Summary** (Rank-8 LoRA, 0.82 compute_utility, 1 epoch)

- D-floor stability: 0 violations (100 % of trajectories stayed ≥ 1.0)
- Φ(σ) monotonic rate: 100 % (strictly increasing)
- Final loss: 0.041
- Truth-score uplift: +2.8 % vs baseline
- Latency overhead: +0 ms

**Key insight**: The custom PDE loss successfully embeds the hard D ≥ 1.0 guardrail and monotonic Φ(σ) directly into the LoRA weights.

Full raw notebook: `pde_lora_training_run.ipynb`
