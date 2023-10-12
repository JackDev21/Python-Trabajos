from django.db import models

class Nomina(models.Model):
    numero_empleado = models.IntegerField()
    salario = models.IntegerField()

    def __str__(self):
        return f'Nómina de {self.numero_empleado}'
    
