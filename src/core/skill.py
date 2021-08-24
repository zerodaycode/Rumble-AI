from abc import ABCMeta, abstractmethod


class Skill(metaclass = ABCMeta):
    """
    Base model class for any of the RumbleAI Skills
    """

    @abstractmethod
    def play(self) -> ():
        """
        Performs the designed action, based on the logic implemented for this method
        by all the classes that subclass this one, and overrides this method
        :return: ()
        """
        pass  # abstract methods does not provides an implementation in Python

