# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class Telegram_Projects(db.Model):
    '''Модель для работы с таблицей Projects
    где собраны данные о проекте клиента, и контактная информация.'''
    __tablename__ = 'Telegram_Projects'

    # Поля id и telegramID по которому пользователь идентифицирован в телеграмме
    id = db.Column(db.Integer(), primary_key=True)
    telegramID = db.Column(db.Integer(), nullable=False)

    # email = db.Column(db.String(255), nullable=True)
    fio = db.Column(db.String(255), nullable=True)
    # phone = db.Column(db.String(255), nullable=True)
    contacts = db.Column(db.Text(), nullable=True)
    aboutProject = db.Column(db.Text(), nullable=True)
    document = db.Column(db.Integer(), default=0, nullable=False)


    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
	    # return "<{}:{}>".format(self.id, self.telegramID, self.username)
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "telegramID={}\n" \
               "fio={}\n" \
               "aboutProject={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.telegramID,
            self.fio,
            self.aboutProject,
            self.created_on,
            self.updated_on
        )