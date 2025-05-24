from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^pacientes/', views.paciente_list, name='pacienteList'),
    url(r'^pacientecreate/$', csrf_exempt(views.paciente_create), name='pacienteCreate'),    
]