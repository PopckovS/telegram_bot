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
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Привет', 'Пока')

    bot.send_message(message.chat.id, 'Здраствуйте {0} {1} вас приветствует бот компании MitLabs \n'
                     .format(message.from_user.first_name, message.from_user.last_name), reply_markup=keyboard1)






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
    await message.reply("Возможности данного бота: 1 2 3 4 5 ... ")






# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)