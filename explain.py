'''Тут собрано описание того как работать с Модулем pyTelegramBotAPI

bot = telebot.TeleBot(config.key_api) - Импортируем модуль telebot, и создаем экземпляр его класса,
передаем ему API ключ для нашего бота< через который и будет аутентификация.

@bot.message_handler(commands=['start']) - Метод обертка, указывает о принятии команды.
Начало работы с любым ботом ы телеграмме начинается с команды /start данный метод будет
работать первым при старте общения.


ReplyKeyboardMarkup - создает шаблоны сообщений которые может отправлять пользователь, только то что написано
может быть отправлено.

InlineKeyboardMarkup - настоящая кастомная клавиатура. Она привязывается к сообщению, с которым была отправлена.
Инлайн кнопки позволяют скрыть в себе внутреннюю телеграм ссылку, ссылку на внешний ресурс, а также шорткат для инлайн запроса.





keyboard = telebot.types.InlineKeyboardMarkup()
btn_url_mitlabs = telebot.types.InlineKeyboardButton(text="Перейти на сайт компании MitLabs", url="https://mitlabs.ru")
keyboard.add(btn_url_mitlabs)

bot.send_message(message.chat.id, 'Здраствуйте {0} {1} вас приветствует бот компании {2} \n'
                 .format(message.from_user.first_name, message.from_user.last_name, 'MitLabs', reply_markup=keyboard))'''