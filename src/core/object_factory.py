class ObjectFactory:
    """
    This interface supports the creation of any type of object.

    Provides a method to register a Builder based on a key-value pair architechture
    and a method to create the concrete object instances based on the key.

    Also provide a way to create more concrete implementations of diverse factory that creates
    concrete instances of more concrete objects
    """

    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        """
        :param key: str
        :param builder:
            The builder parameter can be any object that implements the callable interface.
            This means a Builder can be a function, a class, or an object that implements .__call__().
        """
        self._builders[key] = builder
        # print('BUILDERS:')
        # print(self._builders.items())

    def create(self, key, **kwargs):
        """
        :param key: str
        :param kwargs: dict. The (if present) args of the callbacks
        :return: Object
        """

        print('Imprimiendo los builders a modo de info cuando se llama a create:')
        print(self._builders)

        builder = self._builders.get(key)

        if builder:
            return builder(**kwargs)
        else:
            # raise ValueError(key)
            print(f'No key: {key} found on builders')


