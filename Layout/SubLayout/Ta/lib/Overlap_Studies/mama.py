import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox,QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class mama():
    def __init__(self):
        super().__init__()
        self.fastlimit = self.fastlimitsetup()
        self.slowlimit = self.slowlimitsetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()      
        self.fastlimitlineedit = QLineEdit()
        self.slowlimitlineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'MAMA': {'fastlimit': 0.5, 'slowlimit': 0.05}}

    def entry_exit_base(self):
        self.entryprofo = {'MAMA': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo
    
    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['MAMA']['GOLDEN CROSS']
        self.MACDitem = testitem.loc['MAMA']
        self.MACD_SIGNALitem = testitem.loc['MAMA_FAMA']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        else:
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['MAMA']['Death Cross']
        self.MACDitem = testitem.loc['MAMA']
        self.MACD_SIGNALitem = testitem.loc['MAMA_FAMA']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        else:
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
    
    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MAMA' in tech_dict:
            self.data = tech_dict['MAMA']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'MAMA' in tech_dict:
            self.data = tech_dict['MAMA']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def fastlimitsetup(self):
        tech_dict = self.getterTechValue()
        if 'MAMA' in tech_dict:
            self.data = tech_dict['MAMA']['fastlimit']
            return self.data
        else:
            self.datadef = 0.5
            return self.datadef

    def slowlimitsetup(self):
        tech_dict = self.getterTechValue()
        if 'MAMA' in tech_dict:
            self.data = tech_dict['MAMA']['slowlimit']
            return self.data
        else:
            self.datadef = 0.05
            return self.datadef

    def widgetedit(self):
        self.fastlimitlabel = QLabel('Fastlimit :')
        self.fastlimitlabel.setMinimumSize(QSize(150, 25))
        self.fastlimitlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fastlimitlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.fastlimitlineedit.setText(str(self.fastlimit))
        self.fastlimitlineedit.setMinimumSize(QSize(200, 25))
        self.fastlimitlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.slowlimitlabel = QLabel('Slowlimit :')
        self.slowlimitlabel.setMinimumSize(QSize(150, 25))
        self.slowlimitlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slowlimitlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.slowlimitlineedit.setText(str(self.slowlimit))
        self.slowlimitlineedit.setMinimumSize(QSize(200, 25))
        self.slowlimitlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.fastlimitlabel, self.fastlimitlineedit)
        self.formlayout.addRow(self.slowlimitlabel, self.slowlimitlineedit)
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
        self.tool_dict['MAMA'] = {}
        self.tool_dict['MAMA']['fastlimit'] = self.fastlimitlineedit.text()
        self.tool_dict['MAMA']['slowlimit'] = self.slowlimitlineedit.text()
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
        self.datadb["MAMA"], self.datadb["MAMA_FAMA"] = talib.MAMA(
            self.datadb['Close'], fastlimit=float(self.fastlimit), slowlimit=float(self.slowlimit))
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
        self.tool_dict['MAMA'] = {}
        self.tool_dict['MAMA']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['MAMA']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')