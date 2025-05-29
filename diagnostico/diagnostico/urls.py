from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^diagnosticos/', views.diagnosticoList),
    url(r'^diagnosticocreate/$', csrf_exempt(views.diagnosticoCreate), name='diagnosticoCreate'),
    url(r'^creatediagnosticos/$', csrf_exempt(views.diagnosticosCreate), name='createDiagnosticos'),
]