# Ejercicio sobre errores en tiempo de ejecución
# Crear una aplicación con los siguientes requisitos:
# Que pida el nombre y la edad por consola.
# Si el nombre no es alfanumerico que se lance un error personalizado que le informe al usuario con un print.
# Si la edad no es numérica que se lance un error personalizado que le informe al usuario con un print.
# En caso de que ambos sean correctos, informarlo con un print al usuario. 
# En caso de que alguno de los dos, o los dos sean incorrectos. Pedir los datos de nuevo.


while True:
    try:
        nombre = input("¿Cual es tu nombre?: ") # Solicitamos nombre al usuario.
        if not nombre.isalpha(): # Si el nombre no es alfanumerico, activa el except y vuelve a pedir los datos.
            raise NameError("El nombre tiene que ser alfanumerico.")
       
        
        edad = input("¿Que edad tienes?: ") # Solicitamos edad.
        while not edad.isnumeric(): # Si la edad no es un numero activa el print y vuelve a preguntar la edad.
            print("La edad debe ser un número")
            edad = input("¿Que edad tienes?: ")
            break
            
            

        print("Nombre y edad introducidos correctamente")
        break

    except: 
        print("--- Escribe los datos correctamente ---")

