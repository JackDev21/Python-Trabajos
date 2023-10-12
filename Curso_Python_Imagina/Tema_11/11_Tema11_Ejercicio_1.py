# Crear una clase Calculadora con los siguientes requisitos:
# Que admita un número indefinidos de números en el constructor.
# Que tenga un método público suma, que devuelva la suma de todos los números.


class Calculadora: # Creamos una clase Calculadora con los siguientes requisitos:
    def __init__(self, *args): # Se inicializa el objeto a partir del metodo "__init__".
        self.numero = args

    def suma(self): # Se crea la suma.
        return sum(self.numero) # Se devuelve la suma.

    
mi_calculadora = Calculadora(1, 2, 3, 5, 9, 10, 25) # Creamos varios numeros.

resultado = mi_calculadora.suma() # Calculamos la suma, llamandola resultado.

print(resultado) # Imprimimos el resultado.