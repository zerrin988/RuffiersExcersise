from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from Variables import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.UI()
        self.connect()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(textFw)
        self.resize(winW, winH)
        self.move(winX, winY)