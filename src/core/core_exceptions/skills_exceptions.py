class NoSkillFound(Exception):
    """ Raised when the user query can't be matched against a Rumble skill """

    def __init__(self, user_query):
        super().__init__( f'No skill availiable found with the given query: { user_query }' )


class SkillNotContainsNameParameter(Exception):
    """ Raised when the user query can't be matched against a Rumble skill """

    def __init__(self):
        super().__init__( 'Skill not contains mandatory -> name <- class member' )


class SkillNamesListWrongLength(Exception):
    """ Raised when the user query can't be matched against a Rumble skill """

    def __init__(self, len):
        super().__init__( f'Skill names list not matches the availiable languages on Rumble '
                          f'nowadays { len }' )
