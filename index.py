'''Простой Telegram-бот на Python

Официальная документация находится по адресу.
https://github.com/eternnoir/pyTelegramBotAPI

Регистрируем бота через @BotFather, надо написать ему /start или /newbot
Заполняем поля, название бота и его короткое имя,
После получаем сообщение с токеном бота и ссылкой на документацию.
Сам токен это ед.ключ для взаимодействия с ним.

Писать будем на PyTelegramBotAPI. команда установки:
pip install pytelegrambotapi

Телеграмм умеет сообщать боту о действиях пользователя двумя способами:
1) через ответ на запрос сервера (Long Poll).
2) через Webhook,  когда сервер Телеграмма сам присылает
сообщение о том, что кто-то написал боту.

Второй способ - требует выделенного IP-адреса, и установленного SSL на сервере
Тут будем пользоваться первым методом - Long Poll

Для использования метода Long Poll можно использовать сервис Windscribe
но его бесплатная версия имеет ограничение в 10 .Гб трафика на месяц.

1) Есть другой способ, использование облачного сервиса, самый популярнеый Heroku.
1 - Регистрируемся на Heroku и устанавливаем его этой командой
        sudo snap install heroku --classic
2 - Авторизируемся в терминале командой
        heroku login
    Это откроет браузер со стр.входа, надо будет авторизоваться, и получим сообщение типа
    Logged in as popckovm5@yandex.ru

3 - Для работы с сервисом потребуется создать 2 файла:
    Procfile (без расширения, и записать в него эти строчки, с названием главного рабочего фалйа)
        worker: python bot.py
    requirements.txt (и записать в него)
        appdirs==1.4.3
        certifi==2018.1.18
        Cython==0.23
        Django==1.10.6
        docutils==0.13.1
        packaging==16.8
        pipenv==11.8.0
        psutil==5.0.1
        pyowm==2.8.0
        Pygments==2.2.0
        pyparsing==2.2.0
        pyTelegramBotAPI==3.6.1
        python-telegram-bot==7.0.1
        requests==2.13.0
        six==1.10.0
        virtualenv==15.1.0
        virtualenv-clone==0.3.0

4 - Деплой в Heroku:
    Создаем проект этой командой:
        heroku create
    Получаем в ответ
         ›   Warning: heroku update available from 7.42.0 to 7.42.1.
        Creating app... done, ⬢ murmuring-dawn-56959
        https://murmuring-dawn-56959.herokuapp.com/ | https://git.heroku.com/murmuring-dawn-56959.git
    Это означает что по адресу https://murmuring-dawn-56959.herokuapp.com был создан наш проект, с возможностью
    управления по типу github.
    Далее можем работать с ним как и с git репозиторием:
        git add .
        git commit -am "make it better"
        git push heroku master
    После этого проект будет запушен на сервер, теперь чтобы запустить наш worker dyno сервер
    Исполним эту команду:
        heroku ps:scale worker=1
    Теперь бот будет находиться в постоянно слушающем состоянии.
'''

