'''

# !!! НЕ ЗНАЮ ПО ЧЕМУ И КАК, НО ОПЫТНЫМ ПУТЕМ ВЫЯСНИЛ, ЧТО ЕСТЬ ОГРАНИЧЕНИЕ !!!
# !!! НА ДЛИННУ СТРОКИ ПРИ СТАВКИ ЗНАЧЕНИЯ В callback_data В ДОКАХ ПРО ЭТО НИЧЕГО!!!


?chat_id=932670856&



                <============ getMe ===========>
/getMe
Получить информацию о самом боте

ok : true
result
    id : 1266890760
    is_bot : true
    first_name : "test_sergey_bot_2"
    username : "test_sergey_username_2_bot"
    can_join_groups : true
    can_read_all_group_messages : false
    supports_inline_queries : false



                <=========== sendMessage ===========>
/sendMessage?chat_id=932670856&text=Привет+Человек+!
Послать сообщение от лица бота,пределенному пользователю.


ok	true
result
    message_id	752
    from
        id	1266890760
        is_bot	true
        first_name	"test_sergey_bot_2"
        username	"test_sergey_username_2_bot"
    chat
        id	932670856
        first_name	"Sergey"
        last_name	"Popckov"
        username	"popkovS"
        type	"private"
    date	1597112116
    text	"Привет Человек !"



                <=========== getWebhookInfo ===========>
/getWebhookInfo
Получить информацию о установленном Вэбхуке

ok : true
result
    url	: ""
    has_custom_certificate : false ()
    pending_update_count : 7     (Количество хранящихся сообщений что небыли обработаны)



                <=========== sendContact ===========>
/sendContact?chat_id=932670856&phone_number=89525401561&first_name=Sergey&last_name=Popckov
Отправить пользователю контакт, адрес человека с его иконкой номером телефона и Именем,
По которому пользователь сможет перейти к общению с человеком.

ok	true
result
    message_id	663
    from
    id	1266890760
    is_bot	true
    first_name	"test_sergey_bot_2"
    username	"test_sergey_username_2_bot"
chat
    id	932670856
    first_name	"Sergey"
    last_name	"Popckov"
    username	"popkovS"
    type	"private"
date	1597024145
contact
    phone_number	"89525401561"
    first_name	"Sergey"
    last_name	"Popckov"
    user_id	932670856


                <=========== sendLocation ===========>
/sendLocation?chat_id=932670856&latitude=51.668194&longitude=39.208174
Дать место положение на Яндекс карте по Широта/Долгота
При успешной отправке результат возвращается.

ok	true
result
    message_id	665
    from
        id	1266890760
        is_bot	true
        first_name	"test_sergey_bot_2"
        username	"test_sergey_username_2_bot"
    chat
        id	932670856
        first_name	"Sergey"
        last_name	"Popckov"
        username	"popkovS"
        type	"private"
date	1597024710
location
    latitude	51.66821
    longitude	39.208171



                <=========== sendVenue ===========>
/sendVenue?chat_id=932670856&latitude=51.668194&longitude=39.208174&title=Mitlabs&address=г. Воронеж, Проспект Революции 33Б — 5 Этаж
Тоже самое что и метод sendLocation но с возможностью подписи, указания адреса


ok	true
result
    message_id	671
    from
        id	1266890760
        is_bot	true
        first_name	"test_sergey_bot_2"
        username	"test_sergey_username_2_bot"
    chat
        id	932670856
        first_name	"Sergey"
        last_name	"Popckov"
        username	"popkovS"
        type	"private"
    date	1597025862
    location
        latitude	51.66821
        longitude	39.208171
venue
    location
        latitude	51.66821
        longitude	39.208171
    title	"Mitlabs"
    address	"г. Воронеж, Проспект Революции 33Б — 5 Этаж"



                <=========== sendDice ===========>

                <=========== getMyCommands ===========>
/getMyCommands
Получить список всех команд для бота

'''