#! /usr/bin/python3
# import os
#
# path = '.git'
# files = os.listdir(path)
# result = ''
# for i in files:
#     result += str(i) + '\n'
#
# print(result)


import requests

headers = {
    'User-Agent': "Anonim"
}

response = requests.post('https://www.читай-болтай.рф/feedback/', headers,
                         params={'fio':'SERGIO','email':'pop@yandex.ru','message':'text'},
                         json={'fio':'SERGIO','email':'pop@yandex.ru','message':'text'})

print(response.status_code)
if response.ok:
    print('200')
