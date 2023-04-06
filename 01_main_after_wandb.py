import random
import numpy as np
import logging
import wandb

logger = logging.getLogger("cool_project")
logger.setLevel(logging.INFO)
logging.basicConfig()

def single_run(config):
    random.seed(config['seed'])
    # CHANGE 1
    wandb.init(project='sample_project',config=config)
    # Your crazy RL experiment here
    # Your crazy RL experiment here
    for i in range(config['num_steps']):
        # Craete a dummy learning curve
        # Dummy exponential decay
        loss = config['optimizer']['lr']*np.exp(-i / config['decay_rate'])+random.random()
        # Log the loss
        logging.info("loss: %f", loss)
        # CHANGE 2
        wandb.log({"loss": loss})

        

if __name__ == "__main__":
    config = {
        'seed': 42,
        'num_steps': 100,
        'decay_rate': 10,
        'optimizer':{
            'type': 'adam',
            'lr': 0.001
        }
    }
    logger.info("config: %s", config)
    single_run(config)
    