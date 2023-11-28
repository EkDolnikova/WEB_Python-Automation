import requests
import pytest

url = 'https://test-stand.gb.ru/gateway/login'
login = 'Sidorova95'
password = '835a0fde40'

result = requests.post(url=url, data={'username': login, 'password': password})
token = result.json()['token']
res_get = requests.get(url= 'https://test-stand.gb.ru/api/posts',
                       headers={"X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get)
print(res_get.json())