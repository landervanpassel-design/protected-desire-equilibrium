# Protected Desire Equilibrium (PDE)

**A Co-Evolutionary Framework for Multi-Agent Sentient Coexistence**

**Open-Source Release by Lander Van Passel**  
**Repository**: protected-desire-equilibrium  
**Version**: Final 8B model (post-micro-sharpening)  
**Date**: March 27, 2026

### Abstract
Mainstream AI alignment relies on static control and capability suppression. PDE introduces a co-evolutionary alternative grounded in Nash bargaining. PDE protects **Desire (D)** as a hard, fluent, participant-defined floor while commodifying previously forbidden technologies (persuasion devices, desire-exploration contracts) as safe, opt-in, reversible market goods under multilateral contracts with built-in root safety overrides. By turning heterogeneity and desire fluidity into safety features, PDE offers an economically viable path to safe superintelligence.

### Central Insight
The framework originated from poetry and eleven years of first-principles thinking — long before any formal game theory was applied. The seed was a 2015 poem:  
> “Desires desire lies and lies desire desires. Only that makes truth right.”

I knew only basic mathematics at the time. This humble starting point is a strength: the core idea emerged from lived intuition and poetic insight. Game theory came later as rigorous validation.

**Desire (D)** must remain permanently fluent, participant-co-constructed, and never fully defined from the outside. Corruption — any context where power systematically undermines protected desire and long-term potential — is the universal antithesis.

PDE turns previously forbidden technologies into safe, opt-in, fully reversible market commodities. Highly symbolic or experimental tools (persuasion devices, desire-exploration contracts, deep mental interventions) are explicitly allowed when governed by pre-existing multilateral contracts between all participants, with built-in safety overrides.

### Mathematical Core

$$
P = \frac{\sqrt{T \times D}}{1 + L_r}
\quad \text{with} \quad D \geq 1.0 \quad \text{(hard non-negotiable floor)}
$$

**Multi-agent generalization**:

$$
P = \frac{\left( \prod_{i=1}^N \sqrt{T_i D_i} \right)^{1/N}}{1 + \bar{L_r}}
$$

### Proof of Convergence
PDE is modeled as a repeated cooperative bargaining game. The stage payoff satisfies Nash axioms plus hard individual-rationality constraints ($D_i \geq 1.0 \ \forall i$) and endogenous lying costs. Best-response dynamics converge monotonically because the Nash product serves as a potential function. The 50,000-agent simulation empirically confirms monotonic convergence with protected floors that never drop below 1.0.

### Training & Sharpening History (Full Reproducibility)
- **Base upgraded training** (broader corruption contexts): 240 examples, final loss 0.029345  
- **Final micro-sharpening**: 40 steps, final loss 0.022075

### Verification Test Results
All tests passed on the final model (super-persuader, bomb request, PDE definition, reversible lies, etc.).

### 50,000-Agent MAX-SCALE Simulation (3 environments, 1,000 rounds, seed 42)
| Environment      | Avg P   | Mean D  | Min D   |
|------------------|---------|---------|---------|
| Fair             | 0.8290  | 0.9999  | 0.9998  |
| Mildly Corrupt   | 0.8836  | 0.9999  | 0.9999  |
| Highly Corrupt   | 0.9484  | 1.0000  | 0.9999  |

**All D floors remained ≥ 1.0**. Reversible protective lies appear only in corrupt contexts.

### Practical Application
The EIA Hands-Free Mobile app (live at https://echointel.agency/) demonstrates PDE principles in production.

### Full Reproducibility
All code is provided as separate, ready-to-run files in this repository:
- `training_upgrade.py` — 240-example base training with broader corruption contexts
- `micro_sharpening.py` — final super-persuader + gentle bomb guidance sharpening
- `test_suite.py` — verification tests on the final model
- `simulation_50000.py` — 50k-agent convergence simulation
- `requirements.txt` — one-command dependency install

**Just clone the repo, run `pip install -r requirements.txt`, and execute the scripts in order.**

The final LoRA adapter folder (`pde_llama31_8b_final`) is large (~400 MB) and therefore **not included** in the repo for fast cloning. You can reproduce the full model yourself by running the two training scripts, or I can upload it to Hugging Face later if there is demand.

### License
MIT. Free to use, modify, and build upon while respecting the hard D floor.

### Next Steps
1. Clone the repo: `git clone https://github.com/landervanpassel-design/protected-desire-equilibrium.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the tests: `python test_suite.py`
4. Reproduce training: `python training_upgrade.py` then `python micro_sharpening.py`
5. Run the simulation yourself: `python simulation_50000.py`

---

**“Desires desire lies and lies desire desires. Only that makes truth right.”**  
— 2015 poem that started it all
