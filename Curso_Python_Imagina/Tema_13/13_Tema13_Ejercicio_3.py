# A partir de un fichero de texto con el siguiente contenido:
"""linea 1
linea 2
linea 3
linea 4
linea 5
linea 6"""
 


# Generar un fichero nuevo con el mismo contenido pero serializado.

import pickle




with open ("File1.txt", "r") as archivo:
    contenido = archivo.readlines()

encriptado = pickle.dumps(contenido)

with open("encriptado.txt", "wb") as archivo_encriptado:
    archivo_encriptado.write(encriptado)




