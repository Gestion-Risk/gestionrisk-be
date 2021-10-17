from django.db                  import models
from .areaCapacitacion          import AreaCapacitacion

class Capacitacion(models.Model):
    idCapacitacion = models.AutoField(primary_key=True)
    curso = models.CharField('curso', max_length=60)
    idAreaCapacitacionFk = models.ForeignKey(AreaCapacitacion, related_name='capacitacionAreaFk', on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField('fecha', blank=False)