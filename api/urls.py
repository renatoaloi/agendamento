from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from api import views

urlpatterns = [
    path(r'list', views.agenda_list_view),
    path(r'create', csrf_exempt(views.agenda_create_view)),
    path(r'especialidades/list', views.especialidades_list_view),
    path(r'profissionais/find-by-especialidade/<id>', views.profissionais_find_by_especialidade_view),
    
]
