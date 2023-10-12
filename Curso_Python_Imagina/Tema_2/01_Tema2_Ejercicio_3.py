# Crear un estructura de datos que permita almacenar un conjunto de datos, 
# en la que cada uno de sus elementos represente información de un coche.

# Cada coche tendrá un identificador o clave a partir de su matrícula, y como valor 
# o propiedades una serie de características propias del coche.

# Para el coche 1 la información será:
# marca: seat
#frabricacon: 2010
# matricula 5008KGS
# velocidad_radar: 220
# posicion_xy: 250,300

# Para el coche 2 la información será:
# marca: opel
# frabricacon: 2015
# matricula 0626KTX
# velocidad_radar: 180
# posicion_xy: 255,35

datos_vehiculos = {  # Creamos diccionario llamado datos_vehiculos  para añadir información de las matriculas.
    "5008KGS": {  # Añadimos otro diccionario dentro de datos_vehiculos que damos un valor al vehiculo que es la matricula.
        "marca": "seat", # Le añadimos todos los datos del vehiculo.
        "fabricacion": 2010,
        "matricula": "5008KGS",
        "velocidad_radar": 220,
        "posicion_xy": (255,300)},

    "0626KTX": { # Añadimos otro diccionario dentro de datos_vehiculos que damos un valor al vehiculo que es la matricula.
        "marca": "opel", # Le añadimos todos los datos del vehiculo.
        "fabricacion": 2015, 
        "matricula": "0626KTX",
        "velocidad_radar": 180,
        "posicion_xy": (255,35)}
}

print (datos_vehiculos["5008KGS"]) # Muestra una de las matriculas y todos los datos del vehiculo.
print (datos_vehiculos["0626KTX"])

print (datos_vehiculos["0626KTX"]["marca"]) # Muestra el dato que le pidas al diccionario.
print (datos_vehiculos["0626KTX"]["fabricacion"])
print (datos_vehiculos["0626KTX"]["posicion_xy"]) 