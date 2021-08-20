import logging

from .skill import Skill
from .skill_factory import SkillFactory

# Rumble skills modules
from ..skills.info.date_time import DateTime


class SkillsRegistry:

    word_filter = [
        'a', 'para', 'cabe'
    ]

    def __init__(self):
        self._rumble_skills = rumble_skills_registry

        # Here we starts our skill factory
        skills = SkillFactory()

        # All the availiable Rumble skills
        skills.register_builder(
            self._rumble_skills.get('hour'), DateTime().get_current_time())

    @staticmethod
    def match_skill(user_query: str, id_language: int):

        keywords = [
            word for word in user_query.split()
                if word not in SkillsRegistry.word_filter
        ]

        for word in keywords:
            # logging.Logger.info('Word: ' + word)
            rumble_skills_registry.get( word )


# A list with all the Rumble's availiable skills.

rumble_skills_registry: dict = {
    'hour': Skill(
        'time',
        'Retrieves info about date and/or time',
        {
            'english': ['time'],
            'spanish': ['hora'],
        }
    ),

}