import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """return a random id of 15 characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """dataclass with automatic __init__"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default=generate_id(), init=False)

    def __post_init__(self):
        """post_init required to use self."""
        self.login = self.name[0] + self.surname
