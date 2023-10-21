import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class macd():
    def __init__(self):
        super().__init__()
        self.fastperiod = self.fastperiodsetup()
        self.slowperiod = self.slowperiodsetup()
        self.signalperiod = self.signalperiodsetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.fastperiodlineedit = QLineEdit()
        self.slowperiodlineedit = QLineEdit()
        self.signalperiodlineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'MACD': {'fastperiod': 12, 'slowperiod': 26, 'signalperiod': 9}}

    def entry_exit_base(self):
        self.entryprofo = {
            'MACD': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def fastperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACD' in tech_dict:
            self.data = tech_dict['MACD']['fastperiod']
            return self.data
        else:
            self.datadef = 12
            return self.datadef

    def slowperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACD' in tech_dict:
            self.data = tech_dict['MACD']['slowperiod']
            return self.data
        else:
            self.datadef = 26
            return self.datadef

    def signalperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MACD' in tech_dict:
            self.data = tech_dict['MACD']['signalperiod']
            return self.data
        else:
            self.datadef = 9
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MACD' in tech_dict:
            self.data = tech_dict['MACD']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MACD' in tech_dict:
            self.data = tech_dict['MACD']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['MACD']['GOLDEN CROSS']
        if (self.entryba == 'True'):
            self.MACDitem = testitem.loc['MACD']
            self.MACD_SIGNALitem = testitem.loc['MACD_SIGNAL']
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        else:
            return True

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['MACD']['Death Cross']
        if (self.exitba == 'True'):
            self.MACDitem = testitem.loc['MACD']
            self.MACD_SIGNALitem = testitem.loc['MACD_SIGNAL']
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem)):
                return True
            else:
                return False
        else:
            return True
        
    def Check_Entry_miu(self, testitem, permitem):
        self.tech_dict = permitem
        self.entryba = self.tech_dict['MACD']['GOLDEN CROSS']
        if (self.entryba == 'True'):
            self.MACDitem = testitem.loc['MACD']
            self.MACD_SIGNALitem = testitem.loc['MACD_SIGNAL']
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        else:
            return True

    def Check_Exit_miu(self, testitem, permitem):
        self.tech_dict = permitem
        self.exitba = self.tech_dict['MACD']['Death Cross']
        if (self.exitba == 'True'):
            self.MACDitem = testitem.loc['MACD']
            self.MACD_SIGNALitem = testitem.loc['MACD_SIGNAL']
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem)):
                return True
            else:
                return False
        else:
            return True

    def get_db_for_entry_exit(self, testitem):
        self.ChecklistClose = []
        self.Checklisthis = []
        self.df = self.gettertoolhistory()
        self.targetindex = testitem
        for i in range(1, 3):
            previous_close = self.df.shift(i).loc[(self.df['MACD'] == self.targetindex['MACD']) & (self.df['MACD_SIGNAL'] == self.targetindex['MACD_SIGNAL']) & (
                self.df['Close'] == self.targetindex['Close'])].head(1)
            # Add 'Close' values to self.Checklist
            if not previous_close.empty:
                self.ChecklistClose.append(previous_close['Close'].iloc[0])
                self.Checklisthis.append(previous_close['MACD_HIST'].iloc[0])
            else:
                break
        return self.ChecklistClose, self.Checklisthis

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

        self.signalperiodlabel = QLabel('Signalperiod :')
        self.signalperiodlabel.setMinimumSize(QSize(150, 25))
        self.signalperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.signalperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.signalperiodlineedit.setText(str(self.signalperiod))
        self.signalperiodlineedit.setMinimumSize(QSize(200, 25))
        self.signalperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.Fastperiodlabel, self.fastperiodlineedit)
        self.formlayout.addRow(self.slowperiodlabel, self.slowperiodlineedit)
        self.formlayout.addRow(self.signalperiodlabel,
                               self.signalperiodlineedit)
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
        self.tool_dict['MACD'] = {}
        self.tool_dict['MACD']['fastperiod'] = self.fastperiodlineedit.text()
        self.tool_dict['MACD']['slowperiod'] = self.slowperiodlineedit.text()
        self.tool_dict['MACD']['signalperiod'] = self.signalperiodlineedit.text()
        return self.tool_dict

    def uploadValue(self):
        self.global_dict = self.getterTechValue()
        tool_dict = self.tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterTechValue(self.global_dict)
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
        self.datadb["MACD"], self.datadb["MACD_SIGNAL"], self.datadb["MACD_HIST"] = talib.MACD(
            self.datadb['Close'], fastperiod=int(self.fastperiod), slowperiod=int(self.slowperiod), signalperiod=int(self.signalperiod))
        self.settertoolhistory(self.datadb)

    def calculate_miu(self, database, parameter):
        if 'MACD' in parameter:
            self.fastperiod = parameter['MACD']['fastperiod']
            self.slowperiod = parameter['MACD']['slowperiod']
            self.signalperiod = parameter['MACD']['signalperiod']
        else:
            self.fastperiod = 12
            self.slowperiod = 26
            self.signalperiod = 9

        self.datadb = database
        self.datadb["MACD"], self.datadb["MACD_SIGNAL"], self.datadb["MACD_HIST"] = talib.MACD(
            self.datadb['Close'], fastperiod=int(self.fastperiod), slowperiod=int(self.slowperiod), signalperiod=int(self.signalperiod))
        return self.datadb

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
        self.tool_dict['MACD'] = {}
        self.tool_dict['MACD']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['MACD']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
