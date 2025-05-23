from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path(r'pacientes/', views.paciente_list, name='pacienteList'),
    path(r'pacientecreate/$', csrf_exempt(views.paciente_create), name='pacienteCreate'),    
]