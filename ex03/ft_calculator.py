class calculator:
    """Class to perform operations on vectors"""
    def __init__(self, vector) -> None:
        """Constructor"""
        self.value = vector

    """A simple calculator class"""
    def __add__(self, object) -> None:
        """Add two numbers together"""
        for i in range(len(self.value)):
            self.value[i] += object
        print(self.value)

    def __mul__(self, object) -> None:
        """Multiply two numbers together"""
        for i in range(len(self.value)):
            self.value[i] *= object
        print(self.value)

    def __sub__(self, object) -> None:
        """Subtract two numbers"""
        for i in range(len(self.value)):
            self.value[i] -= object
        print(self.value)

    def __truediv__(self, object) -> None:
        """Divide two numbers"""
        for i in range(len(self.value)):
            try:
                self.value[i] /= object
            except ZeroDivisionError:
                print("Division by zero is not allowed")
        print(self.value)
