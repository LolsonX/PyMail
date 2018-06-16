import imapclient
import pyzmail
from datetime import datetime

from PyMailMessage import Message


class ReceiverModel:
    def __init__(self):
        self.view = None
        self.delegate = None
        self.messages = []
        self.login = None
        self.password = None
        self.server = None
        self.port = None

    def receive_messages(self):
        self.askForConfig()
        connection = imapclient.IMAPClient(self.server, ssl=True, port=self.port)
        connection.login(self.login, self.password)
        connection.select_folder('INBOX', readonly=True)
        uids = connection.search("ALL")
        for uid in uids:
            htmlPart = ""
            textPart = ""
            rawMessage = connection.fetch(uid, 'BODY[]')
            formattedMessage = pyzmail.PyzMessage.factory(rawMessage[uid][b"BODY[]"])
            sender = formattedMessage.get_decoded_header("From")
            subject = formattedMessage.get_decoded_header("Subject")
            date = formattedMessage.get_decoded_header("Date").split(",")[-1]
            date = date.lstrip()
            try:
                if formattedMessage.text_part:
                    textPart = formattedMessage.text_part.get_payload().decode(formattedMessage.text_part.charset)
                if formattedMessage.html_part:
                    htmlPart = formattedMessage.html_part.get_payload().decode(formattedMessage.html_part.charset)
                content = textPart + htmlPart
            except Exception:
                content = "Unable to load charset"
            self.messages.insert(0, Message(sender, subject, date, content, uid))
            if len(self.messages) >=20:
                break
        connection.logout()

    def showMessage(self, uid):
        for mess in self.messages:
            if uid == mess.uid:
                print("Step")
                self.delegate.showMessage(mess)
                break

    def askForConfig(self):
        config = self.delegate.askForConfig(self)
        self.login = config[0]
        self.password = config[1]
        self.server = config[2]
        self.port = config[3]