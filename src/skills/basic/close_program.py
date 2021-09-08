from src.utils.rumble_logger import Logger
from ...core.skill import Skill
import subprocess
import psutil


class NoProgramToClose(Exception):
    """Raised when no program name found on the query"""
    def __init__(self, logs):
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

    @staticmethod
    def _close_programs(rumble, **kwargs) -> None:
        """Closes a program"""
        # Parses the query again, trying to look for what program wants the user to close
        query = kwargs["query"]

        # TODO retrieve program name from the query
        program_name = ''

        try:
            if program_name != '':

                # Powershell command to retrieve processes with an open window. Each process will have
                # PID, executable name and window title.
                powershell_command = "Get-Process | Where-Object {$_.mainWindowTitle} | Select-Object -Property " \
                         "Id, Name, mainWindowtitle | ConvertTo-Csv -NoTypeInformation | Select-Object -skip 1"

                # Execute the powershell command, get the output and split each process on a line. (return as bytes)
                processes_raw_table = subprocess.run(["powershell", "-Command", powershell_command],
                                                     capture_output=True).stdout.splitlines()

                my_processes = []

                for output_line in processes_raw_table:

                    # Data are store as bytes, we need to convert to str, and remove whitespaces.
                    # TODO - Need more testing, encoding may be dynamic
                    output_line = output_line.decode('cp437', 'ignore').strip()

                    # if the output is not an empty line, we should have something like-
                    # ["PID", "Executable name", "Window Title"]
                    if output_line:
                        process_data = output_line.split(",")
                        pid = int(process_data[0].strip('"'))
                        name = process_data[1].strip('"')
                        window_title = process_data[2].strip('"')

                        my_processes.append([pid, name, window_title])

                for process in my_processes:

                    # Process data structure [pid, Executable Name, Window Title]
                    # Check if the "Executable Name" or the "Window Title" is equal to the requested program
                    if process[1].lower() == program_name.lower() or process[2].lower() == program_name.lower():

                        # psutil will manage the process using the PID
                        target_process = psutil.Process(process[0])

                        # Checking if the process is a child process (but not from explorer.exe)
                        if target_process.parent() and target_process.parent().name() != "explorer.exe":
                            target_process = target_process.parent()

                        # Killing the process (either the original or the parent)
                        target_process.terminate()

                        rumble.talk(
                            f'{program_name.strip(".exe")} ha sido cerrado con éxito'
                        )
            else:
                raise NoProgramToClose
        except NoProgramToClose as error:
            Logger.error(error)
            rumble.talk(
                f'No se ha encontrado el programa {program_name}'
            )
