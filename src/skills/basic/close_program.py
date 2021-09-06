from src.utils.rumble_logger import Logger
from ...core.skill import Skill
import subprocess
import psutil


class NoProgramToClose(Exception):
    """Raised when tries to retrieve an object identifier
     that is not registered on the instances dict"""
    def __init__(self):
        super().__init__( f'No program name was identified in order to complete the request' )


class CloseProgram(Skill):
    """
        Tries to close a program based on his process executable name
    """

    def __init__(self, name, description, tags, id_language):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

    def __str__(self):
        return self.name[ self.id_language - 1 ]

    def play(self, rumble, **kwargs) -> None:
        return self._close_programs( rumble, **kwargs )

    def _close_programs(self, rumble, **kwargs) -> None:
        """Closes a program"""
        # Parses the query again, trying to look for what program wants the user to close
        query = kwargs["query"]
        program_name = ''

        # TODO System of retrieve custom program executables identifiers
        if 'lol' in query or 'league of legends':
            program_name = "LeagueClient.exe"  # TODO Create an alias?

        if program_name != '':
            founded = False
            for proc in psutil.process_iter():
                if proc.name().lower() == program_name.lower():
                    proc.kill()
                    rumble.talk(
                        f'{ program_name.strip( ".exe" ) } ha sido cerrado con éxito'
                    )
                    founded = True
            try:
                if not founded:
                    raise NoProgramToClose
            except NoProgramToClose as error:
                Logger.error( error )
                rumble.talk(
                    f'No se ha encontrado el programa {program_name.strip(".exe")}'
                )

