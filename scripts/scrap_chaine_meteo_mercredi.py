# Import des librairies
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Crée un DataFrame vide pour stocker les données de prévision
meteo_semaine = pd.DataFrame(columns=['jour','period', 'meteo', 'temperature', 'vent', 'logo'])

# Dictionnaire permettant d'itérer sur les jours de la semaine
jours = {0:'demain', 1:'vendredi', 2:'samedi', 3:'dimanche', 4:'lundi', 5:'mardi', 6:'mercredi'}

# Boucle sur le dictionnaire pour aller scraper les données et le splacer au fur et à mesure dans meteo_semaine
for key,value in jours.items():

    # Récupère les données d'une page web et la soupifie
    response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-'+value)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape les données de prévision : prévision, température, vent et logo de la prévision, pour une journée
    # Avec 4 périodes : Nuit (0-6h), Matin(6-12h), Après-midi(12-18h), Soir(18h-00h)
    alls = []

    for d in soup.find_all("div", {"class":"quarter"}):
        period = d.find('div', attrs={'class':'front single'})
        text = d.find('div', attrs={'class':'cellText'})
        temperature = d.select('.quarter .data>.splitData:nth-of-type(3) :nth-of-type(1)')[0].find('div')
        vent = d.select('.quarter .data>.splitData:nth-of-type(4)')[0].find('span')
        logo = d.find('img')

        all1=[]

        if period is not None:
            all1.append(period.text.strip())

        if text is not None:
            all1.append(text.text.strip().splitlines())

        if temperature is not None:
            all1.append(temperature.text)

        if vent is not None:
            all1.append(vent.text)

        if logo is not None:
            all1.append(logo['data-src'])

        alls.append(all1)

    # Crée un DataFrame regroupant les données de la journée
    meteo_jour = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
    meteo_jour = meteo_jour.loc[0:3]

    # Récupère le jour et le colle dans le dataframe
    for d in soup.find_all("div", {"id":"forecastContainer"}):
        jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

    meteo_jour.insert(0,'jour',[jour, jour, jour, jour])

    # Ajoute les données de chaque journée dans la loop for
    meteo_semaine = pd.concat([meteo_semaine, meteo_jour], ignore_index=True)

i = 0
while i<4:
    meteo_semaine['jour'][i] = meteo_semaine['jour'][i][6:]
    i += 1

datetime = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

meteo_semaine.to_csv("/home/freebox/Desktop/Meteo/data/chaine_meteo_"+datetime+".csv")
