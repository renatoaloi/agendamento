import os
import requests
import unittest


class FunctionalTestsBase(unittest.TestCase):

    def setUp(self):
        print(f'Test {self.my_name} is up and running!')

    def tearDown(self):
        print(f'Test {self.my_name} is going down!')

    def base_set_up(self, child_name):
        self.my_name = child_name


class HealthFunctionalTests(FunctionalTestsBase):

    def __init__(self, context):
        super().__init__(context)
        super().base_set_up(context)

    def test_if_server_is_up_and_running(self):
        try:
            host = os.environ.get('APP_HOST', 'http://localhost:8000/')
            r = requests.get(f'{host}health-check')
            self.assertTrue(self.is_server_working(r.status_code))
        except Exception as e:
            self.fail(f'Something went badly! Reason: {str(e)}')
    def is_server_working(self, status_code):
        return status_code == 200


class AgendaFunctionalTests(FunctionalTestsBase):

    def __init__(self, context):
        super().__init__(context)
        super().base_set_up(context)
    
    def test_that_will_result_ok(self):
        self.assertTrue(1==1)
    

if __name__ == '__main__':
    unittest.main(warnings='ignore')
