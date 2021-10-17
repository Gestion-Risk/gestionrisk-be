from django.urls import path
from AuthAppEmpleados.views.capacitacionesViews import ListCapacitaciones

urlpatterns = [
    path('capacitacion/',   ListCapacitaciones.as_view(), name = 'capacitacion_list'),
]