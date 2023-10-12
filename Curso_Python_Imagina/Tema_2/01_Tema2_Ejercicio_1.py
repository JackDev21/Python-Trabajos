# Ejercicio 1.

# Crear una lista con los 5 días laborables en orden.
# Añadir a la lista el domingo.
# Añadir a la lista el sábado antes del domingo.
# A partir de la lista crear una nueva solo con lunes, miércoles y  viernes.
# De la última lista, ordenar los días de la semana por orden alfabético.


dias_laborables = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"] # Creamos una lista de los días laborables.

print (len(dias_laborables)) # Mostramos la longitud de la lista
print (dias_laborables) # Print para mostrar en el terminal los dias laborables.

dias_laborables.append ("Domingo") # Añadimos Domingo a la lista.
print (dias_laborables) # Print para ver el resultado de añadir a la lista Domingo.

dias_laborables.insert(5, "Sabado") # Añadimos Sabado A la lista.
print (dias_laborables) # Print para ver el resultado de añadir a la lista Sabado.

nueva_lista = [dias_laborables[0], dias_laborables[2],dias_laborables[4]] # Creamos nueva lista seleccionando los elmentos que queremos.
print (nueva_lista) # Print de la nueva lista para ver el resultado.

nueva_lista.sort() # Ordenar por orden alfabético la nueva lista.
print(nueva_lista) # Print de la lista ordenada alfabeticamente.

dias_laborables.sort() # Ordenar por orden alfabético los días.
print(dias_laborables) # Print par aver el resultado ordenado alfabeticamente

