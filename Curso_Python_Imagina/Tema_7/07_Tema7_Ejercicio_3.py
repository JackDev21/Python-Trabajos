#Ejercicio con listas anidadas

# A partir de la siguiente matriz generada por una lista anidada, obtén una nueva lista con la diagonal izquierda (valores 1, 5 y 9).

# Ejercicio 3
"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
"""


matriz = [
    [1, 2, 3], # Lista en posicion 0
    [4, 5, 6], # Lista en posicion 1
    [7, 8, 9]] # Lista en posicion 2

diagonal = len(matriz) # Comprobamos longitud de la lista
print(diagonal) 

nueva_lista = [matriz[i][i] for i in range(diagonal)] # Recorremos la matriz con "i" y agregamos a la nueva lista los elementos,
print(nueva_lista)                                    # indice de fila e indice de columna son iguales en la diagonal.
    
