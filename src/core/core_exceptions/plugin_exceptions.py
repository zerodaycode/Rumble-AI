class NoInheritsFromSkill(Exception):
    """Raised when tries to retrieve an object identifier
     that is not registered on the instances dict"""

    def __init__(self, obj_identifier):
        super().__init__( f'Plugin class: { self.obj_indentifier } does not inherits from the ABC Skill' )
