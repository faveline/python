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
