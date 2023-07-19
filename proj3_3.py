import csv
from matplotlib import pyplot as plt

def saarc_population():
    afg_population, bang_population, bhut_population =0,0,0
    ind_population, mald_population, nep_population =0,0,0
    pak_population, sri_population =0,0
    with open('population-estimates_csv.csv','r') as populationfile:
        population_reader=csv.DictReader(populationfile)
        for country in population_reader:
            if country['Region']=='Afghanistan':
                afg_population+=round(float(country['Population']))
            elif country['Region']=='Bangladesh':
                bang_population+=round(float(country['Population']))
            elif country['Region']=='Bhutan':
                bhut_population+=round(float(country['Population']))
            elif country['Region']=='India':
                ind_population+=round(float(country['Population']))
            elif country['Region']=='Maldives':
                mald_population+=round(float(country['Population']))
            elif country['Region']=='Nepal':
                nep_population+=round(float(country['Population']))
            elif country['Region']=='Pakistan':
                pak_population+=round(float(country['Population']))
            elif country['Region']=='Sri Lanka':
                sri_population+=round(float(country['Population']))
    saarc_population=[afg_population, bang_population, bhut_population, 
                        ind_population, mald_population, nep_population, 
                        pak_population, sri_population]
    saarc=['Afghanistan', 'Bangladesh', 'Bhutan', 
       'India', 'Maldives', 'Nepal', 
       'Pakistan', 'Sri Lanka']
    plt.bar(saarc,saarc_population)
    plt.ylim(1000,60000000,10000)
    plt.show()
saarc_population()