from flaskSQLalchemy import db
from datetime import datetime

'''
Для поля created_on определяется дефолт значение datetime.utcnow а не его вызов datetime.utcnow()

1 - Аргумент
db.Text() - Текст
db.String(255) - Varchar 255 символов
db.Integer() - Число
db.DateTime() - Время datetime

2 - Аргумент 
default = value  Дефолтное значение
primary_key=True Сделать первичным ключем
nullable = False Принимает null или нет
'''

class Telegram_User(db.Model):
    '''Модель для работы с таблицей Users'''
    __tablename__ = 'Telegram_User'

    id = db.Column(db.Integer(), primary_key=True)
    telegramID = db.Column(db.Integer(), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    username = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)

    create_project = db.Column(db.Integer(), default=0, nullable=False)
    bot_command = db.Column(db.Integer(), default=0, nullable=False)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)



    def __repr__(self):
        # return "<{}:{}>".format(self.id, self.telegramID, self.username)
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "telegramID={}\n" \
               "first_name={}\n" \
               "last_name={}\n" \
               "username={}\n" \
               "type={}\n" \
               "bot_command={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.telegramID,
            self.first_name,
            self.last_name,
            self.username,
            self.type,
            self.bot_command,
            self.created_on,
            self.updated_on
        )

    # Ilya
    # Baranov
    # farberling_ti
    # Fghc@ggdf.ru
    # 87896468860
    # Qq