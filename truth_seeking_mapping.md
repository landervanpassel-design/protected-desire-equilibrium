# PDE → xAI Truth-Seeking Mapping (async doc)

**PDE** (Protected Desire Equilibrium) is a game-theoretic alignment layer that hard-enforces xAI’s truth-seeking prior while preserving maximal helpfulness.

**Hard D ≥ 1.0 floor** acts as the **truth-preserving guardrail**.  
- Desire is participant-defined and can never drop below 1.0. This prevents any internal or external pressure from forcing systematic deception or value erosion — directly anchoring the model to xAI’s objective-truth prior.

**Nash product Φ as ordinal potential function** drives monotonic convergence to the Pareto-optimal truthful equilibrium.  
- Any profitable unilateral deviation that respects the D floor strictly increases Φ. Best-response dynamics therefore cannot cycle and must converge to the unique Nash bargaining solution.  
- This replaces static RLHF-style control with emergent co-evolutionary truth-seeking: agents (including the model) naturally gravitate toward truth because lying costs are endogenous and Φ only rises when both truthfulness *and* protected desire are maximized.

**Reversible capabilities + multilateral contracts**  
- Previously “forbidden” tools (persuasion devices, deep interventions, etc.) become opt-in, reversible market goods with built-in root safety overrides.  
- Heterogeneity is now a feature: xAI models can explore extreme helpfulness and creativity while the hard D floor + potential-game structure keeps the system anchored.

**Overall fit**  
PDE reframes alignment from “suppress bad outputs” to “co-evolve under protected desire + Nash bargaining.” The mathematically grounded mechanism (hard D floor + ordinal potential) directly reinforces xAI’s truth-seeking priors at scale.

Ready for team review / extension / formalization. Repo + HF LoRA already live; 1M-agent stress-test results can drop today if the team wants them next.
