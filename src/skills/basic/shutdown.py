import datetime

from ...core.skill import Skill


class RumbleShutdown(Skill):
    """
        Greets the user when requested
    """

    def __init__(self, name, description, tags, id_language):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

    def __str__(self):
        return self.name[ self.id_language - 1 ]

    def play(self, rumble, **kwargs) -> None:
        rumble.talk(f'Me desconecto por un rato. Gracias, {kwargs[ "username" ]}')
        quit( 0 )
