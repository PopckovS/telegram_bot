#! /usr/bin/python3

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response
from flask_sqlalchemy import SQLAlchemy

# Установка модуля для SSL сертификата, это расширение для фласка
# pip3 install flask-sslify
from flask_sslify import SSLify

import json
import requests
import config
from datetime import datetime

from start import app
from flaskDB import *

from models.Projects import Projects
from models.User import User
from models.Type import Type
from models.Messages import Messages






# 'sendMessage?chat_id = 932670856 & text = Привет - Мир
@app.route("/")
def page_index():
    return get_header() + '<br> Привет Мир !'



@app.route("/getAllUsers")
def page_get_all_user():
    '''Генерация страницы со всеми пользователями.'''
    users = db.session.query(User).all()

    print('==================')
    print(users)
    print('==================')

    return render_template('allUssers.html',
                           menu=get_header(),
                           header='Главная страница',
                           linkMessages='/messages/',
                           users=users)



@app.route("/messages/<telegramID>")
def page_get_all_messages(telegramID):
    '''Генерация страницы со всеми сообщениями от пользователя.'''

    # Получить все сообщения пользователя
    userMessages = db.session.query(Messages).\
        filter(Messages.telegramID == telegramID).all()

    # Получить все сообщения Бота пользователю
    botMessages = db.session.query(Messages). \
        filter(Messages.telegramID == config.BOT_ID,
               Messages.recipient == telegramID).all()


    # Обьединение  обьектов в список, сортировка списка обьектов
    allMessages = userMessages + botMessages
    allMessages = sorted(allMessages, key=lambda x: x.id)

    #
    # print(type(allMessages))
    # print('===============================')
    # for k in allMessages:
    #     # print(type(k))
    #     print(k)
    # print('===============================')

    print(telegramID)
    print(type(telegramID))
    print(config.BOT_ID)
    print(type(config.BOT_ID))

    return render_template('messages.html',
                           menu=get_header(),
                           header='Главная страница',
                           userMessages=userMessages,
                           botMessages=botMessages,
                           allMessages=allMessages,
                           man=int(telegramID),
                           bot=config.BOT_ID,
                           )



@app.route("/sendMessage")
def send_message():
    # / sendMessage?chat_id = 932670856 & text = Привет + Человек +!
    # 932670856
    user = db.session.query(User).filter(User.id == 2).first() # Получаем сущьность из БД
    user.bot_command = 1 # Меняем значение в Сущьности, далее сохраняем ее
    db.session.add(user) # Вносим пользователя в сессию
    db.session.commit()  # Сохраняем данные о пользователе в БД

    text = 'Сообщение от человека, не от бота'
    # response = requests.get(config.BOT_URL + 'sendMessage' + '?chat_id={telegramID}&text={text}'.format(telegramID=932670856, text=text))
    response = requests.get(config.BOT_URL + 'sendMessage' + '?chat_id={telegramID}&text={text}'.format(telegramID=user.telegramID, text=text))
    # return response.json()
    return f"Бот по чату с номером {response.json()['result']['chat']['id']} переключена в режим разговора с человеком.<br>\
            Послано сообщение : {response.json()['result']['text']}"


@app.route("/stopSendMessage")
def stop_send_message():
    user = db.session.query(User).filter(User.id == 2).first()  # Получаем сущьность из БД
    if user.bot_command is 1:
        user.bot_command = 0  # Меняем значение в Сущьности, далее сохраняем ее
        db.session.add(user)  # Вносим пользователя в сессию
        db.session.commit()  # Сохраняем данные о пользователе в БД
    return 'Программа переключена в режим разговора с Ботом'


@app.route("/get-updates")
def get_updates():
    response = requests.get(config.BOT_URL + 'getUpdates')
    write_json(response.json(), 'updates.json')
    return response.json()



@app.route("/info")
def page_info():
    response = requests.get(config.BOT_URL + 'getMe')
    result = f'ok = {response.json()["ok"]} <br> \
             id = {response.json()["result"]["first_name"]} <br> \
             first_name = {response.json()["result"]["first_name"]} <br> \
             username = {response.json()["result"]["username"]} <br> \
             is_bot = {response.json()["result"]["username"]}'
    write_json(response.json(), 'answer.json')
    return get_header() + '<br><h1>Чистый результат</h1>' + str(response.json()) \
           + '<br><h1>Обработанный результат</h1>' + result



def write_json(data, filename):
    with open(config.DIR_JSON + filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)



def get_header():
    header = '<a href="/">Главная</a><br>' \
             '<hr><a href="/getAllUsers">Получить список всех Пользователей</a><hr><br>' \
             '<a href="/info">Информация о Боте</a><br>' \
             '<a href="/get-updates">Получить новые сообщения</a><br>'\
             '<a href="/sendMessage">Режим - разговор с Человеком</a><br>'\
             '<a href="/stopSendMessage">Режим - разговор с Ботом</a><br>'
    return header



# Запуск работы сервера
if __name__ == "__main__":
    app.run(debug=True, port=5000)
