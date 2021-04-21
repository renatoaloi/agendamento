import os
import requests

r = requests.get(os.environ.get('APP_HOST', 'http://localhost:8000/'))

def is_server_working(status_code):
    return status_code == 200

assert is_server_working(r.status_code)
