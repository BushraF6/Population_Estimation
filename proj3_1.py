import csv
from matplotlib import pyplot as plt

years=[]
population_count=[]
with open('population-estimates_csv.csv','r') as populationfile:
    population_reader=csv.DictReader(populationfile)
    for population in population_reader:
        if population['Region']=='India': 
            years.append(int(population['Year']))
            population_count.append(float(population['Population']))
            plt.barh(population['Year'],float(population['Population']))
plt.xlabel("Year")
plt.ylabel('Population Count')
plt.show()