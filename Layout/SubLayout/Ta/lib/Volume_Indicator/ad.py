import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class ad():
    def __init__(self):
        super().__init__()
        self.parameter = self.setup()
        self.buysignal = self.buysignalsetup()
        self.sellsignal = self.sellsignalsetup()
        self.lineedit = QLineEdit()
        self.buysignalcb = QComboBox()
        self.sellsignalcb = QComboBox()

    def base(self):
        return {'AD': 14}

    def entry_exit_base(self):
        self.entryprofo = {
            'AD': {'Bottom Divergence': 'True', 'Top Divergence': 'True'}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['AD']['Bottom Divergence']
        self.itemclose = testitem.loc['Close']
        self.itemad = testitem.loc['AD']
        self.oldclose, self.oldad = self.get_db_for_entry_exit(testitem)
        self.close_test = self.Check_AD_CLOSE_RELAT(
            self.oldclose, self.itemclose)
        self.ad_test = self.Check_AD_CLOSE_RELAT(self.oldad, self.itemad)
        if (self.entryba == 'True'):
            if (self.close_test == "000" and self.ad_test == "111"):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if (self.close_test == "111" and self.ad_test == "000"):
                return True
            else:
                return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.entryba = self.tech_dict['AD']['Top Divergence']
        if (self.entryba == 'True'):
            self.itemclose = testitem.loc['Close']
            self.itemad = testitem.loc['AD']
            self.oldclose, self.oldad = self.get_db_for_entry_exit(testitem)
            self.close_test = self.Check_AD_CLOSE_RELAT(
                self.oldclose, self.itemclose)
            self.ad_test = self.Check_AD_CLOSE_RELAT(self.oldad, self.itemad)
            if (self.close_test == "111" and self.ad_test == "000"):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if (self.close_test == "000" and self.ad_test == "111"):
                return True
            else:
                return False

    def get_db_for_entry_exit(self, testitem):
        self.ChecklistClose = []
        self.ChecklistAD = []
        self.df = self.gettertoolhistory()
        self.targetindex = testitem
        for i in range(1, 3):
            previous_close = self.df.shift(i).loc[(self.df['AD'] == self.targetindex['AD']) & (
                self.df['Close'] == self.targetindex['Close'])].head(1)
            # Add 'Close' values to self.Checklist
            if not previous_close.empty:
                self.ChecklistClose.append(previous_close['Close'].iloc[0])
                self.ChecklistAD.append(previous_close['AD'].iloc[0])
            else:
                break
        return self.ChecklistClose, self.ChecklistAD

    def Check_AD_CLOSE_RELAT(self, rel, new):
        self.new = new
        self.rel = rel
        if (self.rel != []):
            close_0 = self.rel[0]
            if (float(self.new) > float(close_0)):
                return "111"
            elif (float(self.new) < float(close_0)):
                return "000"
            else:
                return "Unknown"
        else:
            return "Unknown"

    def setup(self):
        tech_dict = self.getterTechValue()
        if 'AD' in tech_dict:
            self.data = tech_dict['AD']
            return self.data
        else:
            self.datadef = 14
            return self.datadef

    def buysignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'AD' in tech_dict:
            self.data = tech_dict['AD']['Bottom Divergence']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup(self):
        tech_dict = self.getterEntryTechValue()
        if 'AD' in tech_dict:
            self.data = tech_dict['AD']['Top Divergence']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

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
        self.tool_dict['AD'] = self.lineedit.text()
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
        self.datadb["AD"] = talib.AD(
            self.datadb["High"], self.datadb["Low"], self.datadb["Close"], self.datadb["Volume"])
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel = QLabel('Bottom Divergence :')
        self.buylabel.setMinimumSize(QSize(150, 25))
        self.buylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb.addItems(['True', 'False'])
        self.buysignalcb.setCurrentText(str(self.buysignal))
        self.buysignalcb.setMinimumSize(QSize(200, 25))
        self.buysignalcb.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel = QLabel('Top Divergence :')
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
        self.tool_dict['AD'] = {}
        self.tool_dict['AD']['Bottom Divergence'] = self.buysignalcb.currentText()
        self.tool_dict['AD']['Top Divergence'] = self.sellsignalcb.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
