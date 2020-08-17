import requests
import telebot

from methods import save_user, save_message
from flaskSQLalchemy import db
from models.Projects import Projects

from app import bot


@bot.message_handler(commands=['start'])
def start_message(message):
    '''Главный базовый метод, срабатвает в момент активайии бота, выводит приветствие, и создает кнопки.'''

    db.create_all()

    # Создаем кнопки с общим функционалом который увидит пользователь при начале работы
    # При создании передаем параметр = True это ркгулирует размер кнопок под ширину экрана
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Наши реквизиты', 'Наши цены', 'Факты о нас')
    keyboard.add('Расчитать стоимость проекта')

    # Выводим притствие, и показываем кнопки нашему пользователю
    bot.send_message(message.chat.id, 'Привет {0} {1} вас приветствует бот компании {2} \n'
                     .format(message.from_user.first_name, message.from_user.last_name, 'MitLabs'),
                     reply_markup=keyboard)

    # Создаем и отправляем кнопу для перехода на сайт компании
    keyboard_inline = telebot.types.InlineKeyboardMarkup()
    btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
    keyboard_inline.add(btn_url_mitlabs)
    text = '''Анализируем, планируем, помогаем развиваться:
        - Анализ вашего бизнеса
        - Выявление эффективных каналов продаж
        - Анализ ЦА и конкурентов
        - Разработка детальной стратегии развития
        Планирование digital-стратегии — это создание полного, 
        пошагового руководства к действию, по которому можно
        развивать и поддерживать свою компанию с нуля.
    '''

    # Отправляем сообщение пользователю
    bot.send_message(message.chat.id, text, reply_markup=keyboard_inline)

    # message.text Содержит в себе текст сообщения от пользоватеял
    save_user(message)
    save_message(message)



# TODO сделать регистрацию админа в этом телеграмботе, чтобы бот мог писать админу,
# TODO что клиент хочет с ним пообщаться на тему проекта.
@bot.message_handler(commands=['adminRegistration'])
def admin_registration(message):
    bot.send_message(message.chat.id, 'adminRegistration')



"""ИНТЕРЕСНОЕ - если вставить в текст сообщения пользователю сылку на сайт,
 то пользователь получит картинку сайта, с кратким описанием"""
@bot.message_handler(commands=['url'])
def start_message(message):
    '''Тестовый метод для отправки http запроса на сайт'''

    url = 'https://mitlabs.ru/'
    response = requests.get(url)

    print('==========================' * 50)
    print('==========================' * 50)
    print('==========================' * 50)

    print('======= СТАТУС ОТВЕТ НА GET ЗАПРОС =======')
    print(response.status_code)
    print('=========================='*50)
    print('============= ЗАГОЛОВКИ ОТВЕТА С СЕРВЕРА =============')
    print(response.headers)
    print('==========================' * 50)
    print('============== ТЕЛО ОТВЕТА ============')
    print(response.text)

    text = f'Отправлено сообщение на сайт {url}'

    # Отправляем сообщение пользователю
    bot.send_message(message.chat.id, text)





@bot.message_handler(commands=['get_project'])
def get_project(message):
    '''олучить данные о проекте, данного пользователя по его id в системе'''
    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    print(project.__repr__())
    bot.send_message(message.chat.id, project.__repr__())





@bot.message_handler(commands=["info"])
def handle_docs_audio(message):
    '''Выводит информацию о текущем состоянии чата'''
    # bot.send_poll(message.chat.id, 'вопрос', options=['1', '2', '3'])
    # bot.send_message(message.chat.id, 'Привет')
    # bot.send_message(message.chat.id, message.chat.id)

    '''В ответе с сервера telegram мы получаем'''
    # # bot.send_poll(message.chat.id, 'вопрос', options=['1', '2', '3'])

    bot.send_message(message.chat.id, 'Содержимое переменной message.chat')
    bot.send_message(message.chat.id, f'id = {message.chat.id}')
    bot.send_message(message.chat.id, f'first_name = {message.chat.first_name}')
    bot.send_message(message.chat.id, f'last_name = {message.chat.last_name}')
    bot.send_message(message.chat.id, f'username = {message.chat.username}')
    bot.send_message(message.chat.id, f'type = {message.chat.type}')




@bot.message_handler(commands=['document'])
def handle_docs_photo(message):
    '''Прием документов от пользователя'''

    global src
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # src = '/home/users-name/received/' + message.document.file_name;
        # src = '/document/' + message.document.file_name
        src = message.document.file_name
        with open(src, 'wb') as new_file:
            # new_file.write(downloaded_file)
            new_file.write('/document/' + downloaded_file)
        bot.reply_to(message, "Я сохраню ваш файл")
    except Exception as e:
        bot.reply_to(message, 'Возникла ошибка: ' + e)

    # bot.send_message(message.chat.id, 'message.document.file_name = '+message.document.file_name)




@bot.message_handler(commands=['name'])
def handle_email(message):
    bot.send_message(message.chat.id, str(__name__))




# @bot.message_handler(commands=['document'])
# def handle_email(message):
#     pass

    # uis_pdf = open('document/pres_mitlab.pdf', 'rb')
    # uis_pdf = open('1.pdf', 'rb')
    # bot.send_document(message.chat.id, uis_pdf)

    # img = open('../Peek 2020-06-09 15-44.gif', 'rb')
    # bot.send_photo(message.chat.id, img)

    # bot.send_animation(message.chat.id, img)
    # bot.send_message(id, '<a href="IMG_URL">&#8203;</a>', parse_mode="HTML")
    # bot.send_message(message.chat.id, '<a href="">&#8203;</a>', parse_mode="HTML")


# bot.send_animation - Посылает гифки и возможно видео
# bot.send_photo     - Посылает картинки

# import time
# time.sleep(1)




@bot.message_handler(commands=['help'])
def default_test(message):
    '''Метод помошник, выводит справочную информацию.'''

    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_url_mitlabs = telebot.types.InlineKeyboardButton(
        text="Перейти на сайт компании MitLabs",
        url="https://mitlabs.ru")

    keyboard.add(btn_url_mitlabs)
    bot.send_message(message.chat.id, "Выберите локацию:", reply_markup=keyboard)