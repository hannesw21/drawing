from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Draw")

        self.setMinimumSize(600, 600)

        central_widget = CentralWidget(self)
        self.setCentralWidget(central_widget)
