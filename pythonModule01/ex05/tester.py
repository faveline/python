from load_image import ft_load
from pimp_image import ft_invert
# , ft_red, ft_green, ft_blue, ft_grey
from matplotlib import pyplot as plt


def main():
    try:
        image = ft_load("../landscape.jpg")
        print(image)
        test = ft_invert(image)
        # test = ft_red(image)
        # test = ft_green(image)
        # test = ft_blue(image)
        # test = ft_grey(image)
        print(test)
    except Exception as msg:
        print("ExceptioError:", msg)
        return
    plt.imshow(test)
    plt.show()


if __name__ == "__main__":
    main()
