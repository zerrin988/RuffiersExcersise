from PyQt5.QtCore import Qt, QTimer, QTime
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
        self.desc4 = QLineEdit(FinalTest)
        self.desc5 = QLineEdit(FinalTest1)

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



    def timeTest(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time1event)
        self.timer.start(1000)
    
    def time1event(self):
        global time
        time = time.addSecs(-1)
        self.timeTest.setText(time.toString("hh:mm:ss"))

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timeSits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.time2event)
        self.timer.start(1500)

    def time2event(self):
        self.timeTest.setText(time.toString("hh:mm:ss")[6:8])

        if int(time.toString("hh:mm:ss")[6:8]) == "00":
                self.timer.stop()

    def finalTimer(self):
        global time
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.time3event)
        self.timer.start(1000)

    def time3event(self):
        self.timeTest.setText(time.toString("hh:mm:ss")[6:8])

        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.timer.setStyleSheet("rgb = [0, 255, 0]")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.timer.setStyleSheet("rgb = [255, 0, 0]")
        else:
            self.timer.setStyleSheet("rgb = [0, 0, 0]")

        if int(time.toString("hh:mm:ss")[6:8]) == "00":
            self.timer.stop()

    def connect(self):
        self.buttonUI.clicked.connect(self.nextClick)
        
        self.b2.click.connect(self.timeTest)
        self.b3.click.connect(self.timeSits)
        self.b4.click.connect(self.finalTimer)

    def nextClick(self):
        self.hide()
        self.tw = TestWin()