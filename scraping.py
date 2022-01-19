from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.ole.com.ar/estadisticas/futbol/primera-division.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('td', class_='team')
equipos = list()
count = 0
for i in eq:
    if count < 20:
        equipos.append(i.text)
    else: break
    count += 1

#Puntos

pt = soup.find_all('td', class_='st_relegation_avg')
puntos = list()
count = 0
for i in pt:
    if count < 20:
        puntos.append(i.text)
    else: break
    count += 1
    
df = pd.DataFrame({'Nombre': equipos, 'Puntos':puntos}, index=list(range(1, 21)))
print(df)
df.to_csv('clasificacion.csv', index=False)

