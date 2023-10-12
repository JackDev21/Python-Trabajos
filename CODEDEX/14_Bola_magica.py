# https://www.codedex.io/python/14-magic-8-ball


# Magic 8 Ball 🎱
# Codédex
import random

pregunta = input("¿Cual es tu pregunta? ")

numero_aleatorio = random.randint(1, 9)

if numero_aleatorio == 1:
  respuesta = 'Sí, definitivamente'
elif numero_aleatorio == 2:
  respuesta = 'Es decididamente así'
elif numero_aleatorio == 3:
  respuesta = 'Sin ninguna duda'
elif numero_aleatorio == 4:
  respuesta = 'Respuesta confusa, intenta de nuevo'
elif numero_aleatorio == 5:
  respuesta = 'Pregunta de nuevo más tarde'
elif numero_aleatorio == 6:
  respuesta = 'Mejor no te lo digo ahora'
elif numero_aleatorio == 7:
  respuesta = 'Mis fuentes dicen que no'
elif numero_aleatorio == 8:
  respuesta = 'Las perspectivas no son buenas'
elif numero_aleatorio == 9:
  respuesta = 'Muy dudoso'
else:
  respuesta = 'Error'
  
print('Pregunta:      ' + pregunta) 
print('Bola Mágica 8: ' + respuesta)
