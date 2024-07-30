class calculator:
    def __init__(self, tab):
        """Class constructor"""
        self.tab = tab

    def __add__(self, object) -> None:
        """add object to all value of a list"""
        print([value + object for value in self.tab])

    def __mul__(self, object) -> None:
        """multiply object to all value of a list"""
        print([value * object for value in self.tab])

    def __sub__(self, object) -> None:
        """substracte object to all value of a list"""
        print([value - object for value in self.tab])

    def __truediv__(self, object) -> None:
        """divide object to all value of a list"""
        if (object == 0):
            print("0 not an acceptable div")
            return
        print([value / object for value in self.tab])

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product of 2 lists"""
        sum = 0
        for i in range(min(len(V1), len(V2))):
            sum = sum + V1[i] * V2[i]
        print("Dot product is:", sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """addition of 2 lists"""
        sum = V1.copy()
        for i in range(min(len(V1), len(V2))):
            sum[i] = V1[i] + V2[i]
        print("Add Vector is:", [float(a) for a in sum])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substraction of 2 lists"""
        sous = V1.copy()
        for i in range(min(len(V1), len(V2))):
            sous[i] = V1[i] - V2[i]
        print("Sous Vector is:", [float(a) for a in sous])
