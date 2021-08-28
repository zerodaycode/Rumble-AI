class NoObjectIdentifierFound(Exception):
    """Raised when tries to retrieve an object identifier
     that is not registered on the instances dict"""

    def __init__(self, obj_identifier):
        self.obj_indentifier = obj_identifier
        super().__init__(f'No key: {self.obj_indentifier} found on instance')
