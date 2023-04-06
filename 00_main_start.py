import random
import numpy as np
import logging

logger = logging.getLogger("cool_project")
logger.setLevel(logging.INFO)
logging.basicConfig()

def single_run(config):
    # Your crazy RL experiment here
    for i in range(config['num_steps']):
        # Craete a dummy learning curve
        # Dummy exponential decay
        loss = config['optimizer']['lr']*np.exp(-i / config['decay_rate'])+random.random()
        # Log the loss
        logger.info("loss: %f", loss)

        

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
    