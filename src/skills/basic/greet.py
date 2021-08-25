import datetime

from ...core.skill import Skill


class Greet(Skill):
    """
        Greets the user when requested
    """

    def __init__(self, name, description, tags, id_language, **kwargs):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language
        self.username = kwargs['user'].get('username', '')

    def __str__(self):
        return self.name[self.id_language]

    def play(self, rumble) -> str:
        return self._greet( rumble )

    def _greet(self, rumble):

        hour = datetime.datetime.now().hour

        if (hour >= 6) and (hour <= 13):
            return rumble.talk(
                 f"Buenos días, {self.username}, cómo puedo ayudarte?"
            )
        elif (hour >= 14) and (hour < 21):
            return rumble.talk(
                f"Buenas tardes, {self.username}, cómo puedo ayudarte?"
            )
        elif (hour >= 21) and (hour <= 5):
            return rumble.talk(
                f"Buenas noches, {self.username}, cómo puedo ayudarte?"
            )
        else:
            return rumble.talk(
                f'Hola, {self.username}, cómo puedo ayudarte?'
            )
