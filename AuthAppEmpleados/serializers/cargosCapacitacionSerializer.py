from AuthAppEmpleados.models.areaCapacitacion   import AreaCapacitacion
from AuthAppEmpleados.models.cargos             import Cargos
from AuthAppEmpleados.models.cargosCapacitacion import CargosCapacitacion
from rest_framework                             import serializers

from AuthAppEmpleados.serializers.areaCapacitacionesSerializer  import AreaCapacitacionesSerliazer
from AuthAppEmpleados.serializers.cargosSerializer              import CargosSerializer

class CargosCapacitacionSerializer(serializers.ModelSerializer):
    areacapacitacion = AreaCapacitacionesSerliazer()
    cargos = CargosSerializer()
    class Meta:
        model = CargosCapacitacion
        fields = ['id_car_cap', 'id_cargo_fk', 'cargo_area_fk']

    def to_representation(self, obj):
        cargoscapacitacion = CargosCapacitacion.objects.get(id=obj.idCarCap)
        areacapacitacion = AreaCapacitacion.objects.get(cargoscapacitacion=obj.idAreaCap)
        cargos = Cargos.objects.get(cargoscapacitacion=obj.idCargo)

        return {
            'id_car_cap'    :   cargoscapacitacion.idCarCap,
            'id_cargo_fk'    :   {
                        'area'  :   areacapacitacion.area,
                        'descripcion'   :   areacapacitacion.descripcion
            },
            'cargo_area_fk'     :   {
                    'cargos'    :   cargos.cargo
            }
        }
