from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from Variables import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.UI()
        self.connect()
    
    def set_appear(self):
        self.setWindowTitle(textFw)
        self.resize(winW, winH)
        self.move(winX, winY)

    def UI():
        pass

    def connect():
        pass