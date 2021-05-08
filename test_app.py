import json
import requests

from faker import Faker


class TestHandlers:

    def test_you(self):
        username = Faker().name()
        response = requests.post('http://127.0.0.1:5000/you', json=dict(username=username))
        assert response.json() == dict(greeting=f'hello {username}')
