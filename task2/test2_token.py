import yaml
import requests


with open('config.yaml') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()

def user_login():
    rest1 = S.post(url=address, data={'username': username, 'password': password})
    return rest1.json()['token']

print(user_login())