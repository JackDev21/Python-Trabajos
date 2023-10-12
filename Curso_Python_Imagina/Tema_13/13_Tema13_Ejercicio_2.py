# A partir de un fichero de texto con el siguiente contenido:

"""
linea 1
linea 2
linea 3
linea 4
linea 5
linea 6
"""

# Generar uno nuevo que contenga únicamente las líneas pares, pero filtrando el contenido del fichero original 
# con programación funcional, sin usar en la solución estructuras for ni while


with open("File1.txt", "r") as File1: # Abrimos el archivos "File1.txt" en modo lectura, la llamamos File1.
    File1 = File1.readlines() # Leemos las lineas del archivo "File1.txt"

lineas_filtradas = filter(lambda x: (File1.index(x) + 1) % 2 == 0, File1) # Utilizamos filter() para selecionar las lineas pares de File1. La funcion lambda tomo un argumento "x"
                                                                          # que representa cada linea del archivo, y devuelve True si es par.El resultado se almacena en lineas_filtradas.
with open("File3.txt", "w") as File3: # Creamos un arhivo File3.txt en modo escritura.
    File3.writelines(lineas_filtradas) # Escribe las lineas filtradas en el archivo utilizando "writelines()".




    

