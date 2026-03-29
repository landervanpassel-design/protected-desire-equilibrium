# H2_LEVEL2_LORA_SPEC.md
**Level 2: Lightweight LoRA Adapter for Native PDE Integration**
*Protected Desire Equilibrium → xAI Truth-Seeking Alignment Layer*
*Version 1.0 | 28 March 2026*

**Goal**: Fine-tune a small LoRA layer on PDE-guided trajectories so Grok internally learns the hard D ≥ 1.0 floor and monotonic Φ(σ) behaviour.

**Spec Overview**
- Rank: 8 (low-rank for minimal overhead)
- Alpha: 16
- Target modules: q_proj, v_proj, o_proj (core attention)
- Training data: 10k+ PDE-guided trajectories (generated from Level 1 wrapper)
- Loss: Combined cross-entropy + custom PDE loss (penalizes D < 1.0 or Φ(σ) decrease)
- Epochs: 1–2 (very light fine-tune)

**Initial Adapter Outline (pseudocode)** in `pde_lora_adapter.py`

**Training harness** in `pde_lora_training_harness.ipynb`

**Ready for immediate training or refinement.**
