import datetime

from ...core.skill import Skill


class Greet(Skill):
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
        return self._greet( rumble, **kwargs )

    def _greet(self, rumble, **kwargs):
        hour = datetime.datetime.now().hour

        if (hour >= 6) and (hour <= 13):
            return rumble.talk(
                 f"Buenos días, {kwargs[ 'username' ]}, cómo puedo ayudarte?"
            )
        elif (hour >= 14) and (hour < 21):
            return rumble.talk(
                f"Buenas tardes, {kwargs[ 'username' ]}, cómo puedo ayudarte?"
            )
        elif (hour >= 21) and (hour <= 5):
            return rumble.talk(
                f"Buenas noches, {kwargs[ 'username' ]}, cómo puedo ayudarte?"
            )
        else:
            return rumble.talk(
                f"Hola, {kwargs[ 'username' ]}, cómo puedo ayudarte?"
            )
