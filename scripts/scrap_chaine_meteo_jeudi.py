import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-demain')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_demain = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_demain = meteo_demain.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_demain.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-samedi')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_samedi = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_samedi = meteo_samedi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_samedi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-dimanche')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_dimanche = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_dimanche = meteo_dimanche.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_dimanche.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-lundi')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_lundi = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_lundi = meteo_lundi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_lundi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-mardi')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_mardi = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_mardi = meteo_mardi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_mardi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-mercredi')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_mercredi = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_mercredi = meteo_mercredi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_mercredi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-jeudi')

soup = BeautifulSoup(response.text, 'html.parser')

alls = []

for d in soup.find_all("div", {"class":"quarter"}):
    period = d.find('div', attrs={'class':'front single'})
    text = d.find('div', attrs={'class':'cellText'})
    logo = d.find('img')

    all1=[]

    if period is not None:
        all1.append(period.text.strip())

    if text is not None:
        all1.append(text.text.strip().splitlines())

    if logo is not None:
        all1.append(logo['data-src'])

    alls.append(all1)

meteo_jeudi = pd.DataFrame(alls, columns=['period', 'meteo', 'logo'])
meteo_jeudi = meteo_jeudi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_jeudi.insert(0,'jour',[jour, jour, jour, jour])


meteo_semaine = pd.concat([meteo_demain, meteo_samedi, meteo_dimanche, meteo_lundi, meteo_mardi, meteo_mercredi, meteo_jeudi], ignore_index=True)

semaine = meteo_semaine['jour'][0]

meteo_semaine.to_csv("/home/freebox/Desktop/Meteo/data/chaine_meteo_"+semaine+".csv")
