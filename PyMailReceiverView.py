from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from functools import partial

from PyMailReceiverModel import ReceiverModel


class ReceiverView(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.model = None
        self.delegate = None

    def addButtons(self):

        for mess in self.delegate.listOfMessages():
            button = QPushButton(mess.subject)
            button.clicked.connect(partial(self.delegate.askForMessage, mess.uid))
            self.layout().addWidget(button)