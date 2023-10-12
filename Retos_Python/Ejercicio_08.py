# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir 
# utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar
# la siguiente capa, terminan su trabajo inmediatamente.

# Prueba tu código con los datos que hemos proporcionado.

blocks = int(input("Ingresa el número de bloques: ")) # Pregunta al usuario que ingrese la cantidad de bloques 
height = 0 # Iniciamos la altura desde 0
capas = 0 # Iniciamos la cantidad de capas desde 0

while blocks >= capas + 1: # Mientras la cantidad de bloques sea mayor o igual a la cantidad de capas + 1
    capas += 1 # Aumentamos la cantidad de capas
    blocks -= capas # Disminuimos la cantidad de bloques por cada capa 
    height += 1 # Aumentamos la altura por cada capa


print("La altura de la pirámide:", height)

