import pytest
import yaml
import requests
import pytest

with open('config.yaml') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()

@pytest.fixture()
def user_login():
    rest1 = S.post(url=address, data={'username' : username, 'password' : password})
    return rest1.json()['token']
