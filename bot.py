#! /usr/bin/python3

# Импортируем модлуь для работы с телеграм ботом
import telebot # Модуль pyTelegramBotAPI
from telebot import types
import config  # Файл конфигурации

# Создаем экземпляр класса для работы с библиотекой pyTelegramBotAPI, и передаем ему API токена.
bot = telebot.TeleBot(config.key_api)










# Стартовое приветствие
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('a')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    keyboard.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat_id, "Choose one letter:", reply_markup=keyboard)






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

    bot.send_message(message.from_user.id, message.text)

    # if message.text == "Привет":
    #     bot.send_message(message.from_user.id, "Привет")
    # elif message.text == "/help":
    #     bot.send_message(message.from_user.id, "Напиши привет")
    # elif message.text == "1":
    #     bot.send_message(message.from_user.id, "1")
    # else:
    #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# # Handles all text messages that match the regular expression
# @bot.message_handler(regexp="popckovM5@yandex.ru")
# def handle_message(message):
# 	bot.send_message(message.from_user.id, 'Благодарю вы успешно ввели свой  email адрес = ' + message.text)



















# Если скрипт запущен как основной, то запустить работу бота,
# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)