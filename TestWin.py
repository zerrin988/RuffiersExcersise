from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from Variables import *

#this class is the testWindow class
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.UI()
        self.connect()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(textTw)
        self.resize(winW, winH)
        self.move(winX, winY)

    def UI(self):
        self.line = QHBoxLayout()

        self.desc1 = QLineEdit(fullName)
        self.desc2 = QLineEdit(fullYears)
        self.desc3 = QLineEdit(firstTest)
        self.desc4 = QLineEdit(finalTest)
        self.desc5 = QLineEdit(finalTest1)

        self.t1 = QLabel(text1)
        self.t2 = QLabel(text2)
        self.t3 = QLabel(text3)
        self.t4 = QLabel(text4)
        self.t5 = QLabel(text5)
        self.tTimer = QLabel(textTimer)

        self.b1 = QPushButton(button1)
        self.b2 = QPushButton(button2)
        self.b3 = QPushButton(button3)
        self.b4 = QPushButton(button4)

        self.layoutUI.addWidget(self.textMainUI)
        self.layoutUI.addWidget(self.instructionUI)
        self.layoutUI.addWidget(self.buttonUI)
        self.setLayout(self.layoutUI)
    
    def connect(self):
        self.buttonUI.clicked.connect(self.nextClick)

    def nextClick(self):
        self.hide()
        self.tw = TestWin()