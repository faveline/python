from load_csv import load
from matplotlib import pyplot as plt
import numpy as np


def main():
    try:
        data = load("../life_expectancy_years.csv")
    except Exception as msg:
        print(msg)
        return

    data = data.set_index("country").transpose()

    plt.plot(np.array(data.index), np.array(data["France"]))
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Years")
    plt.ylabel("Life Expectancy")
    plt.xticks([a for a in np.array(data.index)
                if int(a) / 40 == int(int(a) / 40)])
    plt.show()


if __name__ == "__main__":
    main()
