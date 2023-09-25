import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class kdj():
    def __init__(self):
        super().__init__()
        self.fastk_period = self.fastk_periodsetup()
        self.slowk_period = self.slowk_periodsetup()
        self.slowk_matype = self.slowk_matypesetup()
        self.slowd_period = self.slowd_periodsetup()
        self.slowd_matype = self.slowd_matypesetup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.fastk_periodlineedit = QLineEdit()
        self.slowk_periodlineedit = QLineEdit()
        self.slowk_matypelineedit = QLineEdit()
        self.slowd_periodlineedit = QLineEdit()
        self.slowd_matypelineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()

    def base(self):
        return {'KDJ': {'fastk_period': '5', 'slowk_period': '3', 'slowk_matype': '0', 'slowd_period': '3', 'slowd_matype': '0'}}

    def entry_exit_base(self):
        self.entryprofo = {'KDJ': {'HIGH': '90', 'LOW': '10'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['KDJ_SLOWJ']
        self.entryba = self.tech_dict['KDJ']['LOW']
        if (float(self.item) <= float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['KDJ_SLOWJ']
        self.entryba = self.tech_dict['KDJ']['HIGH']
        if (float(self.item) >= float(self.entryba)):
            return True
        else:
            return False

    def fastk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['fastk_period']
            return self.data
        else:
            self.datadef = '5'
            return self.datadef

    def slowk_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['slowk_period']
            return self.data
        else:
            self.datadef = '3'
            return self.datadef

    def slowk_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['slowk_matype']
            return self.data
        else:
            self.datadef = '0'
            return self.datadef

    def slowd_periodsetup(self):
        tech_dict = self.getterTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['slowd_period']
            return self.data
        else:
            self.datadef = '3'
            return self.datadef

    def slowd_matypesetup(self):
        tech_dict = self.getterTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['slowd_matype']
            return self.data
        else:
            self.datadef = '0'
            return self.datadef
        
    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['HIGH']
            return self.data
        else:
            self.datadef = '90'
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'KDJ' in tech_dict:
            self.data = tech_dict['KDJ']['LOW']
            return self.data
        else:
            self.datadef = '10'
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
        self.formlayout.addRow(self.Fastk_periodlabel, self.fastk_periodlineedit)
        self.formlayout.addRow(self.slowk_periodlabel, self.slowk_periodlineedit)
        self.formlayout.addRow(self.slowk_matypelabel, self.slowk_matypelineedit)
        self.formlayout.addRow(self.slowd_periodlabel, self.slowd_periodlineedit)
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
        self.tool_dict['KDJ'] = {}
        self.tool_dict['KDJ']['fastk_period'] = self.fastk_periodlineedit.text()
        self.tool_dict['KDJ']['slowk_period'] = self.slowk_periodlineedit.text()
        self.tool_dict['KDJ']['slowk_matype'] = self.slowk_matypelineedit.text()
        self.tool_dict['KDJ']['slowd_period'] = self.slowd_periodlineedit.text()
        self.tool_dict['KDJ']['slowd_matype'] = self.slowd_matypelineedit.text()
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
        self.datadb["KDJ_SLOWK"], self.datadb["KDJ_SLOWD"] = talib.STOCH(
            self.datadb['High'],self.datadb['Low'],self.datadb['Close'], fastk_period=int(self.fastk_period), slowk_period=int(self.slowk_period), slowk_matype=int(self.slowk_matype), slowd_period=int(self.slowd_period), slowd_matype=int(self.slowd_matype))
        self.datadb['KDJ_SLOWJ']=3*self.datadb['KDJ_SLOWK']-2*self.datadb['KDJ_SLOWD']
        
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
        self.tool_dict['KDJ'] = {}
        self.tool_dict['KDJ']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['KDJ']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
