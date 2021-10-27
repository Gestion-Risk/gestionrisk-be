from AuthAppEmpleados.models.areaCapacitacion   import AreaCapacitacion
from rest_framework                             import serializers

class AreaCapacitacionesSerliazer(serializers.ModelSerializer):
    class Meta:
        model = AreaCapacitacion
        fields = ['idAreaCap','area','descripcion']

        def to_representation(self, obj):
            areacapacitacion = AreaCapacitacion.objects.get(id=obj.idAreaCap)
        
            return{
                        'idAreaCap'             :   areacapacitacion.idAreaCap,
                        'area'                  :   areacapacitacion.area,
                        'descripcion'           :   areacapacitacion.descripcion
                }
            