from ...core.skill import Skill
import subprocess
from os import system


class OpenProgram(Skill):
    """
        Tries to open a program on the computer (if installed)
    """

    def __init__(self, name, description, tags, id_language):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

    def __str__(self):
        return self.name[ self.id_language - 1 ]

    def play(self, rumble, **kwargs) -> None:
        return self._open_program( rumble, **kwargs )

    def _open_program(self, rumble, **kwargs) -> None:
        """Opens a program"""
        # Parses the query again, trying to look for what program wants the user open
        query = kwargs[ "query" ]

        if 'navegador' in query or 'firefox' in query:
            system('start firefox')
        elif "lol" in query or "league of legends" in query:
            rumble.talk('Ea, vamos a fedear un poco!')
            subprocess.call('C:\\Riot Games\\League of Legends\\LeagueClient.exe')
