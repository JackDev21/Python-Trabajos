# A partir del siguiente endpoint relativo a un API público de libros:
# https://www.anapioficeandfire.com/api/books
# Recuperar el número de libros que hay almacenados a partir de una petición GET.

import requests # Importamos libreria requests, permite enviar soluicitudes HTTP en python.
import json # Importamos libreria json, permite trabajar con los datos que recibimos de la api en formato json.


url = "https://www.anapioficeandfire.com/api/books" # URL que se quiere consultar:

respuesta = requests.get(url) # get para solicitar a la URL y la almacenamos en la variable respuesta.

status = (respuesta.status_code) # Imprimimos el codigo de estado de la respuesta HTTP
print (f"Peticion Correcta : {status}") # Comprobamos la peticion si es correcta o no a la URL.

respuesta = json.loads(respuesta.text) # Con json convertimos la respuesta de la API en formato json a un objeto python. 
                                       # Accediendo a text que contiene la respuesta en formato texto.
                                       # Utilizamos loads() de la libreria json para convertirlo en objeto python.

numero_libros = len(respuesta) # Con len calculamos la longitud del objeto que hemos creado a partir de la respuesta API.

print(f"El numero de libros almacenados es {numero_libros}") 