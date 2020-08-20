# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class Telegram_Type(db.Model):
    '''Модель для работы с таблицей Types
    В таблице определены типы, к которым относится конкретный пользователь
    '''
    __tablename__ = 'Telegram_Type'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
	    return "<{}:{}>".format(self.id,  self.title[:10])