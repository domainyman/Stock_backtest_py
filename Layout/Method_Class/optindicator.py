import backtrader as bt
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt


class opt_ind():

    def __init__(self):
        print()

    def rangestep(self):
        return {
            'first': 1,
            'last': 100,
            'step': 25
        }

    def widget_pop(self):
        self.label = QLabel('Parameter :')
        self.label.setMinimumSize(QSize(150, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.rangelabelFirst = QLabel('Range - First:')
        self.rangelabelFirst.setMinimumSize(QSize(150, 25))
        self.rangelabelFirst.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rangelabelFirst.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.lineeditFirst = QLineEdit()
        self.lineeditFirst.setText(str(self.parameter))
        self.lineeditFirst.setMinimumSize(QSize(200, 25))
        self.lineeditFirst.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.rangelabelLast = QLabel('Range - Last:')
        self.rangelabelLast.setMinimumSize(QSize(150, 25))
        self.rangelabelLast.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rangelabelLast.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.lineeditLast = QLineEdit()
        self.lineeditLast.setText(str(self.parameter))
        self.lineeditLast.setMinimumSize(QSize(200, 25))
        self.lineeditLast.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.rangelabelStep = QLabel('Range - Step:')
        self.rangelabelStep.setMinimumSize(QSize(150, 25))
        self.rangelabelStep.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rangelabelStep.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.lineeditStep = QLineEdit()
        self.lineeditStep.setText(str(self.parameter))
        self.lineeditStep.setMinimumSize(QSize(200, 25))
        self.lineeditStep.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.label)
        self.formlayout.addRow(self.rangelabelFirst, self.lineeditFirst)
        self.formlayout.addRow(self.rangelabelLast, self.lineeditLast)
        self.button = QPushButton('Submit')
        self.button.clicked.connect(self.uploadValue)
        self.button.setMinimumSize(QSize(200, 25))
        self.button.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formlayout)
        self.layout.addWidget(self.button)
        return self.layout
