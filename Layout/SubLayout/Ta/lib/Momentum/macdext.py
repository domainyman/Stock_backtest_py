import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class macdext():
    def __init__(self):
        super().__init__()
        self.fastperiod = self.fastperiodsetup()
        self.fastmatype = self.fastmatypesetup()
        self.slowperiod = self.slowperiodsetup()
        self.slowmatype = self.slowmatypesetup()
        self.signalperiod = self.signalperiodsetup()
        self.signalmatype = self.signalmatypesetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.fastperiodlineedit = QLineEdit()
        self.fastmatypelineedit = QLineEdit()
        self.slowperiodlineedit = QLineEdit()
        self.slowmatypelineedit = QLineEdit()
        self.signalperiodlineedit = QLineEdit()
        self.signalmatypelineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'MACDEXT': {'fastperiod': 12, 'fastmatype': 0, 'slowperiod': 26, 'slowmatype': 0, 'signalperiod': 9, 'signalmatype': 0}}

    def entry_exit_base(self):
        self.entryprofo = {'MACDEXT': {
            'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['MACDEXT']['GOLDEN CROSS']
        self.MACDitem = testitem.loc['MACDEXT']
        self.MACD_SIGNALitem = testitem.loc['MACDEXT_SIGNAL']
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
        self.exitba = self.tech_dict['MACDEXT']['Death Cross']
        self.MACDitem = testitem.loc['MACDEXT']
        self.MACD_SIGNALitem = testitem.loc['MACDEXT_SIGNAL']
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

    def fastperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['fastperiod']
            return self.data
        else:
            self.datadef = 12
            return self.datadef

    def fastmatypesetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['fastmatype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def slowperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['slowperiod']
            return self.data
        else:
            self.datadef = 26
            return self.datadef

    def slowmatypesetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['slowmatype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def signalperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['signalperiod']
            return self.data
        else:
            self.datadef = 9
            return self.datadef

    def signalmatypesetup(self):
        tech_dict = self.getterTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['signalmatype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MACDEXT' in tech_dict:
            self.data = tech_dict['MACDEXT']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
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
        self.Fastmatypelabel = QLabel('Fastmatype :')
        self.Fastmatypelabel.setMinimumSize(QSize(150, 25))
        self.Fastmatypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Fastmatypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastmatypelineedit.setText(str(self.fastmatype))
        self.fastmatypelineedit.setMinimumSize(QSize(200, 25))
        self.fastmatypelineedit.setStyleSheet(
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
        self.Slowmatypelabel = QLabel('Slowmatype :')
        self.Slowmatypelabel.setMinimumSize(QSize(150, 25))
        self.Slowmatypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Slowmatypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowmatypelineedit.setText(str(self.slowmatype))
        self.slowmatypelineedit.setMinimumSize(QSize(200, 25))
        self.slowmatypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.signalperiodlabel = QLabel('Signalperiod :')
        self.signalperiodlabel.setMinimumSize(QSize(150, 25))
        self.signalperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.signalperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.signalperiodlineedit.setText(str(self.signalperiod))
        self.signalperiodlineedit.setMinimumSize(QSize(200, 25))
        self.signalperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.Signalmatypelabel = QLabel('Signalmatype :')
        self.Signalmatypelabel.setMinimumSize(QSize(150, 25))
        self.Signalmatypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Signalmatypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.signalmatypelineedit.setText(str(self.signalmatype))
        self.signalmatypelineedit.setMinimumSize(QSize(200, 25))
        self.signalmatypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.Fastperiodlabel, self.fastperiodlineedit)
        self.formlayout.addRow(self.Fastmatypelabel, self.fastmatypelineedit)
        self.formlayout.addRow(self.slowperiodlabel, self.slowperiodlineedit)
        self.formlayout.addRow(self.Slowmatypelabel, self.slowmatypelineedit)
        self.formlayout.addRow(self.signalperiodlabel,
                               self.signalperiodlineedit)
        self.formlayout.addRow(self.Signalmatypelabel,
                               self.signalmatypelineedit)
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
        self.tool_dict['MACDEXT'] = {}
        self.tool_dict['MACDEXT']['fastperiod'] = self.fastperiodlineedit.text()
        self.tool_dict['MACDEXT']['fastmatype'] = self.fastmatypelineedit.text()
        self.tool_dict['MACDEXT']['slowperiod'] = self.slowperiodlineedit.text()
        self.tool_dict['MACDEXT']['slowmatype'] = self.slowmatypelineedit.text()
        self.tool_dict['MACDEXT']['signalperiod'] = self.signalperiodlineedit.text()
        self.tool_dict['MACDEXT']['signalmatype'] = self.signalmatypelineedit.text()
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
        self.datadb["MACDEXT"], self.datadb["MACDEXT_SIGNAL"], self.datadb["MACDEXT_HIST"] = talib.MACDEXT(
            self.datadb['Close'], fastperiod=int(self.fastperiod), fastmatype=int(self.fastmatype), slowperiod=int(self.slowperiod), slowmatype=int(self.slowmatype), signalperiod=int(self.signalperiod), signalmatype=int(self.signalmatype))
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
        self.tool_dict['MACDEXT'] = {}
        self.tool_dict['MACDEXT']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['MACDEXT']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
