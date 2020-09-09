#!/usr/bin/python3
from pandas import read_csv
from matplotlib import pyplot


def main():
	# Initialize
	column_names = ["Date", "Temperature", "Humidity", "Pressure"]
	
	# Open csv file
	df = read_csv("data.csv", names=column_names, sep=";", header=0, index_col=0, parse_dates=True, squeeze=True)
	
	# Plot optins
	df.plot(subplots=True)
	pyplot.show()
	
	# Print data frame to consle
	print(df.head())

if __name__ == "__main__":
	main()