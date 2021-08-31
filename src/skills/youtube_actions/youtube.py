import datetime

import pywhatkit

from ...core.skill import Skill


class YouTube(Skill):
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
        return self._play_on_youtube( rumble )

    def _play_on_youtube(self, rumble):
        """Play the first match encoountered on YouTube based on the input query"""
        rumble.talk( "Qué te apetece escuchar en Youtube?" )

        # This should potencially be upgradeable to more custom actions
        # than just play a video
        pywhatkit.playonyt( rumble.listen() )
