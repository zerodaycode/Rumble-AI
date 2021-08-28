import datetime

from ...core.skill import Skill


class Date(Skill):
    """
    Retrieves the today's date
    """

    def __init__(self, name, description, tags, id_language):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

    def __str__(self):
        return self.name[ self.id_language - 1 ]

    def play(self, rumble, **kwargs) -> str:
        return rumble.talk(
            f'''
                Hoy es el, { str( datetime.datetime.now().day ) },
                del, { str( datetime.datetime.now().month ) },
                del, { str( datetime.datetime.now().year ) }
            '''
        )
