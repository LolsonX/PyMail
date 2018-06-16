from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QAction


class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__()
        self.setMovable(False)
        exitAction = QAction(QIcon(r"res\exit.png"), "Exit", parent)
        exitAction.setStatusTip("Exit")
        exitAction.triggered.connect(parent.close)
        settingsAction = QAction(QIcon(r"res\settings.png"), "Settings", parent)
        settingsAction.setStatusTip("Settings")
        settingsAction.triggered.connect(parent.showSettings)
        helpAction = QAction(QIcon(r"res\help.png"), "Help", parent)
        helpAction.setStatusTip("Help")
        helpAction.triggered.connect(parent.showHelp)
        newAction = QAction(QIcon(r"res\new.png"), "New", parent)
        newAction.setStatusTip("New")
        newAction.triggered.connect(parent.showNewMail)
        receiveAction = QAction(QIcon(R"res\receive.png"), "Receive", parent)
        receiveAction.setStatusTip("Receive")
        receiveAction.triggered.connect(parent.receiveMail)
        self.addAction(newAction)
        self.addAction(receiveAction)
        self.addSeparator()
        self.addAction(settingsAction)
        self.addSeparator()
        self.addAction(helpAction)
        self.addSeparator()
        self.addAction(exitAction)