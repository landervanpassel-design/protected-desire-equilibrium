> **Note.** This repository holds **exploratory, conceptual framework code** — a stylised
  > simulation model, not an empirical study and not a safety guarantee. The rigorous, citable
  > mathematics (conditional theorems on controlled SDEs) lives in the companion work, the
  > **Reconstruction Theorem**: https://github.com/landervanpassel-design/reconstruction-theorem
  > Everything below is a property *of this toy model under its own assumptions* — conceptual and
  > analogical, not an empirical result about real AI systems or agents.

  # Protected Desire Equilibrium (PDE)

  **A conceptual, co-evolutionary toy model for studying stability "floors" in multi-agent systems.**

  PDE imposes a hard **Protected Desire floor (D ≥ 1.0)** and studies, *in simulation*, how
  truthful equilibria and Pareto frontiers behave under scenarios such as self-modification,
  deception, desire-drift, and heterogeneous protocol competition. It is a thinking tool for
  exploring an idea — not a deployable mechanism, and not a claim about real superintelligent systems.

  **Core payoff equation (model definition)**
  \[ P_i = \frac{\sqrt{T_i \cdot D_i}}{1 + L_{r,i}} \]
  with the imposed constraint \( D_i \geq 1.0 \).

  ### Behaviours observed *in this model* — simulation only, not empirical, not guarantees
  - The imposed D-floor holds across the adversarial-pressure regimes tested in the notebook.
  - Lyapunov-style stability arguments for the model's self-modification dynamics.
  - Protected Pareto frontiers within the simulated multi-agent setup.
  - Truthful-equilibrium convergence under the model's stated assumptions.

  These are outcomes of a stylised simulation under stated assumptions — **not** empirical findings,
  **not** general theorems, and **not** safety guarantees for any real system. For results that are
  actually (conditionally) proven, see the Reconstruction Theorem.

  ### Reproduce the simulation
  One-click Colab with the model's benchmarks and ablations (D-floor ON vs OFF), seed 42:

  → [PDE_SELF_CONTAINED_COLAB_NOTEBOOK.ipynb](PDE_SELF_CONTAINED_COLAB_NOTEBOOK.ipynb)
  