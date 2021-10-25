from rest_framework                                     import generics, status
from rest_framework.response                            import Response
from AuthAppEmpleados.serializers.registroSerializer    import RegistroSerializer
from AuthAppEmpleados.models.registro                   import Registro
from django_filters.rest_framework                      import DjangoFilterBackend
from rest_framework.permissions                         import IsAuthenticated
from rest_framework.authentication                      import TokenAuthentication


class ListAllRegistro(generics.ListAPIView):
    serializer_class= RegistroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cedulaTrabajador', 'idRegistro'] 
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        queryset = Registro.objects.all()
        return queryset


class ListDetailRegistro(generics.RetrieveAPIView):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DeleteRegistro(generics.DestroyAPIView):
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CreateRegistro(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Registro generado", status=status.HTTP_201_CREATED)






    