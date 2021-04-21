from django.urls import resolve
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from api.views import health_check_view
from api.models import Especialidade, Profissional

class HealthCheck(TestCase):

    def test_site_health_check(self):
        found = resolve('/health-check')
        self.assertEqual(found.func, health_check_view)

    def test_models_validate_create_especialidade_with_blank_description(self):
        obj = Especialidade(description="")
        with self.assertRaises(ValidationError):
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_especialidade_with_too_long_text(self):
        obj = Especialidade(description=self._text_greather_than_200_chars())
        with self.assertRaises(ValidationError):
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_blank_name(self):
        especialidade_ = Especialidade(description="Teste")
        obj = Profissional(name="", crm="1234", especialidade=especialidade_)
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_blank_crm(self):
        especialidade_ = Especialidade(description="Teste")
        obj = Profissional(name="Jose", crm="", especialidade=especialidade_)
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_blank_especialidade(self):
        obj = Profissional(name="Jose", crm="1234", especialidade=None)
        with self.assertRaises(IntegrityError):
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_too_long_name(self):
        especialidade_ = Especialidade(description="Teste")
        obj = Profissional(name=self._text_greather_than_200_chars(), crm="1234", especialidade=especialidade_)
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_too_long_crm(self):
        especialidade_ = Especialidade(description="Teste")
        obj = Profissional(name="Jose", crm=self._text_greather_than_50_chars(), especialidade=especialidade_)
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()

    def _text_greather_than_200_chars(self):
        return self._text_greather_than_N_chars(200)
    
    def _text_greather_than_50_chars(self):
        return self._text_greather_than_N_chars(50)
    
    def _text_greather_than_N_chars(self, N):
        return "-" * N + "-"