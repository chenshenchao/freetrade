from PySide6.QtWidgets import QWidget
from .panelzone_ui import Ui_PanelZone

class PanelZone(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PanelZone()
        self.ui.setupUi(self)
        