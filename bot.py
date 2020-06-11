#! /usr/bin/python3
# Импортируем модлуь для работы с телеграм ботом
import telebot # это модуль pyTelegramBotAPI

# pip install python-telegram-bot

key_api = '1028658654:AAE4KC14J8oxGPrwQCN7u-t9xY0tqKo5wFY'

# Создаем экземпляр класса, и передаем ему API токена.
bot = telebot.TeleBot(key_api)




# Стартовое приветствие
@bot.message_handler(commands=['start'])
def start_message(message):

    # Создаем кнопки с общим функционалом который увидит пользователь при начале работы
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('1', '2')

    bot.send_message(message.chat.id, 'Здраствуйте {0} {1} вас приветствует бот компании {2} \n'
                     .format(message.from_user.first_name, message.from_user.last_name, 'MitLabs', reply_markup=keyboard))





# url_ya = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
# url_mit = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании", url="https://mitlabs.ru/")
# Стартовое приветствие
@bot.message_handler(commands=['btn'])
def default_test(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_ya = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    url_mit = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании", url="https://mitlabs.ru")
    keyboard.add(url_ya)
    keyboard.add(url_mit)
    bot.send_message(message.chat.id, "Выберите локацию:", reply_markup=keyboard)




# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    '''Добавляем в бот реакцию насообщение.'''

    bot.send_message(message.from_user.id, message.text)
    # if message.text == "Привет":
    #     bot.send_message(message.from_user.id, "Привет")
    # elif message.text == "/help":
    #     bot.send_message(message.from_user.id, "Напиши привет")
    # elif message.text == "1":
    #     bot.send_message(message.from_user.id, "1")
    # else:
    #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")




# Описание возможностей бота
@bot.message_handler(commands=['help'])
async def process_help_command(message):
    message.reply("Возможности данного бота: 1 2 3 4 5 ... ")






# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)