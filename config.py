import requests
import config


# TODO сделать проверку на отправку и получение
def initialBot():
    '''GET запрос к API телеграм бота, чтобы узнать его ID в BotFather'''
    response = requests.get(config.BOT_URL + 'getMe')
    return response.json()['result']['id']

# Получаем ID телеграм бота в системе
# BOT_ID = initialBot()
BOT_ID = 1266890760

# Ключ API для аутентификации с ботом, ключ можно получить от BotFather в telegram
# key_api_heruko = ''
key_api_long_pool = ''

#
IS_MAN = False

#  Подключения к БД через Flask SQLAlchemy
CONNECT_DB = 'mysql+pymysql://serg:11@localhost/telegram'

# Адрес Телеграм Бота
URL = 'https://api.telegram.org/bot'

# Приватный токен для обращения к боту
API_KEY = ''

# Адрес для обращения к боту через API телеграма
BOT_URL = f'{URL}{API_KEY}/'

# Директория для хранения файлов формата json с результатами запросов к API
DIR_JSON = 'json'


