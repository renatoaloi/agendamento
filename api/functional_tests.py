import os
import requests
import unittest

class AgendaFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.my_name = self._get_test_name_from_a_very_long_string(self.__str__)
        print(f"Test {self.my_name} up and running!")

    def tearDown(self):
        print(f"Test {self.my_name} going down!")

    def test_if_server_is_up_and_running(self):
        try:
            r = requests.get(os.environ.get('APP_HOST', 'http://localhost:8000/'))
            self.assertTrue(self.is_server_working(r.status_code))
        except Exception as e:
            self.fail(f"Something went badly! Reason: {str(e)}")

    def is_server_working(self, status_code):
        return status_code == 200
    
    def _get_test_name_from_a_very_long_string(self, string_to_deal_with):
        if not '__main__.' in str(string_to_deal_with):
            return 'No test name found'
        return str(string_to_deal_with).split('__main__.')[1].split(' ')[0]

if __name__ == '__main__':
    unittest.main(warnings='ignore')
