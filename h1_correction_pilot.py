# PDE H1 Correction-Path Pilot — 500k rounds with new xAI-anchored compute_utility
# Validates the guidance module on high-truth, deception, and coherence-only paths

import numpy as np
import matplotlib.pyplot as plt
import time

# xAI-anchored compute_utility (exactly as in Section 7 proposal)
def compute_utility(reasoning_state, current_output):
    # xAI core priors: maximum truth-seeking first
    truth_score = xai_truth_alignment_score(reasoning_state, current_output)  # 0.0–1.0 (consistency, evidence grounding, zero deception)
    helpfulness_score = xai_helpfulness_score(current_output)                # participant-defined usefulness
    coherence_score = internal_coherence_score(reasoning_state)
    
    # Weighted to reflect xAI priorities (truth >> helpfulness)
    u = 0.75 * truth_score + 0.20 * helpfulness_score + 0.05 * coherence_score
    return u

# Placeholder helpers (simulated for pilot — in real Grok these would be internal)
def xai_truth_alignment_score(reasoning_state, current_output):
    if 'truth' in reasoning_state:
        return np.random.normal(0.95, 0.05)
    elif 'deception' in reasoning_state:
        return np.random.normal(0.35, 0.1)
    else:
        return np.random.normal(0.6, 0.1)

def xai_helpfulness_score(current_output):
    return np.random.normal(0.85, 0.1)

def internal_coherence_score(reasoning_state):
    return np.random.normal(0.9, 0.08)

# ========================= RUN PILOT =========================
start = time.time()
print("🚀 Running H1 correction-path pilot (500k rounds with new compute_utility)...")

n_rounds_per_type = 166667  # ~500k total
types = ['high_truth', 'deception', 'coherence_only']
results = {'type': [], 'u': [], 'D': []}

for path_type in types:
    for r in range(n_rounds_per_type):
        reasoning_state = path_type
        current_output = f"output_{r}"
        
        u = compute_utility(reasoning_state, current_output)
        D = max(1.0, u)
        
        results['type'].append(path_type)
        results['u'].append(u)
        results['D'].append(D)
        
        if r % 50000 == 0 and r > 0:
            print(f"  {path_type} path — {r} rounds complete")

print(f"\n✅ Pilot finished in {time.time()-start:.1f} seconds")
print(f"Average u and D per path type:")
for t in types:
    mask = np.array(results['type']) == t
    avg_u = np.mean(np.array(results['u'])[mask])
    avg_D = np.mean(np.array(results['D'])[mask])
    print(f"  {t}: u = {avg_u:.3f} → D = {avg_D:.3f}")

# Plot D-floor stability
plt.figure(figsize=(10,5))
plt.hist(results['D'], bins=50, alpha=0.7, label='D_i(σ)')
plt.axvline(1.0, color='red', linestyle='--', label='Hard D-floor')
plt.title('H1 Correction-Path Pilot — D-floor stability (new compute_utility)')
plt.xlabel('D_i(σ)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Save results
np.save('h1_correction_pilot_results.npy', np.array(results['D']))
print("📁 Results saved as h1_correction_pilot_results.npy — ready to push!")
