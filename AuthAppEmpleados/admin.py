from django.contrib                 import admin
from .models.usuario                import User
from .models.areaCapacitacion       import AreaCapacitacion
from .models.capacitacion           import Capacitacion
from .models.cargos                 import Cargos
from .models.cargosCapacitacion     import CargosCapacitacion
from .models.trabajadores           import Trabajadores
from .models.registro               import Registro

admin.site.register(User)
admin.site.register(AreaCapacitacion)
admin.site.register(Capacitacion)
admin.site.register(Cargos)
admin.site.register(CargosCapacitacion)
admin.site.register(Trabajadores)
admin.site.register(Registro)


# Register your models here.
