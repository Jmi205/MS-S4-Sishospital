from .models import Paciente
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
import json
import requests
    
def paciente_list(request):
    queryset = Paciente.objects.all()
    context = list(queryset.values('id', 'nombre', 'apellido', 'tipoSangre', 'alergias', 'condicionesMedicas', 'fechaNacimiento', 'historiaClinica'))
    return JsonResponse(context, safe=False)

def paciente_create(request):
    if request.method == 'POST':
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            if check_paciente(data_json):
                paciente = Paciente()
                paciente.nombre = data_json["nombre"]
                paciente.apellido = data_json["apellido"]
                paciente.tipoSangre = data_json["tipoSangre"]
                paciente.alergias = data_json["alergias"]
                paciente.condicionesMedicas = data_json["condicionesMedicas"]
                paciente.fechaNacimiento = data_json["fechaNacimiento"]
                paciente.historiaClinica = data_json["historiaClinica"]
                paciente.save()
                return HttpResponse("successfully created paciente")
        

def check_paciente(data):
    r = requests.get(settings.PATH_HC, headers={"Accept":"application/json"})
    historiasC = r.json()
    print(historiasC)
    print(data)
    for historia in historiasC["historiasClinicas"]:
        if data["historiaClinica"] == historia["code"]:
            return True
    return False

