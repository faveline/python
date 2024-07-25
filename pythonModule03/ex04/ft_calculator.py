class calculator:
    def __init__(self, tab):
        self.tab = tab

    def __add__(self, object) -> None:
        print([value + object for value in self.tab])

    def __mul__(self, object) -> None:
        print([value * object for value in self.tab])

    def __sub__(self, object) -> None:
        print([value - object for value in self.tab])

    def __truediv__(self, object) -> None:
        if (object == 0):
            print("0 not an acceptable div")
            return
        print([value / object for value in self.tab])

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        sum = 0
        for i in range(min(len(V1), len(V2))):
            sum = sum + V1[i] * V2[i]
        print("Dot product is:", sum)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        sum = V1.copy()
        for i in range(min(len(V1), len(V2))):
            sum[i] = V1[i] + V2[i]
        print("Add Vector is:", [float(a) for a in sum])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous = V1.copy()
        for i in range(min(len(V1), len(V2))):
            sous[i] = V1[i] - V2[i]
        print("Sous Vector is:", [float(a) for a in sous])
