""" importing the required modules to solve the problem. """
import csv
from matplotlib import pyplot as plt

#Creating lists to store the values.
years=[]
population_count=[]

#Opening file for extracting data.
with open('population-estimates_csv.csv','r') as populationfile:
    population_reader=csv.DictReader(populationfile)
    #Calculate population per year for country India and plot it.
    for population in population_reader:
        if population['Region']=='India': 
            years.append(int(population['Year']))
            population_count.append(float(population['Population']))
            plt.barh(population['Year'],float(population['Population']))

plt.xlabel("Year")
plt.ylabel('Population Count')
plt.show()
