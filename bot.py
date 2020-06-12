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
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Наши реквизиты', 'Наши цены', 'Факты о нас')

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





# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Наши реквизиты':
        bot.send_message(message.from_user.id, mt.get_requisites())
    elif message.text == 'Наши цены':

        # !!! НЕ ЗНАЮ ПО ЧЕМУ И КАК, НО ОПЫТНЫМ ПУТЕМ ВЫЯСНИЛ, ЧТО ЕСТЬ ОГРАНИЧЕНИЕ НА ДЛИННУ СТРОКИ !!!
        keyboard = telebot.types.InlineKeyboardMarkup()

        btn1 = telebot.types.InlineKeyboardButton(text='Дизайн от А до Я', callback_data='Дизайн от А до Я')
        btn2 = telebot.types.InlineKeyboardButton(text='Системный маркетинг', callback_data='Системный маркетинг')
        btn3 = telebot.types.InlineKeyboardButton(text='Разработка сайта', callback_data='Разработка сайта')
        btn4 = telebot.types.InlineKeyboardButton(text='E-COMMERCE', callback_data='E-COMMERCE')
        btn5 = telebot.types.InlineKeyboardButton(text='DEVOPS', callback_data='DEVOPS')
        btn6 = telebot.types.InlineKeyboardButton(text='AI И ML', callback_data='AI И ML')
        btn7 = telebot.types.InlineKeyboardButton(text='Документы и право', callback_data='Документы и право')

        keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, "Услуги компании:", reply_markup=keyboard)

    elif message.text == 'Факты о нас':
        bot.send_message(message.from_user.id, mt.get_facts())
    else:
        bot.send_message(message.from_user.id, message.text)




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