from django.db                  import models
from .cargos                    import Cargos
from .areaCapacitacion          import AreaCapacitacion


class CargosCapacitacion(models.Model):
    idCarCap = models.AutoField('id_car_cap', primary_key=True)
    idcarFk = models.ForeignKey(Cargos,related_name='id_cargo_fk', on_delete=models.CASCADE)
    idAreaCapFk = models.ForeignKey(AreaCapacitacion, related_name='cargo_area_fk', on_delete=models.CASCADE)
    
