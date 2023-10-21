import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class adxr():
    def __init__(self):
        super().__init__()
        self.parameter = self.setup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.lineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()

    def base(self):
        return {'ADXR': 14}

    def entry_exit_base(self):
        self.entryprofo = {'ADXR': {'HIGH': 35, 'LOW': 25}}
        return self.entryprofo

    def setup(self):
        tech_dict = self.getterTechValue()
        if 'ADXR' in tech_dict:
            self.data = tech_dict['ADXR']
            return self.data
        else:
            self.datadef = 14
            return self.datadef

    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ADXR' in tech_dict:
            self.data = tech_dict['ADXR']['HIGH']
            return self.data
        else:
            self.datadef = 35
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ADXR' in tech_dict:
            self.data = tech_dict['ADXR']['LOW']
            return self.data
        else:
            self.datadef = 25
            return self.datadef

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['ADXR']
        self.entryba = self.tech_dict['ADXR']['LOW']
        if (float(self.item) <= float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['ADXR']
        self.entryba = self.tech_dict['ADXR']['HIGH']
        if (float(self.item) >= float(self.entryba)):
            return True
        else:
            return False

    def widgetedit(self):
        self.label = QLabel('Parameter :')
        self.label.setMinimumSize(QSize(150, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.lineedit.setText(str(self.parameter))
        self.lineedit.setMinimumSize(QSize(200, 25))
        self.lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.label, self.lineedit)
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
        self.tool_dict['ADXR'] = self.lineedit.text()
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
        self.datadb["ADXR"] = talib.ADXR(
            self.datadb["High"], self.datadb["Low"], self.datadb["Close"], timeperiod=int(self.parameter))
        self.settertoolhistory(self.datadb)

    def calculate_miu(self, database, parameter):
        if 'ADXR' in parameter:
            self.parameter = parameter['ADXR']
        else:
            self.parameter = 14
        self.datadb = database
        self.datadb["ADXR"] = talib.ADXR(
            self.datadb["High"], self.datadb["Low"], self.datadb["Close"], timeperiod=int(self.parameter))
        return self.datadb

    def Check_Entry_miu(self, testitem, permitem):
        self.tech_dict = permitem
        self.item = testitem.loc['ADXR']
        self.entryba = self.tech_dict['ADXR']['LOW']
        if (float(self.item) <= float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit_miu(self, testitem, permitem):
        self.tech_dict = permitem
        self.item = testitem.loc['ADXR']
        self.entryba = self.tech_dict['ADXR']['HIGH']
        if (float(self.item) >= float(self.entryba)):
            return True
        else:
            return False

    def entrywidgetedit(self):
        self.highlabel = QLabel('HIGH :')
        self.highlabel.setMinimumSize(QSize(150, 25))
        self.highlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.EntryHighlineedit.setText(str(self.entryHIGHparameter))
        self.EntryHighlineedit.setMinimumSize(QSize(200, 25))
        self.EntryHighlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.Lowlabel = QLabel('LOW :')
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
        self.tool_dict['ADXR'] = {}
        self.tool_dict['ADXR']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['ADXR']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
