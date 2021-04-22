import json
import datetime as dt

from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET

from api.models import Agenda
from api.utils import *

@require_GET
def health_check_view(request):
    return JsonResponse(data={})


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


def check_if_agenda_already_exists(json_body):
    data_hora = dt.datetime.now()
    jbd = json_body['data']
    jbh = json_body['hora']
    s = f'{jbd} {jbh}:00'
    try:
        data_hora = dt.datetime.strptime(s, '%d/%m/%Y %H:%M:%S')
    except:
        return None
    agenda_existente = Agenda.objects.filter(data_hora=data_hora.strftime('%Y-%m-%d %H:%M:%S')).first()
    return agenda_existente

def check_if_date_is_from_before_than_today(json_body):
    data_hora_hoje = dt.datetime.now()
    jbd = json_body['data']
    jbh = json_body['hora']
    s = f'{jbd} {jbh}:00'
    try:
        data_hora = dt.datetime.strptime(s, '%d/%m/%Y %H:%M:%S')
        difference_in_days = (data_hora - data_hora_hoje).days
        return difference_in_days < 0
    except:
        pass
    return False

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
