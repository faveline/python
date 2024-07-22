from load_image import ft_load, ft_zoom, ft_rotate
from matplotlib import pyplot as plt


def main():
    x = 400
    y = 400
    chnl = 1
    corx = 100
    cory = 450
    try:
        image = ft_load("../animal.jpeg")
        zoom = ft_zoom(image, x, y, chnl, corx, cory)
        print(zoom)
        rotate = ft_rotate(zoom)
        print(rotate)
    except Exception as msg:
        print("Exception error:", msg)
        return
    if (chnl == 1):
        plt.imshow(rotate, cmap='gray', vmin=0, vmax=255)
        plt.show()
    elif (chnl == 3):
        plt.imshow(rotate)
        plt.show()


if __name__ == "__main__":
    main()
