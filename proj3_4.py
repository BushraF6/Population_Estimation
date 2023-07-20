import csv
from matplotlib import pyplot as plt

asean=['Brunei Darussalam', 'Cambodia', 'Indonesia', " Lao People's Democratic Republic"
        'Malaysia', 'Myanmar', 'Philippines',
        'Singapore', 'Thailand', 'Viet Nam']
years=[i for i in range(2004,2015)]
Brunei=[]
Cambodia=[]
Indonesia=[]
Laos=[]
Malaysia=[]
Myanmar=[]
Phillippines=[]
Singapore=[]
Thailand=[]
Vietnam=[]
lis=[]
with open('population-estimates_csv.csv','r') as populationfile:
    population_reader=csv.DictReader(populationfile)
    for population in population_reader:
        for year in years:
            if year==int(population['Year']):
                    if population['Region']=='Brunei Darussalam':
                         Brunei.append(population['Population'])
                    elif population['Region']=='Cambodia':
                         Cambodia.append(population['Population'])
                    elif population['Region']=='Indonesia':
                         Indonesia.append(population['Population'])
                    elif population['Region']=="Lao People's Democratic Republic":
                         Laos.append(population['Population'])
                    elif population['Region']=='Malaysia':
                         Malaysia.append(population['Population'])
                    elif population['Region']=='Myanmar':
                         Myanmar.append(population['Population'])
                    elif population['Region']=='Philippines':
                         Phillippines.append(population['Population'])
                    elif population['Region']=='Singapore':
                         Singapore.append(population['Population'])
                    elif population['Region']=='Thailand':
                         Thailand.append(population['Population'])
                    elif population['Region']=='Viet Nam':
                         Vietnam.append(population['Population'])
barwidth=0.06
fig = plt.subplots(figsize =(12, 8))
br1=[i for i in range(len(years))]
br2=[x + barwidth for x in br1]
br3=[x + barwidth for x in br2]
br4=[x + barwidth for x in br3]
br5=[x + barwidth for x in br4]
br6=[x + barwidth for x in br5]
br7=[x + barwidth for x in br6]
br8=[x + barwidth for x in br7]
br9=[x + barwidth for x in br8]
br10=[x + barwidth for x in br9]

plt.bar(br1, Brunei, width= barwidth, color= 'r', label= 'Brunei')
plt.bar(br2, Cambodia, width= barwidth, color= 'b', label = 'Cambodia')
plt.bar(br3, Indonesia, width= barwidth, color='g', label= 'Indonesia')
plt.bar(br4, Laos, width= barwidth, color= 'y', label= " Lao People's Democratic Republic")
plt.bar(br5, Malaysia, width= barwidth, color='m', label= 'Malaysia')
plt.bar(br6, Myanmar, width= barwidth, color='c', label= 'Myanmar')
plt.bar(br7, Phillippines, width= barwidth, color='purple', label= 'Philippines')
plt.bar(br8, Singapore, width= barwidth, color='pink', label= 'Singapore')
plt.bar(br9, Thailand, width= barwidth, color='grey', label= 'Thailand')
plt.bar(br10, Vietnam, width= barwidth, color='brown', label= 'Viet Nam')
plt.xticks([r + barwidth for r in range(len(years))],years)
plt.legend()
plt.show()
