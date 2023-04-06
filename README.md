# Practical Guide to running RL Experiments

**Presentation**: [LINK]([https://www.google.com](https://github.com/subho406/Practical-Guide-to-RL-Experiments/raw/main/Presentation.pdf))

## Requirements

```
wandb
hydra-core
omegaconf
```
## Experiments

### Experiment without Weights and Biases
```
python 00_main_start.py
```
### Experiment with Weights and Biases
```
python 01_main_after_wandb.py
```

### Experiment after Hydra
```
python 02_main_after_hydra.py
```

### Experiment with Hydra Group Config
```
python 02_main_after_hydra.py --config-name=02_group_config
```

### Experiment with Hydra Sweep (Basic Launcher)
```
python 02_main_after_hydra.py --config-name=03_config_sweeps
```

### Experiment with Hydra Sweeps in SLURM (Submitit Launcher)
1. Add account name in `config/04_config_sweeps_cc.yaml`
2. Run the following in SLURM based system (such as Compute Canada): 
```
python 02_main_after_hydra.py --config-name=04_config_sweeps_cc 
```
