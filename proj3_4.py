from matplotlib import pyplot as plt
import csv

asean=['Brunei Darussalam', 'Cambodia', 'Indonesia', " Lao People's Democratic Republic",
        'Malaysia', 'Myanmar', 'Philippines',
        'Singapore', 'Thailand', 'Viet Nam']
years=[str(i) for i in range(2004,2015)]
year_country={}
for country in asean:
    for year in years:
        if country not in year_country:
           year_country.update({country: {year:0}})
        else:
           year_country[country].update({year:0})
        
with open('population-estimates_csv.csv','r') as populationfile:
    population_reader=csv.DictReader(populationfile)
    for population in population_reader:
        if population['Year'] in years and population['Region'] in asean:
            year_country[population['Region']][population['Year']]+=round(float(population['Population']))

pop_l=[]
for i in asean:
    pop=[]
    for j in years:
        pop.append(year_country[i][j])
    pop_l.append(pop)
colour=['r','b','g','y','m','c','pink','purple','brown','grey']
barwidth=0.08
fig = plt.subplots(figsize =(12, 8))
br1=[i for i in range(len(years))]
br=[br1]
b=[]
for i in range(1,len(asean)):
    b=[x + barwidth for x in br[i-1]]
    br.append(b)
    b=[]
for i in range(len(asean)):
    plt.bar(br[i], pop_l[i], width= barwidth, color= colour[i], label=asean[i])
plt.xticks([r + barwidth for r in range(len(years))],years)
plt.legend()
plt.show()
