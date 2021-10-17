from AuthAppEmpleados.models.cargos         import Cargos
from rest_framework                         import serializers


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = ['cargo']
 
    def to_representation(self, obj):
        cargos = Cargos.objects.get(idCargo=obj.idCargo)
        return {
            'idCargo': cargos.idCargo,
            'cargo':   cargos.cargo
        }
