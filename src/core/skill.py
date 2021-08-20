class Skill:
    """
    Base model class for the RumbleAI Skills
    """

    def __init__(self, name, description, tags):
        self.name: str = name
        self.description: str = description
        self.tags: dict = tags
