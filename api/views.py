from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

@require_GET
def health_check_view(request):
    return JsonResponse(data={})

@require_GET
def agenda_list_view(request):
    return JsonResponse(data={
        'profissional': '',
        'data': '',
        'hora': '',
        'especialidade': '',
        'crm': ''
    })

@require_POST
def agenda_create_view(request):
    return JsonResponse(data={
        'id': 0,
        'especialidade': '',
        'profissional': '',
        'data': '',
        'hora': ''
    })