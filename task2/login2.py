import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def login():
    responce = requests.post(url=data.get("url_login"),
                             data={"username": data.get("username"), "password": data.get("password")})
    if responce.status_code == 200:
        return responce.json()['token']

def get_post(token):
    print(token)
    responce = requests.post(url=data.get("url_post"),
                             headers={"X-Auth-Token": token},
                             params={"owner": "notMe"})
    print(responce.json())
    return responce.json()

def create_post(token):
    post_data = {
        "title": data.get("title"),
        "description": data.get("description"),
        "content": data.get("content")
    }
    headers = {
        "X-Auth-Token": token
    }
    response = requests.post(data.get("url_post"), headers=headers, data=post_data)
    if response.status_code == 200:
        print("Пост успешно создан")