
# https://github.com/codedex-io/python-101/blob/main/4-loops/17_enter_pin.py

print('=== BANCO DE CODéDEX ===')

pin = int(input('Ingresa tu PIN: '))

while pin != 1234:
  pin = int(input('PIN incorrecto. Ingresa tu PIN nuevamente: '))

if pin == 1234:
  print('¡PIN aceptado!')
