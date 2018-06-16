'''SIMPLE EMAIL CLIENT USING IMAP AND SMTP PROTOCOLS
    AUTHOR: KAROL LOLSONX OSTROWSKI
    TITLE: PYMAIL'''

import sys
from PyQt5.QtWidgets import QApplication

from PyMailController import Controller
from PyMailMainModel import MainModel
from PyMailMainWindow import PyMailMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    delegate = Controller()
    model = MainModel()
    model.delegate = delegate
    delegate.mainModel = model
    window = PyMailMainWindow(delegate)
    delegate.mainView = window
    sys.exit(app.exec_())