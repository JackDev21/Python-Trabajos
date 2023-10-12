# Ejercicio sobre sentencias If/elif/else.

# Dada la siguiente lista de números enteros:

lista_origen = [1,45,4,78,23,2,0,67]

# Obtener una nueva lista con dos elementos, donde:
# El primer elemento esté formado por los números pares de lista_origen.
# El segundo elemento esté formado por los números impares de lista_origen.

pares = [] # Creamos listas "pares" e "impares".
impares = []

for lista in lista_origen: # Recorremos lista_origen, para ver que hay en la lista_origen, y le llamamos lista.
    if lista % 2 == 0:  # Comprobamos los que son divisibles por 2 para buscar los pares
        pares += [lista]
    else:               # Aqui el resto de numeros que no estén en la busqueda de la lista anterior serán los impares.
        impares += [lista] 


print("Numeros pares: ", pares, "\nNumeros impares: ",impares)

