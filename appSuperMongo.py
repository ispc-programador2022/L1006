from bs4 import BeautifulSoup
import requests
import json
import datetime
from os import path
import pymongo
from pymongo import MongoClient 

# Datos para Autenticarse  en el server online de la base

cluster=MongoClient("mongodb+srv://AdminScrap:HXfk6qDTCyzzqhLw@cluster0.oxitgjo.mongodb.net/?retryWrites=true&w=majority")

# Identificacion del cluster (BBDD) con el cual trabajaremos

db = cluster["Precios"]
collection = db["Super"]


# json ejempo para probar la base, tal cual lo arma el scrapper

post ={'super': 'carrefour', 
       'producto': 'Fideos', 
       'url': 'https://supermercado.laanonimaonline.com/almacen/fideos/largos-y-guiseros/fideos-mostachol-lucchetti-x-500-g/art_11/', 
       'fecha': '08-11-2022', 'precio': '290'}


# Ejemplo Insertar datos en la tabla

collection.insert_one(post)
print ("post insertado")

# Ejemplo recoleccion datos en la tabla

resultados=collection.find({"super":"carrefour"})
for result in resultados:
     print(result)

