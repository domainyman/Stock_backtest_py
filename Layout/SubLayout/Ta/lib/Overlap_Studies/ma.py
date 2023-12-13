import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class ma():
    def __init__(self):
        super().__init__()
        self.timeperiod = self.timeperiodsetup()
        self.matype = self.matypesetup()
        self.timeperiodlineedit = QLineEdit()
        self.matypelineedit = QLineEdit()

    def base(self):
        return {'MA': {'timeperiod': 30, 'matype': 0}}
    
    def entry_exit_base(self):
        pass

    def Check_Entry(self, testitem):
        return True

    def Check_Exit(self, testitem):
        return True



    def timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'MA' in tech_dict:
            self.data = tech_dict['MA']['timeperiod']
            return self.data
        else:
            self.datadef = 30
            return self.datadef

    def matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'MA' in tech_dict:
            self.data = tech_dict['MA']['matype']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def widgetedit(self):
        self.timeperiodlabel = QLabel('Timeperiod :')
        self.timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.timeperiodlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.timeperiodlineedit.setText(str(self.timeperiod))
        self.timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.matypelabel = QLabel('Matype :')
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
        self.tool_dict['MA'] = {}
        self.tool_dict['MA']['timeperiod'] = self.timeperiodlineedit.text()
        self.tool_dict['MA']['matype'] = self.matypelineedit.text()
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

    def calculate(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["MA"] = talib.MA(
            self.datadb['Close'], timeperiod=int(self.timeperiod), matype=int(self.matype))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        pass

