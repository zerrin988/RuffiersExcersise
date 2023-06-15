from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from Variables import *

class FinalWin(QWidget):
    def __init__(self, ti):
        super().__init__()
        self.ti = ti
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(textFw)
        self.resize(winW, winH)
        self.move(winX, winY)

    def results():
        pass