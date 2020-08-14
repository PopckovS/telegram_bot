from flask_sqlalchemy import SQLAlchemy
from start import app
import config

# Создаем подключение к БД
app.config['SQLALCHEMY_DATABASE_URI'] = config.CONNECT_DB
db = SQLAlchemy(app)
db.create_all()