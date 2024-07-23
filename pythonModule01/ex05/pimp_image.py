import numpy as np


def ft_invert(image: np.array) -> np.array:
    """Inverts the color of the image received."""
    invert = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            invert[i][j] = 255 - image[i][j]
    return invert


def ft_red(image: np.array) -> np.array:
    """Suppress all green and blue from the image received."""
    invert = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            invert[i][j][1] = 0
            invert[i][j][2] = 0
    return invert


def ft_green(image: np.array) -> np.array:
    """Suppress all red and blue from the image received."""
    invert = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            invert[i][j][0] = 0
            invert[i][j][2] = 0
    return invert


def ft_blue(image: np.array) -> np.array:
    """Suppress all red and green from the image received."""
    invert = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            invert[i][j][0] = 0
            invert[i][j][1] = 0
    return invert


def ft_grey(image: np.array) -> np.array:
    """Change the image received to grey."""
    grey = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            grey[i][j][0] = sum(image[i][j]) / 3
    grey[:, :, 1:2] = grey[:, :, :1]
    grey[:, :, 2:3] = grey[:, :, :1]
    return grey
