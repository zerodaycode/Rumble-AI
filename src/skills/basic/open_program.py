from ...core.skill import Skill
import subprocess

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

        if "lol" in query or "league of legends" in query:
            rumble.talk('Ea, vamos a fedear un poco!')
            subprocess.call('C:\\Riot Games\\League of Legends\\LeagueClient.exe')

    def _close_programs(self, rumble, **kwargs) -> None:
        """Close a program"""
        # Parses the query again, trying to look for what program wants the user open
        query = kwargs["query"]

        # console = subprocess.Popen(['ps','-A'])
        # output, error = console.communicate()
        # print(f'programs:{output}')
        program_name = "LeagueClient.exe"
        #
        # for program_line in output.splitlines():
        #     if program in program_line:
        #         pid = int(program_line.split(None,1)[0])
        #         os.kill(pid)

        import psutil

        for proc in psutil.process_iter():

            print(f'Programa: {proc.name}')
            if proc.name().lower() == program_name.lower():
                proc.kill()

