from AuthAppEmpleados.models.capacitacion                       import Capacitacion
from AuthAppEmpleados.models.areaCapacitacion                   import AreaCapacitacion
from AuthAppEmpleados.serializers.areaCapacitacionesSerializer  import AreaCapacitacionesSerliazer
from rest_framework                                             import serializers

class CapacitacionSerializer(serializers.ModelSerializer):
    areacapacitacion = AreaCapacitacionesSerliazer
    class Meta:
        model = Capacitacion
        fields = ['curso','idAreaCapacitacionFk','fecha', 'hora']
        
    def create(self, validated_data):
        userInstance = Capacitacion.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        capacitacion = Capacitacion.objects.get(idCapacitacion=obj.idCapacitacion)
        areacapacitacion = AreaCapacitacion.objects.get(idAreaCap=obj.idAreaCapacitacionFk_id)
        return{
            'id_capacitacion'   :   capacitacion.idCapacitacion,
            'curso'             :   capacitacion.curso,
            'fecha'             :   capacitacion.fecha,
            'hora'              :   capacitacion.hora,
            'idAreaCapacitacionFk_id'  : {
                    'area'  :   areacapacitacion.area,
                    'descripcion'   :   areacapacitacion.descripcion
            }
        }