from abc import ABC, abstractmethod


class Character(ABC):
    """Create a Character"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass


class Stark(Character):
    """Concrete class for calling Character"""
    def die(self):
        """Turn is_alive to False"""
        self.is_alive = False
