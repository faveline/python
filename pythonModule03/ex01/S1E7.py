from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, "Baratheon", "brown", "dark", is_alive)

    def __str__(self):
        return f'The {self.family_name} have \
{self.eye_color} eyes and {self.hair_color} hair'

    def __repr__(self):
        return f'Vector: (\'{self.family_name}\', \
\'{self.eye_color}\', \'{self.hair_color}\')'


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, "Lannister", "blue", "light", is_alive)

    def __str__(self):
        return f'The {self.family_name} have \
{self.eye_color} eyes and {self.hair_color} hair'

    @classmethod
    def create_lannister(self, first_name: str, is_alive=True):
        """Function to create a Lannister"""
        return (Lannister(first_name, is_alive))
