from django.conf.urls import url, include
from django.urls import path
from api import views

urlpatterns = [
    url(r'^health-check', views.health_check_view, name='health_check'),
    path(r'agenda/', include('api.urls')),
]
