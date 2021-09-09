from src.core.rumble_ai import RumbleAI
from src.core.rumble_config import RumbleConfiguration

if __name__ == '__main__':
    # TODO Create the MongoDB database
    # Get config and save config from there
    rumble_configuration = RumbleConfiguration( 'Álex' )
    rumble = RumbleAI( rumble_configuration )
    rumble.run()
