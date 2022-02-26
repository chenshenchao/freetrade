from PySide6.QtWidgets import QWidget
from .loginzone_ui import Ui_LoginZone

class LoginZone(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginZone()
        self.ui.setupUi(self)