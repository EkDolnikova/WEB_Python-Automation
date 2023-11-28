
import yaml
import requests


with open('config.yaml') as f:
    data = yaml.safe_load(f)
    address = data['address2']


S = requests.Session()

#получение поста
def test_rest(user_login):
    print(S.get(url=address, headers={'X-Auth-Token': user_login}).json())

#отправка поста
def test_post(user_login):
    print(S.post(url=address, headers={'X-Auth-Token': user_login},
                 data = {'title': data['title'],
                         'description': data['description'],
                         'content': data['content']}).json())