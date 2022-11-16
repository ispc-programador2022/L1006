# Importar librerías
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Dirección de la página web
url = "https://www.cronista.com/MercadosOnline/monedas.html"

# Ejecutar GET-Request
web = requests.get(url)
contenido = web.text

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
soup = BeautifulSoup(contenido, 'lxml')
filas = soup.find("ul", class_="list items-6")

#Creamos listas y una constante

monedas = list()
compra = list()
venta = list()
variacion = list()
i = 0

#Recorremos cada una de las filas 
for fila in filas:
    if i > 0:
        monedas.append(fila.find_all('span', class_="name col")[0].get_text())
        compra.append(fila.find_all('span', class_ = "buy-value")[0].get_text())
        venta.append(fila.find_all('div', class_ = "sell col")[0].get_text())
        #try:
            #variacion.append(fila.find_all('span', class_="percentage col")[0].get_text())
            #print(variacion)
       # except:
            #variacion.append(fila.find_all('span', class_ ="percentage up col")[0].get_text())
        
       #except:    
        #    variacion.append(fila.find_all('span', class_ ="percentage down col")[0].get_text())
    i += 1

df = pd.DataFrame({"MONEDAS" : monedas, "COMPRA" : compra, "VENTA" : venta})#, "VARIACIÓN" : variacion})

print(df)

