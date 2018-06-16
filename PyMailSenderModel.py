import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException


class SenderModel:
    def __init__(self):
        self.delegate = None
        self.SMTPServer = None
        self.SMTPPort = None
        self.login = None
        self.password = None

    def sendMessage(self):
        self.askForConfig()
        connection = smtplib.SMTP_SSL(self.SMTPServer, self.SMTPPort)
        self.signIn(connection)

    def signIn(self, connection):

        connection.login(self.login, self.password)
        to, subject, content = self.delegate.getEMailInfo()
        msg = MIMEText(content.encode('utf-8'), _charset='utf-8')
        msg["From"] = self.login
        msg["To"] = to
        msg["Subject"] = subject
        connection.sendmail(self.login, to, "Subject: " + subject + "\n" + msg.as_string())

    def askForConfig(self):
        config = self.delegate.askForConfig(self)
        self.login = config[0]
        self.password = config[1]
        self.SMTPServer = config[2]
        self.SMTPPort = config[3]

    def parseConfig(self, config):
        '''self.imapServer = config["imap"]["server"]
        self.imapPort = config["imap"]["server"]
        self.login = config["logged"]
        self.password = config ["loggedpass"]'''
        pass
