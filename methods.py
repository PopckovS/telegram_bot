from flaskSQLalchemy import db
import config

# Импортируем Модели
from models.User import Telegram_User as User
from models.Messages import Telegram_Messages as Messages



def convert_trace(func_trace):
    '''Метод декоратор(обертка) для методов отладки.'''
    def result_func(arg1):
        print('========================')
        func_trace(arg1)
        print('========================')
    return result_func


@convert_trace
def trace(object):
    '''Метод отладчик, выводи ID и текст сообщения'''
    print(object)
    print(type(object))


@convert_trace
def tracem(message):
    '''Метод отладчик, выводи ID и текст сообщения'''
    print(f'id сообщения = {message.message_id}')
    print(f'text сообщения =  {message.text}')




def save_message(message, text='', mod='user'):
    '''Метод сохраняет в Бд переданное сообщение, сохранение
    может быть как сообщений пользователю боту, так и бота пользователю
    recepient - string сохранение сообщения от кого кому
        user Сохраняется как сообщение от пользователя к телеграм боту
        bot  Сохраняется как сообщение от бота к пользователю
    '''

    if mod is 'user':
        # Сохранение сообщения от пользователя к боту
        message = Messages(telegramID=message.chat.id, message=message.text, recipient=config.BOT_ID, messageID=message.message_id)
    elif mod is 'bot':
        # Сохранение сообщения от бота пользователю
        message = Messages(telegramID=config.BOT_ID, message=text, recipient=message.chat.id, messageID=message.message_id)

    db.session.add(message)
    db.session.commit()




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