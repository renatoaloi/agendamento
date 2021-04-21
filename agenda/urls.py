from django.conf.urls import url
from django.urls import path
from api import views

urlpatterns = [
    url(r'^health-check', views.health_check_view, name='health_check'),
]
