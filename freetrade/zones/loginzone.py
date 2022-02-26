from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from .loginzone_ui import Ui_LoginZone

class LoginZone(QWidget):
    '''
    
    '''

    loginSuccessed = Signal(dict)
    

    def __init__(self, parent=None):
        '''
        
        '''
        
        super().__init__(parent)
        self.ui = Ui_LoginZone()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.onClickLoginButton)

    def onClickLoginButton(self):
        '''
        
        '''

        self.loginSuccessed.emit({})