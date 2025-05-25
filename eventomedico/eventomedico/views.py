from .models import Eventomedico
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

def check_HC_id(data):
    r = requests.get(settings.PATH_PLACES, headers={"Accept":"application/json"})
    historiasClinicas = r.json()
    for hc in historiasClinicas:
        if True:
           return -1
    return -1

def eventomedicoList(request):
    queryset = Eventomedico.objects.all()
    context = []

    for evento in queryset:
        context.append({
            'id': evento.id,
            'fechaEvento': evento.fechaEvento,
            'descripcion': evento.descripcion,
            'paciente': evento.paciente,
            'tipoEvento': evento.get_tipoEvento_display(), 
        })

    return JsonResponse(context, safe=False)

def eventomedicoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_paciente(data_json):
            eventomedico = Eventomedico()
            eventomedico.fechaEvento = data_json['fechaEvento']
            eventomedico.descripcion = data_json['descripcion']
            eventomedico.tipoEvento = data_json['tipoEvento']
            eventomedico.paciente = data_json['paciente']
            eventomedico.save()
            return HttpResponse("successfully created Evento Medico")
        else:
            return HttpResponse("unsuccessfully created Evento Medico. Paciente or Historia Clinica does not exist")

def eventosmedicosCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        eventomedico_list = []
        for eventomedico in data_json:
                    if check_paciente(eventomedico) == True:
                        db_eventomedico = Eventomedico()
                        eventomedico = Eventomedico()
                        eventomedico.fechaEvento = data_json['fechaEvento']
                        eventomedico.descripcion = data_json['descripcion']
                        eventomedico.tipoEvento = data_json['tipoEvento']
                        eventomedico.paciente = data_json['paciente']
                        eventomedico_list.append(db_eventomedico)
                    else:
                        return HttpResponse("unsuccessfully created Evento Medico. Paciente or Historia Clinica does not exist")
        
        Eventomedico.objects.bulk_create(eventomedico_list)
        return HttpResponse("successfully created EventoMedico")
