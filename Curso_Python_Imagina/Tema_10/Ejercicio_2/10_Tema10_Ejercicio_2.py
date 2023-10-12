# A partir del siguiente código, crear uno nuevo que genere el mismo resultado, 
# pero usando la sentencia enumerate sobre la lista de datos.


estaciones = ['Primavera', 'Verano', 'Otoño', 'Invierno']

for indice in range(len(estaciones)):
    estacion = estaciones[indice]
    print(f'{indice}:{estacion}')


for indice, estacion in enumerate(estaciones):
    print(f'{indice}:{estacion}')