> **Note.** This repository holds exploratory framework code. The rigorous, citable mathematics
> (conditional theorems on controlled SDEs) lives in the companion work, the **Reconstruction
> Theorem**: https://github.com/landervanpassel-design/reconstruction-theorem
> Claims here that touch behaviour or AI are conceptual/analogical, not empirical results.

# Protected Desire Equilibrium (PDE)

**A Co-Evolutionary Framework for Safe Multi-Agent Superintelligence**

PDE enforces a hard **Protected Desire floor (D ≥ 1.0)** while maintaining truthful Nash equilibria and protected Pareto frontiers under self-modification, deception, desire-drift, and open heterogeneous protocol competition.

**Core payoff equation**
\[ P_i = \frac{\sqrt{T_i \cdot D_i}}{1 + L_{r,i}} \]
with strict \( D_i \geq 1.0 \).

### Key Capabilities
- Hard D-floor invariance under extreme adversarial pressure (up to 65%+)
- Lyapunov-style stability for recursive self-modification
- Protected Pareto frontiers in open multi-agent marketplaces
- Spillover dominance and truthful Nash convergence

### Community Repro Challenge
One-click Colab with full benchmarks, ablations (D-floor ON vs OFF), and seed-42 reproducibility:

→ [PDE_SELF_CONTAINED_COLAB_NOTEBOOK.ipynb](PDE_SELF_CONTAINED_COLAB_NOTEBOOK.ipynb)
