import csv
from matplotlib import pyplot as plt

saarc=['Afghanistan', 'Bangladesh', 'Bhutan', 
       'India', 'Maldives', 'Nepal', 
       'Pakistan', 'Sri Lanka']
saarc_pop={}
with open('population-estimates_csv.csv','r') as population_file:
    population_reader=csv.DictReader(population_file)
    for population in population_reader:
        if population['Region'] in saarc:
            if population['Region'] not in saarc_pop:
                saarc_pop[population['Region']]=0
            saarc_pop[population['Region']]+=round(float(population['Population']))
plt.bar(saarc,list(saarc_pop.values()))
plt.ylim(1000,60000000,10000)
plt.show()
