from abc import ABC, abstractmethod


class Character(ABC):
    """Create a Character"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def __repr__(self):
        """Return a string representation of the Baratheon family."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Kill the character"""
        self.is_alive = False
