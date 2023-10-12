# Ejercicio de errores de sintaxis.
# Del siguiente script de Python, encontrar los tres errores de sintaxis.

"""a = 5
b = 6
mi_lista = [a; b]
print(f'Primer elemento de mi lista:{mi_lista(0)}')

c = a * b
if c > a And b < c:
    print('C es mayor a todos')
"""


a = 5
b = 6
mi_lista = [a, b]
print(f'Primer elemento de mi lista: {mi_lista[0]}')

c = a * b
if c > a and b < c:
    print('C es mayor a todos')