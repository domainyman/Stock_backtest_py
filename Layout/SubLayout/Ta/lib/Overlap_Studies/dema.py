import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class dema():
    def __init__(self):
        super().__init__()
        self.parameter_1 = self.Parameters_1setup()
        self.parameter_2 = self.Parameters_2setup()
        self.parameter_3 = self.Parameters_3setup()
        self.parameter_4 = self.Parameters_4setup()
        self.parameter_5 = self.Parameters_5setup()
        self.buysignal_1_2 = self.buysignalsetup_1_2()
        self.sellsignal_1_2 = self.sellsignalsetup_1_2()
        self.buysignal_2_3 = self.buysignalsetup_2_3()
        self.sellsignal_2_3 = self.sellsignalsetup_2_3()
        self.buysignal_3_4 = self.buysignalsetup_3_4()
        self.sellsignal_3_4 = self.sellsignalsetup_3_4()
        self.buysignal_4_5 = self.buysignalsetup_4_5()
        self.sellsignal_4_5 = self.sellsignalsetup_4_5()
        self.parameter_1lineedit = QLineEdit()
        self.parameter_2lineedit = QLineEdit()
        self.parameter_3lineedit = QLineEdit()
        self.parameter_4lineedit = QLineEdit()
        self.parameter_5lineedit = QLineEdit()
        self.buysignalcb_1_2 = QComboBox()
        self.sellsignalcb_1_2 = QComboBox()
        self.buysignalcb_2_3 = QComboBox()
        self.sellsignalcb_2_3 = QComboBox()
        self.buysignalcb_3_4 = QComboBox()
        self.sellsignalcb_3_4 = QComboBox()
        self.buysignalcb_4_5 = QComboBox()
        self.sellsignalcb_4_5 = QComboBox()

    def base(self):
        return {'DEMA': {'Parameters_1': 10, 'Parameters_2': 20, 'Parameters_3': 50, 'Parameters_4': 100, 'Parameters_5': 150}}

    def entry_exit_base(self):
        self.entryprofo = {'DEMA': {'Parameters_1 - Parameters_2': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'},
                                    'Parameters_2 - Parameters_3': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'},
                                    'Parameters_3 - Parameters_4': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'},
                                    'Parameters_4 - Parameters_5': {'GOLDEN CROSS': 'True', 'Death Cross': 'True'}}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.parameters_1_Parameters_2 = self.tech_dict['DEMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = self.tech_dict['DEMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = self.tech_dict['DEMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = self.tech_dict['DEMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        self.p1 = testitem.loc['DEMA_parameter_1']
        self.p2 = testitem.loc['DEMA_parameter_2']
        self.p3 = testitem.loc['DEMA_parameter_3']
        self.p4 = testitem.loc['DEMA_parameter_4']
        self.p5 = testitem.loc['DEMA_parameter_5']
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def Check_Exit(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.parameters_1_Parameters_2 = self.tech_dict['DEMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = self.tech_dict['DEMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = self.tech_dict['DEMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = self.tech_dict['DEMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        self.p1 = testitem.loc['DEMA_parameter_1']
        self.p2 = testitem.loc['DEMA_parameter_2']
        self.p3 = testitem.loc['DEMA_parameter_3']
        self.p4 = testitem.loc['DEMA_parameter_4']
        self.p5 = testitem.loc['DEMA_parameter_5']
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def buysignalsetup_1_2(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_1 - Parameters_2']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_1_2(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_1 - Parameters_2']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_2_3(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_2 - Parameters_3']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_2_3(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_2 - Parameters_3']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_3_4(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_3 - Parameters_4']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_3_4(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_3 - Parameters_4']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_4_5(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_4 - Parameters_5']['GOLDEN CROSS']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_4_5(self):
        tech_dict = self.getterEntryTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_4 - Parameters_5']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def Parameters_1setup(self):
        tech_dict = self.getterTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_1']
            return self.data
        else:
            self.datadef = 10
            return self.datadef

    def Parameters_2setup(self):
        tech_dict = self.getterTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_2']
            return self.data
        else:
            self.datadef = 20
            return self.datadef

    def Parameters_3setup(self):
        tech_dict = self.getterTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_3']
            return self.data
        else:
            self.datadef = 50
            return self.datadef

    def Parameters_4setup(self):
        tech_dict = self.getterTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_4']
            return self.data
        else:
            self.datadef = 100
            return self.datadef

    def Parameters_5setup(self):
        tech_dict = self.getterTechValue()
        if 'DEMA' in tech_dict:
            self.data = tech_dict['DEMA']['Parameters_5']
            return self.data
        else:
            self.datadef = 150
            return self.datadef

    def widgetedit(self):
        self.parameter_1label = QLabel('Parameter_1 :')
        self.parameter_1label.setMinimumSize(QSize(150, 25))
        self.parameter_1label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_1label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_1lineedit.setText(str(self.parameter_1))
        self.parameter_1lineedit.setMinimumSize(QSize(200, 25))
        self.parameter_1lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_2label = QLabel('Parameter_2 :')
        self.parameter_2label.setMinimumSize(QSize(150, 25))
        self.parameter_2label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_2label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_2lineedit.setText(str(self.parameter_2))
        self.parameter_2lineedit.setMinimumSize(QSize(200, 25))
        self.parameter_2lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_3label = QLabel('Parameter_3 :')
        self.parameter_3label.setMinimumSize(QSize(150, 25))
        self.parameter_3label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_3label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_3lineedit.setText(str(self.parameter_3))
        self.parameter_3lineedit.setMinimumSize(QSize(200, 25))
        self.parameter_3lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_4label = QLabel('Parameter_4 :')
        self.parameter_4label.setMinimumSize(QSize(150, 25))
        self.parameter_4label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_4label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_4lineedit.setText(str(self.parameter_4))
        self.parameter_4lineedit.setMinimumSize(QSize(200, 25))
        self.parameter_4lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_5label = QLabel('Parameter_5 :')
        self.parameter_5label.setMinimumSize(QSize(150, 25))
        self.parameter_5label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_5label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_5lineedit.setText(str(self.parameter_5))
        self.parameter_5lineedit.setMinimumSize(QSize(200, 25))
        self.parameter_5lineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.parameter_1label, self.parameter_1lineedit)
        self.formlayout.addRow(self.parameter_2label, self.parameter_2lineedit)
        self.formlayout.addRow(self.parameter_3label, self.parameter_3lineedit)
        self.formlayout.addRow(self.parameter_4label, self.parameter_4lineedit)
        self.formlayout.addRow(self.parameter_5label, self.parameter_5lineedit)
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
        self.tool_dict['DEMA'] = {}
        self.tool_dict['DEMA']['Parameters_1'] = self.parameter_1lineedit.text()
        self.tool_dict['DEMA']['Parameters_2'] = self.parameter_2lineedit.text()
        self.tool_dict['DEMA']['Parameters_3'] = self.parameter_3lineedit.text()
        self.tool_dict['DEMA']['Parameters_4'] = self.parameter_4lineedit.text()
        self.tool_dict['DEMA']['Parameters_5'] = self.parameter_5lineedit.text()
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
        self.datadb["DEMA_parameter_1"] = talib.DEMA(
            self.datadb["Close"], timeperiod=int(self.parameter_1))
        self.datadb["DEMA_parameter_2"] = talib.DEMA(
            self.datadb["Close"], timeperiod=int(self.parameter_2))
        self.datadb["DEMA_parameter_3"] = talib.DEMA(
            self.datadb["Close"], timeperiod=int(self.parameter_3))
        self.datadb["DEMA_parameter_4"] = talib.DEMA(
            self.datadb["Close"], timeperiod=int(self.parameter_4))
        self.datadb["DEMA_parameter_5"] = talib.DEMA(
            self.datadb["Close"], timeperiod=int(self.parameter_5))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel_1_2 = QLabel('Parameters_1-2-GOLDEN CROSS:')
        self.buylabel_1_2.setMinimumSize(QSize(150, 25))
        self.buylabel_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_1_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_1_2.addItems(['True', 'False'])
        self.buysignalcb_1_2.setCurrentText(str(self.buysignal_1_2))
        self.buysignalcb_1_2.setMinimumSize(QSize(200, 25))
        self.buysignalcb_1_2.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_1_2 = QLabel('Parameters_1-2-Death Cross :')
        self.selllabel_1_2.setMinimumSize(QSize(150, 25))
        self.selllabel_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_1_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_1_2.addItems(['True', 'False'])
        self.sellsignalcb_1_2.setCurrentText(str(self.sellsignal_1_2))
        self.sellsignalcb_1_2.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_1_2.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_2_3 = QLabel('Parameters_2-3-GOLDEN CROSS:')
        self.buylabel_2_3.setMinimumSize(QSize(150, 25))
        self.buylabel_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_2_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_2_3.addItems(['True', 'False'])
        self.buysignalcb_2_3.setCurrentText(str(self.buysignal_2_3))
        self.buysignalcb_2_3.setMinimumSize(QSize(200, 25))
        self.buysignalcb_2_3.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_2_3 = QLabel('Parameters_2-3-Death Cross :')
        self.selllabel_2_3.setMinimumSize(QSize(150, 25))
        self.selllabel_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_2_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_2_3.addItems(['True', 'False'])
        self.sellsignalcb_2_3.setCurrentText(str(self.sellsignal_2_3))
        self.sellsignalcb_2_3.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_2_3.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_3_4 = QLabel('Parameters_3-4-GOLDEN CROSS:')
        self.buylabel_3_4.setMinimumSize(QSize(150, 25))
        self.buylabel_3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_3_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_3_4.addItems(['True', 'False'])
        self.buysignalcb_3_4.setCurrentText(str(self.buysignal_3_4))
        self.buysignalcb_3_4.setMinimumSize(QSize(200, 25))
        self.buysignalcb_3_4.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_3_4 = QLabel('Parameters_3-4-Death Cross :')
        self.selllabel_3_4.setMinimumSize(QSize(150, 25))
        self.selllabel_3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_3_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_3_4.addItems(['True', 'False'])
        self.sellsignalcb_3_4.setCurrentText(str(self.sellsignal_3_4))
        self.sellsignalcb_3_4.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_3_4.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_4_5 = QLabel('Parameters_4-5-GOLDEN CROSS:')
        self.buylabel_4_5.setMinimumSize(QSize(150, 25))
        self.buylabel_4_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_4_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_4_5.addItems(['True', 'False'])
        self.buysignalcb_4_5.setCurrentText(str(self.buysignal_4_5))
        self.buysignalcb_4_5.setMinimumSize(QSize(200, 25))
        self.buysignalcb_4_5.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_4_5 = QLabel('Parameters_4-5-Death Cross :')
        self.selllabel_4_5.setMinimumSize(QSize(150, 25))
        self.selllabel_4_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_4_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_4_5.addItems(['True', 'False'])
        self.sellsignalcb_4_5.setCurrentText(str(self.sellsignal_4_5))
        self.sellsignalcb_4_5.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_4_5.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.buylabel_1_2, self.buysignalcb_1_2)
        self.formlayout.addRow(self.selllabel_1_2, self.sellsignalcb_1_2)
        self.formlayout.addRow(self.buylabel_2_3, self.buysignalcb_2_3)
        self.formlayout.addRow(self.selllabel_2_3, self.sellsignalcb_2_3)
        self.formlayout.addRow(self.buylabel_3_4, self.buysignalcb_3_4)
        self.formlayout.addRow(self.selllabel_3_4, self.sellsignalcb_3_4)
        self.formlayout.addRow(self.buylabel_4_5, self.buysignalcb_4_5)
        self.formlayout.addRow(self.selllabel_4_5, self.sellsignalcb_4_5)
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
        self.tool_dict['DEMA'] = {}
        self.tool_dict['DEMA']['Parameters_1 - Parameters_2'] = {}
        self.tool_dict['DEMA']['Parameters_1 - Parameters_2']['GOLDEN CROSS'] = self.buysignalcb_1_2.currentText()
        self.tool_dict['DEMA']['Parameters_1 - Parameters_2']['Death Cross'] = self.sellsignalcb_1_2.currentText()
        self.tool_dict['DEMA']['Parameters_2 - Parameters_3'] = {}
        self.tool_dict['DEMA']['Parameters_2 - Parameters_3']['GOLDEN CROSS'] = self.buysignalcb_2_3.currentText()
        self.tool_dict['DEMA']['Parameters_2 - Parameters_3']['Death Cross'] = self.sellsignalcb_2_3.currentText()
        self.tool_dict['DEMA']['Parameters_3 - Parameters_4'] = {}
        self.tool_dict['DEMA']['Parameters_3 - Parameters_4']['GOLDEN CROSS'] = self.buysignalcb_3_4.currentText()
        self.tool_dict['DEMA']['Parameters_3 - Parameters_4']['Death Cross'] = self.sellsignalcb_3_4.currentText()
        self.tool_dict['DEMA']['Parameters_4 - Parameters_5'] = {}
        self.tool_dict['DEMA']['Parameters_4 - Parameters_5']['GOLDEN CROSS'] = self.buysignalcb_4_5.currentText()
        self.tool_dict['DEMA']['Parameters_4 - Parameters_5']['Death Cross'] = self.sellsignalcb_4_5.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
