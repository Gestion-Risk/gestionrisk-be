from django.db                  import models
from .cargos                    import Cargos

class Trabajadores(models.Model):
    cedula = models.BigIntegerField(primary_key=True)
    nombres = models.CharField('nombres', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    email = models.EmailField('email', max_length=50, unique=True)
    cargoIdFk = models.ForeignKey(Cargos, related_name='cargoIdFk', on_delete=models.SET_NULL, null=True)
    