from django.urls import resolve
from django.test import TestCase
from django.core.exceptions import ValidationError

from api.views import health_check_view
from api.models import Especialidade

class HealthCheck(TestCase):

    def test_site_health_check(self):
        found = resolve('/health-check')
        self.assertEqual(found.func, health_check_view)

    def test_models_create_especialidade_with_blank_description(self):
        obj = Especialidade(description="")
        with self.assertRaises(ValidationError):
            obj.save()
            obj.full_clean()
