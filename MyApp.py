from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from TestWin import *
from Variables import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.UI()
        self.connect()
        self.show()

    def set_appear(self): 
        self.setWindowTitle(textMain)
        self.resize(winW, winH)
        self.move(winX, winY)

    def UI(self):
        self.textMainUI = QLabel(textMain)
        self.instructionUI = QLabel(textInstruction)
        self.buttonUI = QPushButton(textNext)

        self.layoutUI = QVBoxLayout()

        self.layoutUI.addWidget(self.instructionUI)
        self.layoutUI.addWidget(self.buttonUI)
        self.setLayout(self.layoutUI)
    
    def connect(self):
        self.buttonUI.clicked.connect(self.nextClick)

    def nextClick(self):
        self.hide()
        self.tw = TestWin()

application = QApplication([])
mainWindow = MainWin()
application.exec_()