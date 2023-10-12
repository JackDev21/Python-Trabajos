# https://www.codedex.io/python/18-guess-number


adivinar = 0
intentos = 0

while adivinar != 6 and intentos < 5:
  adivinar = int(input('Adivina el número: '))
  intentos = intentos + 1

if adivinar != 6:
  print('Te quedaste sin intentos.')
else:
  print('¡Lo lograste!')
