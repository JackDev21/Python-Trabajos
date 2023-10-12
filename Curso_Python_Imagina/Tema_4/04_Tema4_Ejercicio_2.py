# Ejercicio 2

# A partir del texto:

# 'el movil de ella fue encontrado en el parque’

# Sustituir con una expresión regular la palabra parque por cine.
# Imprimir por pantalla el número de veces que se ha hecho el reemplazo.

import re # Importamos el modulo re, para reemplazar una palabra especifica.

texto ="el movil de ella fue encontrado en el parque"

palabra = re.compile (r"\bparque\b")  # Creamos una variable llamado palabra. Busca la palabra "parque" en el texto.

nuevo_texto, num_reemplazos = palabra.subn("cine", texto) # Utilizamos subn() para reemplazar todas las ocurrencias de "parque", en el texto.

print(nuevo_texto)
print(f"Se ha hecho {num_reemplazos} reemplazo.")



