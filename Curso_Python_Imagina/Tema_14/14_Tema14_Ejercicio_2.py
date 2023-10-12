# A partir del siguiente endpoint relativo a un API público de libros:
# https://www.anapioficeandfire.com/api/books
# Recuperar la información del libro cuyo nombre es:
# ‘A Game of Thrones’
# Nota: El parámetro a usar en la petición GET es name

import requests  # Imprtamos libreria para hacer solicitud HTTP.
import json # Importamos json para procesar los datos en json.

url = "https://www.anapioficeandfire.com/api/books" # Asignamos a la variable url el valro de la URL que queremos consultar.
nombre_libro = {"name": "A Game of Thrones"} # Definimos diccionario con la variable nombre_libro con la clave name y valor "A Game of Thrones" 
                                             # para filtar el nombre del libro.

respuesta = requests.get(url, params = nombre_libro) # Con get hacemos solicitud a la url y la api se almacena en la variable respuesta.
status = respuesta.status_code # Status code para ver el estado de la respuesta.
print(status)

res = json.loads(respuesta.text) # Con la libreria json convertimos de json  a un objeto de Python, accediendo a text para que la respuesta sea en texto.



print (f"Titulo libro: {res[0]['name']}") # El libro se encuentra en la posicion 0 de la lista llamada res, 
                                          # habiendo filtrado anteriormente el libro para que solo aparezca el libro elegido. Luego se obtiene el valor asociado del diccinario "name". 

print (f"Autor : {res[0]['authors']}")
print (f"Isbn :  {res[0]['isbn']}")
print (f"Numero de páginas: {res[0]['numberOfPages']} ")
print (f"Pais : {res[0]['country']}")
print (f"Editorial: {res[0]['publisher']}")
print (f"Fecha publicación: {res[0]['released']}")























