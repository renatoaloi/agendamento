from django.test import TestCase

class HealthCheck(TestCase):

    def test_site_health_check(self):
        self.fail('Health check terminated!')

