# Ejercicio de entrada de datos

# Realizar las siguientes operaciones:

# Pedir por consola el año de nacimiento.
# Calcular la edad.
# Mostrar con un print la edad calculada.
 
# Nota: Para calcular el año actual, usar este código:
# import datetime
# year = datetime.date.today().strftime("%Y")

import datetime
year = datetime.date.today().strftime("%Y")  

año_nacimiento = (input("¿En que año naciste? ")) 
calculo_edad = int(year) - int(año_nacimiento)


print (f"Tienes {calculo_edad} años")
