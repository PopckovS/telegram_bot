# import necessary packages

# popckovM5@yandex.ru
# IremOfPilars
# smtp.yandex.ru
# 465

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = "Thank you"

# setup the parameters of the message
password = "IremOfPilars"
msg['From'] = "popckovM5@yandex.ru"
msg['To'] = "popckovM5@yandex.ru"
msg['Subject'] = "Subscription"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
# server = smtplib.SMTP('smtp.yandex.ru: 587')
server = smtplib.SMTP('smtp.yandex.ru:465')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to")