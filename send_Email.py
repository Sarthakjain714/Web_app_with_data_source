import smtplib
import ssl
def sendEmail(message):
    host="smtp.gmail.com"
    username="jainsarthak6021@gmail.com"
    password="gait ivvh ybpg aviu"
    port = 465
    context = ssl.create_default_context()
    receiver="jainsarthak6021@gmail.com"

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
