# Sobre el siguiente extracto de código, introduce las sentencias 
# necesarias dentro de la funcion my_function_1 para que el 
# valor de a que muestre el print sea de 25.
"""a = 20

def my_funcion_1():
……….
……….
my_funcion_1()
print(a)"""

a = 20

def my_funcion_1(): # Definicion my_function_1()
    global a # Utilizamos "global" para modificar el valor global de "a"
    a = 25
 
my_funcion_1() 
print(a)
