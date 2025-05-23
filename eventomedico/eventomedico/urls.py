from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^eventosmedicos/', views.eventomedicoList),
    url(r'^eventomedicocreate/$', csrf_exempt(views.eventomedicoCreate), name='eventomedicoCreate'),
    url(r'^createeventosmedicos/$', csrf_exempt(views.eventosmedicosCreate), name='createEventosmedicos'),
]