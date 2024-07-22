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
        return
    image = np.array(Image.open(path))
    print("The shape of image is:", image.shape)
    return image
