from flaskSQLalchemy import db
import config

# Импортируем Модели
from models.User import User
from models.Messages import Messages





def save_message(message, text='', mod='user'):
    '''Метод сохраняет в Бд переданное сообщение
    recepient - string сохранение сообщения от кого кому
        user Сохраняется как сообщение от пользователя к телеграм боту
        bot  Сохраняется как сообщение от бота к пользователю
    '''
    # print('================')
    # print(config.BOT_ID)
    # print('================')
    if mod is 'user':
        # Сохранение сообщения от пользователя к боту
        message = Messages(telegramID=message.chat.id, message=message.text, recipient=config.BOT_ID)
    elif mod is 'bot':
        # Сохранение сообщения от бота пользователю
        message = Messages(telegramID=config.BOT_ID, message=text, recipient=message.chat.id)

    # print(message)

    db.session.add(message)  # Вносим сообщение в сессию
    db.session.commit() # Сохраняем сообщение в БД



def save_user(message):
    '''Метод делает запрос к БД проверяет существует ли пользователь
    с таким telegramID если его не существует, то создаем нового пользователя.'''

    # Получаем первую запись из Бд с таким telegramID
    result = db.session.query(User).filter(User.telegramID == message.chat.id).first()

    # Если пользователь не существует, то создаем его
    if result is None:
        # Создаем обьект и вносим данные в его атрибуты
        user = User(
            telegramID=message.chat.id,
            first_name=message.chat.first_name,
            last_name=message.chat.last_name,
            username=message.chat.username,
            type=message.chat.type
        )

        db.session.add(user)  # Вносим пользователя в сессию
        db.session.commit()  # Сохраняем данные о пользователе в БД
        print('Новый пользователь создан')
    else:
        print('Пользователь с таким id уже существует')