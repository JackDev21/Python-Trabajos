# A partir del siguiente código que calcula la raíz cubica de cada elemento de una lista y genera una nueva. 
# Crear uno equivalente con programación funcional.

"""
def raiz_cubica(data):
    res = []
    for item in data:
        res.append(pow(item,1/3))
    return res
data = [8, 4, 6, 10, 7]
print(raiz_cubica(data))
"""


raiz_cubica = list(map(lambda num : pow(num, 1/3), [8, 4, 6, 10, 7])) # Creamos variable, creamos una lista, seguido de un map para recorrer la lista. 
print(raiz_cubica)                                                    # Seguido de lambda con su argumento y el calculo de la raíz cubica.


