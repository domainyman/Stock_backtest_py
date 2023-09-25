import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox,QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class stochf():
    def __init__(self):
        super().__init__()
        self.fastk_period = self.fastk_periodsetup()
        self.fastd_period = self.fastd_periodsetup()
        self.fastd_matype = self.fastd_matypesetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()    
        self.fastk_periodlineedit = QLineEdit()
        self.fastd_periodlineedit = QLineEdit()
        self.fastd_matypelineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'STOCHF': {'fastk_period': '5', 'fastd_period': '3', 'fastd_matype': '0'}}

    def entry_exit_base(self):
        self.entryprofo = {'STOCHF': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo
    
    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['STOCHF']['GOLDEN CROSS']
        if (self.entryba == 'True'):
            self.MACDitem = testitem.loc['STOCHF_FASTK']
            self.MACD_SIGNALitem = testitem.loc['STOCHF_FASTD']
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        else:
                return True

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['STOCHF']['Death Cross']
        if (self.exitba == 'True'):
            self.MACDitem = testitem.loc['STOCHF_FASTK']
            self.MACD_SIGNALitem = testitem.loc['STOCHF_FASTD']
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                    return False
        else:
            return True

    def fastk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHF' in tech_dict:
            self.data = tech_dict['STOCHF']['fastk_period']
            return self.data
        else:
            self.datadef = '5'
            return self.datadef

    def fastd_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHF' in tech_dict:
            self.data = tech_dict['STOCHF']['fastd_period']
            return self.data
        else:
            self.datadef = '3'
            return self.datadef

    def fastd_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHF' in tech_dict:
            self.data = tech_dict['STOCHF']['fastd_matype']
            return self.data
        else:
            self.datadef = '0'
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCHF' in tech_dict:
            self.data = tech_dict['STOCHF']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCHF' in tech_dict:
            self.data = tech_dict['STOCHF']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def widgetedit(self):
        self.fastk_periodlabel = QLabel('Fastk_period :')
        self.fastk_periodlabel.setMinimumSize(QSize(150, 25))
        self.fastk_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastk_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastk_periodlineedit.setText(str(self.fastk_period))
        self.fastk_periodlineedit.setMinimumSize(QSize(200, 25))
        self.fastk_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.fastd_periodlabel = QLabel('Fastd_period :')
        self.fastd_periodlabel.setMinimumSize(QSize(150, 25))
        self.fastd_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastd_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastd_periodlineedit.setText(str(self.fastd_period))
        self.fastd_periodlineedit.setMinimumSize(QSize(200, 25))
        self.fastd_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.fastd_matypelabel = QLabel('Fastd_matype :')
        self.fastd_matypelabel.setMinimumSize(QSize(150, 25))
        self.fastd_matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastd_matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastd_matypelineedit.setText(str(self.fastd_matype))
        self.fastd_matypelineedit.setMinimumSize(QSize(200, 25))
        self.fastd_matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.fastk_periodlabel,
                               self.fastk_periodlineedit)
        self.formlayout.addRow(self.fastd_periodlabel,
                               self.fastd_periodlineedit)
        self.formlayout.addRow(self.fastd_matypelabel,
                               self.fastd_matypelineedit)
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
        self.tool_dict['STOCHF'] = {}
        self.tool_dict['STOCHF']['fastk_period'] = self.fastk_periodlineedit.text()
        self.tool_dict['STOCHF']['fastd_period'] = self.fastd_periodlineedit.text()
        self.tool_dict['STOCHF']['fastd_matype'] = self.fastd_matypelineedit.text()
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
        self.datadb["STOCHF_FASTK"], self.datadb["STOCHF_FASTD"] = talib.STOCHF(
            self.datadb['High'], self.datadb['Low'], self.datadb['Close'], fastk_period=int(self.fastk_period), fastd_period=int(self.fastd_period), fastd_matype=int(self.fastd_matype))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel = QLabel('High :')
        self.buylabel.setMinimumSize(QSize(150, 25))
        self.buylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb.addItems(['True','False'])
        self.buysignalcb.setCurrentText(str(self.buysignal))
        self.buysignalcb.setMinimumSize(QSize(200, 25))
        self.buysignalcb.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel = QLabel('Low :')
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
        self.tool_dict['STOCHF'] = {}
        self.tool_dict['STOCHF']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['STOCHF']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
