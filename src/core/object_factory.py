from src.core.core_exceptions.factory_exceptions import NoObjectIdentifierFound


class ObjectFactory:
    """
    This interface supports the creation of any type of object.

    Provides a method to register a Builder based on a key-value pair architechture
    and a method to create the concrete object instances based on the key.

    Also provide a way to create more concrete implementations of diverse factory that creates
    concrete instances of more concrete objects
    """

    def __init__(self):
        self._instances = { }

    @property
    def instances(self):
        return self._instances

    def register_object_identifier(self, key, instance):
        """
        :param key: str
        :param instance:
            The instance parameter can be any object that implements the callable interface.
            This means an Instance can be a function, a class, or an object that implements .__call__().
        """
        self._instances[ key ] = instance

    def create_instance(self, key, **kwargs):
        """
        Creates a new object if the provided key matches any of the self._instances keys
        :param key: str
        :param kwargs: dict. The (if present) args of the callbacks
        :return: Object
        """

        instance = self._instances.get( key )

        if instance:
            # If an object identifier is founded, creates a new instance (notate the parenthesis)
            # and pass the extra arguments to the constructor
            return instance( **kwargs )
        else:
            raise NoObjectIdentifierFound


