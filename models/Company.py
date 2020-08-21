from flaskSQLalchemy import db
from datetime import datetime


class Company(db.Model):
    '''Модель для работы с таблицей Company'''
    __tablename__ = 'Company'

    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(255), nullable=True)
    caption = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    requisites = db.Column(db.Text(), nullable=True)
    facts = db.Column(db.Text(), nullable=True)
    phone = db.Column(db.String(50), default=0, nullable=True)

    # Поле для связи 1 ко Многим
    CompanyDescription = db.relationship('CompanyDescription', backref='Company')

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
               "phone={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.name,
            self.caption,
            self.email,
            self.requisites,
            self.phone,
            self.created_on,
            self.updated_on
        )
