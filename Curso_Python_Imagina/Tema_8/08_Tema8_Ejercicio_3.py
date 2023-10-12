# Crear un programa que cree una guía telefónica a modo de diccionario donde la clave 
# sea el nombre de la persona y el valor el número de móvil. Sobre la guía final se aplicará una ordenación por nombre.

# El nombre y el móvil se pedirán por consola.
 
# Se pedirán de forma recurrente nombre y móvil hasta que se pulse enter sin introducir ningún valor en el nombre.

def guia(): # Definición de la función
    guia_telefonica = {} # Creamos un diccionario vacío.

    while True: # Creamos una condicion.
        nombre = input("Introduce el nombre: ") # Preguntamos al usuario que introduzca el nombre.
        if nombre == "":  # Si el usuario no introduce ningún valor, se termina.
            break 
        else:
            telefono = input("Introduce el número de móvil: ") # Preguntamos al usuario que introduzca el número de móvil.
            guia_telefonica[nombre] = telefono # Agregamos el nombre y el número de móvil al diccionario.

    guia_telefonica_ordenada = dict(sorted(guia_telefonica.items())) # Ordenamos el diccionario.

    print(guia_telefonica_ordenada) # Imprimimos el diccionario ordenado.

    for nombre, telefono in guia_telefonica_ordenada.items(): # Recorremos el diccionario ordenado.
        print(f"Nombre: {nombre} /_\ Nº Teléfono: {telefono}")

guia()