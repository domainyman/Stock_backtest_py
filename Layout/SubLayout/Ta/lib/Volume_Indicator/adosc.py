import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue
import numpy as np


class adosc():
    def __init__(self):
        super().__init__()
        self.fastperiod = self.fastperiodsetup()
        self.slowperiod = self.slowperiodsetup()
        self.fastperiodlineedit = QLineEdit()
        self.slowperiodlineedit = QLineEdit()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'ADOSC': {'fastperiod': 3, 'slowperiod': 10}}

    def entry_exit_base(self):
        self.entryprofo = {
            'ADOSC': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['ADOSC']['GOLDEN CROSS']
        if (self.entryba == 'True'):
            self.itemclose = testitem.loc['Close']
            self.itemADOSC = testitem.loc['ADOSC']
            self.oldclose, self.oldad = self.get_db_for_entry_exit(testitem)
            self.ad_test = self.Check_RELAT(
                self.oldclose, self.itemclose, self.oldad, self.itemADOSC)
            if (self.ad_test == "111"):
                return True
            else:
                return False
        else:
            return True

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['ADOSC']['Death Cross']
        if (self.entryba == 'True'):
            self.itemclose = testitem.loc['Close']
            self.itemADOSC = testitem.loc['ADOSC']
            self.oldclose, self.oldad = self.get_db_for_entry_exit(testitem)
            self.ad_test = self.Check_RELAT(
                self.oldclose, self.itemclose, self.oldad, self.itemADOSC)
            if (self.ad_test == "000"):
                return True
            else:
                return False
        else:
            return True

    def get_db_for_entry_exit(self, testitem):
        self.ChecklistClose = []
        self.ChecklistAD = []
        self.df = self.gettertoolhistory()
        self.targetindex = testitem
        for i in range(1, 3):
            self.adoscitem = self.targetindex['ADOSC']
            if (self.adoscitem != np.nan):
                previous_close = self.df.shift(i).loc[(self.df['ADOSC'] == self.targetindex['ADOSC']) & (
                    self.df['Close'] == self.targetindex['Close'])].head(1)
                # Add 'Close' values to self.Checklist
                if not previous_close.empty:
                    self.ChecklistClose.append(previous_close['Close'].iloc[0])
                    self.ChecklistAD.append(previous_close['ADOSC'].iloc[0])
            else:
                break
        return self.ChecklistClose, self.ChecklistAD

    def Check_RELAT(self, relclose, newclose, relad, newad):
        self.relclose = relclose
        self.relad = relad

        if (self.relad != [] and self.relclose != []):

            if (self.CheckMathis(newad) == "0" and self.CheckMathis(self.relad[0]) == "1"):
                return "111"
            elif (self.CheckMathis(newad) == "1" and self.CheckMathis(self.relad[0]) == "0"):
                return "000"
            else:
                return "Unknown"
        else:
            return "Unknown"

    def CheckMathis(self, item):
        self.math = item
        if (self.math > 0):
            return "1"
        elif (self.math < 0):
            return "0"
        else:
            return "-"

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ADOSC' in tech_dict:
            self.data = tech_dict['ADOSC']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ADOSC' in tech_dict:
            self.data = tech_dict['ADOSC']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def fastperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'ADOSC' in tech_dict:
            self.data = tech_dict['ADOSC']['fastperiod']
            return self.data
        else:
            self.datadef = 3
            return self.datadef

    def slowperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'ADOSC' in tech_dict:
            self.data = tech_dict['ADOSC']['slowperiod']
            return self.data
        else:
            self.datadef = 10
            return self.datadef

    def widgetedit(self):
        self.Fastperiodlabel = QLabel('Fastperiod :')
        self.Fastperiodlabel.setMinimumSize(QSize(150, 25))
        self.Fastperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Fastperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastperiodlineedit.setText(str(self.fastperiod))
        self.fastperiodlineedit.setMinimumSize(QSize(200, 25))
        self.fastperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowperiodlabel = QLabel('Slowperiod :')
        self.slowperiodlabel.setMinimumSize(QSize(150, 25))
        self.slowperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowperiodlineedit.setText(str(self.slowperiod))
        self.slowperiodlineedit.setMinimumSize(QSize(200, 25))
        self.slowperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.Fastperiodlabel, self.fastperiodlineedit)
        self.formlayout.addRow(self.slowperiodlabel, self.slowperiodlineedit)
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
        self.tool_dict['ADOSC'] = {}
        self.tool_dict['ADOSC']['fastperiod'] = self.fastperiodlineedit.text()
        self.tool_dict['ADOSC']['slowperiod'] = self.slowperiodlineedit.text()
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
        self.datadb["ADOSC"] = talib.ADOSC(
            self.datadb['High'], self.datadb['Low'], self.datadb['Close'], self.datadb['Volume'], fastperiod=int(self.fastperiod), slowperiod=int(self.slowperiod))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel = QLabel('GOLDEN CROSS :')
        self.buylabel.setMinimumSize(QSize(150, 25))
        self.buylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb.addItems(['True', 'False'])
        self.buysignalcb.setCurrentText(str(self.buysignal))
        self.buysignalcb.setMinimumSize(QSize(200, 25))
        self.buysignalcb.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel = QLabel('Death Cross :')
        self.selllabel.setMinimumSize(QSize(150, 25))
        self.selllabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb.addItems(['True', 'False'])
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
        self.tool_dict['ADOSC'] = {}
        self.tool_dict['ADOSC']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['ADOSC']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
