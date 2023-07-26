"""Importing required modules to solve the problem."""
import csv
import matplotlib.pyplot as plt

# Creating 2 lists to store the values of years and population_count.
years = []
population_count = []
# Opening file to extract data.
with open('population-estimates_csv.csv', 'r', encoding='utf-8') as popfile:
    population_reader = csv.DictReader(popfile)
    # Calculate population of India per year and plot it.
    for population in population_reader:
        if population['Region'] == 'India':
            years.append(int(population['Year']))
            population_count.append(float(population['Population']))
            plt.barh(population['Year'], float(population['Population']))
plt.ylabel("Year")
plt.xlabel('Population Count')
plt.show()
