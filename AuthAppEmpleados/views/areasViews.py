from rest_framework                                             import generics, status
from AuthAppEmpleados.serializers.areaCapacitacionesSerializer  import AreaCapacitacionesSerliazer
from AuthAppEmpleados.models.areaCapacitacion                   import AreaCapacitacion
from rest_framework.permissions                                 import IsAuthenticated


class ListAreas(generics.ListAPIView):
    serializer_class = AreaCapacitacionesSerliazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = AreaCapacitacion.objects.all()
        return queryset