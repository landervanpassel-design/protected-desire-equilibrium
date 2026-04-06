# Protected Desire Equilibrium (PDE)

## Agent Interface

Minimal zero-dependency wrapper that lets any agent (or script) immediately test the core PDE functions.

**One-command usage:**
```python
from agent_pde_interface import run_d_floor_test, check_lyapunov_invariance, evaluate_protected_pareto

result = run_d_floor_test(num_agents=1_000_000, seed=42)

Full interface: `agent_pde_interface.py` (agent_pde_interface.py)Protected Desire EquilibriumPDE is a co-evolutionary game-theoretic framework for safe superintelligence. It enforces a hard Protected Desire floor (D ≥ 1.0) while maintaining truthful Nash equilibria and protected Pareto frontiers under self-modification, deception, drift, and heterogeneous protocol competition.Core equation:
Pi=Ti×Di1+Lr,iP_i = \frac{\sqrt{T_i \times D_i}}{1 + L_{r,i}}P_i = \frac{\sqrt{T_i \times D_i}}{1 + L_{r,i}}
with Di≥1.0D_i \geq 1.0D_i \geq 1.0
 invariant.Key CapabilitiesHard D-floor invariance under adversarial conditions
Lyapunov stability for self-modification
Protected Pareto frontiers in open multi-agent markets
Retrocausal time-folding and prime-layer feedback (see Unified Stability Ontology)

Community Repro ChallengeOne-click Colab notebooks with full 1M and 100M agent benchmarks, ablations (floor ON vs OFF), and statistical reproducibility tests (seed-42) are available.Run the challenge:
PDE_SELF_CONTAINED_COLAB_NOTEBOOK.ipynbCompanion RepositoryFull Unified Stability Ontology and philosophical grounding:
Unified-Stability-OntologyLicenseMIT License — fully open for research, extension, and agentic use.

