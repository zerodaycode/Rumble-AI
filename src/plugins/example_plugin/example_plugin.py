from src.core.skill import Skill

name: list[str] = ['Example Plugin', 'ejemplo']
description: str = 'An example of how to desing a basic working plugin for Rumble'
tags: dict = {
    'tags': {
        'english': [ 'example plugin', 'multiexample', 'parse_this' ],
        'spanish': [ 'ejemplo', 'plugin de ejemplo', 'flípalo', 'gózalo' ]
    }
}


class ExamplePlugin(Skill):
    """
        Just exemplifies how to make a plugin for Rumble
    """
    def __init__(self, name: str, description: str, tags: dict, id_language: int):
        self.name: list[str] = name
        self.description: str = description
        self.tags: list[str] = tags
        self.id_language: int = id_language

    def __str__(self) -> str:
        return self.name[ self.id_language - 1 ]

    def play(self, rumble, **kwargs) -> None:
        return rumble.talk(
            self.text_to_voice()
        )

    def text_to_voice(self) -> str:
        """
            Helper that can encaplusale the availiable responses of Rumble
            for a concrete skill depending on the language
        """
        return [
            'Hi there, I am a plugin test working as intended!',
            'Hola, soy un plugin de prueba funcionando cómo se esperaba!'
        ][ self.id_language - 1 ]
