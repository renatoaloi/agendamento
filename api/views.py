import json
import datetime as dt

from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET

from api.models import Agenda


def futuramente_verificar_login(func):
    """ TODO: Verificar login pois o metodo atual retorna a lista toda, sem filtro de paciente """
    return func


def _is_data_invalida(data):
    try:
        dt.datetime.strptime(data, "%d/%m/%Y")
        return False
    except:
        return True


def _is_hora_invalida(hora):
    try:
        dt.datetime.strptime(hora, "%H:%M")
        return False
    except:
        return True


def _check_if_is_bad_request(json_body):
    # formato data = DD/MM/YYYY
    # formato hora = HH:MM
    return 'profissional_id' not in json_body or \
            'data' not in json_body or \
            'hora' not in json_body or \
            _is_data_invalida(json_body['data']) or \
            _is_hora_invalida(json_body['hora'])


def _create_agendamento(json_body):
    novo_agendamento = Agenda()
    novo_agendamento.profissional_id = json_body['profissional_id']
    json_data = json_body['data']
    json_hora = json_body['hora']
    dt_naive = dt.datetime.strptime(f'{json_data} {json_hora}:00', '%d/%m/%Y %H:%M:%S')
    dt_aware = timezone.make_aware(dt_naive)
    novo_agendamento.data_hora = dt_aware
    novo_agendamento.save()


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
                'profissional': '',
                'data': '',
                'hora': '',
                'especialidade': '',
                'crm': ''
            }
        )
    return JsonResponse(data=json_de_retorno, safe=False)


@require_POST
@futuramente_verificar_login
def agenda_create_view(request):
    json_body = json.loads(request.body)

    if _check_if_is_bad_request(json_body):
        return HttpResponseBadRequest(content={})

    _create_agendamento(json_body)

    return JsonResponse(data={
        'id': 0,
        'especialidade': '',
        'profissional': '',
        'data': '',
        'hora': ''
    })
