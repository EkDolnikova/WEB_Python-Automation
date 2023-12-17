import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import sendemail
import requests


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    # инициализация firefox
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    # инициализация chrome
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
    sendemail()


# browser = testdata['browser']
# name = testdata['login']
# passwd = testdata['password']


# API

# @pytest.fixture()
# def login():
#     r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': name, 'password': passwd})
#     return r.json()['token']
#
#
# @pytest.fixture()
# def not_my_post():
#     return ' '
#
#
# @pytest.fixture()
# def my_post():
#     return ' '

