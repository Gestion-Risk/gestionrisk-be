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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('admin/',          admin.site.urls), #use defaul Djando Admin

    path('login/',          TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',        TokenRefreshView.as_view()), # generate new access token

    path('createuser/',     authAppViews.UserCreateView.as_view()), # create a new user
    
    path('createcapacitaciones/', authAppViews.CreateCapacitaciones.as_view()), # Create a new capacitacion
    path('deletecapacitaciones/<int:pk>',   authAppViews.DeleteCapacitaciones.as_view()), #Delete capacitaciones
    path('listcapacitaciones/',             authAppViews.ListCapacitaciones.as_view()), #List all capacitaciones
    path('updatecapacitaciones/<int:pk>',           authAppViews.UpdateCapacitaciones.as_view()), #Update all capacitaciones

    path('listalltrabajadores/',            authAppViews.ListAllTrabajadores.as_view()), #Lista todos los trabajdores

    path('listareas/',              authAppViews.ListAreas.as_view()), #lista areas disponibles

    path('createregistros/',    authAppViews.CreateRegistro.as_view()),#Crea registros
    path('listallregistros/',   authAppViews.ListAllRegistro.as_view()),#Lista todos los registro hechos
    path('deleteregistros/<int:pk>',    authAppViews.DeleteRegistro.as_view()), #ELimina un registro
    
  
   
]
