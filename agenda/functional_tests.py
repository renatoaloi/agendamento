import os
import requests
import unittest
import datetime as dt

class FunctionalTestsBase(unittest.TestCase):

    def __init__(self, test):
        super().__init__(test)
        self.base_set_up(test)
        self.host = os.environ.get('APP_HOST', 'http://localhost:8000/')

    def setUp(self):
        print(f'Test {self.my_name} is up and running!')

    def tearDown(self):
        print(f'Test {self.my_name} is going down!')

    def base_set_up(self, child_name):
        self.my_name = child_name

    def is_server_working(self, status_code):
        return status_code == 200
    
    def check_if_is_bad_request(self, status_code):
        return status_code == 400


class HealthFunctionalTests(FunctionalTestsBase):

    def __init__(self, test):
        super().__init__(test)

    def test_if_server_is_up_and_running(self):
        try:
            r = requests.get(f'{self.host}health-check')
            self.assertTrue(self.is_server_working(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')


class AgendaFunctionalTests(FunctionalTestsBase):

    def __init__(self, test):
        super().__init__(test)
    
    def test_validate_list_json_response(self):
        try:
            r = requests.get(f'{self.host}agenda/list')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_especialidades_list_json_response(self):
        try:
            r = requests.get(f'{self.host}agenda/especialidades/list')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_especialidades_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_profissionais_list_json_response(self):
        try:
            r = requests.get(f'{self.host}agenda/profissionais/list')
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = r.json()
            for json in json_data:
                self.assertTrue(self.validate_list_profissionais_json_data(json))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
        
    def test_validate_create_json_response(self):
        try:
            json_data = {
                "profissional_id": 2,
                "data": "29/04/2022",
                "hora": dt.datetime.now().strftime("%H:%M")
            }
            r = requests.post(f'{self.host}agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
            self.assertTrue(self.validate_create_json_data(r.json()))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_with_invalid_fields(self):
        try:
            r = requests.post(f'{self.host}agenda/create', json={ 'nada': '' })
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_two_appointments_at_same_time(self):
        try:
            hora = dt.datetime.now().strftime("%H:%M")
            json_data = {
                "profissional_id": 2,
                "data": "23/05/2022",
                "hora": hora
            }
            r = requests.post(f'{self.host}agenda/create', json=json_data)
            self.assertTrue(self.is_server_working(r.status_code))
            json_data = {
                "profissional_id": 2,
                "data": "23/05/2022",
                "hora": hora
            }
            r = requests.post(f'{self.host}agenda/create', json=json_data)
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    
    def test_validate_create_with_date_before_today(self):
        try:
            json_data = {
                "profissional_id": 2,
                "data": "23/09/1999",
                "hora": dt.datetime.now().strftime("%H:%M")
            }
            r = requests.post(f'{self.host}agenda/create', json=json_data)
            self.assertTrue(self.check_if_is_bad_request(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')

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


if __name__ == '__main__':
    unittest.main(warnings='ignore')
