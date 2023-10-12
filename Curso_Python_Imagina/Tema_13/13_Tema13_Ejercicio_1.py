# A partir de un fichero de texto con el siguiente contenido:
"""
linea 1
linea 2
linea 3
linea 4
linea 5
linea 6

"""

# Generar uno nuevo que contenga únicamente las líneas pares.


contenido = """linea 1
linea 2
linea 3
linea 4
linea 5
linea 6
"""

fichero1 = open("File1.txt", "w") # Creamos fichero File1.txt y con "w"(write) para tener permisos de escritura.
fichero1.write(contenido) # Write para obtener permisos de escribir dentro de File1.txt el contenido.
print("Fichero creado") # Print para indicar que el archivos ha sido creado.
fichero1.close() # Cerramos fichero creado.

fichero1 = open("File1.txt", "r") # Abrimos fichero File1.txt con "r" para poder leerlo.
fichero2 = open("File2.txt", "w") # Creamos fichero File2.txt con "w" para poder escribir.

i = 1 # Creamos variable i, igualando a 1 para llevar la cuenta de la linea actual.
for linea in fichero1: # Recorremos el bucle "for" de cada linea del archivo "File1.txt".
    if i % 2 == 0:  # Si la linea es par, la escribe en el archivo fichero2 (File2.txt).
        fichero2.write(linea)
    i = i + 1 # Incrementamos el valor de la variable en 1.


fichero1.close()
fichero2.close()










        
        
    





    



    