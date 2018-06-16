import PyMailMainWindow
from PyMailMessageViewer import MessageViewer
from PyMailReceiverModel import ReceiverModel
from PyMailSenderModel import SenderModel
from PyMailStartUpWindow import StartUpWindow


class Controller:
    def __init__(self):
        self.mainView = None
        self.mainModel = None
        self.senderView = None
        self.senderModel = None
        self.receiverView = None
        self.receiverModel = None
        self.configView = None
        self.startUpWindow = None

    def reset(self):
        self.senderView = None
        self.senderModel = None
        self.configView = None
        self.startUpWindow = None

    def transmitConfig(self):
        return self.mainModel.config

    def sendEMail(self):
        self.senderModel.sendMessage()

    def getEMailInfo(self):
        try:
            to = self.senderView.toInput.text()
        except:
            print("To error")
        try:
            subject = self.senderView.subjectInput.text()
        except:
            print("Subject error")
        try:
            content = self.senderView.contentInput.toPlainText()
        except:
            print("content error")
        return to, subject, content

    def showMessage(self, msg):
        messageView = MessageViewer(msg.sender, msg.subject, msg.content)
        self.mainView.centralWidget().changeRightWidget(messageView)

    def askForMessage(self, uid):
        self.receiverModel.showMessage(uid)

    def listOfMessages(self):
        self.receiverModel.receive_messages()
        return self.receiverModel.messages

    def setConfig(self, login, password, SMTPServer, SMTPPort, IMAPPort, IMAPServer):
        self.mainModel.login = login
        self.mainModel.password = password
        self.mainModel.SMTPServer = SMTPServer
        self.mainModel.SMTPPort = SMTPPort
        self.mainModel.IMAPServer = IMAPServer
        self.mainModel.IMAPPort = IMAPPort

    def registerView(self, view):
        if type(view) == PyMailMainWindow:
            self.mainView = view
        elif type(view) == StartUpWindow:
            self.startUpWindow = view

    def askForConfig(self, source):
        if type(source) == ReceiverModel:
            return self.mainModel.login, self.mainModel.password, self.mainModel.IMAPServer, self.mainModel.IMAPPort
        elif type(source) == SenderModel:
            return self.mainModel.login, self.mainModel.password, self.mainModel.SMTPServer, self.mainModel.SMTPPort
