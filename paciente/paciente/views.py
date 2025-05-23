from .models import Paciente
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json
    
def paciente_list(request):
    queryset = Paciente.objects.all()
    context = list(queryset.values('id', 'nombre', 'apellido', 'tipoSangre', 'alergias', 'condicionesMedicas', 'fechaNacimiento', 'historiaClinica'))
    return JsonResponse(context, safe=False)

def paciente_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        paciente = Paciente()
        paciente.name = data_json["nombre"]
        paciente.apellido = data_json["apellido"]
        paciente.tipoSangre = data_json["tipoSangre"]
        paciente.alergias = data_json["alergias"]
        paciente.condicionesMedicas = data_json["condicionesMedicas"]
        paciente.fechaNacimiento = data_json["fechaNacimiento"]
        paciente.historiaClinica = data_json["historiaClinica"]
        paciente.save()
        return HttpResponse("successfully created paciente")
