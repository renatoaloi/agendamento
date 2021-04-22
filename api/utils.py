import datetime as dt

from django.utils import timezone

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


def check_if_is_bad_request(json_body):
    # formato data = DD/MM/YYYY
    # formato hora = HH:MM
    return 'profissional_id' not in json_body or \
            'data' not in json_body or \
            'hora' not in json_body or \
            _is_data_invalida(json_body['data']) or \
            _is_hora_invalida(json_body['hora'])


def create_agendamento(json_body):
    novo_agendamento = Agenda()
    novo_agendamento.profissional_id = json_body['profissional_id']
    json_data = json_body['data']
    json_hora = json_body['hora']
    dt_naive = dt.datetime.strptime(f'{json_data} {json_hora}:00', '%d/%m/%Y %H:%M:%S')
    dt_aware = timezone.make_aware(dt_naive)
    novo_agendamento.data_hora = dt_aware
    novo_agendamento.save()
    return novo_agendamento


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