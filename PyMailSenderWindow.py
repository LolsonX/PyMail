from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QAction


class SenderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.delegate = None
        self.setLayout(QGridLayout())
        self.toLbl = QLabel("To: ")
        self.subjectLbl = QLabel("Subject: ")
        self.contentLbl = QLabel("Content: ")
        self.toInput = QLineEdit()
        self.subjectInput = QLineEdit()
        self.contentInput = QTextEdit()
        self.sendBtn = QPushButton("Send")
        self.layout().addWidget(self.toLbl, 0, 0)
        self.layout().addWidget(self.subjectLbl, 1, 0)
        self.layout().addWidget(self.contentLbl, 2, 0)
        self.layout().addWidget(self.toInput, 0, 1)
        self.layout().addWidget(self.subjectInput, 1, 1)
        self.layout().addWidget(self.contentInput, 2, 1)
        self.layout().addWidget(self.sendBtn, 0, 2)

    def set_actions(self):
        self.sendBtn.clicked.connect(self.delegate.sendEMail)