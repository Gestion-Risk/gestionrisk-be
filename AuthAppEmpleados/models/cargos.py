from django.db  import models

class Cargos(models.Model):
    idCargo = models.AutoField(primary_key=True)
    cargo = models.CharField('cargo', max_length=45) 
        