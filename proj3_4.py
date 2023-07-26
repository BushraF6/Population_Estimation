""" Importing required modules to solve the problem. """
import csv
from matplotlib import pyplot as plt

# Creating list containing the names of ASEAN countries
asean = ['Brunei Darussalam', 'Cambodia', 'Indonesia',
         " Lao People's Democratic Republic",
         'Malaysia', 'Myanmar', 'Philippines',
         'Singapore', 'Thailand', 'Viet Nam']
# List containing years.
years = [str(i) for i in range(2004, 2015)]
# Dictionary to store population of every ASEAN countries per year.
year_country = {}
# Initializing the year_count dictionary with asean countries.
for country in asean:
    for year in years:
        if country not in year_country:
            year_country.update({country: {year: 0}})
        else:
            year_country[country].update({year: 0})
# Opening file and extracting data.
with open('population-estimates_csv.csv', 'r', encoding='utf-8') as popfile:
    population_reader = csv.DictReader(popfile)
    # Calculating ASEAN countries population per year.
    for pop in population_reader:
        if pop['Year'] in years and pop['Region'] in asean:
            year_country[pop['Region']][pop['Year']] += round(float(pop['Population']))
# Creating list and appending population_count of ASEAN countries per year.
pop_l = []
for i in asean:
    pop = []
    for j in years:
        pop.append(year_country[i][j])
    pop_l.append(pop)
# Plotting the data by setting width, colours and doing iteration.
colour = ['r', 'b', 'g', 'y', 'm', 'c', 'pink', 'purple', 'brown', 'grey']
BWIDTH = 0.08
fig = plt.subplots()
br1 = list(range(len(years)))
br = [br1]
b = []
for i in range(1, len(asean)):
    b = [x+BWIDTH for x in br[i-1]]
    br.append(b)
    b = []
for i, asean in enumerate(asean):
    plt.bar(br[i], pop_l[i], width=BWIDTH, color=colour[i], label=asean)
plt.xticks([r + BWIDTH for r in range(len(years))], years)
plt.xlabel('Years')
plt.ylabel('Population_count')
plt.legend()
plt.show()
