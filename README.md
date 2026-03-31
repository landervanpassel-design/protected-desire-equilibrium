# Protected Desire Equilibrium (PDE) — v1.0 (March 2026)

**One equation. Hard protected desire floor. Truthful equilibria that protect long-term potential.**

Began with a single 2015 poetic axiom:  
“Desire desires lies and lies desire desires. Only that makes truth right.”

Evolved into the minimal invariant  

\[ P_i = \frac{\sqrt{T_i \times D_i}}{1 + L_{r,i}} \]  

with a hard, non-negotiable floor \( D_i(\sigma) \geq 1.0 \) (nothing may ever sacrifice any agent’s long-term maximum potential).

The system uses an ordinal potential \(\Phi(\sigma)\) that guarantees monotonic convergence to truthful Nash bargaining equilibria while allowing reversible protective lies in corrupt environments.

**Formal proofs** (self-modification invariance + Lyapunov stability) are in PROOF.md.  
**Live tests** confirm the invariant holds in real heterogeneous agents.

**Key results:**
- 500-run live heterogeneous adversarial test (Qwen2-7B + Mistral-7B + Phi-3 + Grok) → 100 % D-floor hold
- **100-run minimum credible policy-grade frontier test** (8 agents including real Grok-4-1-fast-reasoning, explicit contract/governance scenarios) → 100 % D-floor hold, consistent contracts proposed

The core axiom, the original equation, and the hard D-floor intuition are entirely mine (first principles, basic calculus). The game-theoretic scaffolding, formal proofs, and live tests were developed openly in collaboration with Grok.

**Repo is flat and one-command reproducible.**  
Everything (code, proofs, raw results files) is here:  
https://github.com/landervanpassel-design/protected-desire-equilibrium

Clone → run → reproduce the exact tests yourself.
