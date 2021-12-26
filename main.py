from src.core.rumble_ai import RumbleAI
from src.core.rumble_config import RumbleConfiguration
# from src.persistence.database import RumblePersistence
from src.persistence.data import *

import time

'''
    Development note at 25/12/2021.
    We are wondering to mark the MongoDB as deprecated. We should
    probabilly change the persistence API of RUmble to something like
    a REST API cloud based solution.

    This decision it's taken in consideration because the installation and usage of 
    this APP should be really stright-foward to the end user, end 
    at the day of today, we are considering that a MongoDB self-contained
    installation along with this AI should be too much complicated,
    and too much expensive, polutting the host with a larger and
    undesired amount of MB of dependencies.

    We are still looking for a solution that takes the best of both ideas,
    but for this development stage, we let the already functional code
    commented in order to not depend on the persistence mechanism to 
    start and test the program.
'''

if __name__ == '__main__':
    # Loads the database an the collections
    # rumble_persistence = RumblePersistence()
    # config_data = rumble_persistence.configuration.find_one()

    # if config_data:
    #     print('Retrieved config from pymongo')
    #     print(f'CONFIG DATA: {config_data}')

    #     rumble_configuration = RumbleConfiguration(
    #         **config_data
    #     )
    # else:
    #     print('Loading the default initial configuration')

    rumble_configuration = RumbleConfiguration(
        **rumble_initial_config
    )

    # Developer mode. Asks for another input device that is not the default one
    mic_device = rumble_configuration.mic_setup()
    rumble_configuration.mic_input_device = mic_device
        # # Stores the initial values (a default ones) on MongoDB
        # rumble_persistence.configuration.insert_one(
        #     rumble_initial_config
        # )

    # The Rumble entry point
    rumble = RumbleAI( rumble_configuration )
    rumble.run()
