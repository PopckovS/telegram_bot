#!/usr/bin/python3
import re

# pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
email = ''

# is_valid = pattern.match(email)
while not re.search(r'[\w.-]+@[\w.-]+\.?[\w]+?', email):
    email = input('inter you email:')
    result = re.search(r'[\w.-]+@[\w.-]+\.?[\w]+?', email)
    if result == None:
        print('Кажется, это неправильный email :( Попробуй еще раз!')

#     popcovM5@yandex.ru
# if is_valid:
#     print('правильный email:', is_valid.group())
#     # объект is_valid содержит 3 метода
#     print('методы: start:', is_valid.start(), 'end:',\
#     is_valid.end(), 'group:', is_valid.group())
# else:
#     print('неверный email! введите email...\n')

phone = ''
while not re.search(r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b", phone):
    phone = input('Введите телефон:')
    result = re.search(r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b", phone)
    if result == None:
        print('Кажется, это неправильный номер телефона :( Попробуй еще раз!')
