# from flaskDB import db
from flaskSQLalchemy import db
from datetime import datetime

class Brif(db.Model):
    '''Модель для работы с таблицей Projects
    где собраны данные о проекте клиента, и контактная информация.'''
    __tablename__ = 'Brif'

    # Поля id и telegramID по которому пользователь идентифицирован в телеграмме
    id = db.Column(db.Integer(), primary_key=True)
    telegramID = db.Column(db.Integer(), nullable=False)

    full_name = db.Column(db.Text(), nullable=True)
    contact_info = db.Column(db.Text(), nullable=True)
    area_of_activity = db.Column(db.Text(), nullable=True)
    brend = db.Column(db.Text(), nullable=True)
    brend_geography = db.Column(db.Text(), nullable=True)
    task = db.Column(db.Text(), nullable=True)
    competitors = db.Column(db.Text(), nullable=True)
    services = db.Column(db.Text(), nullable=True)
    language_version = db.Column(db.Text(), nullable=True)
    information_materials = db.Column(db.Text(), nullable=True)
    restrictions_for_website = db.Column(db.Text(), nullable=True)
    interactions_sites = db.Column(db.Text(), nullable=True)
    logo = db.Column(db.Text(), nullable=True)
    like_sites = db.Column(db.Text(), nullable=True)
    brand_strategy = db.Column(db.Text(), nullable=True)
    seo = db.Column(db.Text(), nullable=True)
    social_networks = db.Column(db.Text(), nullable=True)
    another_information = db.Column(db.Text(), nullable=True)

    # Даты созданияи обновления
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def description(self):
        return {
                'full_name':'Полное название компании',
                'contact_info':'Контактная информация',
                'area_of_activity':'Область деятельности',
                'brend':'Бренд',
                'brend_geography':'География бренда',
                'task':'Что нужно сделать?',
                'competitors':'Прямые и косвенные конкуренты',
                'services':' Сервисы сайта',
                'language_version':'Публикация иностранных версий',
                'information_materials':'Информационные материалы для сайта?',
                'restrictions_for_website':'Ограничения для разработки сайта',
                'interactions_sites':'Взаимодействия со сторонними сайтами',
                'logo':'Логотип или фирменный стиль компании',
                'like_sites':'Какие сайты вам нравятся',
                'brand_strategy':'Существует ли стратегия продвижения бренда ?',
                'seo':'Расчет стоимости продвижения сайта в поисковых системах ?',
                'social_networks':'Продвижения проекта в социальных сетях? ',
                'another_information':'Дополнительные материалы к брифу',
                }


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