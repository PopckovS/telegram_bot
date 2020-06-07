'''
Официальная документация находится по адресу.
https://github.com/eternnoir/pyTelegramBotAPI
'''

# Импортируем модлуь для работы с телеграм ботом
import telebot

# Создаем экземпляр класса, и передаем ему API токена.
bot = telebot.TeleBot('тут токен для работы с API')

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