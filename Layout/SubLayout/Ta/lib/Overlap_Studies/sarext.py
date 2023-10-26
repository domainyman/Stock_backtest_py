import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class sarext():
    def __init__(self):
        super().__init__()
        self.startvalue = self.startvaluesetup()
        self.offsetonreverse = self.offsetonreversesetup()
        self.accelerationinitlong = self.accelerationinitlongsetup()
        self.accelerationlong = self.accelerationlongsetup()
        self.accelerationmaxlong = self.accelerationmaxlongsetup()
        self.accelerationinitshort = self.accelerationinitshortsetup()
        self.accelerationshort = self.accelerationshortsetup()
        self.accelerationmaxshort = self.accelerationmaxshortsetup()
        self.entryHIGHparameter = self.highsetup()
        self.entryLOWparameter = self.lowsetup()
        self.startvaluelineedit = QLineEdit()
        self.offsetonreverselineedit = QLineEdit()
        self.accelerationinitlonglineedit = QLineEdit()
        self.accelerationlonglineedit = QLineEdit()
        self.accelerationmaxlonglineedit = QLineEdit()
        self.accelerationinitshortlineedit = QLineEdit()
        self.accelerationshortlineedit = QLineEdit()
        self.accelerationmaxshortlineedit = QLineEdit()
        self.EntryHighlineedit = QLineEdit()
        self.EntryLowlineedit = QLineEdit()

    def base(self):
        return {'SAREXT': {'startvalue': 0, 'offsetonreverse': 0, 'accelerationinitlong': 0.02, 'accelerationlong': 0.02,
                            'accelerationmaxlong': 0.2, 'accelerationinitshort': 0.02, 'accelerationshort': 0.02, 'accelerationmaxshort': 0.2}}
    
    def entry_exit_base(self):
        self.entryprofo = {'SAREXT': {'HIGH': '100', 'LOW': '-100'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['SAREXT']
        self.entryba = self.tech_dict['SAREXT']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.item = testitem.loc['SAREXT']
        self.entryba = self.tech_dict['SAREXT']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def startvaluesetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['startvalue']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def offsetonreversesetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['offsetonreverse']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def accelerationinitlongsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationinitlong']
            return self.data
        else:
            self.datadef = 0.02
            return self.datadef

    def accelerationlongsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationlong']
            return self.data
        else:
            self.datadef = 0.02
            return self.datadef

    def accelerationmaxlongsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationmaxlong']
            return self.data
        else:
            self.datadef = 0.2
            return self.datadef

    def accelerationinitshortsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationinitshort']
            return self.data
        else:
            self.datadef = 0.02
            return self.datadef

    def accelerationshortsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationshort']
            return self.data
        else:
            self.datadef = 0.02
            return self.datadef

    def accelerationmaxshortsetup(self):
        tech_dict = self.getterTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['accelerationmaxshort']
            return self.data
        else:
            self.datadef = 0.2
            return self.datadef
        
    def highsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['HIGH']
            return self.data
        else:
            self.datadef = 100
            return self.datadef

    def lowsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'SAREXT' in tech_dict:
            self.data = tech_dict['SAREXT']['LOW']
            return self.data
        else:
            self.datadef = -100
            return self.datadef

    def widgetedit(self):
        self.startvaluelabel = QLabel('Startvalue :')
        self.startvaluelabel.setMinimumSize(QSize(150, 25))
        self.startvaluelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.startvaluelabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.startvaluelineedit.setText(str(self.startvalue))
        self.startvaluelineedit.setMinimumSize(QSize(200, 25))
        self.startvaluelineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.offsetonreverselabel = QLabel('Offsetonreverse :')
        self.offsetonreverselabel.setMinimumSize(QSize(150, 25))
        self.offsetonreverselabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.offsetonreverselabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.offsetonreverselineedit.setText(str(self.offsetonreverse))
        self.offsetonreverselineedit.setMinimumSize(QSize(200, 25))
        self.offsetonreverselineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.accelerationinitlonglabel = QLabel('Accelerationinitlong :')
        self.accelerationinitlonglabel.setMinimumSize(QSize(150, 25))
        self.accelerationinitlonglabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.accelerationinitlonglabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationinitlonglineedit.setText(
            str(self.accelerationinitlong))
        self.accelerationinitlonglineedit.setMinimumSize(QSize(200, 25))
        self.accelerationinitlonglineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.accelerationlonglabel = QLabel('Accelerationlong :')
        self.accelerationlonglabel.setMinimumSize(QSize(150, 25))
        self.accelerationlonglabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accelerationlonglabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationlonglineedit.setText(str(self.accelerationlong))
        self.accelerationlonglineedit.setMinimumSize(QSize(200, 25))
        self.accelerationlonglineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.accelerationmaxlonglabel = QLabel('Accelerationmaxlong :')
        self.accelerationmaxlonglabel.setMinimumSize(QSize(150, 25))
        self.accelerationmaxlonglabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.accelerationmaxlonglabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationmaxlonglineedit.setText(str(self.accelerationmaxlong))
        self.accelerationmaxlonglineedit.setMinimumSize(QSize(200, 25))
        self.accelerationmaxlonglineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.accelerationinitshortlabel = QLabel('Accelerationinitshort :')
        self.accelerationinitshortlabel.setMinimumSize(QSize(150, 25))
        self.accelerationinitshortlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.accelerationinitshortlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationinitshortlineedit.setText(
            str(self.accelerationinitshort))
        self.accelerationinitshortlineedit.setMinimumSize(QSize(200, 25))
        self.accelerationinitshortlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.accelerationshortlabel = QLabel('Accelerationshort :')
        self.accelerationshortlabel.setMinimumSize(QSize(150, 25))
        self.accelerationshortlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.accelerationshortlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationshortlineedit.setText(str(self.accelerationshort))
        self.accelerationshortlineedit.setMinimumSize(QSize(200, 25))
        self.accelerationshortlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.accelerationmaxshortlabel = QLabel('Accelerationmaxshort :')
        self.accelerationmaxshortlabel.setMinimumSize(QSize(150, 25))
        self.accelerationmaxshortlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.accelerationmaxshortlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.accelerationmaxshortlineedit.setText(
            str(self.accelerationmaxshort))
        self.accelerationmaxshortlineedit.setMinimumSize(QSize(200, 25))
        self.accelerationmaxshortlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.startvaluelabel, self.startvaluelineedit)
        self.formlayout.addRow(self.offsetonreverselabel,
                               self.offsetonreverselineedit)
        self.formlayout.addRow(
            self.accelerationinitlonglabel, self.accelerationinitlonglineedit)
        self.formlayout.addRow(self.accelerationlonglabel,
                               self.accelerationlonglineedit)
        self.formlayout.addRow(self.accelerationmaxlonglabel,
                               self.accelerationmaxlonglineedit)
        self.formlayout.addRow(self.accelerationinitshortlabel,
                               self.accelerationinitshortlineedit)
        self.formlayout.addRow(self.accelerationshortlabel,
                               self.accelerationshortlineedit)
        self.formlayout.addRow(self.accelerationmaxshortlabel,
                               self.accelerationmaxshortlineedit)
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
        self.tool_dict['SAREXT'] = {}
        self.tool_dict['SAREXT']['startvalue'] = self.startvaluelineedit.text()
        self.tool_dict['SAREXT']['offsetonreverse'] = self.offsetonreverselineedit.text()
        self.tool_dict['SAREXT']['accelerationinitlong'] = self.accelerationinitlonglineedit.text()
        self.tool_dict['SAREXT']['accelerationlong'] = self.accelerationlonglineedit.text()
        self.tool_dict['SAREXT']['accelerationmaxlong'] = self.accelerationmaxlonglineedit.text()
        self.tool_dict['SAREXT']['accelerationinitshort'] = self.accelerationinitshortlineedit.text()
        self.tool_dict['SAREXT']['accelerationshort'] = self.accelerationshortlineedit.text()
        self.tool_dict['SAREXT']['accelerationmaxshort'] = self.accelerationmaxshortlineedit.text()
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
        self.datadb["SAREXT"] = talib.SAREXT(self.datadb['High'],self.datadb['Low'], startvalue=float(self.startvalue), offsetonreverse=float(self.offsetonreverse), accelerationinitlong=float(
            self.accelerationinitlong), accelerationlong=float(self.accelerationlong), accelerationmaxlong=float(self.accelerationmaxlong),
            accelerationinitshort=float(self.accelerationinitshort), accelerationshort=float(self.accelerationshort), accelerationmaxshort=float(self.accelerationmaxshort))
        self.settertoolhistory(self.datadb)

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
        self.tool_dict['SAREXT'] = {}
        self.tool_dict['SAREXT']['HIGH'] = self.EntryHighlineedit.text()
        self.tool_dict['SAREXT']['LOW'] = self.EntryLowlineedit.text()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
