import requests
import config


# TODO сделать проверку на отправку и получение
def initialBot():
    '''GET запрос к API телеграм бота, чтобы узнать его ID в BotFather'''
    response = requests.get(config.BOT_URL + 'getMe')
    return response.json()['result']['id']

# Название компании, для которой будут изьяты данные из БД
COMPANY = 'Mitlabs'

# Ссылка на БРИФ в гугул страницах
GOOGLE_FORM_BRIF = 'https://docs.google.com/forms/d/e/1FAIpQLSdAhEeEfNyv4fnTHRt_EmxfbZ3JQtU1uH5lQr7bvgIXfP_ZVA/viewform'

# Получаем ID телеграм бота в системе
# BOT_ID = initialBot()
BOT_ID = 1266890760

# Ключ API для аутентификации с ботом, ключ можно получить от BotFather в telegram
API_KEY = ''

# Ссылка на бота для начала взаимодействия
BOT_LINK = 'https://t.me/test_sergey_username_2_bot'

# Сайт для управления ботом
SAIT = 'localhost:5000'

#
IS_MAN = False

# База Данных которую мы используем для работы
DB = 'bot'

#  Подключения к БД через Flask SQLAlchemy
CONNECT_DB = 'mysql+pymysql://serg:11@localhost/' + DB

# Адрес Телеграм Бота
URL = 'https://api.telegram.org/bot'

# Адрес для обращения к боту через API телеграма
BOT_URL = f'{URL}{API_KEY}/'

# Директория для хранения файлов формата json с результатами запросов к API
DIR_JSON = 'json'

# Emoji Полный список находится по адресу
# http://www.unicode.org/emoji/charts/full-emoji-list.html
SMILE = "👁 📙 📄 ⚙ ❤ 🙂 📘 🖋 🗑 🔒 🔗 👉 " \
        "💰 💹 📅 📎 🔓 ✔ ❌ 👍 👎 📍 📌 📊 ⚠ ☢"



