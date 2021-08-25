import logging

# from .rumble_ai import RumbleAI
from .skill import Skill
from .skill_factory import SkillFactory

# Rumble skills modules
from ..skills.basic.greet import Greet
from ..skills.info.date import Date
from ..skills.info.time import Time
from ..skills.youtube_actions.youtube import YouTube


class SkillsRegistry:
    word_filter = [
        'rumble',  # ... TODO --- Complete it
        'a', 'para', 'cabe',
    ]

    def __init__(self, id_language: int):
        # self._rumble_skills = rumble_skills_registry
        self.id_language = id_language - 1

        # Here we starts our skill factory
        self.skill_factory = SkillFactory( )

        # Automatize the process of register every skill on the skill's dict
        for skill, kwargs in rumble_skills_registry.items():
            print(f'Skill: {skill}, kwargs: {kwargs}')
            self.skill_factory.register_builder(
                kwargs[ 'name' ][ self.id_language ], skill
            )

    def match_skill(self, user_query: str) -> Skill:

        # Filter no interesting words to match
        keywords = list(
            filter(
                lambda word: word not in SkillsRegistry.word_filter,
                user_query.split( )
            )
        )

        for skill_instance, skill_attrs in rumble_skills_registry.items():
            identifiers = list(
                skill_attrs[ "tags" ].values( )
            )[ self.id_language ]
            print(identifiers)
            for tag in identifiers:
                if tag in keywords:

                    skill_attrs.update( { 'id_language': self.id_language } )

                    return self.skill_factory.get_instance(
                        tag, **skill_attrs
                    )


# A list with all the Rumble's availiable skills.
rumble_skills_registry: dict = {

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
            'spanish': ['saluda, saludar, saludo'],
        },
        'user': {
            'username': 'Alex'
        }
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
