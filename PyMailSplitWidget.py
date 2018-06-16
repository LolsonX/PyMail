from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCalendarWidget, QScrollArea

from PyMailConfigWindow import ConfigWindow
from PyMailMessageViewer import MessageViewer
from PyMailReceiverModel import ReceiverModel
from PyMailReceiverView import ReceiverView


class SplitWidget(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.leftWidget = QScrollArea(self)
        self.rightWidget = QWidget()
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.leftWidget)
        self.layout().addWidget(self.rightWidget)

    def resizeWidget(self):
        self.leftWidget.setMaximumWidth(int(self.parent.width() * 0.3))
        self.rightWidget.setMaximumWidth(int(self.parent.width() * 0.7))

    def changeRightWidget(self, newWidget):
        assert isinstance(newWidget, QWidget)
        self.layout().removeWidget(self.rightWidget)
        self.rightWidget.setParent(None)
        self.rightWidget = newWidget
        self.layout().addWidget(self.rightWidget)
        self.resizeWidget()

    def changeLeftWidget(self, newWidget):
        assert isinstance(newWidget, QWidget)
        if isinstance(newWidget, ReceiverView):
            tmp = QScrollArea(self)
            newWidget.model = ReceiverModel()
            newWidget.addButtons()
            tmp.setWidget(newWidget)
            newWidget = tmp
        self.layout().removeWidget(self.leftWidget)
        self.layout().removeWidget(self.rightWidget)
        self.leftWidget.setParent(None)
        self.leftWidget = newWidget
        self.layout().addWidget(self.leftWidget)
        self.layout().addWidget(self.rightWidget)
        self.resizeWidget()
