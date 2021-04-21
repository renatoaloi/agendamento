from django.urls import resolve
from django.test import TestCase
from api.views import health_check_view

class HealthCheck(TestCase):

    def test_site_health_check(self):
        found = resolve('/health-check')
        self.assertEqual(found.func, health_check_view)

