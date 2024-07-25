from load_csv import load
from matplotlib import pyplot as plt
import numpy as np
import sys


def ft_yaxis(x: int):
    if (x / 1000000000 >= 1):
        x = x / 1000000000
        return ("{:.2f}G".format(x))
    if (x / 1000000 >= 1):
        x = x / 1000000
        return ("{:.0f}M".format(x))
    if (x / 1000 >= 1):
        x = x / 1000
        return ("{:.0f}k".format(x))


def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        return
    try:
        data = load("../population_total.csv")
        dataArg = data.set_index("country").transpose()[sys.argv[1]]
    except Exception as msg:
        print("ExceptionError:", msg)
        return

    cpy = data.set_index("country").transpose()
    dataFr = cpy["France"]
    limx = np.where(np.array(cpy.index) == "2050")[0][0]
    X = np.array(cpy.index)[:limx]
    Yfr = np.array(dataFr.replace(
        {'B': 'e+09', 'M': 'e+06', 'k': 'e+03'},
        regex=True))[:limx].astype(float).astype(int)
    Yarg = np.array(dataArg.replace(
        {'B': 'e+09', 'M': 'e+06', 'k': 'e+03'},
        regex=True))[:limx].astype(float).astype(int)

    plt.plot(X, Yarg, color='b', label=sys.argv[1])
    plt.plot(X, Yfr, color='g', label="France")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks([a for a in X if int(a) / 40 == int(int(a) / 40)])
    plt.yticks(np.arange(0, max(Yfr[-1], Yarg[-1]) * 1.05, 20000000))
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels([ft_yaxis(x) for x in current_values])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
