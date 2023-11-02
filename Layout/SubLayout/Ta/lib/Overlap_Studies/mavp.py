import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue
import numpy as np


class mavp():
    def __init__(self):
        super().__init__()
        self.periods = self.periodssetup()
        self.minperiod = self.minperiodsetup()
        self.maxperiod = self.maxperiodsetup()
        self.matype = self.matypesetup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.periodslineedit = QLineEdit()
        self.minperiodlineedit = QLineEdit()
        self.maxperiodlineedit = QLineEdit()
        self.matypelineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()


    def base(self):
        return {'MAVP': {'periods': 10, 'minperiod': 2, 'maxperiod': 30, 'matype': 0}}
    
    def entry_exit_base(self):
        self.entryprofo = {'MAVP': {'HIGH': 70, 'LOW': 30}}
        return self.entryprofo
    
    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['MAVP']
        self.entryba = self.tech_dict['MAVP']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['MAVP']
        self.entryba = self.tech_dict['MAVP']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def periodssetup(self):
        tech_dict = self.getterTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['periods']
            return self.data
        else:
            self.datadef = 10
            return self.datadef

    def minperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['minperiod']
            return self.data
        else:
            self.datadef = 2
            return self.datadef

    def maxperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['maxperiod']
            return self.data
        else:
            self.datadef = 30
            return self.datadef

    def matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef
        
    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['HIGH']
            return self.data
        else:
            self.datadef = 70
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MAVP' in tech_dict:
            self.data = tech_dict['MAVP']['LOW']
            return self.data
        else:
            self.datadef = 30
            return self.datadef

    def widgetedit(self):
        self.periodslabel = QLabel('Periods :')
        self.periodslabel.setMinimumSize(QSize(150, 25))
        self.periodslabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.periodslabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.periodslineedit.setText(str(self.periods))
        self.periodslineedit.setMinimumSize(QSize(200, 25))
        self.periodslineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.minperiodlabel = QLabel('Minperiod :')
        self.minperiodlabel.setMinimumSize(QSize(150, 25))
        self.minperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.minperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.minperiodlineedit.setText(str(self.minperiod))
        self.minperiodlineedit.setMinimumSize(QSize(200, 25))
        self.minperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.maxperiodlabel = QLabel('Maxperiod :')
        self.maxperiodlabel.setMinimumSize(QSize(150, 25))
        self.maxperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maxperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.maxperiodlineedit.setText(str(self.maxperiod))
        self.maxperiodlineedit.setMinimumSize(QSize(200, 25))
        self.maxperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.matypelabel = QLabel('Matype :')
        self.matypelabel.setMinimumSize(QSize(150, 25))
        self.matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.matypelineedit.setText(str(self.matype))
        self.matypelineedit.setMinimumSize(QSize(200, 25))
        self.matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.periodslabel,
                               self.periodslineedit)
        self.formlayout.addRow(self.minperiodlabel,
                               self.minperiodlineedit)
        self.formlayout.addRow(self.maxperiodlabel,
                               self.maxperiodlineedit)
        self.formlayout.addRow(self.matypelabel,
                               self.matypelineedit)
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
        self.tool_dict['MAVP'] = {}
        self.tool_dict['MAVP']['periods'] = self.periodslineedit.text()
        self.tool_dict['MAVP']['minperiod'] = self.minperiodlineedit.text()
        self.tool_dict['MAVP']['maxperiod'] = self.maxperiodlineedit.text()
        self.tool_dict['MAVP']['matype'] = self.matypelineedit.text()
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
    
    def setterEntryTechValue(self, text):
        TechValue.set_tech_Entry_var(text)

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()


    def calculate(self):
        self.datadb = self.gettertoolhistory()
        self.periods = np.array([5, 10, 20, 60, 100, 200])
        self.datadb["MAVP"] = talib.MAVP(
            self.datadb['Close'], self.periods, minperiod=int(self.minperiod), maxperiod=int(self.maxperiod), matype=int(self.matype))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.highlabel = QLabel('Exit :')
        self.highlabel.setMinimumSize(QSize(150, 25))
        self.highlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.EntryHighlineedit.setText(str(self.entryHIGHparameter))
        self.EntryHighlineedit.setMinimumSize(QSize(200, 25))
        self.EntryHighlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.Lowlabel = QLabel('Entry :')
        self.Lowlabel.setMinimumSize(QSize(150, 25))
        self.Lowlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Lowlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.EntryLowlineedit.setText(str(self.entryLOWparameter))
        self.EntryLowlineedit.setMinimumSize(QSize(200, 25))
        self.EntryLowlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.highlabel, self.EntryHighlineedit)
        self.formlayout.addRow(self.Lowlabel, self.EntryLowlineedit)
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
        self.tool_dict['MAVP'] = {}
        self.tool_dict['MAVP']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['MAVP']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
