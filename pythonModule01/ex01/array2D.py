import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert family, "list must not be None"
        assert len(family) > 0, "list must contain at list 1 element"
        assert len(family[0]) > 0, "lists must contain at list 1 element"
        assert all(len(leng) == len(family[0]) for leng in family), \
            "all lists should be the same size"
        assert start >= 0 and start < len(family), \
            "start should be in family lenght range"
    except AssertionError as msg:
        print("AssertionError:", msg)
        return
    sliced = np.array(family)[start:end]
    print("My shape is:", len(family), len(family[0]))
    print("My new shape is:", len(sliced), len(sliced[0]))
    return sliced.tolist()
