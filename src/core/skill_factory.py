'''
    The module that holds the factory of skills
'''

from .object_factory import ObjectFactory


class SkillFactory(ObjectFactory):
    '''
     Provides an interface that is concrete to the application context.
     Inherits ObjectFactory, and specializes it in this class as a SkillFactory
    '''
