
# popckovM5@yandex.ru
# IremOfPilars
# smtp.yandex.ru
# 465


import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

addr_from = "popckovM5@yandex.ru"
addr_to   = "popckovM5@yandex.ru"
password  = "IremOfPilars"

msg = MIMEMultipart()
msg['From']    = addr_from
msg['To']      = addr_to
msg['Subject'] = 'Тема сообщения'

body = "Текст сообщения"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.yandex.ru', 465)
server.set_debuglevel(True)
server.starttls()
server.login(addr_from, password)
server.send_message(msg)
server.quit()