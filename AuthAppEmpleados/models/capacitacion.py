from django.db                  import models
from .areaCapacitacion          import AreaCapacitacion

class Capacitacion(models.Model):
    idCapacitacion = models.AutoField(primary_key=True)
    curso = models.CharField('curso', max_length=60)
    idAreaCapacitacionFk = models.ForeignKey(AreaCapacitacion, related_name='capacitacionAreaFk', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField('fecha', blank=False)
    hora  = models.TimeField('hora',auto_now=False, auto_now_add=False,default='18:00')