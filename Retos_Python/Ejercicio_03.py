# Ejercicio 3: Conversión de temperatura

# Escribe un programa en Python que convierta una temperatura en grados Celsius a grados Fahrenheit. El programa debe solicitar al usuario ingresar la temperatura en grados Celsius y luego mostrar la temperatura equivalente en grados Fahrenheit.

# La fórmula para convertir de grados Celsius a grados Fahrenheit es:

# "f" = 9/5 * C + 32

# "f" es la temperatura en grados Fahrenheit y 
# "c" es la temperatura en grados Celsius.

c = float(input("Ingrese la temperatura en grados Celsius: ")) 
f = (9/5 * c) + 32

print ("La temperatura en grados Fahrenheit es: " + str(f))