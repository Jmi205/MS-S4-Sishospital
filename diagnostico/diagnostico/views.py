from .models import Diagnostico
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_paciente(data):
    r = requests.get(settings.PATH_PAC, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if data["paciente"] == paciente["id"]:
            data["paciente"]= paciente["apellido"] + " " + paciente["nombre"]
            return True
    return False

def diagnosticoList(request):
    queryset = Diagnostico.objects.all()
    context = []

    for evento in queryset:
        context.append({
            'id': evento.id,
            'fechaDiagnostico': evento.fechaDiagnostico,
            'descripcion': evento.descripcion,
            'recomendaciones': evento.recomendaciones,
            'paciente': evento.paciente,
        })

    return JsonResponse(context, safe=False)

def diagnosticoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_paciente(data_json):
            diagnostico = Diagnostico()
            diagnostico.fechaDiagnostico = data_json['fechaDiagnostico']
            diagnostico.descripcion = data_json['descripcion']
            diagnostico.recomendaciones = data_json['recomendaciones']
            diagnostico.paciente = data_json['paciente']
            diagnostico.save()
            return HttpResponse("successfully created Diagnostico")
        else:
            return HttpResponse("unsuccessfully created Diagnostico. Paciente does not exist")

def diagnosticosCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        diagnostico_list = []
        for diagnostico in data_json:
                    if check_paciente(diagnostico) == True:
                        db_diagnostico = Diagnostico()
                        db_diagnostico.fechaDiagnostico = diagnostico['fechaDiagnostico']
                        db_diagnostico.descripcion = diagnostico['descripcion']
                        db_diagnostico.recomendaciones = diagnostico['recomendaciones']
                        db_diagnostico.paciente = diagnostico['paciente']
                        diagnostico_list.append(db_diagnostico)
                    else:
                        return HttpResponse("unsuccessfully created Diagnostico. Paciente does not exist")
        
        Diagnostico.objects.bulk_create(diagnostico_list)
        return HttpResponse("successfully created Diagnostico")
