class NoSkillFound(Exception):
    """ Raised when the user query can't be matched against a Rumble skill """

    def __init__(self, user_query):
        super().__init__( f'No skill availiable found with the given query: { user_query }' )
