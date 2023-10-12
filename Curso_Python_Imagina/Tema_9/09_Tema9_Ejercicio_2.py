# A partir de los siguientes datos, calcular el peso medio del sexo masculino menores de edad.

data = [
    {'nombre': 'Juan', 'edad': 20, 'sexo': 'M', 'peso': 60},
    {'nombre': 'Sergio', 'edad': 13, 'sexo': 'M','peso': 45},
    {'nombre': 'Ana', 'edad': 18, 'sexo': 'F','peso': 50},
    {'nombre': 'Alba', 'edad': 14, 'sexo': 'F','peso': 35},
    {'nombre': 'Leo', 'edad': 6, 'sexo': 'M','peso': 23},
    {'nombre': 'Evan', 'edad': 9, 'sexo': 'M','peso': 26}
]


filtro_edad_sexo = list(filter(lambda x: x["edad"] < 18 and x["sexo"] == 'M', data)) # Filtro de sexo masculino y edad menor de 18 años.
print(list(filtro_edad_sexo))

menores_edad = list(filtro_edad_sexo) # Lista con los datos menores de edad.

from functools import reduce # Funcion reduce para sumar los pesos de los datos menores de edad.
suma_peso = reduce(lambda acum, x: acum + x["peso"], menores_edad, 0) # Suma los pesos de los datos menores de edad.
peso_medio = suma_peso / len(menores_edad) # Calcula el peso medio de los hombres menores de edad.

print ("Peso medio de los hombres menores de edad : ", round(peso_medio, 2)) # Round para redondearlos decimales, y ponemos cuantos decimales deseamos.

