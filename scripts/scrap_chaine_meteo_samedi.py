import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-demain')

soup = BeautifulSoup(response.text, 'html.parser')

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

meteo_demain = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
meteo_demain = meteo_demain.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_demain.insert(0,'jour',[jour, jour, jour, jour])

response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-lundi')

soup = BeautifulSoup(response.text, 'html.parser')

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

meteo_lundi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
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

meteo_mardi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
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

meteo_mercredi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
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

meteo_jeudi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
meteo_jeudi = meteo_jeudi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_jeudi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-vendredi')

soup = BeautifulSoup(response.text, 'html.parser')

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

meteo_vendredi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
meteo_vendredi = meteo_vendredi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_vendredi.insert(0,'jour',[jour, jour, jour, jour])


response = requests.get('https://www.lachainemeteo.com/meteo-france/ville-215860/previsions-meteo-saint-georges-d-oleron-samedi')

soup = BeautifulSoup(response.text, 'html.parser')

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

meteo_samedi = pd.DataFrame(alls, columns=['period', 'meteo', 'temperature', 'vent', 'logo'])
meteo_samedi = meteo_samedi.loc[0:3]

for d in soup.find_all("div", {"id":"forecastContainer"}):
    jour = d.find('h3', attrs={'class':'toggleDesktop'}).text

meteo_samedi.insert(0,'jour',[jour, jour, jour, jour])

meteo_semaine = pd.concat([meteo_demain, meteo_lundi, meteo_mardi, meteo_mercredi, meteo_jeudi, meteo_vendredi, meteo_samedi], ignore_index=True)

i = 0
while i<4:
    meteo_semaine['jour'][i] = meteo_semaine['jour'][i][9:]
    i += 1

datetime = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

meteo_semaine.to_csv("/home/freebox/Desktop/Meteo/data/chaine_meteo_"+datetime+".csv")
