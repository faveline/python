from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.array:
    """load an image as np.array"""
    try:
        assert path, "path can't be null"
        assert os.path.exists(path), "path doesn't exist"
        assert len(path) >= 5, "size error"
        assert path[-4:] == ".jpg" or path[-5:] == ".jpeg", \
            "only .jpg and .jpeg are handled"
    except AssertionError as msg:
        print("AssertionError:", msg)
        raise Exception("")
    image = np.array(Image.open(path))
    print("The shape of image is:", image.shape)
    return image


def ft_zoom(image: np.array, zx: int, zy: int, nbrChnl: int,
            corX: int, corY: int) -> np.array:
    """zoom an image"""
    try:
        assert image.any, "image can't be null"
        assert all(i > 0 for i in image.shape), \
            "all image shapes should be strictly positive"
        assert zx > 0 and zy > 0 and nbrChnl > 0 \
            and corX > 0 and corY > 0, "all ints should be strictly positive"
    except AssertionError as msg:
        print("AssertionError:", msg)
        raise Exception("")
    if (zx > image.shape[0]):
        zx = image.shape[0]
    if (zy > image.shape[1]):
        zy = image.shape[1]
    if (nbrChnl > image.shape[2]):
        nbrChnl = image.shape[2]
    if (corX + zx > image.shape[0]):
        corX = 0
    if (corY + zy > image.shape[1]):
        corY = 0
    zoom = image[corX:(zx + corX), corY:(zy + corY), 0:nbrChnl]
    print("New shape after slicing:", zoom.shape, "or", zoom.shape[0:2])
    return (zoom)


def ft_rotate(zoom: np.array) -> np.array:
    """rotate an image"""
    try:
        assert zoom.any, "image can't be null"
        assert all(i > 0 for i in zoom.shape), \
            "all image shapes should be strictly positive"
    except AssertionError as msg:
        print("AssertionError:", msg)
        raise Exception("")
    rotate = np.array([zoom[0].reshape(-1)] * len(zoom))
    for i in range(len(zoom)):
        for j in range(len(zoom[0])):
            rotate[i][j] = np.array([zoom[j][i].reshape(-1)])
    print("New shape after transpose:", rotate.shape)
    return rotate
