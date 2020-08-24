# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class BrifDescription(db.Model):
    '''Модель для работы с таблицей BrifDescription
    Для хранения информации о самом БРИФЕ.'''
    __tablename__ = 'BrifDescription'

    # Поля id и telegramID по которому пользователь идентифицирован в телеграмме
    id = db.Column(db.Integer(), primary_key=True)

    # Поле со связью 1::M Указывает к какому брифу конкретно принадлежит данное поле
    Brif_id = db.Column(db.Integer(), db.ForeignKey('Brif.id'))

    # Поля хранят название поля для БРИФА и его описание, и ответ пользователя на данный вопрос
    name = db.Column(db.Text(), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    answer = db.Column(db.Text(), nullable=True)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)



    # def __repr__(self):
	#     # return "<{}:{}>".format(self.id, self.telegramID, self.username)
    #     '''Возвращает все поля текущего обьекта.'''
    #     return "id={}\n" \
    #            "telegramID={}\n" \
    #            "email={}\n" \
    #            "fio={}\n" \
    #            "phone={}\n" \
    #            "aboutProject={}\n" \
    #            "created_on={}\n" \
    #            "updated_on={}".format(
    #         self.id,
    #         self.telegramID,
    #         self.email,
    #         self.fio,
    #         self.phone,
    #         self.aboutProject,
    #         self.created_on,
    #         self.updated_on
    #     )