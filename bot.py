#! /usr/bin/python3

import re
import config

from mitlabs import MitLabs
from methods import *
from commands import *

# pip3 install emoji
# Библиотека для работы
from emoji import emojize
from random import choice

#
# Создаем экземляр класса для получения из него данных о компании
mt = MitLabs()



@bot.message_handler(commands=['test'])
def test(message):
    # smile = emojize(choice(config.SMILE), use_aliases=True)
    # smile = emojize('\ud83d\ude17', use_aliases=True)
    smile = emojize('\N{grinning face}', use_aliases=True)
    bot.send_message(message.from_user.id, 'Рандомно выбран emoji = ' + smile)
    bot.send_sticker(message.chat.id, 'CAADBQADiQMAAukKyAPZH7wCI2BwFxYE')



# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    # Сохраняем информацию о сообщении,акимбы оно не было
    save_message(message)

    user = db.session.query(User).filter(User.telegramID == message.chat.id).first()

    print('========================')
    print(message.message_id)
    print('========================')

    if user.bot_command == 0:
        if message.text == 'Наши реквизиты':
            save_message(message, "Пользователю показан блок 'Наши реквизиты'", 'bot')
            bot.send_message(message.from_user.id, mt.get_requisites())
        elif message.text == 'Наши услуги':

            # !!! НЕ ЗНАЮ ПО ЧЕМУ И КАК, НО ОПЫТНЫМ ПУТЕМ ВЫЯСНИЛ, ЧТО ЕСТЬ ОГРАНИЧЕНИЕ !!!
            # !!! НА ДЛИННУ СТРОКИ ПРИ СТАВКИ ЗНАЧЕНИЯ В callback_data В ДОКАХ ПРО ЭТО НИЧЕГО!!!
            keyboard = telebot.types.InlineKeyboardMarkup()

            btn1 = telebot.types.InlineKeyboardButton(text='Дизайн от А до Я', callback_data='Дизайн от А до Я')
            btn2 = telebot.types.InlineKeyboardButton(text='Маркетинг', callback_data='Маркетинг')
            btn3 = telebot.types.InlineKeyboardButton(text='Разработка сайта', callback_data='Разработка сайта')
            btn4 = telebot.types.InlineKeyboardButton(text='E-COMMERCE', callback_data='E-COMMERCE')
            btn5 = telebot.types.InlineKeyboardButton(text='DEVOPS', callback_data='DEVOPS')
            btn6 = telebot.types.InlineKeyboardButton(text='AI И ML', callback_data='AI И ML')
            em1 = emojize('\N{page facing up}', use_aliases=True)
            btn7 = telebot.types.InlineKeyboardButton(text= em1 + ' Документы и право', callback_data='Документы и право')

            keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

            em2 = emojize('gear', use_aliases=True)
            save_message(message, "Пользователю показан блок 'Услуг Компании'", 'bot')
            bot.send_message(message.chat.id, f"{em2} Услуги компании:", reply_markup=keyboard)

        elif message.text == 'Факты о нас':
            save_message(message, "Пользователю показан блок 'Факты о нас'", 'bot')
            bot.send_message(message.from_user.id, mt.get_facts())
        elif message.text == 'Расчитать стоимость проекта':
            # bot.send_sticker(message.chat.id, 'CAADBQADiQMAAukKyAPZH7wCI2BwFxYE')
            # Тут мы задаем пользователб вопрос, с которого начинается цикл вопросов пользователю
            bot.send_message(message.from_user.id, "Как Вас зовут?")
            save_message(message, "Как Вас зовут?", 'bot')
            bot.register_next_step_handler(message, get_name)
        elif message.text == 'Говорить с нашим Менеджером':
            send_contacts_manager(message)
        elif message.text == 'Говорить с нашим Менеджером в чате этого бота':
            send_contacts_manager(message)
        else:
            bot.send_message(message.from_user.id, 'Я вас не понимаю :( Чем я могу тебе помочь?')
            save_message(message, 'Я вас не понимаю :( Чем я могу тебе помочь?', 'bot')



def send_contacts_manager(message):
    '''Показать клиенту контакты наших менеджеров.'''


    # bot.send_message(message.chat.id, "Доступные контакты:", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Доступные контакты:")


    bot.send_message(message.from_user.id, "Руководитель проектов\nМария Преснякова\n+79056542592\nEmail: mp@mitlabs.ru\nТелеграм: https://t.me/ma_svarchuk")


    bot.send_message(message.from_user.id, "Системный маркетинг\nДарина Терехова\n+79515521503\nEmail: dt@mitlabs.ru\nТелеграм: https://t.me/nemayakovsky")

    # btn1 = telebot.types.InlineKeyboardButton(
    #     text='Руководитель проектов\nМария Преснякова\n+79056542592\nEmail: mp@mitlabs.ru\nТелеграм: https://t.me/ma_svarchuk', callback_data='Мария Преснякова')
    # btn2 = telebot.types.InlineKeyboardButton(
    #     text='Системный маркетинг\nДарина Терехова\n+79515521503\nEmail: dt@mitlabs.ru\nТелеграм: https://t.me/nemayakovsky', callback_data='Дарина Терехова')


    # keyboard.add(btn1, btn2)

    save_message(message, "Пользователю показаны контакты Менеджеров'", 'bot')





@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    '''Метод обработчик нажатых Inline кнопок, тоесть заранее заготов.кнопок меню.'''

    if call.message:

        # Это для обработки запроса на показ Услуг компании.
        # Если callback_data что была передана есть в массиве данных
        if call.data in mt.get_price():
            list_price = mt.get_price()
            # По ключу что был передан в callback_data получаю значение и вывожу пользователю
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=list_price[call.data])

        if call.data == 'project_yes':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Прекрасно, продолжим')


        if call.data == 'project_no':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо, давайте с начала')
            # bot.send_message(call.message.from_user.id, 'Хорошо, давайте с начала')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как Вас зовут?')
            # bot.send_message(call.message.from_user.id, "Как Вас зовут?")
            bot.register_next_step_handler(call.message, get_name)
    # Если сообщение из инлайн-режима
    # elif call.inline_message_id:
    #     if call.data == "test":
    #         bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")












# Это ПОТОК команд, метод register_next_step_handler регистрирует ряд методов
# которые будут выполняться последовательно, один за другим, создавая и устанавливая
# в нутри методов циклы, можно зациклить эти вопросы, до тех пор пока мы не получим
# нужный результат, а если пользователь хочет выйти из потока методов, то мы можем
# сделать исключение при помощи InlineKeyboardButton и просто не регистрировать
# следующего метода, а просто выйти из потока методов.
def get_name(message):

    '''Метод получает от пользователя Имя Фамилию по установленному паттерну'''

    # Сохраняем ФИО пользователя в БД
    # user = User(telegramID=message.chat.id, fio=message.text)

    # Обновляем поле fio в БД, по ее message.chat.id тоесть по ник id пользователя в телеграмме.
    # project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    # Сохраняяем ФИО пользователя в поле fio модели Projects
    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    # Если такого пользователя не существует, то создадим нового,
    # если существует то уже его изьяли, используем.
    if project is None:
        project = Projects(telegramID=message.chat.id, fio=message.text)

    db.session.add(project)
    db.session.commit()

    # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
    save_message(message)
    save_message(message, "Ваш email ?", 'bot')

    em = emojize('\N{envelope}', use_aliases=True)
    bot.send_message(message.from_user.id, f'Ваш email {em} ?')
    bot.register_next_step_handler(message, get_email)

    # keyboard = telebot.types.InlineKeyboardMarkup()
    # btn_no_email = telebot.types.InlineKeyboardButton(text='Да все верно', callback_data='no_email')
    # keyboard.add(btn_no_email)
    #
    # bot.send_message(message.from_user.id, 'Ваш email ?')
    # bot.register_next_step_handler(message, get_email)

#     keyboard = telebot.types.InlineKeyboardMarkup()
#     btn_yes = telebot.types.InlineKeyboardButton(text='Да все верно', callback_data='project_yes')
#     btn_no = telebot.types.InlineKeyboardButton(text='Нет, заполнить с начала', callback_data='project_no')
#     keyboard.add(btn_yes, btn_no)



def get_email(message):
    '''Метод получает от пользователя email'''

    result = re.search(r'[\w.-]+@[\w.-]+\.?[\w]+?', message.text)

    if result == None:

        # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
        save_message(message)
        save_message(message, "Кажется, это неправильный email :( Попробуй еще раз!", 'bot')

        bot.send_message(message.from_user.id, 'Кажется, это неправильный email :( Попробуй еще раз!')
        bot.register_next_step_handler(message, get_email)
    else:
        # Email введен правильно, сохраняем его в БД
        # Обновляем поле email в БД, по ее id
        # Сохраняяем Почту проекта в поле email модели Projects
        project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
        project.email = message.text
        db.session.add(project)
        db.session.commit()

        # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
        save_message(message)
        save_message(message, "Ваш телефон ?", 'bot')

        em = emojize('☎', use_aliases=True)
        bot.send_message(message.from_user.id, f'{em} Ваш телефон  ?')
        bot.register_next_step_handler(message, get_phone)




def get_phone(message):
    '''Метод получает от пользователя телефон'''

    result = re.search(r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b", message.text)

    if result == None:

        # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
        save_message(message)
        save_message(message, "Кажется, это неправильный телефона :( Попробуй еще раз!", 'bot')

        bot.send_message(message.from_user.id, 'Кажется, это неправильный телефона :( Попробуй еще раз!')
        bot.register_next_step_handler(message, get_phone)
    else:
        # Если мы попали сюда, то телефон введен правильно, и мы его сохраняем.
        # Обновляем поле phone в БД, по ее id
        # Сохраняяем Телефон проекта в поле phone модели Projects
        project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
        project.phone = message.text
        db.session.add(project)
        db.session.commit()

        # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
        save_message(message)
        save_message(message, "Расскажите о Вашем проекте", 'bot')

        bot.send_message(message.from_user.id, 'Расскажите о Вашем проекте')
        bot.register_next_step_handler(message, get_about_project)




def get_about_project(message):

    # Сохраняяем Описание проекта в поле aboutProject модели Projects
    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    project.aboutProject = message.text
    db.session.add(project)
    db.session.commit()

    # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
    save_message(message)
    save_message(message, "Пользователю задан вопрос 'Правильно ли он заполнил данные'", 'bot')

    # ======================= Новая версия ======================
    keyboard = get_btn_project() # Добавляем кнопки к результату заполнения опроса
    result_text = f"Все правильно ? \nВас зовут = {project.fio}"
    result_text += f'\nВаш email = {project.email}'
    result_text += f'\nВаш телефон = {project.phone}'
    result_text += f'\nОписание проекта = {project.aboutProject}'
    # ======================= Старая версия ======================
    # keyboard = get_btn_project() # Добавляем кнопки к результату заполнения опроса
    # result_text = f"Все правильно ? \nВас зовут = {name}"
    #
    # if not email == '':
    #     result_text += f'\nВаш email = {email}'
    # if not phone == '':
    #     result_text += f'\nВаш телефон = {phone}'
    #
    # result_text += f'\nОписание проекта = {about_project}'
    # =============================================

    bot.send_message(message.from_user.id, result_text, reply_markup=keyboard)
    bot.register_next_step_handler(message, get_answer)

    # save_message(message, "Пользователю задан вопрос 'Правильно ли заполнил данные'", 'bot')

    # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
    # save_message(message)
    # save_message(message, "Пользователю задан вопрос 'Правильно ли заполнил данные'", 'bot')

    # msg = bot.send_poll(message.chat.id, 'Оцените работу бота', options=['Ужасно', 'Рок группа "Dark Funeral" полное го*но !', 'Хорошо'])
    # all_response.chat_id = msg.chat.id


# Завершающий вопрос о правильности заполнения данных.
def get_answer(message):
    save_message(message)


def get_btn_project():
    '''Создаем и добавляем inline кнопки, да/нет для продолжения или сброса опроса'''

    keyboard = telebot.types.InlineKeyboardMarkup()

    emoji_yes = emojize('✅', use_aliases=True)
    emoji_no = emojize('❌', use_aliases=True)

    btn_yes = telebot.types.InlineKeyboardButton(text=f'{emoji_yes} Да все верно', callback_data='project_yes')
    btn_no = telebot.types.InlineKeyboardButton(text=f'{emoji_no} Нет, заполнить с начала', callback_data='project_no')
    keyboard.add(btn_yes, btn_no)

    return keyboard




# Если скрипт запущен как основной, то запустить работу бота,
# Наш бот будет постоянно спрашивать у сервера телеграмма, ввел что либо пользователь.
# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
