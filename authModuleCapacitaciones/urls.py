"""authModuleCapacitaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls    import path, include
from rest_framework.authtoken   import views
from AuthAppEmpleados   import views as authAppViews



urlpatterns = [
    path('admin/',          admin.site.urls), #use defaul Djando Admin

    path('createuser/',     authAppViews.UserCreateView.as_view()), # create a new user
    path('generate/',       views.ObtainAuthToken.as_view()),

    path('loginuser/',      authAppViews.Login.as_view()), #Login del user
    path('api/1.0/',        include(('AuthAppEmpleados.urls', 'api'))),
    path('logout/',         authAppViews.Logout.as_view()),#Salir de la sesion

    path('createcapacitaciones/', authAppViews.CreateCapacitaciones.as_view()), # Create a new capacitacion
    path('deletecapacitaciones/<int:pk>',   authAppViews.DeleteCapacitaciones.as_view()), #Delete capacitaciones
    path('listcapacitaciones/',             authAppViews.ListCapacitaciones.as_view(), name='list_capa'), #List all capacitaciones
    path('updatecapacitaciones/<int:pk>',           authAppViews.UpdateCapacitaciones.as_view()), #Update all capacitaciones
    
    #path('listonetrabajadores/<int:pk>',    authAppViews.ListFilterTrabajadores.as_view()),#Muestra info por cedula
    path('listalltrabajadores/',            authAppViews.ListAllTrabajadores.as_view()), #Lista todos los trabajdores

    path('createregistros/',    authAppViews.CreateRegistro.as_view()),#Crea registros
    path('listallregistros/',   authAppViews.ListAllRegistro.as_view()),#Lista todos los registro hechos
    #path('listoneregistros/<int:pk>',   authAppViews.ListDetailRegistro.as_view()),#Lista registro especifico
    path('deleteregistros/<int:pk>',    authAppViews.DeleteRegistro.as_view()), #ELimina un registro
    
  
   
]
