import csv
from matplotlib import pyplot as plt

def asean_2014():
    asean=['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic",
        'Malaysia', 'Myanmar', 'Philippines',
        'Singapore', 'Thailand', 'Viet Nam']
    with open('population-estimates_csv.csv','r') as populationfile:
            population_reader=csv.DictReader(populationfile)
            for population in population_reader:
                if population['Year']=='2014' and population['Region'] in asean:
                    plt.barh(population['Region'],float(population['Population']))
    plt.xlabel=('ASEAN Countries')
    plt.ylabel("Population Count")
    plt.show()
asean_2014()     