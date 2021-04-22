import json
import datetime as dt

from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET

from api.models import Agenda, Especialidade, Profissional
from api.utils import *


@require_GET
def health_check_view(request):
    return JsonResponse(data={})


@require_GET
@futuramente_verificar_login
def especialidades_list_view(request):
    json_de_retorno = []
    especialidades = Especialidade.objects.all()
    for especialidade in especialidades:
        json_de_retorno.append(
            {
                'id': especialidade.id,
                'description': especialidade.description
            }
        )
    return JsonResponse(data=json_de_retorno, safe=False)

@require_GET
@futuramente_verificar_login
def profissionais_find_by_especialidade_view(request, id):
    json_de_retorno = []
    especialidade = Especialidade.objects.filter(id=id).first()
    if especialidade:
        profissionais = Profissional.objects.filter(especialidade=especialidade)
        for profissional in profissionais:
            json_de_retorno.append(
                {
                    'id': profissional.id,
                    'name': profissional.name,
                    'crm': profissional.crm,
                    'especialidade': profissional.especialidade.description
                }
            )
    return JsonResponse(data=json_de_retorno, safe=False)

@require_GET
@futuramente_verificar_login
def agenda_list_view(request):
    json_de_retorno = []
    agendas = Agenda.objects.all()
    for agenda in agendas:
        json_de_retorno.append(
            {
                'profissional': agenda.profissional.name,
                'data': agenda.data_hora.strftime('%d/%m/%Y'),
                'hora': agenda.data_hora.strftime('%H:%M'),
                'especialidade': agenda.profissional.especialidade.description,
                'crm': agenda.profissional.crm
            }
        )
    return JsonResponse(data=json_de_retorno, safe=False)


@require_POST
@futuramente_verificar_login
def agenda_create_view(request):
    json_body = json.loads(request.body)

    if check_if_is_bad_request(json_body):
        return HttpResponseBadRequest(content={ 'error': 'Bad fields at request!' })

    if check_if_agenda_already_exists(json_body):
        return HttpResponseBadRequest(content={ 'error': 'Appointment already exists!' })
    
    if check_if_date_is_from_before_than_today(json_body):
        return HttpResponseBadRequest(content={ 'error': 'Date before today!' })

    agenda = create_agendamento(json_body)

    return JsonResponse(data={
        'id': agenda.id,
        'especialidade': agenda.profissional.especialidade.description,
        'profissional': agenda.profissional.name,
        'data': agenda.data_hora.strftime('%d/%m/%Y'),
        'hora': agenda.data_hora.strftime('%H:%M')
    })
