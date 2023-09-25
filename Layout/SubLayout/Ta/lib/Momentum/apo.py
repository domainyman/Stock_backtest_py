import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class apo():
    def __init__(self):
        super().__init__()
        self.fastperiod = self.fastperiodsetup()
        self.slowperiod = self.slowperiodsetup()
        self.matype = self.matypesetup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.fastperiodlineedit = QLineEdit()
        self.slowperiodlineedit = QLineEdit()
        self.matypelineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()

    def base(self):
        return {'APO': {'fastperiod': '12', 'slowperiod': '26', 'matype': '0'}}

    def entry_exit_base(self):
        self.entryprofo = {'ADXR': {'HIGH': '5', 'LOW': '-5'}}
        return self.entryprofo

    def fastperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'APO' in tech_dict:
            self.data = tech_dict['APO']['fastperiod']
            return self.data
        else:
            self.datadef = '12'
            return self.datadef

    def slowperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'APO' in tech_dict:
            self.data = tech_dict['APO']['slowperiod']
            return self.data
        else:
            self.datadef = '26'
            return self.datadef

    def matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'APO' in tech_dict:
            self.data = tech_dict['APO']['matype']
            return self.data
        else:
            self.datadef = '0'
            return self.datadef
        
    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'APO' in tech_dict:
            self.data = tech_dict['APO']['HIGH']
            return self.data
        else:
            self.datadef = '5'
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'APO' in tech_dict:
            self.data = tech_dict['APO']['LOW']
            return self.data
        else:
            self.datadef = '-5'
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
        self.formlayout.addRow(self.Fastperiodlabel, self.fastperiodlineedit)
        self.formlayout.addRow(self.slowperiodlabel, self.slowperiodlineedit)
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
        self.tool_dict['APO'] = {}
        self.tool_dict['APO']['fastperiod'] = self.fastperiodlineedit.text()
        self.tool_dict['APO']['slowperiod'] = self.slowperiodlineedit.text()
        self.tool_dict['APO']['matype'] = self.matypelineedit.text()
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
        self.datadb["APO"] = talib.APO(
            self.datadb['Close'], fastperiod=int(self.fastperiod), slowperiod=int(self.slowperiod), matype=int(self.matype))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.highlabel = QLabel('High :')
        self.highlabel.setMinimumSize(QSize(150, 25))
        self.highlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.EntryHighlineedit.setText(str(self.entryHIGHparameter))
        self.EntryHighlineedit.setMinimumSize(QSize(200, 25))
        self.EntryHighlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.Lowlabel = QLabel('Low :')
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
        self.tool_dict['APO'] = {}
        self.tool_dict['APO']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['APO']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')