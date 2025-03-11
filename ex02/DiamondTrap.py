from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the King family."""
        return Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the eyes color of the King family."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hairs color of the King family."""
        self.hairs = hairs

    def get_eyes(self):
        """Get the eyes color of the King family."""
        return self.eyes

    def get_hairs(self):
        """Get the hairs color of the King family."""
        return self.hairs
