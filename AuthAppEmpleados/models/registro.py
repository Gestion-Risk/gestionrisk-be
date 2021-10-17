from django.db                  import models
from .trabajadores                   import Trabajadores
from .capacitacion                   import Capacitacion


class Registro(models.Model):
    idRegistro = models.AutoField(primary_key=True)
    idCapacitacionFk = models.ForeignKey(Capacitacion, related_name='idCapacitacionFk', on_delete=models.CASCADE)
    cedulaTrabajador = models.ForeignKey(Trabajadores, related_name='cedulaTrabajadorFk', on_delete=models.CASCADE)

