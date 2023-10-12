# Dados dos módulos en la misma carpeta con nombres modulo_1 y modulo_2, y siendo el contenido de cada uno:


#modulo_1

# Importamos del modulo_2 "sumatorio nombrandola s_func y "c" nombrandola "z"

from Curso_Python_Imagina.Tema_10.Ejercicio_1.modulo_2 import sumatorio as s_func, c as z

x = 2
y = 3
print(s_func(2, 3, z))





"""
# modulo_2

def sumatorio(a, b, c):
    return a + b + c
c = 20
"""

#Añadir al modulo_1 los imports que faltan para que el print funcione y muestre 25.