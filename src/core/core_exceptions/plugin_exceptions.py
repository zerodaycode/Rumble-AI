class NotValidPluginFound(Exception):
    """Raised when tries to retrieve an object identifier
     that is not registered on the instances dict"""

    def __init__(self, obj_identifier):
        super().__init__( f'Founded a NOT valid plugin -> { obj_identifier } <- on the plugins folder' )


class NoInheritsFromSkill(Exception):
    """Raised when tries to retrieve an object identifier
     that is not registered on the instances dict"""

    def __init__(self, obj_identifier):
        super().__init__( f'{ obj_identifier } does not inherits from the ABC Skill' )
