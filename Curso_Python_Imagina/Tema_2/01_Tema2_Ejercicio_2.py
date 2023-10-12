# Ejercicio 2.
# Crear un set vacío.
# Añadir al set los números del 1 al 10.
# Crear un segundo set con números del 5 al 15.
# Crea un nuevo set que tenga los números de ambos set.
# Sobre el último set dejar sólo los elementos que no estén en el segundo set.

primer_set = set() # Creamos set vacio.
primer_set.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]) # Añadimos elementos al set.
print(primer_set) # Imprimimos el set.

segundo_set = set()
segundo_set.update([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(segundo_set) # Imprimimos el set.

union_set = primer_set.union(segundo_set) # Creamos nuevo set, uniendo los primer_set y segundo_set
print(union_set) # Imprimimos el resultado.

dif_set = union_set.difference(segundo_set) # Creamos set sin los elementos de segundo_set.
print(dif_set) # Imprimimos el resultado.