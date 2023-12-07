import yaml
import time
import random, string

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata['address'])

def test_step1(site, login_xpath, pswd_xpath, btn_xpath, result_xpath):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys('test')
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys('test')
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    err_label = site.find_element('xpath', result_xpath)
    assert err_label.text == '401'



def test_step2(site, login_xpath, pswd_xpath, btn_xpath, result_success):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys(testdata['password'])
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    login = site.find_element('xpath', result_success)
    assert login.text == 'Blog'


# ДЗ№2
def test_step3(site, login_xpath, pswd_xpath, btn_xpath, btn_create_post,
               btn_save_post, tittle_post_xpath, description_post_xpath,
               content_post_xpath, tittle_save_post):
    input1 = site.find_element('xpath', login_xpath)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', pswd_xpath)
    input2.send_keys(testdata['password'])
    btn = site.find_element('xpath', btn_xpath)
    btn.click()
    time.sleep(testdata['sleep_time'])
    btn_create = site.find_element('xpath', btn_create_post)
    btn_create.click()
    time.sleep(testdata['sleep_time'])
    input1 = site.find_element('xpath', tittle_post_xpath)
    input1.send_keys('Selenium')
    input2 = site.find_element('xpath', description_post_xpath)
    input2.send_keys('12345')
    input2 = site.find_element('xpath', content_post_xpath)
    input2.send_keys("".join(random.choices(string.ascii_lowercase + string.digits, k=300)))
    btn_post = site.find_element('xpath', btn_save_post)
    btn_post.click()
    time.sleep(testdata['sleep_time'])
    result = site.find_element('xpath', tittle_save_post)
    assert result.text == 'Selenium'

