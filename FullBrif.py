import config

from methods import trace
from methods import tracem

from bot import bot
from bot import db

from models.Brif import Brif
from models.User import Telegram_User

class FullBrif():

    '''Класс для заполнения БРИФА пользователем в боте Telegram'''

    def __init__(self):
        pass

    def start(self, message):
        '''Этот метод дает старт, на регистрацию всех последующих полей для заполнения БРИФА'''

        brif = db.session.query(Brif).filter(Brif.telegramID == message.from_user.id).first()

        if brif is None:
            brif = Brif(telegramID=message.from_user.id,)

            db.session.add(brif)
            db.session.commit()

        self.fiels = brif.description()
        bot.send_message(message.from_user.id, brif)

        trace(self.fiels)




 # bot.send_message(message.from_user.id, "Системный маркетинг\nДарина Терехова\n+79515521503\nEmail: dt@mitlabs.ru\nТелеграм: https://t.me/nemayakovsky")

# keyboard = telebot.types.InlineKeyboardMarkup()
# btn_google_brif = telebot.types.InlineKeyboardButton(text="В Google форме", url=config.GOOGLE_FORM_BRIF)
# keyboard.add(btn_google_brif, btn_brif)
# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Где вы хотите пройти Бриф:", reply_markup=keyboard)

# bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как Вас зовут?')
# bot.register_next_step_handler(call.message, get_name)