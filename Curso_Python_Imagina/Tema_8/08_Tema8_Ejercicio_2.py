# Crear un programa que a partir de los datos numéricos de una lista L, 
# cree una nueva estructura de datos con los números de la lista original L que no sean múltiplos de X

# La lista L se creará en tiempo de ejecución y tendrá valores del 1 al 100 incluidos.
 
# X será un entero solicitado por consola, cuyo valor sea entre 2 y 10.

lista =list(range(1, 101)) # Creamos una lista con los números del 1 al 100.


def multiplos(x):
    while x < 2 or x > 10: # Creamos una condición while (bucle) y decimos que el numero debe estar entre 2 y 10.
        print("El número debe estar entre 2 y 10")
        x = int(input("Ingrese un número entre 2 y 10: "))
        
    lista_multiplos = [] # Creamos una lista vacía.
    for numero in lista: # Recorremos la lista.
        if numero % x != 0: # Verificamos si el número no es múltiplo de X.
            lista_multiplos.append(numero) # Añadimos el número a la lista.

    print(f"No son multiplos de {x} : {lista_multiplos}")

multiplos(int(input("Ingrese un número entre 2 y 10: "))) # Ejecutamos la función y pedimos el número.
