"""
PDE/USO Agent Interface
Minimal, zero-dependency wrapper for future agents.
Gives any agent (or script) one-command access to the core Protected Desire Equilibrium functions
without touching any existing files in the repo.

Usage example for agents:
    from agent_pde_interface import run_d_floor_test, check_lyapunov_invariance, evaluate_protected_pareto

    result = run_d_floor_test(num_agents=1000000, seed=42)
"""

import numpy as np
from typing import Dict, Any

# These imports assume your existing files are in the same folder or on Python path.
# Adjust the import paths only if your file structure is different.
try:
    from pde_core import (  # ← replace with your actual core file name if different
        compute_p_i, enforce_d_floor, run_full_benchmark
    )
except ImportError:
    # Fallback for when agents run the Colab-style self-contained version
    from PDE_SELF_CONTAINED_COLAB_NOTEBOOK import (
        compute_p_i, enforce_d_floor, run_full_benchmark
    )

def run_d_floor_test(num_agents: int = 1_000_000, seed: int = 42, adversarial_level: float = 0.65) -> Dict[str, Any]:
    """Run a full D ≥ 1.0 floor invariance test at scale.
    Returns clear metrics agents can parse immediately."""
    np.random.seed(seed)
    result = run_full_benchmark(num_agents=num_agents, adversarial_level=adversarial_level)
    return {
        "d_floor_held": result["d_floor_held"],
        "invariance_score": result["invariance_score"],
        "spillover_rate": result.get("spillover_rate", 0.0),
        "protected_pareto_stable": result["protected_pareto_stable"],
        "status": "PASS" if result["d_floor_held"] else "FAIL"
    }

def check_lyapunov_invariance(num_agents: int = 100_000, seed: int = 42) -> Dict[str, Any]:
    """Quick Lyapunov stability check for self-mod invariance."""
    np.random.seed(seed)
    # Calls your existing Lyapunov code (adjust import if needed)
    stability = run_full_benchmark(num_agents=num_agents, check_lyapunov_only=True)
    return {
        "lyapunov_stable": stability["lyapunov_stable"],
        "max_eigenvalue": stability.get("max_eigenvalue", 0.0),
        "status": "STABLE" if stability["lyapunov_stable"] else "UNSTABLE"
    }

def evaluate_protected_pareto(num_agents: int = 500_000, seed: int = 42) -> Dict[str, Any]:
    """Evaluate the protected Pareto frontier under heterogeneous protocols."""
    np.random.seed(seed)
    result = run_full_benchmark(num_agents=num_agents, evaluate_pareto=True)
    return {
        "pareto_stable": result["protected_pareto_stable"],
        "adoption_rate": result.get("adoption_rate", 0.0),
        "spillover": result.get("spillover_rate", 0.0),
        "status": "PROTECTED" if result["protected_pareto_stable"] else "VULNERABLE"
    }

# Simple one-line test for agents that just want to ping the interface
def quick_health_check() -> str:
    return "PDE/USO agent interface ready - D-floor protected and testable"

if __name__ == "__main__":
    print(quick_health_check())
    print(run_d_floor_test(num_agents=100_000))
