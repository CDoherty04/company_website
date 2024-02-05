import smtplib
import ssl


def send_email(message):

    username = "charlieedoherty@gmail.com"
    receiver = "charlieedoherty@gmail.com"
    password = ""
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
