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

    def play(self) -> str:
        return self._greet()

    def _greet(self):

        hour = datetime.datetime.now().hour

        if (hour >= 6) and (hour <= 13):
            return f"Buenos días, {self.username}, cómo puedo ayudarte?"
        elif (hour >= 14) and (hour < 21):
            return f'Buenas tardes, {self.username}, cómo puedo ayudarte?'
        elif (hour >= 21) and (hour <= 5):
            return f'Buenas moches, {self.username}, cómo puedo ayudarte?'
        else:
            return f'Buenas moches, {self.username}, cómo puedo ayudarte?'
