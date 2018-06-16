from PyQt5.QtWidgets import QTabWidget, QWidget


class ConfigWindow (QTabWidget):
    def __init__(self, parent):
        super().__init__()
        self.displayTab = QWidget()
        self.accountTab = QWidget()
        self.addTab(self.displayTab, "Display")
        self.addTab(self.accountTab, "Account")
        self.delegate = parent.delegate

