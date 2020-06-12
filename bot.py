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
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('Наши реквизиты', 'Наши цены', 'Факты')

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

        keyboard = telebot.types.InlineKeyboardMarkup()
        list_price = mt.get_price()
        for item in list_price:
            btn = telebot.types.InlineKeyboardButton(text=item, callback_data="test")
            keyboard.add(btn)
        bot.send_message(message.chat.id, "Услуги компании:", reply_markup=keyboard)

    elif message.text == 'Факты':
        bot.send_message(message.from_user.id, mt.get_facts())
    else:
        bot.send_message(message.from_user.id, message.text)




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
















# Если скрипт запущен как основной, то запустить работу бота,
# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)