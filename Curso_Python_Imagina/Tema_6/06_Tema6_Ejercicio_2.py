# Ejercicio sobre error semántico

# El siguiente código calcula la suma de los números pares de una lista. Se pide hallar el error semántico.
"""
mi_lista = [1, 2, 3, 4, 5, 6 , 7 , 8, 9 ,10]
lst_pares = []
for elemento in mi_lista:
    if elemento % 2 != 0:
        lst_pares.append(elemento)

suma = 0
for elemento_par in lst_pares:
    suma = suma + elemento_par
print(f'suma total = {suma}')
"""

mi_lista = [1, 2, 3, 4, 5, 6 , 7 , 8, 9 ,10]
lst_pares = []
for elemento in mi_lista:
    if elemento % 2 == 0:
        lst_pares.append(elemento)

suma = 0
for elemento_par in lst_pares:
    suma = suma + elemento_par
print(f'suma total = {suma}')