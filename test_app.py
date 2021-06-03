import json
import requests

from hypothesis import given, strategies as st


class TestHandlers:

    @given(username=st.text())
    def test_hp_you(self, username):
        response = requests.post('http://127.0.0.1:5000/you', json=dict(username=username))
        assert response.json() == dict(greeting=f'hello {username}')
