class calculator:
    """Class to perform operations on vectors"""
    def __init__(self, vector) -> None:
        """Constructor"""
        self.value = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Return the dot product of two vectors"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f'Dot product is: {result}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Return the addition of two vectors"""
        result = []
        for i in range(len(V1)):
            result.append(V1[i] + V2[i])
        print(f'Addition of vectors is: {result}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Return the subtraction of two vectors"""
        result = []
        for i in range(len(V1)):
            result.append(V1[i] - V2[i])
        print(f'Subtraction of vectors is: {result}')
