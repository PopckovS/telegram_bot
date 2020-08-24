from flaskSQLalchemy import db
from datetime import datetime


class CompanyDescription(db.Model):
    '''Модель для работы с таблицей CompanyDescription'''
    __tablename__ = 'CompanyDescription'

    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(255), nullable=True)
    text = db.Column(db.Text(), nullable=True)

    # Внешний ключ для связывания с таблицей Company
    Company_id = db.Column(db.Integer(), db.ForeignKey('Company.id'))

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)



    def __repr__(self):
        # return "<{}:{}>".format(self.id, self.telegramID, self.username)
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "title={}\n" \
               "text={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.title,
            self.text,
            self.created_on,
            self.updated_on
        )
