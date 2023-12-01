from .plugins_registry import PluginsRegistry
from .skill import Skill
from .skill_factory import SkillFactory
from .plugin_factory import PluginFactory

# Rumble skills modules
from ..skills.basic.greet import Greet
from ..skills.basic.open_program import OpenProgram
from ..skills.basic.close_program import CloseProgram
from ..skills.basic.shutdown import RumbleShutdown
from ..skills.info.date import Date
from ..skills.info.time import Time
from ..skills.youtube_actions.youtube import YouTube
from ..utils.rumble_logger import Logger


class SkillsRegistry:
    """
        Takes care about handle a way to store and retrieve all the Rumble's availiable skills
    """

    def __init__(self, id_language: int):
        # id_language it's used to slice through the list of a skill names property
        self.id_language = id_language

        # The query that it's being processed
        self.current_query = None

        # Here we starts our skill and plugin factory
        self.skill_factory = SkillFactory()
        self.plugin_factory = PluginFactory()

        # Add the plugins already "installed"
        self.plugin_registry = PluginsRegistry()

        # Loading external plugins on the registry
        for plugin in self.plugin_registry.get_plugins:
            for skill, kwargs in plugin.items():
                rumble_skills_registry.update(
                    { skill: kwargs }
                )

        # Automatize the process of register every skill on the skill's dict
        for skill, kwargs in rumble_skills_registry.items():
            self.skill_factory.register_object_identifier(
                kwargs[ 'name' ][ self.id_language - 1 ], skill
            )

        Logger.info('Instances identifiers availiables on the program:')
        for key, instance in self.skill_factory.instances.items():
            print(f'\t{ key.title() } -> { instance }')

    def match_skill(self, keywords: list[str]) -> Skill:
        """
            Tries to find an skill based on a list of words created by parsing
            what the user had requested through the audio input
        """
        for skill_instance, skill_args in rumble_skills_registry.items():
            identifiers = list(
                skill_args['tags']
                .values( )
            )[ self.id_language - 1 ]

            for tag in identifiers:
                if tag in keywords:
                    skill_args.update( {
                        'id_language': self.id_language,
                    } )

                    return self.skill_factory.get_instance(
                        skill_args[ 'name' ][ self.id_language - 1 ], **skill_args
                    )


# A list with all the Rumble's availiable skills.
rumble_skills_registry: dict = {
    # TODO when the skills are loaded, just redo this dic to hold only
    # the necessary data for the skill to work in that language
    RumbleShutdown: {
        'name': ['shutdown', 'apagar'],
        'description': 'Shutdowns Rumble',
        'tags': {
            'english': ['shutdown'],
            'spanish': ['apágate']
        }
    },
    Time: {
        'name': ['hour', 'hora'],
        'description': 'Retrieves info about current time',
        'tags': {
            'english': ['time', 'hour'],
            'spanish': ['hora'],
        },
    },
    Date: {
        'name': ['date', 'fecha'],
        'description': 'Retrieves info about current date',
        'tags': {
            'english': ['date'],
            'spanish': ['fecha'],
        },
    },
    Greet: {
        'name': ['greet', 'saludar'],
        'description': 'Greets the user (or any one) when requested',
        'tags': {
            'english': ['greet'],
            'spanish': ['saluda', 'saludar'],
        },
    },
    OpenProgram: {
        'name': ['open', 'abrir'],
        'description': 'Opens an installed program on the local machine',
        'tags': {
            'english': ['open'],
            'spanish': ['abre', 'ábreme']
        },
    },
    CloseProgram: {
        'name': ['close', 'cerrar'],
        'description': 'Closes a current running program',
        'tags': {
            'english': ['close'],
            'spanish': ['cierra', 'ciérrame']
        },
    },
    YouTube: {
        'name': ['youtube', 'youtube'],
        'description': 'Makes a search, or plays a video '
                       'on YouTube based on an user audio input',
        'tags': {
            'english': ['youtube'],
            'spanish': ['youtube']
        }
    },
}
