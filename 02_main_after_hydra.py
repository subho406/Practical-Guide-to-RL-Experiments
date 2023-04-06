import random
import numpy as np
import logging
import wandb
import hydra
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger("cool_project")
logger.setLevel(logging.INFO)
logging.basicConfig()


@hydra.main(version_base=None, config_path="config", config_name="01_config")
def main(config: DictConfig):
    logger.info("Starting Job for Config:\n"+str(OmegaConf.to_yaml(config)))
    random.seed(config['seed'])
    wandb.init(project='sample_project',config=OmegaConf.to_container(config),tags=config.get('tags',None))
    # Your crazy RL experiment here
    # Your crazy RL experiment here
    for i in range(config['num_steps']):
        # Craete a dummy learning curve
        # Dummy exponential decay
        loss = config['optimizer']['lr']*np.exp(-i / config['decay_rate'])+random.random()
        # Log the loss
        logging.info("loss: %f", loss)
        wandb.log({"loss": loss})

        

if __name__ == "__main__":
    main()
    