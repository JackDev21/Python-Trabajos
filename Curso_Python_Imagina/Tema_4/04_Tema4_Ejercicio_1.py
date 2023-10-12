# Ejercicio de operaciones sobre strings.

# A partir del siguiente texto, realizar las transformaciones necesarias para que: el texto:
 
#'       el año 2022    está teniendo un     gran conflicto    internacional  '#
 
# No haya espacios al principio ni al final.
# Las palabras estén separadas por espacios simples.
# La primera letra del texto esté en mayúsculas.


texto = "       el año 2022    está teniendo un     gran conflicto    internacional "
texto = texto.strip() # Aqui eliminamos los espacios del principio y el final.
print (texto)

texto = texto.split() # Separamos texto en palabras
print (texto)         

texto = " ".join (texto) # join() para unir las palabras con un solo espacio, toma una lista de palabras
                         # y las une en una sola cadena de texto.

print (texto)

texto = texto.capitalize() # capitalize() para poner la primera letra del texto en mayúscula.
print (texto)
