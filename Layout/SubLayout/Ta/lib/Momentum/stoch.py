import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class stoch():
    def __init__(self):
        super().__init__()
        self.fastk_period = self.fastk_periodsetup()
        self.slowk_period = self.slowk_periodsetup()
        self.slowk_matype = self.slowk_matypesetup()
        self.slowd_period = self.slowd_periodsetup()
        self.slowd_matype = self.slowd_matypesetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.fastk_periodlineedit = QLineEdit()
        self.slowk_periodlineedit = QLineEdit()
        self.slowk_matypelineedit = QLineEdit()
        self.slowd_periodlineedit = QLineEdit()
        self.slowd_matypelineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'STOCH': {'fastk_period': 5, 'slowk_period': 3, 'slowk_matype': 0, 'slowd_period': 3, 'slowd_matype': 0}}

    def entry_exit_base(self):
        self.entryprofo = {
            'STOCH': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['STOCH']['GOLDEN CROSS']
        self.MACDitem = testitem.loc['STOCH_SLOWK']
        self.MACD_SIGNALitem = testitem.loc['STOCH_SLOWD']
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
        self.exitba = self.tech_dict['STOCH']['Death Cross']
        self.MACDitem = testitem.loc['STOCH_SLOWK']
        self.MACD_SIGNALitem = testitem.loc['STOCH_SLOWD']
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

    def fastk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['fastk_period']
            return self.data
        else:
            self.datadef = 5
            return self.datadef

    def slowk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['slowk_period']
            return self.data
        else:
            self.datadef = 3
            return self.datadef

    def slowk_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['slowk_matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def slowd_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['slowd_period']
            return self.data
        else:
            self.datadef = 3
            return self.datadef

    def slowd_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['slowd_matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'STOCH' in tech_dict:
            self.data = tech_dict['STOCH']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def widgetedit(self):
        self.Fastk_periodlabel = QLabel('Fastk_period :')
        self.Fastk_periodlabel.setMinimumSize(QSize(150, 25))
        self.Fastk_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Fastk_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastk_periodlineedit.setText(str(self.fastk_period))
        self.fastk_periodlineedit.setMinimumSize(QSize(200, 25))
        self.fastk_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowk_periodlabel = QLabel('Slowk_period :')
        self.slowk_periodlabel.setMinimumSize(QSize(150, 25))
        self.slowk_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowk_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowk_periodlineedit.setText(str(self.slowk_period))
        self.slowk_periodlineedit.setMinimumSize(QSize(200, 25))
        self.slowk_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowk_matypelabel = QLabel('Slowk_matype :')
        self.slowk_matypelabel.setMinimumSize(QSize(150, 25))
        self.slowk_matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowk_matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowk_matypelineedit.setText(str(self.slowk_matype))
        self.slowk_matypelineedit.setMinimumSize(QSize(200, 25))
        self.slowk_matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowd_periodlabel = QLabel('Slowd_period :')
        self.slowd_periodlabel.setMinimumSize(QSize(150, 25))
        self.slowd_periodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowd_periodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowd_periodlineedit.setText(str(self.slowd_period))
        self.slowd_periodlineedit.setMinimumSize(QSize(200, 25))
        self.slowd_periodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowd_matypelabel = QLabel('Slowd_matype :')
        self.slowd_matypelabel.setMinimumSize(QSize(150, 25))
        self.slowd_matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowd_matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowd_matypelineedit.setText(str(self.slowd_matype))
        self.slowd_matypelineedit.setMinimumSize(QSize(200, 25))
        self.slowd_matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.Fastk_periodlabel,
                               self.fastk_periodlineedit)
        self.formlayout.addRow(self.slowk_periodlabel,
                               self.slowk_periodlineedit)
        self.formlayout.addRow(self.slowk_matypelabel,
                               self.slowk_matypelineedit)
        self.formlayout.addRow(self.slowd_periodlabel,
                               self.slowd_periodlineedit)
        self.formlayout.addRow(self.slowd_matypelabel,
                               self.slowd_matypelineedit)
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
        self.tool_dict['STOCH'] = {}
        self.tool_dict['STOCH']['fastk_period'] = self.fastk_periodlineedit.text()
        self.tool_dict['STOCH']['slowk_period'] = self.slowk_periodlineedit.text()
        self.tool_dict['STOCH']['slowk_matype'] = self.slowk_matypelineedit.text()
        self.tool_dict['STOCH']['slowd_period'] = self.slowd_periodlineedit.text()
        self.tool_dict['STOCH']['slowd_matype'] = self.slowd_matypelineedit.text()
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
        self.datadb["STOCH_SLOWK"], self.datadb["STOCH_SLOWD"] = talib.STOCH(
            self.datadb['High'], self.datadb['Low'], self.datadb['Close'], fastk_period=int(self.fastk_period), slowk_period=int(self.slowk_period), slowk_matype=int(self.slowk_matype), slowd_period=int(self.slowd_period), slowd_matype=int(self.slowd_matype))
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
        self.tool_dict['STOCH'] = {}
        self.tool_dict['STOCH']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['STOCH']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
