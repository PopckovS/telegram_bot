#! /usr/bin/python3

# Импортируем модлуь для работы с телеграм ботом
import telebot # Модуль pyTelegramBotAPI
import config  # Файл конфигурации
import re # Импортирую модулья для работы с регулярными выражениями, проверки email, phone
import os
from mitlabs import MitLabs # Импортирую класс с информацией о компании

# Создаем экземпляр класса для работы с библиотекой pyTelegramBotAPI, и передаем ему API токена.
bot = telebot.TeleBot(config.key_api)

# Создаем экземляр класса для получения из него данных о компании
mt = MitLabs()

# Обьявление ряда переменных, для получения и сохранения игформации от пользователя
name = ''
email = ''
phone = ''
about_project = ''
other = ''




@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):

    '''Прием документов от пользователя'''

    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # src = '/home/users-name/received/' + message.document.file_name;
        src = 'received/' + message.document.file_name;
        src = message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Я сохраню ваш файл")
    except Exception as e:
        bot.reply_to(message, 'Возникла ошибка: ' + e)

# Стартовое приветствие
@bot.message_handler(commands=['start'])
def start_message(message):

    '''Главный базовый метод, срабатвает в момент активайии бота, выводит приветствие, и создает кнопки.'''

    path = 'received'
    files = os.listdir(path)
    result = ''
    for i in files:
        result += str(i)

    bot.send_message(message.chat.id, result)





# Стартовое приветствие
@bot.message_handler(commands=['help'])
def default_test(message):

    '''Метод помошник, выводит справочную информацию.'''

    keyboard = telebot.types.InlineKeyboardMarkup()

    btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
    # btn_question = telebot.types.InlineKeyboardButton(text="Задать вопрос человеку", url="https://mitlabs.ru")
    # btn_out = telebot.types.InlineKeyboardButton(text="Отписаться", url="https://mitlabs.ru")

    keyboard.add(btn_url_mitlabs)
    # keyboard.add(btn_question)
    # keyboard.add(btn_out)

    bot.send_message(message.chat.id, "Выберите локацию:", reply_markup=keyboard)







# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    '''Метод обработчик нажатых Inline кнопок, тоесть заранее заготов.кнопок меню.'''

    if call.message:

        # Это для обработки запроса на показ Услуг компании.
        # Если callback_data что была передана есть в массиве данных
        if call.data in mt.get_price():
            list_price = mt.get_price()
            # По ключу что был передан в callback_data получаю значение и вывожу пользователю
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=list_price[call.data])

        if call.data == 'project_yes':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Прекрасно, продолжим')
            # bot.send_message(call.message.from_user.id, 'Прекрасно, продолжим')
        if call.data == 'project_no':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Хорошо, давайте с начала')
            # bot.send_message(call.message.from_user.id, 'Хорошо, давайте с начала')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Как Вас зовут?')
            # bot.send_message(call.message.from_user.id, "Как Вас зовут?")
            bot.register_next_step_handler(call.message, get_name)
    # Если сообщение из инлайн-режима
    # elif call.inline_message_id:
    #     if call.data == "test":
    #         bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")










# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Наши реквизиты':
        bot.send_message(message.from_user.id, mt.get_requisites())
    elif message.text == 'Наши цены':

        # !!! НЕ ЗНАЮ ПО ЧЕМУ И КАК, НО ОПЫТНЫМ ПУТЕМ ВЫЯСНИЛ, ЧТО ЕСТЬ ОГРАНИЧЕНИЕ !!!
        # !!! НА ДЛИННУ СТРОКИ ПРИ СТАВКИ ЗНАЧЕНИЯ В callback_data В ДОКАХ ПРО ЭТО НИЧЕГО!!!
        keyboard = telebot.types.InlineKeyboardMarkup()

        btn1 = telebot.types.InlineKeyboardButton(text='Дизайн от А до Я', callback_data='Дизайн от А до Я')
        btn2 = telebot.types.InlineKeyboardButton(text='Маркетинг', callback_data='Системный маркетинг')
        btn3 = telebot.types.InlineKeyboardButton(text='Разработка сайта', callback_data='Разработка сайта')
        btn4 = telebot.types.InlineKeyboardButton(text='E-COMMERCE', callback_data='E-COMMERCE')
        btn5 = telebot.types.InlineKeyboardButton(text='DEVOPS', callback_data='DEVOPS')
        btn6 = telebot.types.InlineKeyboardButton(text='AI И ML', callback_data='AI И ML')
        btn7 = telebot.types.InlineKeyboardButton(text='Документы и право', callback_data='Документы и право')

        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

        bot.send_message(message.chat.id, "Услуги компании:", reply_markup=keyboard)

    elif message.text == 'Факты о нас':
        bot.send_message(message.from_user.id, mt.get_facts())
    elif message.text == 'Расчитать стоимость проекта':
        # Тут мы задаем пользователб вопрос, с которого начинается цикл вопросов пользователю
        bot.send_message(message.from_user.id, "Как Вас зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю :( Чем я могу тебе помочь?')






# class User:
#     def __init__(self, name):
#         self.name = name
#         self.age = None
#         self.sex = None
#
#
# def process_name_step(message):
#     try:
#         chat_id = message.chat.id
#         name = message.text
#         user = User(name)
#         user_dict[chat_id] = user
#         msg = bot.reply_to(message, 'How old are you?')
#         bot.register_next_step_handler(msg, process_age_step)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')










# pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')


#     popcovM5@yandex.ru
# if is_valid:
#     print('правильный email:', is_valid.group())
#     # объект is_valid содержит 3 метода
#     print('методы: start:', is_valid.start(), 'end:',\
#     is_valid.end(), 'group:', is_valid.group())
# else:
#     print('неверный email! введите email...\n')




# Это ПОТОК команд, метод register_next_step_handler регистрирует ряд методов
# которые будут выполняться последовательно, один за другим, создавая и устанавливая
# в нутри методов циклы, можно зациклить эти вопросы, до тех пор пока мы не получим
# нужный результат, а если пользователь хочет выйти из потока методов, то мы можем
# сделать исключение при помощи InlineKeyboardButton и просто не регистрировать
# следующего метода, а просто выйти из потока методов.
def get_name(message):

    '''Метод получает от пользователя Имя Фамилию по установленному паттерну'''

    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Ваш email ?')
    bot.register_next_step_handler(message, get_email)

    # keyboard = telebot.types.InlineKeyboardMarkup()
    # btn_no_email = telebot.types.InlineKeyboardButton(text='Да все верно', callback_data='no_email')
    # keyboard.add(btn_no_email)
    #
    # bot.send_message(message.from_user.id, 'Ваш email ?')
    # bot.register_next_step_handler(message, get_email)

#     keyboard = telebot.types.InlineKeyboardMarkup()
#     btn_yes = telebot.types.InlineKeyboardButton(text='Да все верно', callback_data='project_yes')
#     btn_no = telebot.types.InlineKeyboardButton(text='Нет, заполнить с начала', callback_data='project_no')
#     keyboard.add(btn_yes, btn_no)



def get_email(message):
    '''Метод получает от пользователя email'''

    global email

    result = re.search(r'[\w.-]+@[\w.-]+\.?[\w]+?', message.text)

    if result == None:
        bot.send_message(message.from_user.id, 'Кажется, это неправильный email :( Попробуй еще раз!')
        bot.register_next_step_handler(message, get_email)
    else:
        email = message.text
        bot.send_message(message.from_user.id, 'Ваш телефон ?')
        bot.register_next_step_handler(message, get_phone)



def get_phone(message):
    '''Метод получает от пользователя телефон'''

    global phone

    result = re.search(r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b", message.text)

    if result == None:
        bot.send_message(message.from_user.id, 'Кажется, это неправильный телефона :( Попробуй еще раз!')
        bot.register_next_step_handler(message, get_phone)
    else:
        phone = message.text
        bot.send_message(message.from_user.id, 'Расскажите о Вашем проекте')
        bot.register_next_step_handler(message, get_about_project)



def get_about_project(message):
    global about_project
    about_project = message.text
    # while about_project == '':
    #     try:
    #         about_project = str(message.text)
    #     except Exception:
    #          bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    keyboard = get_btn_project() # Добавляем кнопки к результату заполнения опроса

    result_text = f"Все правильно ? \nВас зовут = {name}"

    if not email == '':
        result_text += f'\nВаш email = {email}'
    if not phone == '':
        result_text += f'\nВаш телефон = {phone}'

    result_text += f'\nОписание проекта = {about_project}'

    bot.send_message(message.from_user.id, result_text, reply_markup=keyboard)
    bot.send_poll(message.chat.id, 'Оцените работу бота', options=['Ужасно', 'Рок группа "Dark Funeral" полное говно !', 'Хорошо'])





def get_btn_project():
    '''Создаем и добавляем inline кнопки, да/нет для продолжения или сброса опроса'''

    keyboard = telebot.types.InlineKeyboardMarkup()
    btn_yes = telebot.types.InlineKeyboardButton(text='Да все верно', callback_data='project_yes')
    btn_no = telebot.types.InlineKeyboardButton(text='Нет, заполнить с начала', callback_data='project_no')
    keyboard.add(btn_yes, btn_no)

    return keyboard






# Если скрипт запущен как основной, то запустить работу бота,
# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)