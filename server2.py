#! /usr/bin/python3


import config
import requests
from flaskSQLalchemy import db

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response
from flask_sqlalchemy import SQLAlchemy

# Импортируем Модели
from models.Projects import Telegram_Projects as Projects
from models.User import Telegram_User as User
from models.Messages import Telegram_Messages as Messages
from models.Admin import Telegram_Admin as Admin
from models.Company import Company

# Запускаем сервер на lask
app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = config.CONNECT_DB

# Создаем подключение к БД
db = SQLAlchemy(app)
db.create_all()


@app.route("/create")
def page_index():
    company = Company(name='11', caption='22', email='33', requisites='44',
                      facts='55', phone='66')
    db.session.add(company)
    db.session.commit()

@app.route("/sh")
def page_show():
    company = db.session.query(Company).all()

    print(company)
    print('==================')
    print(company.__repr__())



if __name__ == "__main__":
    app.run(debug=True, port=5000)


