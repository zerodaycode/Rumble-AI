'''
    The entry point of 'Rumble-AI'
'''

from src.core.rumble_ai import RumbleAI
from src.core.rumble_config import RumbleConfiguration
from src.persistence.data import RUMBLE_INITIAL_CONFIG

if __name__ == '__main__':
    # TODO There's still the spanish language used as a default for some parts of
    # the codebase. This should be changed to English ASAP

    # TODO Create a initial configuration module that, if there's no user configuration
    # (assumed the first) time, then makes a kind of interview to set up rumble for the customer
    # Since it's handled from within the RumbleAI type, pass it via constructor (or empty if is the first one)
    rumble_configuration = RumbleConfiguration(
        **RUMBLE_INITIAL_CONFIG
    )

    # Developer mode. Asks for another input device that is not the default one
    rumble_configuration.mic_setup()

    # The Rumble entry point
    rumble = RumbleAI(rumble_configuration)
    rumble.run()
