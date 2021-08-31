from abc import ABCMeta, abstractmethod
from typing import Any


class Skill(metaclass = ABCMeta):
    """
    Base model class for any of the RumbleAI Skills
    """

    @abstractmethod
    def play(self, rumble, **kwargs) -> Any:
        """
        Performs the designed action, based on the logic implemented for this method
        by all the classes that subclass this one, and overrides this method
        :param rumble: Play method should receive the currently working Rumble instance, in order
        to be able to access the skill 'talk', which it's directly implemented of the Rumble's
        main class
        :return: Any


        """
        pass  # abstract methods does not provides an implementation in Python
