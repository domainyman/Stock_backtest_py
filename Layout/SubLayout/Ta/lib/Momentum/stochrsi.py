import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox,QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class stochrsi():
    def __init__(self):
        super().__init__()
        self.timeperiod = self.timeperiodsetup()
        self.fastk_period = self.fastk_periodsetup()
        self.fastd_period = self.fastd_periodsetup()
        self.fastd_matype = self.fastd_matypesetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()    
        self.timeperiodlineedit = QLineEdit()
        self.fastk_periodlineedit = QLineEdit()
        self.fastd_periodlineedit = QLineEdit()
        self.fastd_matypelineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'STOCHRSI': {'timeperiod': 14, 'fastk_period': 5, 'fastd_period': 3, 'fastd_matype': 0}}
    
    def entry_exit_base(self):
        self.entryprofo = {'STOCHRSI': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['STOCHRSI']['GOLDEN CROSS']
        self.MACDitem = testitem.loc['STOCHRSI_SLOWK']
        self.MACD_SIGNALitem = testitem.loc['STOCHRSI_SLOWD']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['STOCHRSI']['Death Cross']
        self.MACDitem = testitem.loc['STOCHRSI_SLOWK']
        self.MACD_SIGNALitem = testitem.loc['STOCHRSI_SLOWD']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        
    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['timeperiod']
            return self.data
        else:
            self.datadef = 14
            return self.datadef

    def fastk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['fastk_period']
            return self.data
        else:
            self.datadef = 5
            return self.datadef

    def fastd_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['fastd_period']
            return self.data
        else:
            self.datadef = 3
            return self.datadef

    def fastd_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCHRSI' in tech_dict:
            self.data = tech_dict['STOCHRSI']['fastd_matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef


    def widgetedit(self):
        self.timeperiodlabel = QLabel('timeperiod :')
        self.timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.timeperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.timeperiodlineedit.setText(str(self.timeperiod))
        self.timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.fastk_periodlabel = QLabel('fastk_period :')
        self.fastk_periodlabel.setMinimumSize(QSize(150, 25))
        self.fastk_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastk_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastk_periodlineedit.setText(str(self.fastk_period))
        self.fastk_periodlineedit.setMinimumSize(QSize(200, 25))
        self.fastk_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.fastd_periodlabel = QLabel('fastd_period :')
        self.fastd_periodlabel.setMinimumSize(QSize(150, 25))
        self.fastd_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastd_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastd_periodlineedit.setText(str(self.fastd_period))
        self.fastd_periodlineedit.setMinimumSize(QSize(200, 25))
        self.fastd_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.fastd_matypelabel = QLabel('fastd_matype :')
        self.fastd_matypelabel.setMinimumSize(QSize(150, 25))
        self.fastd_matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastd_matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastd_matypelineedit.setText(str(self.fastd_matype))
        self.fastd_matypelineedit.setMinimumSize(QSize(200, 25))
        self.fastd_matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.timeperiodlabel, self.timeperiodlineedit)
        self.formlayout.addRow(self.fastk_periodlabel, self.fastk_periodlineedit)
        self.formlayout.addRow(self.fastd_periodlabel, self.fastd_periodlineedit)
        self.formlayout.addRow(self.fastd_matypelabel, self.fastd_matypelineedit)
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
        self.tool_dict['STOCHRSI'] = {}
        self.tool_dict['STOCHRSI']['timeperiod'] = self.timeperiodlineedit.text()
        self.tool_dict['STOCHRSI']['fastk_period'] = self.fastk_periodlineedit.text()
        self.tool_dict['STOCHRSI']['fastd_period'] = self.fastd_periodlineedit.text()
        self.tool_dict['STOCHRSI']['fastd_matype'] = self.fastd_matypelineedit.text()
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
        self.datadb["STOCHRSI_SLOWK"], self.datadb["STOCHRSI_SLOWD"] = talib.STOCHRSI(
            self.datadb['Close'], timeperiod=int(self.timeperiod), fastk_period=int(self.fastk_period), fastd_period=int(self.fastd_period), fastd_matype=int(self.fastd_matype))
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
        self.tool_dict['STOCHRSI'] = {}
        self.tool_dict['STOCHRSI']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['STOCHRSI']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
