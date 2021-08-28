from .object_factory import ObjectFactory


class SkillFactory(ObjectFactory):
    """
     Provides an interface that is concrete to the application context.
     Inherits ObjectFactory, and specializes it in this class as a SkillFactory
    """

    def get_instance(self, skill, **kwargs):
        """
        This method invokes the generic .create(key, **kwargs) method from ObjectFactory
        :param skill:
        :param kwargs:
        :return:
        """
        return self.create_instance(skill, **kwargs)

