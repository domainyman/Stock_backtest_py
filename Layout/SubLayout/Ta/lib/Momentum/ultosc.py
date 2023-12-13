import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class ultosc():
    def __init__(self):
        super().__init__()
        self.timeperiod1 = self.timeperiod1setup()
        self.timeperiod2 = self.timeperiod2setup()
        self.timeperiod3 = self.timeperiod3setup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.timeperiod1lineedit = QLineEdit()
        self.timeperiod2lineedit = QLineEdit()
        self.timeperiod3lineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()

    def base(self):
        return {'ULTOSC': {'timeperiod1': 7, 'timeperiod2': 14, 'timeperiod3': 28}}

    def entry_exit_base(self):
        self.entryprofo = {'ULTOSC': {'HIGH': 70, 'LOW': 30}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['ULTOSC']
        self.entryba = self.tech_dict['ULTOSC']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['ULTOSC']
        self.entryba = self.tech_dict['ULTOSC']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def timeperiod1setup(self):
        tech_dict = self.getterTechValue()
        if 'ULTOSC' in tech_dict:
            self.data = tech_dict['ULTOSC']['timeperiod1']
            return self.data
        else:
            self.datadef = 7
            return self.datadef

    def timeperiod2setup(self):
        tech_dict = self.getterTechValue()
        if 'ULTOSC' in tech_dict:
            self.data = tech_dict['ULTOSC']['timeperiod2']
            return self.data
        else:
            self.datadef = 14
            return self.datadef

    def timeperiod3setup(self):
        tech_dict = self.getterTechValue()
        if 'ULTOSC' in tech_dict:
            self.data = tech_dict['ULTOSC']['timeperiod3']
            return self.data
        else:
            self.datadef = 28
            return self.datadef
        
    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ULTOSC' in tech_dict:
            self.data = tech_dict['ULTOSC']['HIGH']
            return self.data
        else:
            self.datadef = 70
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'ULTOSC' in tech_dict:
            self.data = tech_dict['ULTOSC']['LOW']
            return self.data
        else:
            self.datadef = '30'
            return self.datadef

    def widgetedit(self):
        self.timeperiod1label = QLabel('Timeperiod1 :')
        self.timeperiod1label.setMinimumSize(QSize(150, 25))
        self.timeperiod1label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeperiod1label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.timeperiod1lineedit.setText(str(self.timeperiod1))
        self.timeperiod1lineedit.setMinimumSize(QSize(200, 25))
        self.timeperiod1lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.timeperiod2label = QLabel('Timeperiod2 :')
        self.timeperiod2label.setMinimumSize(QSize(150, 25))
        self.timeperiod2label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeperiod2label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.timeperiod2lineedit.setText(str(self.timeperiod2))
        self.timeperiod2lineedit.setMinimumSize(QSize(200, 25))
        self.timeperiod2lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.timeperiod3label = QLabel('Timeperiod3 :')
        self.timeperiod3label.setMinimumSize(QSize(150, 25))
        self.timeperiod3label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeperiod3label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.timeperiod3lineedit.setText(str(self.timeperiod3))
        self.timeperiod3lineedit.setMinimumSize(QSize(200, 25))
        self.timeperiod3lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.timeperiod1label,
                               self.timeperiod1lineedit)
        self.formlayout.addRow(self.timeperiod2label,
                               self.timeperiod2lineedit)
        self.formlayout.addRow(self.timeperiod3label,
                               self.timeperiod3lineedit)
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
        self.tool_dict['ULTOSC'] = {}
        self.tool_dict['ULTOSC']['timeperiod1'] = self.timeperiod1lineedit.text()
        self.tool_dict['ULTOSC']['timeperiod2'] = self.timeperiod2lineedit.text()
        self.tool_dict['ULTOSC']['timeperiod3'] = self.timeperiod3lineedit.text()
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
        self.datadb["ULTOSC"] = talib.ULTOSC(
            self.datadb['High'], self.datadb['Low'], self.datadb['Close'], timeperiod1=int(self.timeperiod1), timeperiod2=int(self.timeperiod2), timeperiod3=int(self.timeperiod3))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.highlabel = QLabel('Exit :')
        self.highlabel.setMinimumSize(QSize(150, 25))
        self.highlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.EntryHighlineedit.setText(str(self.entryHIGHparameter))
        self.EntryHighlineedit.setMinimumSize(QSize(200, 25))
        self.EntryHighlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.Lowlabel = QLabel('Entry :')
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
        self.tool_dict['ULTOSC'] = {}
        self.tool_dict['ULTOSC']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['ULTOSC']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
