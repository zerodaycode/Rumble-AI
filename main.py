from src.core.rumble_ai import RumbleAI
from src.core.rumble_config import RumbleConfiguration
from src.persistence.database import RumblePersistence
from src.persistence.data import *

import time

if __name__ == '__main__':
    # Loads the database an the collections
    rumble_persistence = RumblePersistence()
    config_data = rumble_persistence.configuration.find_one()

    if config_data:
        print('Retrieved config from pymongo')
        print(f'CONFIG DATA: {config_data}')

        rumble_configuration = RumbleConfiguration(
            **config_data
        )
    else:
        print('Not data on config collection yet')
        print('Loading the default initial configuration')

        rumble_configuration = RumbleConfiguration(
            **rumble_initial_config
        )
        # Stores the initial values (a default ones) on MongoDB
        rumble_persistence.configuration.insert_one(
            rumble_initial_config
        )

    # The Rumble entry point
    rumble = RumbleAI( rumble_configuration )
    rumble.run()
