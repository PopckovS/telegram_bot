import config

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response

from flask_sqlalchemy import SQLAlchemy

# Запускаем сервер на lask
app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = config.CONNECT_DB

# Создаем подключение к БД
db = SQLAlchemy(app)

