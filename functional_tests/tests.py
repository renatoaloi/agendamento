import os
import requests
import unittest
import datetime as dt

from django.test import LiveServerTestCase

from api.models import Profissional, Especialidade

class FunctionalTestsBase(LiveServerTestCase):

    def setUp(self):
        staging_server = os.environ.get('STAGING_SERVER', False)
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def is_server_working(self, status_code):
        return status_code == 200
    
    def check_if_is_bad_request(self, status_code):
        return status_code == 400


class HealthFunctionalTests(FunctionalTestsBase):

    def test_if_server_is_up_and_running(self):
        try:
            r = requests.get(f'{self.live_server_url}/health-check')
            self.assertTrue(self.is_server_working(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')


class AgendaFunctionalTests(FunctionalTestsBase):
    
    def test_validate_list_json_response(self):
        try:
            r = requests.get(f'{self.live_server_url}/agenda/list')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_especialidades_list_json_response(self):
        try:
            r = requests.get(f'{self.live_server_url}/agenda/especialidades/list')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_especialidades_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_profissionais_list_json_response(self):
        try:
            id = self.load_temp_data_and_get_profissional_id()
            r = requests.get(f'{self.live_server_url}/agenda/profissionais/find-by-especialidade/{id}')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_profissionais_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
        
    def test_validate_create_json_response(self):
        try:
            json_data = {
                "profissional_id": self.load_temp_data_and_get_profissional_id(),
                "data": "29/04/2022",
                "hora": dt.datetime.now().strftime("%H:%M")
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
            self.assertTrue(self.validate_create_json_data(r.json()))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_with_invalid_fields(self):
        try:
            r = requests.post(f'{self.live_server_url}/agenda/create', json={ 'nada': '' })
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_two_appointments_at_same_time(self):
        try:
            profissional_id = self.load_temp_data_and_get_profissional_id()
            hora = dt.datetime.now().strftime("%H:%M")
            json_data = {
                "profissional_id": profissional_id,
                "data": "23/05/2022",
                "hora": hora
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = {
                "profissional_id": profissional_id,
                "data": "23/05/2022",
                "hora": hora
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_two_appointments_at_same_time_but_two_different_proffesionals(self):
        try:
            profissional_id = self.load_temp_data_and_get_profissional_id()
            other_profissional_id = self.load_temp_data_and_get_profissional_id()
            hora = dt.datetime.now().strftime("%H:%M")
            json_data = {
                "profissional_id": profissional_id,
                "data": "24/06/2022",
                "hora": hora
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = {
                "profissional_id": other_profissional_id,
                "data": "24/06/2022",
                "hora": hora
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_with_date_before_today(self):
        try:
            json_data = {
                "profissional_id": self.load_temp_data_and_get_profissional_id(),
                "data": "23/09/1999",
                "hora": dt.datetime.now().strftime("%H:%M")
            }
            r = requests.post(f'{self.live_server_url}/agenda/create', json=json_data)
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')

    def load_temp_data_and_get_profissional_id(self):
        e = Especialidade()
        e.description = "Teste"
        e.save()
        p = Profissional()
        p.name = "Teste"
        p.crm = "1234"
        p.especialidade = e
        p.save()
        return p.id

    def validate_list_especialidades_json_data(self, json_data):
        return 'id' in json_data and \
               'description' in json_data
    
    def validate_list_profissionais_json_data(self, json_data):
        return 'id' in json_data and \
               'name' in json_data and \
               'crm' in json_data and \
               'especialidade' in json_data

    def validate_list_json_data(self, json_data):
        return 'profissional' in json_data and \
               'data' in json_data and \
               'hora' in json_data and \
               'especialidade' in json_data and \
               'crm' in json_data
    
    def validate_create_json_data(self, json_data):
        return 'id' in json_data and \
               'especialidade' in json_data and \
               'profissional' in json_data and \
               'data' in json_data and \
               'hora' in json_data
