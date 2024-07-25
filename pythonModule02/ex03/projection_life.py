from load_csv import load
from matplotlib import pyplot as plt
import matplotlib.ticker


def main():
    path = "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    try:
        dataGpd = load(path)
        dataLife = load("../life_expectancy_years.csv")
    except Exception as msg:
        print("ExceptionError:", msg)
        return

    dataGpd = dataGpd["1900"]
    dataLife = dataLife["1900"]

    fig1, ax1 = plt.subplots()
    plt.scatter(dataGpd, dataLife)
    ax1.set_xscale('log')
    ax1.set_xticks([300, 1000, 10000])
    ax1.get_xaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(
            lambda x, p: str(int(x / 1000)) + 'k' if (x >= 1000) else x))
    plt.title("1900")
    plt.xlabel("Gross domestic produce")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
