from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QScrollArea


class MessageViewer(QWidget):
    def __init__(self, sender, subject, content):
        super().__init__()
        self.delegate = None
        self.setLayout(QGridLayout())
        self.scrollWidget = QScrollArea()
        self.fromLbl = QLabel("From: ")
        self.subjectLbl = QLabel("Subject: ")
        self.contentLbl = QLabel("Content: ")
        self.fromOutput = QLineEdit()
        self.fromOutput.setText(sender)
        self.fromOutput.setReadOnly(True)
        self.subjectOutput = QLineEdit()
        self.subjectOutput.setText(subject)
        self.subjectOutput.setReadOnly(True)
        self.contentOutput = QTextEdit()
        self.contentOutput.setReadOnly(True)
        self.contentOutput.append(content)
        self.layout().addWidget(self.fromLbl, 0, 0)
        self.layout().addWidget(self.subjectLbl, 1, 0)
        self.layout().addWidget(self.contentLbl, 2, 0)
        self.layout().addWidget(self.fromOutput, 0, 1)
        self.layout().addWidget(self.subjectOutput, 1, 1)
        self.layout().addWidget(self.contentOutput, 2, 1)