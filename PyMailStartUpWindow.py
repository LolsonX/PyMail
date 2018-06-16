from PyQt5.QtCore import QRegExp, Qt, Qt
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QKeyEvent
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QDialog, QMessageBox


class StartUpWindow(QDialog):
    def __init__(self, parent, delegate):
        super().__init__()
        self.setWindowTitle("PyMailConfig")
        self.delegate = delegate
        self.parent = parent
        self.delegate.registerView(self)
        self.loginLbl = QLabel("EMail Adress")
        self.passwordLbl = QLabel ("Password")
        self.IMAPServerLbl = QLabel("IMAP Server")
        self.IMAPPortLbl = QLabel("IMAP Port")
        self.SMTPServerLbl = QLabel("SMTP Server")
        self.SMTPPortLbl = QLabel("SMTP Port")
        self.okBtn = QPushButton("Ok")
        self.loginInput = QLineEdit()
        self.loginInput.setValidator(QRegExpValidator(QRegExp("\S+@\S+\.\S+")))
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setValidator(QRegExpValidator(QRegExp("\S{4,}")))
        self.IMAPServerInput = QLineEdit()
        self.IMAPServerInput.setValidator(QRegExpValidator(QRegExp("\w+\.\w+\.\w+")))
        self.IMAPPortInput = QLineEdit()
        self.IMAPPortInput.setValidator(QIntValidator())
        self.SMTPServerInput = QLineEdit()
        self.SMTPServerInput.setValidator(QRegExpValidator(QRegExp("\w+\.\w+\.\w+")))
        self.SMTPPortInput = QLineEdit()
        self.SMTPPortInput.setValidator(QIntValidator())
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.loginLbl)
        self.layout().addWidget(self.loginInput)
        self.layout().addWidget(self.passwordLbl)
        self.layout().addWidget(self.passwordInput)
        self.layout().addWidget(self.IMAPServerLbl)
        self.layout().addWidget(self.IMAPServerInput)
        self.layout().addWidget(self.IMAPPortLbl)
        self.layout().addWidget(self.IMAPPortInput)
        self.layout().addWidget(self.SMTPServerLbl)
        self.layout().addWidget(self.SMTPServerInput)
        self.layout().addWidget(self.SMTPPortLbl)
        self.layout().addWidget(self.SMTPPortInput)
        self.layout().addWidget(self.okBtn)
        self.okBtn.clicked.connect(self.validate)
        self.exec_()

    def validate(self):
        IMAPServer = self.IMAPServerInput.text()
        SMTPServer = self.SMTPServerInput.text()
        IMAPPort = self.IMAPPortInput.text()
        SMTPPort = self.SMTPPortInput.text()
        login = self.loginInput.text()
        password = self.passwordInput.text()
        IMAPServerState = self.IMAPServerInput.validator().validate(self.IMAPServerInput.text(), 2)[0]
        SMTPServerState = self.SMTPServerInput.validator().validate(self.SMTPServerInput.text(), 2)[0]
        loginInputState = self.loginInput.validator().validate(self.loginInput.text(), 2)[0]
        passwordInputState = self.passwordInput.validator().validate(self.passwordInput.text(), 2)[0]
        if IMAPServerState == 2 and SMTPServerState == 2 and loginInputState == 2 and passwordInputState == 2:
            self.delegate.setConfig(login, password, SMTPServer, SMTPPort, IMAPPort, IMAPServer)
            self.accept()
        else:
            QMessageBox.about(None, "Invalid Data", "Data You entered is invalid!")

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.parent.exit()


