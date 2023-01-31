import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import from_email, password, passwordFile
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys
import subprocess

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

subject= 'КОД'
ranx=str(randint(100000,999999))

msg = MIMEMultipart()
msg['Subject'] = subject

to_email = 'ivoles1202@gmail.com'
message = 'Босс, ваш код: ' + ranx
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()

def Abeme():
    global ranx
    if form.lineEdit_2.text() == passwordFile and form.lineEdit.text() == ranx:
        subprocess.Popen('explorer "E:\SECURITY"')
        sys.exit()
    else:
        form.label_4.setText("Неверный код или пароль.")

form.pushButton.clicked.connect(Abeme)
app.exec()