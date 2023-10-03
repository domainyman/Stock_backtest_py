import talib
import pandas as pd
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox,QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue
import numpy as np


class aroon():
    def __init__(self):
        super().__init__()
        self.parameter = self.setup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()    
        self.lineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'AROON': 14}

    def entry_exit_base(self):
        self.entryprofo = {'AROON': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def setup(self):
        tech_dict = self.getterTechValue()
        if 'AROON' in tech_dict:
            self.data = tech_dict['AROON']
            return self.data
        else:
            self.datadef = 14
            return self.datadef
        
    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'AROON' in tech_dict:
            self.data = tech_dict['AROON']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'AROON' in tech_dict:
            self.data = tech_dict['AROON']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['AROON']['GOLDEN CROSS']
        if (self.entryba == 'True'):
            self.item = testitem.loc['AROON_UP']
            self.SIGNALitem = testitem.loc['AROON_DOWN']
            if float(self.item) > float(self.SIGNALitem):
                return True
            else:
                return False
        else:
                return True

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['AROON']['Death Cross']
        if (self.exitba == 'True'):
            self.item = testitem.loc['AROON_UP']
            self.SIGNALitem = testitem.loc['AROON_DOWN']
            if float(self.item) < float(self.SIGNALitem):
                return True
            else:
                    return False
        else:
            return True

    def widgetedit(self):
        self.label = QLabel('Parameter :')
        self.label.setMinimumSize(QSize(150, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.lineedit.setText(str(self.parameter))
        self.lineedit.setMinimumSize(QSize(200, 25))
        self.lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.label, self.lineedit)
        self.button = QPushButton('Submit')
        self.button.clicked.connect(self.uploadValue)
        self.button.setMinimumSize(QSize(200, 25))
        self.button.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formlayout)
        self.layout.addWidget(self.button)
        return self.layout

    def tool_dicts(self):
        self.tool_dict = {}
        self.tool_dict['AROON'] = self.lineedit.text()
        return self.tool_dict

    def uploadValue(self):
        self.global_dict = self.getterTechValue()
        tool_dict = self.tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterTechValue(self.global_dict)
        print(self.getterTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')

    def setterTechValue(self, text):
        TechValue.set_tech_toolperm_var(text)

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

    def settertoolhistory(self, text):
        GlobalValue.set_TechTool_history_var(text)

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()
    
    def setterEntryTechValue(self, text):
        TechValue.set_tech_Entry_var(text)

    def calculate(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["AROON_UP"], self.datadb["AROON_DOWN"] = talib.AROON(
            self.datadb["High"], self.datadb["Low"], timeperiod=int(self.parameter))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel = QLabel('GOLDEN CROSS :')
        self.buylabel.setMinimumSize(QSize(150, 25))
        self.buylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb.addItems(['True','False'])
        self.buysignalcb.setCurrentText(str(self.buysignal))
        self.buysignalcb.setMinimumSize(QSize(200, 25))
        self.buysignalcb.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel = QLabel('Death Cross :')
        self.selllabel.setMinimumSize(QSize(150, 25))
        self.selllabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb.addItems(['True','False'])
        self.sellsignalcb.setCurrentText(str(self.sellsignal))
        self.sellsignalcb.setMinimumSize(QSize(200, 25))
        self.sellsignalcb.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.buylabel, self.buysignalcb)
        self.formlayout.addRow(self.selllabel, self.sellsignalcb)
        self.button = QPushButton('Submit')
        self.button.clicked.connect(self.uploadentryValue)
        self.button.setMinimumSize(QSize(200, 25))
        self.button.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formlayout)
        self.layout.addWidget(self.button)
        return self.layout
    
    def Entry_tool_dicts(self):
        self.tool_dict = {}
        self.tool_dict['AROON'] = {}
        self.tool_dict['AROON']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['AROON']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')