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
