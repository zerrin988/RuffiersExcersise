from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from FinalWin import *
from Variables import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.UI()
        self.connect()
    
    def set_appear(self):
        self.setWindowTitle(textTw)
        self.resize(winW, winH)
        self.move(winX, winY)

    def UI(self):
        self.lineh = QHBoxLayout()
        self.liner = QVBoxLayout()
        self.linel = QVBoxLayout()

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

        self.linel.addWidget(self.t1)
        self.linel.addWidget(self.desc1)

        self.linel.addWidget(self.t2)
        self.linel.addWidget(self.desc2)

        self.linel.addWidget(self.t3)
        self.linel.addWidget(self.b1)
        self.linel.addWidget(self.desc3)

        self.linel.addWidget(self.t4)
        self.linel.addWidget(self.b2)

        self.linel.addWidget(self.t5)
        self.linel.addWidget(self.b3)
        self.linel.addWidget(self.desc4)
        self.linel.addWidget(self.desc5)
        
        self.linel.addWidget(self.b4)

        self.liner.addWidget(self.tTimer)

        self.lineh.addLayout(self.linel)
        self.lineh.addLayout(self.liner)

        self.setLayout(self.lineh)

    def timeTest(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time1event)
        self.timer.start(1000)
    
    def time1event(self):
        global time
        time = time.addSecs(-1)
        self.tTimer.setText(time.toString("hh:mm:ss"))

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timeSits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time2event)
        self.timer.start(1500)

    def time2event(self):
        global time
        self.tTimer.setText(time.toString("hh:mm:ss")[6:8])
        time = time.addSecs(-1)

        if time.toString("hh:mm:ss") == "00:00:00":
                self.timer.stop()

    def finalTimer(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time3event)
        self.timer.start(1000)

    def time3event(self):
        global time
        self.tTimer.setText(time.toString("hh:mm:ss"))
        time = time.addSecs(-1)

        if time.toString("hh:mm:ss") >= "00:00:45":
            self.tTimer.setStyleSheet("color: rgb(0, 255, 0)")
        elif time.toString("hh:mm:ss") <= "00:00:15":
            self.tTimer.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            self.tTimer.setStyleSheet("color: rgb(0, 0, 0)")

        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def connect(self):
        self.b1.clicked.connect(self.timeTest)
        self.b2.clicked.connect(self.timeSits)
        self.b3.clicked.connect(self.finalTimer)
        self.b4.clicked.connect(self.nextClick)

    def nextClick(self):
        self.hide()
        self.tw = FinalWin()