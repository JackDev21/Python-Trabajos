
# https://www.codedex.io/python/10-currency 

pesos = int(input('Cuanto tienes en pesos? '))
soles = int(input('Cuanto tienes en soles? '))
reais = int(input('Cuanto tienes en reais? '))

total = pesos * 0.058 + soles * 0.28 + reais * 0.21

print(total, "USD")