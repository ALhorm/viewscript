from PySide6.QtWidgets import QMainWindow, QWidget
from .Window import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def add_widget(self, widget: QWidget):
        self.ui.main_layout.addWidget(widget)
