# Ejercicio 2: Calculadora de área de un triángulo

# Escribe un programa en Python que calcule el área de un triángulo. El programa debe solicitar al usuario que ingrese la base y la altura del triángulo y luego mostrar el área calculada.

# Recuerda que el área de un triángulo se calcula como (base * altura) / 2.

base = float (input("Ingrese la base del triángulo: "))
altura = float (input("Ingrese la altura del triángulo: "))

area = (base * altura) / 2

print ("El área del triángulo es: " + str(area))