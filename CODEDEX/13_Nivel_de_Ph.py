# https://www.codedex.io/python/13-ph-levels



ph = int(input('Introduce nivel de ph (0-14): '))

if ph > 7:
  print('Basico')
elif ph < 7:
  print('Acido')
else:
  print('Neutro')