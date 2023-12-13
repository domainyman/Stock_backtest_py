import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class sar():
    def __init__(self):
        super().__init__()
        self.acceleration = self.accelerationsetup()
        self.maximum = self.maximumsetup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.accelerationlineedit = QLineEdit()
        self.maximumlineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'SAR': {'acceleration': 0.02, 'maximum': 0.2}}

    def entry_exit_base(self):
        self.entryprofo = {
            'SAR': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['SAR']['GOLDEN CROSS']
        self.MIDPOINTitem = testitem.loc['SAR']
        self.Closeitem = testitem.loc['Close']
        if (self.entryba == 'True'):
            if float(self.MIDPOINTitem) < float(self.Closeitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MIDPOINTitem) > float(self.Closeitem):
                return True
            else:
                return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.exitba = self.tech_dict['SAR']['Death Cross']
        self.MIDPOINTitem = testitem.loc['SAR']
        self.Closeitem = testitem.loc['Close']
        if (self.exitba == 'True'):
            if float(self.MIDPOINTitem) > float(self.Closeitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MIDPOINTitem) < float(self.Closeitem):
                return True
            else:
                return False

    def accelerationsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAR' in tech_dict:
            self.data = tech_dict['SAR']['acceleration']
            return self.data
        else:
            self.datadef = 0.02
            return self.datadef

    def maximumsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAR' in tech_dict:
            self.data = tech_dict['SAR']['maximum']
            return self.data
        else:
            self.datadef = 0.2
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'SAR' in tech_dict:
            self.data = tech_dict['SAR']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'SAR' in tech_dict:
            self.data = tech_dict['SAR']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def widgetedit(self):
        self.accelerationlabel = QLabel('Acceleration :')
        self.accelerationlabel.setMinimumSize(QSize(150, 25))
        self.accelerationlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accelerationlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationlineedit.setText(str(self.acceleration))
        self.accelerationlineedit.setMinimumSize(QSize(200, 25))
        self.accelerationlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.maximumlabel = QLabel('Maximum :')
        self.maximumlabel.setMinimumSize(QSize(150, 25))
        self.maximumlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.maximumlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.maximumlineedit.setText(str(self.maximum))
        self.maximumlineedit.setMinimumSize(QSize(200, 25))
        self.maximumlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.accelerationlabel,
                               self.accelerationlineedit)
        self.formlayout.addRow(self.maximumlabel, self.maximumlineedit)
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
        self.tool_dict['SAR'] = {}
        self.tool_dict['SAR']['acceleration'] = self.accelerationlineedit.text()
        self.tool_dict['SAR']['maximum'] = self.maximumlineedit.text()
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
        self.datadb["SAR"] = talib.SAR(
            self.datadb['High'], self.datadb['Low'], acceleration=float(self.acceleration), maximum=float(self.maximum))
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
        self.tool_dict['SAR'] = {}
        self.tool_dict['SAR']['GOLDEN CROSS'] = self.buysignalcb.currentText()
        self.tool_dict['SAR']['Death Cross'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
