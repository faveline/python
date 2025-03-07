import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
  -> list[int | float]:
    """return a list of bmi"""
    try:
        assert height and weight, "lists must not be None"
        assert len(height) == len(weight), "lists must be the same size"
        assert len(height) > 0, "lists must contain at list 1 element"
        assert all(isinstance(h, (int, float)) for h in height), \
            "height must only be composed of int and float"
        assert all(isinstance(w, (int, float)) for w in weight), \
            "weight must only be composed of int and float"
    except AssertionError as msg:
        print("AssertionError:", msg)
        return
    return (list(np.divide(weight, np.multiply(height, height))))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """check whether bmi is under a certain value or not"""
    try:
        assert bmi, "list must not be None"
        assert len(bmi) > 0, "list must contain at list 1 element"
        assert all(isinstance(h, (int, float)) for h in bmi), \
            "bmi must only be composed of int and float"
        assert isinstance(limit, (int, float)), \
            "limit must be an integer or a float"
    except AssertionError as msg:
        print("AssertionError:", msg)
        return
    return list(np.array(bmi) > limit)
