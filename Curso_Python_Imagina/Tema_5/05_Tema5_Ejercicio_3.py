# Pedir al usuario por consola que introduzca números enteros, para ello mostrar un mensaje 
# donde se pida un número, y tras pulsar enter se vuelva a pedir otro, y así hasta que el usuario pulse cero.
# Con los números introducidos, crear una lista de los que son primos, sin elementos duplicados y mostrarla por pantalla.

# Nota: Se considera un número primo, aquel número entero que sólo es divisible 
# (resto cero) por si mismo o por 1. Por ejemplo, 1, 2, 3, 5, 7 etc.

def numero_primo(): # Definimos funcion "numero_primo"
    for num in set(numeros): # bucle para iterar en los elmentos de "numeros" usando set para eliminar duplicados, lo llamamos "num".
        if num < 2 :    # Numero menor que 2 no es primo, por lo tanto continua.
            continue
        primo = True # Establecemos True en "primo" para que todo lo que es mayor que dos es True.
        for divisible in range(2, num): # Buscamos desde 2  hasta los numeros que hay dentro de "num".
            if num % divisible == 0:    # Comprobamos si "num" es divisibles entre si.
                primo = False           # Si no lo son es false y se descartan.
                
        if primo:
            lista_primo.append(num) # Aqui añadimos a la lista_primo los numeros que obtenemos de "primo".

lista_primo = [] # Creamos una lista
numeros = [] # Lista para almacenar los numeros.

num = int(input("Introduce numero (0 termina la ejecución): ")) # Le pedimos al usuario que introduzca números, y los almacenamos en "num".

while num != 0: # Creamos un bucle
    numeros.append(num) # Añadimos a la lista "num" los numeros introducidos por el usuario.
    num = int(input("Introduce numero (0 termina la ejecución): ")) # Le pedimos al usuario que introduzca otro número.

numero_primo()
print("Los numeros primos son: ", lista_primo)





