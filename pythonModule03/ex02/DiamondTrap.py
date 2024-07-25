from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """I AM THE KING !"""
    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        self.eye_color = color

    def set_hairs(self, color: str):
        self.hair_color = color

    def get_eyes(self):
        return (self.eye_color)

    def get_hairs(self):
        return (self.hair_color)
