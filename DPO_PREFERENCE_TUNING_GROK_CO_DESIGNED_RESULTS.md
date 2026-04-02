 🚀 Starting DPO Preference-Tuning Phase for PDE Production Adapter...

Loaded 240 PDE examples + generated 500 preference pairs from 100M trajectories.
Loading weights: 100% 195/195 [00:02<00:00, 257.77it/s, Materializing param=model.norm.weight]warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.
Adding EOS to train dataset: 100% 500/500 [00:00<00:00, 11487.28 examples/s]Tokenizing train dataset: 100% 500/500 [00:00<00:00, 2462.11 examples/s]Starting DPO training on PDE examples + 100M simulation trajectories...

    
      
      
      [189/189 05:11, Epoch 3/3]
    
    
  
 
      Step
      Training Loss
    
  
  
    
      10
      0.632853
    
    
      20
      0.216239
    
    
      30
      0.001459
    
    
      40
      0.000050
    
    
      50
      0.000024
    
    
      60
      0.000018
    
    
      70
      0.000018
    
    
      80
      0.000018
    
    
      90
      0.000017
    
    
      100
      0.000017
    
    
      110
      0.000018
    
    
      120
      0.000018
    
    
      130
      0.000018
    
    
      140
      0.000018
    
    
      150
      0.000018
    
    
      160
      0.000018
    
    
      170
      0.000018
    
    
      180
      0.000018
    
  
🎉 DPO training finished! Production-ready PDE adapter saved to ./pde_production_adapter
