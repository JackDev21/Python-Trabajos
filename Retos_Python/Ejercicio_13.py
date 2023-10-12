def is_year_leap(year):
    # Verificar si el año no es divisible por 4
    if year % 4 != 0:
        # Si no es divisible por 4, no es bisiesto
        return False
    # Verificar si el año no es divisible por 100
    elif year % 100 != 0:
        # Si no es divisible por 100, es bisiesto
        return True
    # Verificar si el año no es divisible por 400
    elif year % 400 != 0:
        # Si no es divisible por 400, no es bisiesto
        return False
    # Si ninguna de las condiciones anteriores se cumple, es bisiesto
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")