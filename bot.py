#! /usr/bin/python3

# Импортируем модлуь для работы с телеграм ботом
import telebot # Модуль pyTelegramBotAPI
import config  # Файл конфигурации
from mitlabs import MitLabs # Импортирую класс с информацией о компании

# Создаем экземпляр класса для работы с библиотекой pyTelegramBotAPI, и передаем ему API токена.
bot = telebot.TeleBot(config.key_api)
mt = MitLabs()







# Стартовое приветствие
@bot.message_handler(commands=['start'])
def start_message(message):

    # Создаем кнопки с общим функционалом который увидит пользователь при начале работы
    # При создании передаем параметр = True это ркгулирует размер кнопок под ширину экрана
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Наши реквизиты', 'Наши цены', 'Факты о нас')
    keyboard.add('Расчитать стоимость вашего проекта')

    # Выводим притствие, и показываем кнопки нашему пользователю
    bot.send_message(message.chat.id, 'Здраствуйте {0} {1} вас приветствует бот компании {2} \n'
                     .format(message.from_user.first_name, message.from_user.last_name, 'MitLabs'), reply_markup=keyboard)







# Стартовое приветствие
@bot.message_handler(commands=['help'])
def default_test(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
    btn_question = telebot.types.InlineKeyboardButton(text="Задать вопрос человеку", url="https://mitlabs.ru")
    btn_out = telebot.types.InlineKeyboardButton(text="Отписаться", url="https://mitlabs.ru")

    keyboard.add(btn_url_mitlabs)
    keyboard.add(btn_question)
    keyboard.add(btn_out)

    bot.send_message(message.chat.id, "Выберите локацию:", reply_markup=keyboard)







# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    # Если сообщение из чата с ботом
    if call.message:
        # Если callback_data что была передана есть в массиве данных
        if call.data in mt.get_price():
            list_price = mt.get_price()
            # По ключу что был передан в callback_data получаю значение и вывожу пользователю
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=list_price[call.data])
    # Если сообщение из инлайн-режима
    # elif call.inline_message_id:
    #     if call.data == "test":
    #         bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")








name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')







# # Handles all text messages that match the regular expression
# @bot.message_handler(regexp="popckovM5@yandex.ru")
# def handle_message(message):
# 	bot.send_message(message.from_user.id, 'Благодарю вы успешно ввели свой  email адрес = ' + message.text)

    #
    # keyboard = telebot.types.InlineKeyboardMarkup()
    #
    # btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
    # btn_question = telebot.types.InlineKeyboardButton(text="Задать вопрос человеку", url="https://mitlabs.ru")
    # btn_out = telebot.types.InlineKeyboardButton(text="Отписаться", url="https://mitlabs.ru")
    #
    # keyboard.add(btn_url_mitlabs)
    # keyboard.add(btn_question)
    # keyboard.add(btn_out)






 # if call.message:
 #        if call.data == 'Дизайн от А до Я':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Дизайн от А до Я')
 #        if call.data == 'Системный маркетинг':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Системный маркетинг')
 #        if call.data == 'Разработка сайта':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Разработка сайта')
 #        if call.data == 'E-COMMERCE продвигаем и продаем':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='E-COMMERCE продвигаем и продаем')
 #        if call.data == 'DEVOPS, АДМИНИСТРИРОВАНИЕ, ТЕХНИЧЕСКАЯ ПОДДЕРЖКА':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='DEVOPS, АДМИНИСТРИРОВАНИЕ, ТЕХНИЧЕСКАЯ ПОДДЕРЖКА')
 #        if call.data == 'AI И ML':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='AI И ML')
 #        if call.data == 'Документы и право':
 #            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Документы и право')









# Если скрипт запущен как основной, то запустить работу бота,
# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)