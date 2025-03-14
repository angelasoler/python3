from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the Baratheon family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon family."""
        return super().__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Constructor for the Lannister family."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string representation of the Lannister family."""
        return super().__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister family."""
        return Lannister(first_name, is_alive)
