from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Abstract Class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
        return

    def __repr__(self):
        return f'Vector: (\'{self.name}\', \
\'{self.eye_color}\', \'{self.hair_color}\')'


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
