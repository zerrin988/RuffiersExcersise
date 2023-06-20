from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from Variables import *

age_ranges = {
    (15, float('inf')):
    {
        (15, float('inf')): txt_res1,
        (11, 13.9): txt_res2,
        (6, 10.9): txt_res3,
        (0.5, 5.9): txt_res4,
        (-float('inf'), 0.4): txt_res5,
    },
    (13, 14):
    {
        (16.5, float('inf')): txt_res1,
        (12.5, 16.4): txt_res2,
        (7.5, 13.4): txt_res3,
        (2, 7.4): txt_res4,
        (-float('inf'), 1.9): txt_res5,
    },
    (11, 12):
    {
        (18, float('inf')): txt_res1,
        (14, 17.9): txt_res2,
        (9, 13.9): txt_res3,
        (3.5, 8.9): txt_res4,
        (-float('inf'), 3.4): txt_res5,
    },
    (9, 10):
    {
        (19.5, float('inf')): txt_res1,
        (15.5, 19.4): txt_res2,
        (10.5, 15.4): txt_res3,
        (5, 10.4): txt_res4,
        (-float('inf'), 4.9): txt_res5,
    },
    (7, 8):
    {
        (21, float('inf')): txt_res1,
        (17, 20.9): txt_res2,
        (12, 16.9): txt_res3,
        (6.5, 11.9): txt_res4,
        (-float('inf'), 6.4): txt_res5,
    },
}

class ResultChecker:
    def __init__(self, age_ranges):
        self.age_ranges = age_ranges

    def resultChecker(self, age, result):
        for age_range, result_ranges in self.age_ranges.items():
            if float(age_range[0]) <= age <= float(age_range[1]):
                for result_range, action in result_ranges.items():
                    if float(result_range[0]) <= float(result) <= float(result_range[1]):
                        return action

        return "."


class FinalWin(QWidget):
    def __init__(self, ti, result):
        super().__init__()
        self.ti = ti
        self.UI()
        self.result = result
        self.show()

    def set_appear(self):
        self.setWindowTitle(textFw)
        self.resize(winW, winH)
        self.move(winX, winY)

    def UI(self):
        self.line = QVBoxLayout()
        
        self.work_text = QLabel(txt_workheart + str(self.ti.index))
        self.index_text = QLabel(txt_index + str(self.results()))

        self.line.addWidget(self.work_text)
        self.line.addWidget(self.index_text)

        self.setLayout(self.line)

    def results(self):
        checker = ResultChecker(age_ranges)
        self.result = checker.resultChecker(self.ti.index, self.ti.age)
        return self.result