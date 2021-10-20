from rest_framework                             import serializers

from AuthAppEmpleados.models.registro           import Registro
from AuthAppEmpleados.models.capacitacion       import Capacitacion
from AuthAppEmpleados.models.cargos             import Cargos
from AuthAppEmpleados.models.areaCapacitacion   import AreaCapacitacion
from AuthAppEmpleados.models.trabajadores       import Trabajadores

from AuthAppEmpleados.serializers.capacitacionSerializer        import CapacitacionSerializer
from AuthAppEmpleados.serializers.cargosSerializer              import CargosSerializer
from AuthAppEmpleados.serializers.areaCapacitacionesSerializer  import AreaCapacitacionesSerliazer
from AuthAppEmpleados.serializers.trabajadoresSerializer        import TrabajadoresSerializer


class RegistroSerializer(serializers.ModelSerializer):
    capacitaciones = CapacitacionSerializer
    Cargos      = CargosSerializer
    areacapacitacion = AreaCapacitacionesSerliazer
    trabajadores = TrabajadoresSerializer

    class Meta:
        model = Registro
        fields = ['idCapacitacionFk', 'cedulaTrabajador']
        
    def to_representation(self, obj):
        registro = Registro.objects.get(idRegistro=obj.idRegistro)
        capacitacion = Capacitacion.objects.get(idCapacitacion=obj.idCapacitacionFk_id)
        trabajador = Trabajadores.objects.get(cedula=obj.cedulaTrabajador_id)
        cargos = Cargos.objects.get(idCargo=trabajador.cargoIdFk_id)
        areacapacitacion = AreaCapacitacion.objects.get(idAreaCap=capacitacion.idAreaCapacitacionFk_id)
    
        return{
            'idRegistro'   :   registro.idRegistro,
            'cedulaTrabajador' :  registro.cedulaTrabajador_id,
            'cedulaTrabajadorFk' :   {
                        'cedula'    :   trabajador.cedula,
                        'nombres'   :   trabajador.nombres,
                        'apellidos' :   trabajador.apellidos,
                        'email'     :   trabajador.email,
                        'cargoIdFk'   :   {
                                'cargo'     :   cargos.cargo
                        }
            },
            'idCapacitacionFk'    :   {
                        'curso'     :   capacitacion.curso,
                        'fecha'     :   capacitacion.fecha,
                        'hora'      :   capacitacion.hora, 
                        'idAreaCapacitacionFk'    :   {
                            'area'  :   areacapacitacion.area,
                            'descripcion'   :   areacapacitacion.descripcion
                        }
            }            
        } 
        


