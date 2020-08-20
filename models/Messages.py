# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class Telegram_Messages(db.Model):
    '''Модель для работы с таблицей Messages
    Хранит все сообщения для бота telegram'''

    __tablename__ = 'Telegram_Messages'

    id = db.Column(db.Integer(), primary_key=True)
    telegramID = db.Column(db.Integer(), nullable=False)
    recipient = db.Column(db.Integer(), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    messageID = db.Column(db.Integer(), nullable=False)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "telegramID={}\n" \
               "recipient={}\n" \
               "message={}\n" \
               "messageID={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.telegramID,
            self.recipient,
            self.message,
            self.messageID,
            self.created_on,
            self.updated_on
        )