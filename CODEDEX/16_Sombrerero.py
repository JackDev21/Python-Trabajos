
# https://github.com/codedex-io/python-101/blob/main/3-control-flow/16_sorting_hat_1.py



gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('El Sombrero Seleccionador')
print('===============')

# ~~~~~~~~~~~~~~~ Pregunta 1 ~~~~~~~~~~~~~~~

print('Q1) ¿Te gusta el amanecer o el anochecer?')

print('  1) Amanecer')
print('  2) Anochecer')

respuesta = int(input('Ingresa tu respuesta (1-2): '))

if respuesta == 1:
  gryffindor += 1
  ravenclaw += 1
elif respuesta == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Respuesta incorrecta.')

# ~~~~~~~~~~~~~~~ Pregunta 2 ~~~~~~~~~~~~~~~

print("\nQ2) Cuando muera, quiero que la gente me recuerde como:")

print('  1) El Bueno')
print('  2) El Grande')
print('  3) El Sabio')
print('  4) El Audaz')

respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
  hufflepuff += 2
elif respuesta == 2:
  slytherin += 2
elif respuesta == 3:
  ravenclaw += 2
elif respuesta == 4:
  gryffindor += 2
else:
  print('Respuesta incorrecta.')

# ~~~~~~~~~~~~~~~ Pregunta 3 ~~~~~~~~~~~~~~~

print('\nQ3) ¿Qué tipo de instrumento te agrada más escuchar?')

print('  1) El violín')
print('  2) La trompeta')
print('  3) El piano')
print('  4) La batería')

respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
  slytherin += 4
elif respuesta == 2:
  hufflepuff += 4
elif respuesta == 3:
  ravenclaw += 4
elif respuesta == 4:
  gryffindor += 4
else:
  print('Respuesta incorrecta.')

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

mayor_puntaje = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == mayor_puntaje:
  print('🦁 ¡Gryffindor!')
elif ravenclaw == mayor_puntaje:
  print('🦅 ¡Ravenclaw!')
elif hufflepuff == mayor_puntaje:
  print('🦡 ¡Hufflepuff!')
else:
  print('🐍 ¡Slytherin!')
