
# https://www.codedex.io/python/20-99-bottles

for x in range(99, 0, -1): # La función range en este caso es el siguiente: 
                           #range(start(99), stop(0), step(-1)) emppieza en 99, termina en 0, y step es el incremento ó el decremento del numero.
    print(f"Hay {x} de cervezas en la pared")
    print(f"{x} botellas de cerveza")
    print("Coge una y pásala")
    print(f"Quedan {x-1} de cerveza en la pared")