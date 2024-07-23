from load_csv import load
# from matplotlib import pyplot as plt


def main():
	try:
		data = load("../life_expectancy_years.csv")
	except:
		return
	franceData = data.loc[data["country"] == "France"]
	print(data.loc[data["country"] == "France"])

if __name__ == "__main__":
	main()