""" Importing modules to solve the problem."""
import csv
from matplotlib import pyplot as plt

# List containing asean country names.
asean = ['Brunei Darussalam', 'Cambodia',
         'Indonesia', "Lao People's Democratic Republic",
         'Malaysia', 'Myanmar', 'Philippines',
         'Singapore', 'Thailand', 'Viet Nam']
# Opening file to extract data.
with open('population-estimates_csv.csv', 'r', encoding='utf-8') as popfile:
    population_reader = csv.DictReader(popfile)
    # Calculate the asean countries population in year 2014 and plot it.
    for population in population_reader:
        if population['Year'] == '2014' and population['Region'] in asean:
            plt.barh(population['Region'], float(population['Population']))
plt.ylabel('ASEAN Countries')
plt.xlabel('Population Count')
plt.show()
