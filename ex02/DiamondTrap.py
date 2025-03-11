from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Representing the King family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the King family."""
        super().__init__(first_name, is_alive)
        self.family_name = "King"
        self.eyes = "green"
        self.hairs = "black"

    def __str__(self):
        """Return a string representation of the King family."""
        return super().__str__()

    @classmethod
    def create_king(cls, first_name, is_alive=True):
        """Create a King family."""
        return King(first_name, is_alive)
