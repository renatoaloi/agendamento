import json
from django.utils import timezone as dt

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_GET

from api.models import Agenda


def futuramente_verificar_login(func):
    """ TODO: Verificar login pois o metodo atual retorna a lista toda, sem filtro de paciente """
    return func


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
    if 'profissional_id' not in json_body or \
        'data' not in json_body or \
        'hora' not in json_body:

        return HttpResponseBadRequest(content={})
    novo_agendamento = Agenda()
    novo_agendamento.profissional_id = json_body['profissional_id']
    novo_agendamento.data_hora = dt.now()
    novo_agendamento.save()
    return JsonResponse(data={
        'id': 0,
        'especialidade': '',
        'profissional': '',
        'data': '',
        'hora': ''
    })
