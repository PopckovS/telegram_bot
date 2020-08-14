'''

Установка модуля для SSL сертификата
pip3 install flask-sslify

Импорты разного полезного
import requests
import telebot
import config
import re
import os

from methods import save_user, save_message
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response

from datetime import datetime
from flaskSQLalchemy import db
from mitlabs import MitLabs

# Импортируем Модели
from models.User import User
from models.Type import Type
from models.Messages import Messages
from models.Projects import Projects

from app import bot



def sef(message):
    # Создаем обьект модели сообщений и вносим данные в его атрибуты
    message = Messages(telegramID=message.chat.id, message=message.text)

    # Вносим сообщение в сессию
    db.session.add(message)
    # Сохраняем сообщение в БД
    db.session.commit()


SELECT message FROM Messages WHERE Messages.telegramID = 956339263
ID бота в системе 1266890760

Установка Телеграм Бота
pip3 install pytelegrambotapi

Установка SQLAlchemy
pip3 install flask-sqlalchemy
pip3 install pymysql
'''

'''Тут собрано описание того как работать с Модулем pyTelegramBotAPI

bot = telebot.TeleBot(config.key_api) - Импортируем модуль telebot, и создаем экземпляр его класса,
передаем ему API ключ для нашего бота< через который и будет аутентификация.

@bot.message_handler(commands=['start']) - Метод обертка, указывает о принятии команды.
Начало работы с любым ботом ы телеграмме начинается с команды /start данный метод будет
работать первым при старте общения.


ReplyKeyboardMarkup - создает шаблоны сообщений которые может отправлять пользователь, только то что написано
может быть отправлено.

InlineKeyboardMarkup - настоящая кастомная клавиатура. Она привязывается к сообщению, с которым была отправлена.
Инлайн кнопки позволяют скрыть в себе внутреннюю телеграм ссылку, ссылку на внешний ресурс, а также шорткат для инлайн запроса.





keyboard = telebot.types.InlineKeyboardMarkup()
btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
keyboard.add(btn_url_mitlabs)

bot.send_message(message.chat.id, 'Здраствуйте {0} {1} вас приветствует бот компании {2} \n'
                 .format(message.from_user.first_name, message.from_user.last_name, 'MitLabs', reply_markup=keyboard))'''

'''Простой Telegram-бот на Python

Официальная документация находится по адресу.
https://github.com/eternnoir/pyTelegramBotAPI

Регистрируем бота через @BotFather, надо написать ему /start или /newbot
Заполняем поля, название бота и его короткое имя,
После получаем сообщение с токеном бота и ссылкой на документацию.
Сам токен это ед.ключ для взаимодействия с ним.

Писать будем на PyTelegramBotAPI. команда установки:
pip install pytelegrambotapi

Телеграмм умеет сообщать боту о действиях пользователя двумя способами:
1) через ответ на запрос сервера (Long Poll).
2) через Webhook,  когда сервер Телеграмма сам присылает
сообщение о том, что кто-то написал боту.

Второй способ - требует выделенного IP-адреса, и установленного SSL на сервере
Тут будем пользоваться первым методом - Long Poll

Для использования метода Long Poll можно использовать сервис Windscribe
но его бесплатная версия имеет ограничение в 10 .Гб трафика на месяц.

1) Есть другой способ, использование облачного сервиса, самый популярнеый Heroku.
1 - Регистрируемся на Heroku и устанавливаем его этой командой
        sudo snap install heroku --classic
2 - Авторизируемся в терминале командой
        heroku login
    Это откроет браузер со стр.входа, надо будет авторизоваться, и получим сообщение типа
    Logged in as popckovm5@yandex.ru

3 - Для работы с сервисом потребуется создать 2 файла:
    Procfile (без расширения, и записать в него эти строчки, с названием главного рабочего фалйа)
        worker: python bot.py
    requirements.txt (и записать в него)
        appdirs==1.4.3
        certifi==2018.1.18
        Cython==0.23
        Django==1.10.6
        docutils==0.13.1
        packaging==16.8
        pipenv==11.8.0
        psutil==5.0.1
        pyowm==2.8.0
        Pygments==2.2.0
        pyparsing==2.2.0
        pyTelegramBotAPI==3.6.1
        python-telegram-bot==7.0.1
        requests==2.13.0
        six==1.10.0
        virtualenv==15.1.0
        virtualenv-clone==0.3.0

4 - Деплой в Heroku:
    Создаем проект этой командой:
        heroku create
    Получаем в ответ
         ›   Warning: heroku update available from 7.42.0 to 7.42.1.
        Creating app... done, ⬢ murmuring-dawn-56959
        https://murmuring-dawn-56959.herokuapp.com/ | https://git.heroku.com/murmuring-dawn-56959.git
    Это означает что по адресу https://murmuring-dawn-56959.herokuapp.com был создан наш проект, с возможностью
    управления по типу github.
    Далее можем работать с ним как и с git репозиторием:
        git add .
        git commit -am "make it better"
        git push heroku master
    После этого проект будет запушен на сервер, теперь чтобы запустить наш worker dyno сервер
    Исполним эту команду:
        heroku ps:scale worker=1
    Теперь бот будет находиться в постоянно слушающем состоянии.
'''

# Можно работать с картинками по их id а можно по их имени, для этого потребуется установить
# модуль emoji
# модуль sqlite3

# Так можно получить данные о пользователе с которым общается наш бот
# message.from_user.id
# message.from_user.first_name
# message.from_user.last_name
# message.from_user.username


'''
Примеры работы с API Telegram по средствам GET,POST,PUT,DELETE запросов по средству протокола https.
Очень интересные статьи по этой теме, можно найти на сайте: http://docs.botmother.com/

по документации, можно работать с ботом телеграмма, при помощт https
задавая различные методы и получая результат.
Результат возвращается в виде json
Тело в GET запросе можно передавать в строке URL, для остальных запросов — только в специальном поле компонента.

1) Метод getMe выводит информацию о самом боте, его id, бот это или нет, имя бота, username бота.
    https://api.telegram.org/bot{ТОКЕН_API}/getMe
    {"ok":true,"result":
        {"id":1266890760,
        "is_bot":true,
        "first_name":"test_sergey_bot_2",
        "username":"test_sergey_username_2_bot",
        "can_join_groups":true,
        "can_read_all_group_messages":false,
        "supports_inline_queries":false}
    }

2) Послать сообщенение от лица бота в определенный чат, тоесть конкретному человеку.   
    Этот запрсо типа Get отправит в чат с id = 932670856 текст "Привет-Мир"
    Что это значит, мы можем отправлять сообщения в различные чаты, при помощи
    стандартного модуля requests то-есть управлять ботом.

    Также при отправки текстов в место пробелов надо исп-ть символ + при GET запросе.

    https://api.telegram.org/bot{ТОКЕН_API}/sendMessage?chat_id=932670856&text=Привет-Мир

    В ответе получим, номер сообщения(тоесть сколько всего сообщений вабще было топравлено за все время)
    от кого, id бота его имя и прочее. И кому, id чата, имя фамилия человека в телеграмме.
    {"ok":true,"result":
        {
        "message_id":98,
        "from":
            {"id":1266890760,
            "is_bot":true,
            "first_name":"test_sergey_bot_2",
            "username":"test_sergey_username_2_bot"
            },
        "chat":
            {"id":932670856,
            "first_name":"Sergey",
            "last_name":"Popckov",
            "username":"popkovS",
            "type":"private"
            },
        "date":1592263743,
        "text":"\u0425\u0430\u0439-\u0411\u043b\u044f\u0442\u044c"
        }
    }

    Ошибка если не указать чат id при отправки GET запроса.
    {"ok":false,"error_code":400,"description":"Bad Request: chat_id is empty"}
'''
