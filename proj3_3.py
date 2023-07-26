""" Importing required modules to solve the problem. """
import csv
from matplotlib import pyplot as plt

# Creating list of names of SAARC countries.
saarc = ['Afghanistan', 'Bangladesh', 'Bhutan',
         'India', 'Maldives', 'Nepal',
         'Pakistan', 'Sri Lanka']
# Creating dictionary to store countries and their population count.
saarc_pop = {}
with open('population-estimates_csv.csv', 'r', encoding='utf-8') as popfile:
    population_reader = csv.DictReader(popfile)
    for popl in population_reader:
        if popl['Region'] in saarc:
            if popl['Region'] not in saarc_pop:
                saarc_pop[popl['Region']] = 0
            saarc_pop[popl['Region']] += round(float(popl['Population']))
plt.bar(saarc, list(saarc_pop.values()))
plt.ylim(1000, 60000000, 10000)
plt.xlabel('SAARC Countries')
plt.ylabel('Population_Count')
plt.show()
