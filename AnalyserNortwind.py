#Hovedprogram til opgave 4 del 2 hvor der indlæses data fra northwind.sql databasen, og analysers samt laves passende graf til dette.

#Opgaven:
#Brug Python og SQLite3-pakken til at forbinde til Northwind databasen.
#Brug SQL til at hente data fra de forskellige tabeller.
#Brug Pandas til at indlæse dataene og udføre en analyse for at finde salget for hvert land.
#Brug matplotlib til at lave et søjlediagram, der viser salget for hvert land.
#Analyser data og opret 2-3 yderligere relevante diagrammer ud fra data

#laver en python class som forbinder til northwind.sql og har en funktion til at hente søjler, eventuelt laver jeg flere funktioner...
import hentedata
import pandas as pd
import matplotlib.pyplot as plt

#sætte en dataframe op med ordreværdi, land og dato

#men jeg prøver først at bruge en pandas import funktion til hele order tabellen
#henter først tabel med ordre

#Opsætning af diverse dataframes
northwinddataframe=hentedata.fetchDataframeRestraint("Orders","all","hmm")
#herefter tabel med ordredetails
northwinddetailsdata=hentedata.fetchDataframeRestraint("OrderDetails","all","hmm")
#her laves en dataframe med lande, den er unik (her er lavet et snydekode i hentedata som bør kigges på , virker kun med unik liste)
landeliste = hentedata.fetchDataframe("Orders","ShipCountry")
#print(northwinddetailsdata.head(2))

#Her laves en merge af to dataframes, således en ny dataframe laves, hvor der kun er orderdetails for et enkelt land

#Der beregnes i løkken over hvert land, samlte omsætning og samlet ordrerprland
indkomstliste = []
antalordrerprland = []
for lande in landeliste["ShipCountry"]:
    ordrenummer = northwinddataframe.loc[northwinddataframe['ShipCountry']==lande,'OrderID']
    antalordrerprland.append(ordrenummer.shape[0])
    filtreretDetails=pd.merge(northwinddetailsdata,ordrenummer,on='OrderID')
    UKsum=(filtreretDetails['UnitPrice']*filtreretDetails['Quantity']-filtreretDetails['UnitPrice']*filtreretDetails['Quantity']*filtreretDetails['Discount']).sum()/1000
    indkomstliste.append(UKsum)






#opsætning af grafer 

landeliste['Omsætning']=indkomstliste
landeliste['ordercount']=antalordrerprland

fig,ax = plt.subplots()

#Jeg laver her et plot over ordrer pr. land i forhold til samlet indkomst

navnetags =landeliste['ShipCountry']
datay = landeliste['Omsætning']

#scatter graf
ax.scatter(landeliste['Omsætning'],landeliste['ordercount'])

ax.set_xlabel('antal ordrer')
ax.set_ylabel('samlet salg i tusinde')
ax.set_title('antal ordrer pr land')
ax.legend(title='omsætning i forhold til antal ordrer')

plt.show()



#del som laver mit plot

fig,ax = plt.subplots()

navnetags =landeliste['ShipCountry']
datay = landeliste['Omsætning']

ax.bar(navnetags, datay, color='red')

ax.set_ylabel('samlet salg i tusinde')
ax.set_title('Salg pr land')
ax.legend(title='Salg')

plt.show()


