# Crear una estructura de clases con las siguientes características:

# Una clase padre abstracta llamada Coche.
# Dos clases hijas de Coche llamadas Electrico y Combustion.
# La clase padre debe tener en su constructor la asignación del atributo marca y un método abstracto llamado gasto_cada_100_km.
# La clase hija Electrico en su constructor debe asignar la marca y los atributos consumo_watios_hora y precio_watios_hora.
# La clase hija Combustion en su constructor debe asignar la marca y los atributos consumo_litros_100 y precio_litro.
# Cada clase hija debe implementar de forma obligatoria el método abstracto gasto_cada_100_km.

# El método gasto_cada_100_km en la clase Electrico debe devolver el gasto con la siguiente formula:
 # Gasto = consumo_watios_hora * precio_watios_hora

# El método gasto_cada_100_km en la clase Combustion debe devolver el gasto con la siguiente formula:
 # Gasto = consumo_litros_100 * precio_litro


from abc import ABC, abstractmethod
class Coche(ABC): # Clase padre atributo llamada Coche.
    
    def __init__ (self, marca): # Contructor con definicion vehiculo, con atributo marca.
        self.marca = marca # Atributo marca.
        
        
        
    # Con el metodo @abstractmethod podemos implementar el metodo abstracto creado.

    @abstractmethod  # Metodo abstracto llamado gasto_cada_100_km.
    def gasto_cada_100_km(self): 
        pass # Utilizamos pass para dejarlo vacio.
          
class Electrico(Coche): # Clase hija llamada Electrico.
    def __init__(self, marca, consumo_watios_hora, precio_watios_hora): # Constructor de la clase Electrico, con los argumentos.
        super().__init__(marca) # Llamamos con super() para que se pueda acceder a los atributos de la clase padre Electrico.
        self.consumo_watios_hora = consumo_watios_hora # Atributos consumo_watios_hora.
        self.precio_watios_hora = precio_watios_hora # Atributos precio_watios_hora.

    def gasto_cada_100_km(self): # Método abstracto llamado gasto_cada_100_km
        return self.consumo_watios_hora * self.precio_watios_hora # Construimos la formula para luego retornar el gasto.
    
class Combustion(Coche): # Clase hija llamada Combustion.
    def __init__(self, marca, consumo_litros_100, precio_litro): # Constructor de la clase Combustion, con los argumentos.
        super().__init__(marca) # Llamamos con super(). para acceder a los argumentos de la clase padre Combustion.
        self.consumo_litros_100 = consumo_litros_100 # Atributos consumo_litros_100.
        self.precio_litro = precio_litro # Atributos precio_litro.
        return

    def gasto_cada_100_km(self): # Método abstracto llamado gasto_cada_100_
        return self.consumo_litros_100 * self.precio_litro # Creamos la formula para luego retornar el gasto.
    

coche_electrico = Electrico("Mazda", 21000, 0.00018 ) # Creamos variable, llamando a la clase Electrico 
                                                      # y colocando los argumentos ( marca, consumo_watios_hora, precio_watios_hora).
coche_combustion = Combustion("Mazda", 6.1, 1.50) # Creamos variable, llamando a la clase Combustion
                                                # y colocando los argumentos ( marca, consumo_litros_100, precio_litro).

print(f"El gasto del vehiculo {coche_electrico.marca} eléctrico es de:", round(coche_electrico.gasto_cada_100_km(), 2)) # Hacemos print, llamando a la variable coche electrico 
                                           # y llamando a la formula .gasto_cada_100_km para retornar el gasto.
print(f"El gasto del vehiculo {coche_combustion.marca} de combustión es de:",round(coche_combustion.gasto_cada_100_km(), 2))
        


