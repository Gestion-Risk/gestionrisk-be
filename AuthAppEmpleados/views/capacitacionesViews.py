from rest_framework                                         import generics, status
from rest_framework.response                                import Response
from AuthAppEmpleados.serializers.capacitacionSerializer    import CapacitacionSerializer
from AuthAppEmpleados.models.capacitacion                   import Capacitacion
from rest_framework.permissions                             import IsAuthenticated
from django_filters.rest_framework                          import DjangoFilterBackend

class CreateCapacitaciones(generics.CreateAPIView):
    serializer_class = CapacitacionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = CapacitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Capacitacion Creada", status=status.HTTP_201_CREATED)


class DeleteCapacitaciones(generics.DestroyAPIView):
    serializers_class =CapacitacionSerializer
    queryset = Capacitacion.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):    
        return super().destroy(request, *args, **kwargs)


class ListCapacitaciones(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idCapacitacion']
    serializer_class = CapacitacionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Capacitacion.objects.all()
        return queryset


class UpdateCapacitaciones(generics.UpdateAPIView):
    serializer_class = CapacitacionSerializer
    queryset = Capacitacion.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

        