# pde_lora_training_run.ipynb
**LoRA Training Run for PDE Integration (10k+ trajectories)**

```python
# Simple LoRA training harness (Colab)
from pde_lora_adapter import PDE_LoRA
model = PDE_LoRA(grok_base_model)
trainer = PDE_LoRA_Trainer(model, pde_guided_dataset_10k)
trainer.train(epochs=1)
print("LoRA adapter training complete — D-floor and Φ(σ) metrics recorded.")
