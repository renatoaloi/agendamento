import datetime as dt
import pytz

from django.utils import timezone
from django.urls import resolve
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from api.views import health_check_view
from api.models import Especialidade, Profissional, Agenda


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
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        obj = Profissional(
            name="", 
            crm=self._generate_4_digits_string(), 
            especialidade=especialidade_
        )
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_blank_crm(self):
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        obj = Profissional(
            name=self._generate_dummy_description(), 
            crm="", 
            especialidade=especialidade_
        )
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_blank_especialidade(self):
        obj = Profissional(
            name=self._generate_dummy_description(), 
            crm=self._generate_4_digits_string(), 
            especialidade=None
        )
        with self.assertRaises(IntegrityError):
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_too_long_name(self):
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        obj = Profissional(
            name=self._text_greather_than_200_chars(), 
            crm=self._generate_4_digits_string(), 
            especialidade=especialidade_
        )
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_profissional_with_too_long_crm(self):
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        obj = Profissional(
            name=self._generate_dummy_description(), 
            crm=self._text_greather_than_50_chars(), 
            especialidade=especialidade_
        )
        with self.assertRaises(ValidationError):
            especialidade_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_agenda_with_blank_profissional(self):
        obj = Agenda(profissional=None, data_hora=timezone.now())
        with self.assertRaises(IntegrityError):
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_agenda_with_null_date_time(self):
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        profissional_ = Profissional(
            name=self._generate_dummy_description(), 
            crm=self._generate_4_digits_string(), 
            especialidade=especialidade_
        )
        obj = Agenda(profissional=profissional_, data_hora=None)
        with self.assertRaises(IntegrityError):
            especialidade_.save()
            profissional_.save()
            obj.save()
            obj.full_clean()
    
    def test_models_validate_create_agenda_with_invalid_date_time(self):
        especialidade_ = Especialidade(description=self._generate_dummy_description())
        profissional_ = Profissional(
            name=self._generate_dummy_description(), 
            crm=self._generate_4_digits_string(), 
            especialidade=especialidade_
        )
        obj = Agenda(
            profissional=profissional_, 
            data_hora=self._generate_magic_invalid_date()
        )
        with self.assertRaises(ValidationError):
            especialidade_.save()
            profissional_.save()
            obj.save()
            obj.full_clean()

    def _generate_4_digits_string(self):
        return "1234"

    def _generate_dummy_description(self):
        return "dummy"
    
    def _generate_magic_invalid_date(self):
        return '2020-13-32 25:55:69'

    def _text_greather_than_200_chars(self):
        return self._text_greather_than_N_chars(200)
    
    def _text_greather_than_50_chars(self):
        return self._text_greather_than_N_chars(50)
    
    def _text_greather_than_N_chars(self, N):
        return "-" * N + "-"

class RestCheck(TestCase):

    def test_fetch_agenda_list(self):
        found = resolve('/health-check')
        self.assertEqual(found.func, health_check_view)