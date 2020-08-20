from flaskSQLalchemy import db
from datetime import datetime


class CompanyDescription(db.Model):
    '''Модель для работы с таблицей CompanyDescription'''
    __tablename__ = 'CompanyDescription'

    id = db.Column(db.Integer(), primary_key=True)
    id

    name = db.Column(db.String(255), nullable=True)
    caption = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    requisites = db.Column(db.String(255), nullable=True)
    facts = db.Column(db.String(255), nullable=True)
    services = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(50), default=0, nullable=True)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)



    def __repr__(self):
        # return "<{}:{}>".format(self.id, self.telegramID, self.username)
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "name={}\n" \
               "caption={}\n" \
               "email={}\n" \
               "requisites={}\n" \
               "services={}\n" \
               "price={}\n" \
               "phone={}\n" \
               "bot_command={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.name,
            self.caption,
            self.email,
            self.requisites,
            self.services,
            self.price,
            self.phone,
            self.bot_command,
            self.created_on,
            self.updated_on
        )
