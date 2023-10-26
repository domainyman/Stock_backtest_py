import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox,QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class bbands():
    def __init__(self):
        super().__init__()
        self.timeperiod = self.timeperiodsetup()
        self.nbdevup = self.nbdevupsetup()
        self.nbdevdn = self.nbdevdnsetup()
        self.matype = self.matypesetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()        
        self.timeperiodlineedit = QLineEdit()
        self.nbdevuplineedit = QLineEdit()
        self.nbdevdnlineedit = QLineEdit()
        self.matypelineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'BBANDS': {'timeperiod': 5, 'nbdevup': 2, 'nbdevdn': 2, 'matype': 0}}
    
    def entry_exit_base(self):
        self.entryprofo = {'BBANDS': {'BBANDS_UPPERBAND': 'True', 'BBANDS_LOWERBAND': 'True'}}
        return self.entryprofo
    
    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['BBANDS']['BBANDS_UPPERBAND']
        self.MACDitem = testitem.loc['Close']
        self.MACD_SIGNALitem = testitem.loc['BBANDS_UPPERBAND']
        self.entryMIDDLEBAND = testitem.loc['BBANDS_MIDDLEBAND']
        if (self.entryba == 'True'):
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem) and float(self.MACDitem) < float(self.entryMIDDLEBAND)):
                return True
            else:
                return False
        elif(self.entryba == 'False'):
            if (float(self.MACDitem) > float(self.MACD_SIGNALitem) and float(self.MACDitem) > float(self.entryMIDDLEBAND)):
                return True
            else:
                return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['BBANDS']['BBANDS_LOWERBAND']
        self.MACDitem = testitem.loc['Close']
        self.MACD_SIGNALitem = testitem.loc['BBANDS_LOWERBAND']
        self.entryMIDDLEBAND = testitem.loc['BBANDS_MIDDLEBAND']
        if (self.exitba == 'True'):
            if (float(self.MACDitem) > float(self.MACD_SIGNALitem) and float(self.MACDitem) > float(self.entryMIDDLEBAND)):
                return True
            else:
                return False
        elif(self.entryba == 'False'):
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem) and float(self.MACDitem) < float(self.entryMIDDLEBAND)):
                return True
            else:
                return False

    def timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['timeperiod']
            return self.data
        else:
            self.datadef = 5
            return self.datadef

    def nbdevupsetup(self):
        tech_dict = self.getterTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['nbdevup']
            return self.data
        else:
            self.datadef = 2
            return self.datadef

    def nbdevdnsetup(self):
        tech_dict = self.getterTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['nbdevdn']
            return self.data
        else:
            self.datadef = 2
            return self.datadef

    def matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['BBANDS_LOWERBAND']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'BBANDS' in tech_dict:
            self.data = tech_dict['BBANDS']['BBANDS_UPPERBAND']
            return self.data
        else:
            self.datadef = 'True'
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
        self.nbdevuplabel = QLabel('nbdevup :')
        self.nbdevuplabel.setMinimumSize(QSize(150, 25))
        self.nbdevuplabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nbdevuplabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.nbdevuplineedit.setText(str(self.nbdevup))
        self.nbdevuplineedit.setMinimumSize(QSize(200, 25))
        self.nbdevuplineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.nbdevdnlabel = QLabel('nbdevdn :')
        self.nbdevdnlabel.setMinimumSize(QSize(150, 25))
        self.nbdevdnlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nbdevdnlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.nbdevdnlineedit.setText(str(self.nbdevdn))
        self.nbdevdnlineedit.setMinimumSize(QSize(200, 25))
        self.nbdevdnlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.matypelabel = QLabel('matype :')
        self.matypelabel.setMinimumSize(QSize(150, 25))
        self.matypelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.matypelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.matypelineedit.setText(str(self.matype))
        self.matypelineedit.setMinimumSize(QSize(200, 25))
        self.matypelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.timeperiodlabel, self.timeperiodlineedit)
        self.formlayout.addRow(self.nbdevuplabel, self.nbdevuplineedit)
        self.formlayout.addRow(self.nbdevdnlabel, self.nbdevdnlineedit)
        self.formlayout.addRow(self.matypelabel, self.matypelineedit)
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
        self.tool_dict['BBANDS'] = {}
        self.tool_dict['BBANDS']['timeperiod'] = self.timeperiodlineedit.text()
        self.tool_dict['BBANDS']['nbdevup'] = self.nbdevuplineedit.text()
        self.tool_dict['BBANDS']['nbdevdn'] = self.nbdevdnlineedit.text()
        self.tool_dict['BBANDS']['matype'] = self.matypelineedit.text()
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
        self.datadb["BBANDS_UPPERBAND"], self.datadb["BBANDS_MIDDLEBAND"], self.datadb["BBANDS_LOWERBAND"] = talib.BBANDS(
            self.datadb['Close'], timeperiod=int(self.timeperiod), nbdevup=int(self.nbdevup), nbdevdn=int(self.nbdevdn), matype=int(self.matype))
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
        self.tool_dict['BBANDS'] = {}
        self.tool_dict['BBANDS']['BBANDS_LOWERBAND'] = self.buysignalcb.currentText()
        self.tool_dict['BBANDS']['BBANDS_UPPERBAND'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')