from rest_framework                                         import generics
from AuthAppEmpleados.serializers.trabajadoresSerializer    import TrabajadoresSerializer
from AuthAppEmpleados.models.trabajadores                   import Trabajadores
from django_filters.rest_framework                          import DjangoFilterBackend
from rest_framework.permissions                             import IsAuthenticated
from rest_framework.authentication                          import TokenAuthentication


class ListAllTrabajadores(generics.ListAPIView):
    serializer_class = TrabajadoresSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cedula']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Trabajadores.objects.all()
        return queryset