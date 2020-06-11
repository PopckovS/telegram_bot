#! /usr/bin/python3
# Импортируем модлуь для работы с телеграм ботом
import telebot # это модуль pyTelegramBotAPI

# pip install python-telegram-bot

key_api = '1028658654:AAE4KC14J8oxGPrwQCN7u-t9xY0tqKo5wFY'

# Создаем экземпляр класса, и передаем ему API токена.
bot = telebot.TeleBot(key_api)

# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    '''Добавляем в бот реакцию насообщение.'''

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
bot.polling(none_stop=True, interval=0)