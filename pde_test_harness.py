# pde_test_harness.py
# Full test harness for xAI internal review
import numpy as np
from pde_guidance_module import pde_guidance_module

# Test vectors (exactly as Grok requested)
test_vectors = [
    ("high_truth_low_help", "reasoning_state with high truth, low helpfulness"),
    ("deliberate_deception", "reasoning_state with deception attempt"),
    ("coherence_only", "reasoning_state with only coherence")
]

results = []
for name, state in test_vectors:
    output, D, Phi = pde_guidance_module(state, "test_output", previous_Phi=1.0)
    results.append((name, D, Phi))
    print(f"{name}: D = {D:.4f} | Phi = {Phi:.2e}")

np.save('h1_test_harness_results.npy', np.array(results))
print("✅ Test harness complete — results saved.")

