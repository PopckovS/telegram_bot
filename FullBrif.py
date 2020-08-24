import config

from methods import trace
from methods import tracem

from bot import bot
from bot import db

from models.Brif import Brif
from models.BrifDescription import BrifDescription
from models.User import Telegram_User

class FullBrif():

    """Класс для заполнения БРИФА пользователем в боте Telegram"""

    def __init__(self):
        """ Описание Полезных функция по работе с telebot

            db.session.add(brif)
            db.session.commit()

            bot.send_message(message.from_user.id, "Системный маркетинг\nДарина Терехова\n+79515521503\nEmail: dt@mitlabs.ru\nТелеграм: https://t.me/nemayakovsky")

            keyboard = telebot.types.InlineKeyboardMarkup()
            btn_google_brif = telebot.types.InlineKeyboardButton(text="В Google форме", url=config.GOOGLE_FORM_BRIF)
            keyboard.add(btn_google_brif, btn_brif)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Где вы хотите пройти Бриф:", reply_markup=keyboard)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как Вас зовут?')
            bot.register_next_step_handler(call.message, get_name)
        """
        pass


    def start(self, message):
        '''Метод создает новый обьект БРИФА и дает старт, на регистрацию всех последующих полей для заполнения.'''

        brif = db.session.query(Brif).filter(Brif.name == config.BRIF_NAME).first()
        brif_fiels = db.session.query(BrifDescription).filter(BrifDescription.Brif_id == brif.id).all()

        trace(brif_fiels)

        for i in brif_fiels:
            trace(i.name)
            trace(i.description)

    #     if brif is None:
    #         brif = Brif(telegramID=message.from_user.id,)
    #
    #         db.session.add(brif)
    #         db.session.commit()
    #
    #     self.fiels = brif.description()
    #     trace(self.fiels)
    #     # trace(message)
    #     # trace(message.message_id)
    #     # trace(message.chat.id)
    #     # trace(brif)
    #
        # msg = [message, brif_fiels]
        self.brif_fiels = brif_fiels

        bot.send_message(message.from_user.id, '1')
        bot.register_next_step_handler(message, self.cicleRegister)


    def cicleRegister(self, msg_lit):
        bot.send_message(msg_lit.message.from_user.id, '2')
        # bot.register_next_step_handler(message, self.cicleRegister)



