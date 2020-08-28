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

from models.Projects import Telegram_Projects as Projects
from models.User import Telegram_User as User
from models.Type import Telegram_Type as Type
from models.Messages import Telegram_Messages as Messages





@app.route("/")
def page_index():
    '''Главная страница со статистикой работы Бота'''

    # Получаем всех пользователей кроме самого телеграм Бота
    user = db.session.query(User).filter(User.telegramID != config.BOT_ID).all()

    # Получаем все имеющиеся проекты
    project = db.session.query(Projects).all()

    return render_template('index.html',
                            bot_status = page_get_bot(),  # Информация о самом боте
                            bot_link = config.BOT_LINK,   # URL сылка на телеграм бота
                            user_count = len(user),       # Информация о Пользователях
                            project_count = len(project), # Информация о Проектах
                           )




@app.route("/users")
def page_all_users():
    '''Генерация страницы со всеми пользователями.'''

    # Получить всех пользователей
    users = db.session.query(User).filter(User.telegramID != config.BOT_ID).all()
    # project = db.session.query(User, Projects).join(Projects, User.telegramID == Projects.telegramID  ).filter(User.telegramID != config.BOT_ID).all()
    # users_project = db.session.query(User, Projects).join(Projects, User.telegramID == Projects.telegramID  ).filter(User.telegramID != config.BOT_ID).all()

    return render_template('users.html',
                           users=users,
                           )




@app.route("/projects")
def page_all_projects():
    '''Генерация страницы со всеми проектами.'''

    # Получить все проекты
    projects = db.session.query(User, Projects).join(Projects, User.telegramID == Projects.telegramID  ).filter(User.telegramID != config.BOT_ID).all()

    return render_template('projects.html',
                           projects=projects,
                           )



# @app.route("/projects/<telegramID>")
# def page_one_projects():
#     '''Показать конкретный прокет пользователя.'''
#     return render_template('projects.html',



@app.route("/change-mod/<telegramID>/<recipient>")
def change_bot_mode(telegramID, recipient):

    print('=========')
    print('telegramID = '+ telegramID)
    print('recipient = '+ recipient)
    print('=========')

    user = db.session.query(User).filter(User.telegramID == telegramID).first()
    print('bot_command = ' + str(user.bot_command))

    switch = 0
    if user.bot_command == 1:
        user.bot_command = 0
        switch = '0'
    elif user.bot_command == 0:
        user.bot_command = 1
        switch = '1'

    db.session.add(user)  # Вносим пользователя в сессию
    db.session.commit()  # Сохраняем данные о пользователе в БД

    return switch



# /deleteMessage?chat_id=CID&message_id=MID
@app.route("/DeleteMessage/<telegramID>/<messageID>")
def delete_message(telegramID, messageID):
    response = requests.get(config.BOT_URL + 'deleteMessage?chat_id={chat_id}&message_id={message_id}'
                            .format(chat_id=telegramID, message_id=messageID))

    # Если с Сервера пришел True результат, то значит сообщение успешно удалено
    # Удаляем сообщение по его messageID из БД, и возвращаем пользователю уведомление
    if response.json()['result'] is True:
        # Находим запись в БД по его messageID - уникальный идентификатор конкретного сообщения в переписке телеграмма
        message = db.session.query(Messages).filter(Messages.messageID == messageID).first()
        # Удаляем запись и комитим изменения
        db.session.delete(message)
        db.session.commit()
        return {'delete': True, 'messageID': messageID}

    return 'Произошла неизвестная ошибка'





@app.route("/SendMessage/", methods=['POST', 'GET'])
def send_message_from():
    if request.method == 'POST':
        text = request.form.get("message")
        telegramID = request.form.get("telegramID")
    else:
        return 'Не верный метод http запроса, принимаем только POST'

    # Когда отправляем HTTP GET запрос на сервер, в ответ получаем описание нашего запроса
    # Где
    response = requests.get(config.BOT_URL + 'sendMessage' + '?chat_id={telegramID}&text={text}'.
                            format(telegramID=telegramID, text=text))

    # Сохраняем сообщение отправленное администратором клиенту бота в телеграмме
    # Где словарь result содержит в себе message_id с номером типа int который
    # содержит в себе номер сообщения, по которому мы можем обращаться с
    message_id = 1
    # message = Messages(telegramID=config.BOT_ID, message=text, recipient=telegramID, messageID=message_id)
    message = Messages(telegramID=config.BOT_ID, message=text, recipient=telegramID, messageID=response.json()['result']['message_id'])

    db.session.add(message)  # Вносим сообщение в сессию
    db.session.commit()  # Сохраняем сообщение в БД

    # print('=============')
    # print(response)
    # print('=============')
    # print(response.json())
    # print(response.json()['result']['message_id'])
    # print('=============')

    return 'Сообщение отправлено'

# Получить по id пользователя его аватарки
# https://api.telegram.org/bot1266890760:AAEok8g0d0_-c5kIiz4jctShKp_yoIbw8QI/getUserProfilePhotos?user_id=932670856

# https://api.telegram.org/file/bot1266890760:AAEok8g0d0_-c5kIiz4jctShKp_yoIbw8QI/AgACAgIAAxUAAV85uGyBQstQVIP9p4NI3HKt-mPgAAKtpzEbiG2XN-jPJt3kads9Lxy5ki4AAwEAAwIAA2EAAxewAwABGgQ
# https://api.telegram.org/file/bot1266890760:AAEok8g0d0_-c5kIiz4jctShKp_yoIbw8QI/AQADLxy5ki4AAxewAwAB
# AgACAgIAAxUAAV85uGyBQstQVIP9p4NI3HKt-mPgAAKtpzEbiG2XN-jPJt3kads9Lxy5ki4AAwEAAwIAA2EAAxewAwABGgQ
# AQADLxy5ki4AAxewAwAB
# https://api.telegram.org/file/bot<token>/<file_path>

# https://www.google.com/maps/place?latitude=51.668194&longitude=39.208174
# /sendVenue?chat_id=932670856&latitude=51.668194&longitude=39.208174&title=Mitlabs&address=г. Воронеж, Проспект Революции 33Б — 5 Этаж
@app.route("/SendVenue/", methods=['GET', 'POST'])
def send_message_location():
    if request.method == 'POST':
        data = request.post
        print('=============')
        print(data)
        print('=============')
    else:
        return 'Метод принимает только запросы типа POST'

    return '---'




@app.route("/messages/<telegramID>")
def page_messages_history(telegramID):
    '''История всей переписки, конкретного пользователя с ботом.'''

    # Получаем самого пользователя и Его проект если тот имеется
    user = db.session.query(User).filter(User.telegramID == telegramID).first()
    project = db.session.query(Projects).filter(Projects.telegramID == telegramID).first()

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


    print(telegramID)
    print(type(telegramID))
    print(config.BOT_ID)
    print(type(config.BOT_ID))

    return render_template('messages.html',
                           user=user,
                           project=project,
                           userMessages=userMessages,
                           botMessages=botMessages,
                           allMessages=allMessages,
                           man=int(telegramID),
                           bot=config.BOT_ID,
                           )

# Красивое форматирование Даты времени
# dt = datetime.fromtimestamp(message['time'])
# dt_beauty = dt.strftime('%Y:%m:%d %H:%M:%S')





@app.route("/getTelegramBot")
def page_get_bot():
    '''Сделать GET http запрос к API, узнать информацию о боте '''
    response = requests.get(config.BOT_URL + 'getMe')
    return response.json()['result']




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
    app.run(debug=True, port=5001)
