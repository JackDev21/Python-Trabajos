# Ejercicio balance de gastos.

# Definir la expresión para calcular el balance de ingresos y gastos donde:
# Ingresos Totales = 2000.60 euros.
# Gasto1 = 500.30 euros.
# Gasto2 = 400.20 euros.
# Gasto3 = 100.10 euros.

# El resultado final debe ser igual a 1000.0

from decimal import Decimal

ingresos = Decimal ("2000.60")  # Variables con los valores.
gasto1 = Decimal ("500.30")
gasto2 = Decimal ("400.20")
gasto3 = Decimal ("100.10")

total = ingresos - gasto1 - gasto2 - gasto3 # Calculo de los valores.

print(total) # Total del calculo
