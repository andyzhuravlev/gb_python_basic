#
# from time import time, sleep
# import datetime
#
#
# start = time()
# for itm in range(10):
#     print(itm)
#     sleep(2)
# end = time()
#
# print(end - start)

# сетевое взаимодействие
# import requests
#
#
# response = requests.get('https://geekbrains.ru')
#
# print(response.text)


import _json
import json

import requests
from requests.auth import HTTPBasicAuth
import _json

status_codes = {401: 'Не авторизован',
                405: 'метод не поддерживается',
                500: 'внутренняя ошибка сервера'}

__status__ok = 200
__success__ = 'Success'

organizations_dict = {'None': None}

user = 'ECR'
pwd = '12'
uri = "http://178.159.33.160:11080//urpd//hs//Priveleges//api//v1//get-user-description"

data = json.dumps({'UserId': '41cc805e-0341-4127-9639-434d64cf04c1'})
headers = {'user': user, 'password': pwd, 'Content-Type': 'application/json'}

session = requests.session()
session.auth = HTTPBasicAuth(user, pwd)

response_dict = None
response = session.post(uri, data=data)
if response.status_code == __status__ok:
    response_dict = json.loads(response.text)
    if response_dict['Code'] == __success__:
        user_description = response_dict['Description']['UserName']
        for org_id, org_desc in response_dict['Description']['Organizations']:
            organizations_dict.setdefault('OrganizationId', org_desc['OrganizationId'])
        print(organizations_dict)

# print(response.text)
# response = requests.put(uri, data=data, headers=headers)
# tmp_code = response.status_code
# tmp_description = status_codes.get(tmp_code)
# tmp_description = tmp_code if tmp_description is None else tmp_description
# print(tmp_description)
# print(response.text)
