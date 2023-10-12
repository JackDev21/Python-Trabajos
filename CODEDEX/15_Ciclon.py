# https://www.codedex.io/python/15-the-cyclone

altura = 250
creditos = 10
con_persona_alta = False

if creditos < 10:
  print("No tienes suficientes créditos para subir.")
elif altura >= 137 and creditos >= 10:
  print("¡Disfruta del paseo!")
elif altura < 137:
  if altura < 100 or not con_persona_alta:
    print("Todavía no tienes suficiente altura para este paseo.")
  elif altura >= 100 and con_persona_alta:
    print("¡Disfruten el paseo, amigos!")
else:
  print("Datos no válidos.")
