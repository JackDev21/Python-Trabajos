# A partir del siguiente endpoint relativo a un API público de libros:
# https://www.anapioficeandfire.com/api/books
# Devolver el número de páginas del libro: ‘'A Feast for Crows’’
# Nota: El atributo que se debe consultar es: 'numberOfPages'

import requests
import json

url = "https://www.anapioficeandfire.com/api/books"

nombre_del_libro = {"name": "A Feast for Crows"}

respuesta = requests.get(url, params = nombre_del_libro)
status = respuesta.status_code # Status code para ver el estado de la respuesta.
print(status)

res = json.loads(respuesta.text)


print (f"Numero de páginas del libro: {res[0]['numberOfPages']}")

