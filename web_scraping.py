# Importar librerías
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import sqlite3 as sql

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
    i += 1

df = pd.DataFrame({"MONEDAS" : monedas, "COMPRA" : compra, "VENTA" : venta})

print(df)

#Remplazamos el signo $ y la , por un . para poder luego manipular los datos como si fueran flotantes en la base de datos
df["COMPRA"] = df["COMPRA"].apply(lambda x: x.replace("$",""))
df["COMPRA"] = df["COMPRA"].apply(lambda x: x.replace(",","."))
df["VENTA"] = df["VENTA"].apply(lambda x: x.replace("$",""))
df["VENTA"] = df["VENTA"].apply(lambda x: x.replace(",","."))

#Exportamos el dataframe a un archivo CSV
df.to_csv("Marcado online.csv")

#Leemos el archivo CSV para transformar sus datos a una lista y luego exportarlos a una base de datos
cotizacion = pd.read_csv("C:/Users/manu_/Marcado online.csv")

print(cotizacion)
#Transformamos las filas del DF en una lista para luego insertarlas en una base de datos
Lista_valores = cotizacion.values.tolist()

print(Lista_valores)