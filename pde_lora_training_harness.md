# pde_lora_training_harness.ipynb
**LoRA Training Harness for PDE Integration**

```python
# Simple LoRA training harness (run in Colab)
from pde_lora_adapter import PDE_LoRA

model = PDE_LoRA(grok_base_model)
trainer = PDE_LoRA_Trainer(model, pde_guided_dataset)
trainer.train(epochs=1)

print("LoRA adapter training complete — PDE guidance now native.")
