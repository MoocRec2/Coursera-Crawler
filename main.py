import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import json
from json import JSONDecodeError
# from db_connector import Thread
from pprint import pprint
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

try:
    with open('./credentials.json') as json_file:
        credentials = json.load(json_file)
        email = credentials['coursera']['email']
        password = credentials['coursera']['password']
except FileNotFoundError:
    print('Credentials File Missing')
    email = input('Email: ')
    password = input('Password: ')

driver = webdriver.Chrome('C:/chromedriver', options=options)

driver.get('https://www.coursera.org/?authMode=login')

email_input = driver.find_element_by_name('email')
password_input = driver.find_element_by_name('password')

email_input.send_keys(email)
password_input.send_keys(password)

login_form = driver.find_element_by_tag_name('form')
buttons = login_form.find_elements_by_tag_name(('button'))

count = 0
for btn in buttons:
    count += 1

print('Count', count)
# login_btn = login_form.find_element_by_tag_name('button')

while True:
    try:
        buttons[1].click()
        break
    except:
        time.sleep(1)

time.sleep(10)

driver.quit()
