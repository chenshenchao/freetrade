from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    '''
    
    '''

    def __init__(self, parent =None) -> None:
        '''
        
        '''
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':/assets/freetrade.ico'))
        self.ui.login.loginSuccessed.connect(self.onLoginSuccessed)

    def onLoginSuccessed(self, info):
        '''
        
        '''

        self.ui.zones.setCurrentIndex(1)