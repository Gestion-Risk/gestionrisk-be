from django.db                  import models

class AreaCapacitacion(models.Model):
    idAreaCap = models.AutoField(primary_key=True)
    area = models.CharField('area', max_length=55)
    descripcion = models.CharField('descripcion', max_length=120)
    
