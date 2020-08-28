# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class Telegram_Admin(db.Model):
    '''Модель для работы с таблицей Admin
    Хранит информацию о администраторах.'''

    __tablename__ = 'Telegram_Admin'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=True)
    telegramID = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    get_messages = db.Column(db.Integer(), default=0, nullable=False)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "name={}\n" \
               "telegramID={}\n" \
               "password={}\n" \
               "get_messages={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.name,
            self.telegramID,
            self.password,
            self.get_messages,
            self.created_on,
            self.updated_on
        )