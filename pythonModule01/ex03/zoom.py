from load_image import ft_load, ft_zoom
from matplotlib import pyplot as plt


def main():
    x = 400
    y = 400
    chnl = 1
    corx = 100
    cory = 450
    try:
        image = ft_load("animal.jpeg")
        print(image)
        zoom = ft_zoom(image, x, y, chnl, corx, cory)
        print(zoom)
    except Exception:
        return
    if (chnl == 1):
        plt.imshow(zoom, cmap='gray', vmin=0, vmax=255)
        plt.show()
    elif (chnl == 3):
        plt.imshow(zoom)
        plt.show()


if __name__ == "__main__":
    main()
