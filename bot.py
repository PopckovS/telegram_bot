#! /usr/bin/python3

import re
import config

from methods import *
from commands import *

# pip3 install emoji
# Библиотека для работы
from emoji import emojize

import FullBrif

from models.Brif import Brif
from models.BrifDescription import BrifDescription
from models.Projects import Telegram_Projects
from models.Company import Company
from models.CompanyDescription import CompanyDescription

db.create_all()



# Обьявляем метод для получения текстовых сообщений, это слушатель для
# текс сообщ, полу content_types - может приним сообщ и не не только сообщение.
# Можно указать и многое другое.
# @bot.message_handler(content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Метод обработчик любого введенного текста, также обрабатывает нажатие Inline кнопок."""

    tracem(message)
    save_message(message)

    # Получаем пользователя из БД
    user = db.session.query(User).filter(User.telegramID == message.chat.id).first()

    # Режим работы бота с пользователем, общение с человеком/ботом
    if user.bot_command == 0:
        if message.text == 'Реквизиты':

            company = db.session.query(Company).filter(Company.name == config.COMPANY).first()

            save_message(message, "Пользователю показан блок 'Наши реквизиты'", 'bot')
            bot.send_message(message.from_user.id, company.requisites)
        elif message.text == 'Наши услуги':
            keyboard = telebot.types.InlineKeyboardMarkup()

            btn1 = telebot.types.InlineKeyboardButton(text='Дизайн от А до Я', callback_data='Дизайн от А до Я')
            btn2 = telebot.types.InlineKeyboardButton(text='Маркетинг', callback_data='Маркетинг')
            btn3 = telebot.types.InlineKeyboardButton(text='Разработка сайта', callback_data='Разработка сайта')
            btn4 = telebot.types.InlineKeyboardButton(text='E-COMMERCE', callback_data='E-COMMERCE')
            btn5 = telebot.types.InlineKeyboardButton(text='DEVOPS', callback_data='DEVOPS')
            btn6 = telebot.types.InlineKeyboardButton(text='AI И ML', callback_data='AI И ML')
            em1 = emojize('\N{page facing up}', use_aliases=True)
            btn7 = telebot.types.InlineKeyboardButton(text=em1 + ' Документы и право', callback_data='Документы и право')

            keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

            save_message(message, "Пользователю показан блок 'Услуг Компании'", 'bot')
            # em2 = emojize('gear', use_aliases=True)
            bot.send_message(message.chat.id, f"Услуги компании:", reply_markup=keyboard)

        elif message.text == 'Факты о нас':
            company = db.session.query(Company).filter(Company.name == config.COMPANY).first()
            save_message(message, "Пользователю показан блок 'Факты о нас'", 'bot')
            bot.send_message(message.from_user.id, company.facts)
        elif message.text == 'Заполнить БРИФ для вашего сайта':
            '''Начало цикла заполнения информации по проекту'''
            keyboard = telebot.types.InlineKeyboardMarkup()

            btn_questions = telebot.types.InlineKeyboardButton(text='Короткий опрос', callback_data='Короткий опрос')
            btn_brif = telebot.types.InlineKeyboardButton(text='Полноценный БРИФ', callback_data='Полноценный БРИФ')
            keyboard.add(btn_questions, btn_brif)
            bot.send_message(message.from_user.id, "Есть несколько способов заполнить анкету:", reply_markup=keyboard)
        elif message.text == 'Контакты наших Менеджеров':
            send_contacts_manager(message)
        else:
            text = 'Я вас не понимаю :( Чем я могу тебе помочь?'
            bot.send_message(message.from_user.id, text)
            save_message(message, text, 'bot')







@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    '''Метод обработчик нажатых Inline кнопок, тоесть заранее заготов.кнопок меню.'''

    # Получить из БД компанию и ее описание для панельных кнопок
    company = db.session.query(Company).filter(Company.name == config.COMPANY).first()
    descriptions = db.session.query(CompanyDescription).filter(CompanyDescription.Company_id == company.id).all()

    current = None
    # Получаем текущую нажатую кнопку
    for elem in descriptions:
        if call.data == elem.title:
            current = elem

    if call.message:
        # Это для обработки запроса на показ Услуг компании.
        # Если callback_data что была передана есть в массиве данных
        if current is not None:
            # Нажатая кнопка найдена
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=current.text)
        if call.data == 'Короткий опрос':
            '''Заполнение короткой Анкеты'''
            # bot.send_message(message.from_user.id, "Есть несколько способов заполнить анкету:", reply_markup=keyboard)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Начнем заполнение анкеты:\nКак вас зовут ?")
            bot.register_next_step_handler(call.message, get_name)
        if call.data == 'Полноценный БРИФ':
            '''Выбор Какой БРИФ заполнить в Telegram/Google'''
            keyboard = telebot.types.InlineKeyboardMarkup()
            btn_brif = telebot.types.InlineKeyboardButton(text='В телеграм боте', callback_data='В телеграм боте')
            btn_google_brif = telebot.types.InlineKeyboardButton(text="В Google форме", url=config.GOOGLE_FORM_BRIF)
            keyboard.add(btn_google_brif, btn_brif)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Где вы хотите пройти Бриф:", reply_markup=keyboard)
        if call.data == 'В телеграм боте':
            '''Заполнение полноценного БРИФА пользователем в Telegram'''
            Brif_obj = FullBrif.FullBrif()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Для более четкого определения целей, стоящих перед будущим сайтом, необходимо заполнить анкету максимально подробно:")
            bot.register_next_step_handler(call.message, Brif_obj.start)
        if call.data == 'project_yes':
            # Пользователь подтвердил заполнение анкеты
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Прекрасно, мы обработаем вашу анкету.')
        if call.data == 'project_no':
            # Пользователь отказался подтвердить заполнение анкеты
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо, давайте с начала')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Как Вас зовут?')
            bot.register_next_step_handler(call.message, get_name)






def send_contacts_manager(message):
    '''Показать клиенту контакты наших менеджеров.'''

    bot.send_message(message.chat.id, "Доступные контакты:")
    bot.send_message(message.from_user.id, "Руководитель проектов\nМария Преснякова\n+79056542592\nEmail: mp@mitlabs.ru\nТелеграм: https://t.me/ma_svarchuk")
    bot.send_message(message.from_user.id, "Системный маркетинг\nДарина Терехова\n+79515521503\nEmail: dt@mitlabs.ru\nТелеграм: https://t.me/nemayakovsky")

    save_message(message, "Пользователю показаны контакты Менеджеров'", 'bot')




def get_name(message):
    '''Метод получает от пользователя Имя Фамилию по установленному паттерну'''

    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()

    if project is None:
        project = Projects(telegramID=message.chat.id, fio=message.text)
    else:
        project.fio = message.text

    db.session.add(project)
    db.session.commit()

    # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
    save_message(message)
    save_message(message, "Контактная информация ?", 'bot')

    em_email = emojize('\N{envelope}', use_aliases=True)
    em_phone = emojize('☎', use_aliases=True)
    bot.send_message(message.from_user.id, f'Контактная информация: email {em_email} телефон {em_phone} другое ?')
    bot.register_next_step_handler(message, get_contacts)



def get_contacts(message):
    '''Метод получает от пользователя контактную информацию'''
    save_message(message)

    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    project.contacts = message.text

    db.session.add(project)
    db.session.commit()

    bot_message = 'Расскажите о Вашем проекте'
    save_message(message, bot_message, 'bot')

    bot.send_message(message.from_user.id, bot_message)
    bot.register_next_step_handler(message, get_about_project)




# TODO РАЬНЬШЕ ЭТОЛТ МЕТОД ВЫПОЛНЯЛ ФУНКЦИЮ РЕГИСТРАЦИИ EMAIL ПОЛЬЗОВАТЕЛЯ, ПОКА НЕ ИСПОЛЬЗУЕТСЯ
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



# TODO РАЬНЬШЕ ЭТОЛТ МЕТОД ВЫПОЛНЯЛ ФУНКЦИЮ РЕГИСТРАЦИИ PHONE ПОЛЬЗОВАТЕЛЯ, ПОКА НЕ ИСПОЛЬЗУЕТСЯ
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
    """Метод сохраняет данные о проекте, опрашивает пользователя на правильность заполнения данных."""

    # Сохраняяем Описание проекта в поле aboutProject модели Projects
    project = db.session.query(Projects).filter(Projects.telegramID == message.chat.id).first()
    project.aboutProject = message.text
    db.session.add(project)
    db.session.commit()

    # Сохраняем и ответ пользователя на превыдущий вопрос и новый вопрос бота
    save_message(message)
    save_message(message, "Пользователю задан вопрос 'Правильно ли он заполнил данные'", 'bot')


    keyboard = get_btn_project()
    result_text = f"Все правильно ? \nВас зовут = {project.fio}"
    # result_text += f'\nВаш email = {project.email}'
    # result_text += f'\nВаш телефон = {project.phone}'
    result_text += f'\nВаши котакты = {project.contacts}'
    result_text += f'\nОписание проекта = {project.aboutProject}'

    bot.send_message(message.from_user.id, result_text, reply_markup=keyboard)
    bot.register_next_step_handler(message, get_answer)





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




# none_stop=True Опрашивать бота постоянно
# interval=0     Интервал между опросом
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
