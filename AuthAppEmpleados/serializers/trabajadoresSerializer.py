from AuthAppEmpleados.models.trabajadores           import Trabajadores
from AuthAppEmpleados.models.cargos                 import Cargos
from AuthAppEmpleados.serializers.cargosSerializer  import CargosSerializer
from rest_framework                                 import serializers

class TrabajadoresSerializer(serializers.ModelSerializer):
    cargos = CargosSerializer
    class Meta:
        model   =   Trabajadores
        fields  =   ['cedula', 'nombres', 'apellidos', 'email', 'cargoIdFk']
    
    def to_representation(self, obj):
        trabajadores = Trabajadores.objects.get(cedula=obj.cedula)
        cargos       = Cargos.objects.get(idCargo=obj.cargoIdFk_id)
 
        return{
            'cedula'    :   trabajadores.cedula,
            'nombres'   :   trabajadores.nombres,
            'apellidos' :   trabajadores.apellidos,
            'email'     :   trabajadores.email,
            'cargoIdFk' :   {
                    "cargo" :   cargos.cargo
            } 
        }

