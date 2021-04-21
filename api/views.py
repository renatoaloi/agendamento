from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

def futuramente_verificar_login(*params):
    """ TODO: Verificar login pois o metodo atual retorna a lista toda, sem filtro de paciente """
    pass

@require_GET
def health_check_view(request):
    return JsonResponse(data={})

@require_GET
@futuramente_verificar_login
def agenda_list_view(request):
    return JsonResponse(data=[
        {
            'profissional': '',
            'data': '',
            'hora': '',
            'especialidade': '',
            'crm': ''
        }
    ], safe=False)

@require_POST
@futuramente_verificar_login
def agenda_create_view(request):
    return JsonResponse(data={
        'id': 0,
        'especialidade': '',
        'profissional': '',
        'data': '',
        'hora': ''
    })
