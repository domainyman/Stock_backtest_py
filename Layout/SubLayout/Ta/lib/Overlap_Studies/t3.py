import talib
from PyQt6.QtWidgets import QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QMessageBox, QComboBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class t3():
    def __init__(self):
        super().__init__()
        self.parameter_1timeperiod = self.parameter_1timeperiodsetup()
        self.parameter_1vfactor = self.parameter_1vfactorsetup()
        self.parameter_1timeperiodlineedit = QLineEdit()
        self.parameter_1vfactorlineedit = QLineEdit()

        self.parameter_2timeperiod = self.parameter_2timeperiodsetup()
        self.parameter_2vfactor = self.parameter_2vfactorsetup()
        self.parameter_2timeperiodlineedit = QLineEdit()
        self.parameter_2vfactorlineedit = QLineEdit()

        self.parameter_3timeperiod = self.parameter_3timeperiodsetup()
        self.parameter_3vfactor = self.parameter_3vfactorsetup()
        self.parameter_3timeperiodlineedit = QLineEdit()
        self.parameter_3vfactorlineedit = QLineEdit()

        self.parameter_4timeperiod = self.parameter_4timeperiodsetup()
        self.parameter_4vfactor = self.parameter_4vfactorsetup()
        self.parameter_4timeperiodlineedit = QLineEdit()
        self.parameter_4vfactorlineedit = QLineEdit()

        self.parameter_5timeperiod = self.parameter_5timeperiodsetup()
        self.parameter_5vfactor = self.parameter_5vfactorsetup()
        self.parameter_5timeperiodlineedit = QLineEdit()
        self.parameter_5vfactorlineedit = QLineEdit()

        self.buysignal_1_2 = self.buysignalsetup_1_2()
        self.sellsignal_1_2 = self.sellsignalsetup_1_2()
        self.buysignal_2_3 = self.buysignalsetup_2_3()
        self.sellsignal_2_3 = self.sellsignalsetup_2_3()
        self.buysignal_3_4 = self.buysignalsetup_3_4()
        self.sellsignal_3_4 = self.sellsignalsetup_3_4()
        self.buysignal_4_5 = self.buysignalsetup_4_5()
        self.sellsignal_4_5 = self.sellsignalsetup_4_5()
        self.buysignalcb_1_2 = QComboBox()
        self.sellsignalcb_1_2 = QComboBox()
        self.buysignalcb_2_3 = QComboBox()
        self.sellsignalcb_2_3 = QComboBox()
        self.buysignalcb_3_4 = QComboBox()
        self.sellsignalcb_3_4 = QComboBox()
        self.buysignalcb_4_5 = QComboBox()
        self.sellsignalcb_4_5 = QComboBox()

    def base(self):
        return {'T3': {'parameter_1timeperiod': 5, 'parameter_1vfactor': 0,
                       'parameter_2timeperiod': 20, 'parameter_2vfactor': 0,
                       'parameter_3timeperiod': 50, 'parameter_3vfactor': 0,
                       'parameter_4timeperiod': 100, 'parameter_4vfactor': 0,
                       'parameter_5timeperiod': 150, 'parameter_5vfactor': 0}}

    def entry_exit_base(self):
        self.entryprofo = {'T3': {'Parameters_1 - Parameters_2': {'Golden Cross': 'True', 'Death Cross': 'True'},
                                  'Parameters_2 - Parameters_3': {'Golden Cross': 'True', 'Death Cross': 'True'},
                                  'Parameters_3 - Parameters_4': {'Golden Cross': 'True', 'Death Cross': 'True'},
                                  'Parameters_4 - Parameters_5': {'Golden Cross': 'True', 'Death Cross': 'True'}}}
        return self.entryprofo

    def Check_Entry(self, testitem):
        self.tech_dict = self.getterEntryTechValue()
        self.parameters_1_Parameters_2 = self.tech_dict['T3'][
            'Parameters_1 - Parameters_2']['Golden Cross']
        self.parameters_2_Parameters_3 = self.tech_dict['T3'][
            'Parameters_2 - Parameters_3']['Golden Cross']
        self.parameters_3_Parameters_4 = self.tech_dict['T3'][
            'Parameters_3 - Parameters_4']['Golden Cross']
        self.parameters_4_Parameters_5 = self.tech_dict['T3'][
            'Parameters_4 - Parameters_5']['Golden Cross']
        self.p1 = testitem.loc['T3_parameter_1']
        self.p2 = testitem.loc['T3_parameter_2']
        self.p3 = testitem.loc['T3_parameter_3']
        self.p4 = testitem.loc['T3_parameter_4']
        self.p5 = testitem.loc['T3_parameter_5']
        
        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
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
        self.parameters_1_Parameters_2 = self.tech_dict['T3'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = self.tech_dict['T3'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = self.tech_dict['T3'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = self.tech_dict['T3'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = testitem.loc['T3_parameter_1']
        self.p2 = testitem.loc['T3_parameter_2']
        self.p3 = testitem.loc['T3_parameter_3']
        self.p4 = testitem.loc['T3_parameter_4']
        self.p5 = testitem.loc['T3_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
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

    def parameter_1timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_1timeperiod']
            return self.data
        else:
            self.datadef = 5
            return self.datadef

    def parameter_1vfactorsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_1vfactor']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def parameter_2timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_2timeperiod']
            return self.data
        else:
            self.datadef = 20
            return self.datadef

    def parameter_2vfactorsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_2vfactor']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def parameter_3timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_3timeperiod']
            return self.data
        else:
            self.datadef = 50
            return self.datadef

    def parameter_3vfactorsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_3vfactor']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def parameter_4timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_4timeperiod']
            return self.data
        else:
            self.datadef = 100
            return self.datadef

    def parameter_4vfactorsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_4vfactor']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def parameter_5timeperiodsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_5timeperiod']
            return self.data
        else:
            self.datadef = 150
            return self.datadef

    def parameter_5vfactorsetup(self):
        tech_dict = self.getterTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['parameter_5vfactor']
            return self.data
        else:
            self.datadef = 0
            return self.datadef

    def buysignalsetup_1_2(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_1 - Parameters_2']['Golden Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_1_2(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_1 - Parameters_2']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_2_3(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_2 - Parameters_3']['Golden Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_2_3(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_2 - Parameters_3']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_3_4(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_3 - Parameters_4']['Golden Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_3_4(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_3 - Parameters_4']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def buysignalsetup_4_5(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_4 - Parameters_5']['Golden Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def sellsignalsetup_4_5(self):
        tech_dict = self.getterEntryTechValue()
        if 'T3' in tech_dict:
            self.data = tech_dict['T3']['Parameters_4 - Parameters_5']['Death Cross']
            return self.data
        else:
            self.datadef = 'True'
            return self.datadef

    def widgetedit(self):
        self.parameter_1timeperiodlabel = QLabel('parameter_1timeperiod :')
        self.parameter_1timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.parameter_1timeperiodlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.parameter_1timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_1timeperiodlineedit.setText(
            str(self.parameter_1timeperiod))
        self.parameter_1timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_1timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_1vfactorlabel = QLabel('parameter_1vfactor :')
        self.parameter_1vfactorlabel.setMinimumSize(QSize(150, 25))
        self.parameter_1vfactorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_1vfactorlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_1vfactorlineedit.setText(str(self.parameter_1vfactor))
        self.parameter_1vfactorlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_1vfactorlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.parameter_2timeperiodlabel = QLabel('parameter_2timeperiod :')
        self.parameter_2timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.parameter_2timeperiodlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.parameter_2timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_2timeperiodlineedit.setText(
            str(self.parameter_2timeperiod))
        self.parameter_2timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_2timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_2vfactorlabel = QLabel('parameter_2vfactor :')
        self.parameter_2vfactorlabel.setMinimumSize(QSize(150, 25))
        self.parameter_2vfactorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_2vfactorlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_2vfactorlineedit.setText(str(self.parameter_2vfactor))
        self.parameter_2vfactorlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_2vfactorlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.parameter_3timeperiodlabel = QLabel('parameter_3timeperiod :')
        self.parameter_3timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.parameter_3timeperiodlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.parameter_3timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_3timeperiodlineedit.setText(
            str(self.parameter_3timeperiod))
        self.parameter_3timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_3timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_3vfactorlabel = QLabel('parameter_3vfactor :')
        self.parameter_3vfactorlabel.setMinimumSize(QSize(150, 25))
        self.parameter_3vfactorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_3vfactorlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_3vfactorlineedit.setText(str(self.parameter_3vfactor))
        self.parameter_3vfactorlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_3vfactorlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_4timeperiodlabel = QLabel('parameter_4timeperiod :')
        self.parameter_4timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.parameter_4timeperiodlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.parameter_4timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_4timeperiodlineedit.setText(
            str(self.parameter_4timeperiod))
        self.parameter_4timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_4timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_4vfactorlabel = QLabel('parameter_4vfactor :')
        self.parameter_4vfactorlabel.setMinimumSize(QSize(150, 25))
        self.parameter_4vfactorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_4vfactorlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_4vfactorlineedit.setText(str(self.parameter_4vfactor))
        self.parameter_4vfactorlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_4vfactorlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.parameter_5timeperiodlabel = QLabel('parameter_5timeperiod :')
        self.parameter_5timeperiodlabel.setMinimumSize(QSize(150, 25))
        self.parameter_5timeperiodlabel.setAlignment(
            Qt.AlignmentFlag.AlignCenter)
        self.parameter_5timeperiodlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_5timeperiodlineedit.setText(
            str(self.parameter_5timeperiod))
        self.parameter_5timeperiodlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_5timeperiodlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.parameter_5vfactorlabel = QLabel('parameter_5vfactor :')
        self.parameter_5vfactorlabel.setMinimumSize(QSize(150, 25))
        self.parameter_5vfactorlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parameter_5vfactorlabel.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")

        self.parameter_5vfactorlineedit.setText(str(self.parameter_5vfactor))
        self.parameter_5vfactorlineedit.setMinimumSize(QSize(200, 25))
        self.parameter_5vfactorlineedit.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

        self.formlayout = QFormLayout()
        self.formlayout.addRow(
            self.parameter_1timeperiodlabel, self.parameter_1timeperiodlineedit)
        self.formlayout.addRow(self.parameter_1vfactorlabel,
                               self.parameter_1vfactorlineedit)

        self.formlayout.addRow(
            self.parameter_2timeperiodlabel, self.parameter_2timeperiodlineedit)
        self.formlayout.addRow(self.parameter_2vfactorlabel,
                               self.parameter_2vfactorlineedit)
        self.formlayout.addRow(
            self.parameter_3timeperiodlabel, self.parameter_3timeperiodlineedit)
        self.formlayout.addRow(self.parameter_3vfactorlabel,
                               self.parameter_3vfactorlineedit)

        self.formlayout.addRow(
            self.parameter_4timeperiodlabel, self.parameter_4timeperiodlineedit)
        self.formlayout.addRow(self.parameter_4vfactorlabel,
                               self.parameter_4vfactorlineedit)
        self.formlayout.addRow(
            self.parameter_5timeperiodlabel, self.parameter_5timeperiodlineedit)
        self.formlayout.addRow(self.parameter_5vfactorlabel,
                               self.parameter_5vfactorlineedit)
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
        self.tool_dict['T3'] = {}
        self.tool_dict['T3']['parameter_1timeperiod'] = self.parameter_1timeperiodlineedit.text()
        self.tool_dict['T3']['parameter_1vfactor'] = self.parameter_1vfactorlineedit.text()
        self.tool_dict['T3']['parameter_2timeperiod'] = self.parameter_2timeperiodlineedit.text()
        self.tool_dict['T3']['parameter_2vfactor'] = self.parameter_2vfactorlineedit.text()
        self.tool_dict['T3']['parameter_3timeperiod'] = self.parameter_3timeperiodlineedit.text()
        self.tool_dict['T3']['parameter_3vfactor'] = self.parameter_3vfactorlineedit.text()
        self.tool_dict['T3']['parameter_4timeperiod'] = self.parameter_4timeperiodlineedit.text()
        self.tool_dict['T3']['parameter_4vfactor'] = self.parameter_4vfactorlineedit.text()
        self.tool_dict['T3']['parameter_5timeperiod'] = self.parameter_5timeperiodlineedit.text()
        self.tool_dict['T3']['parameter_5vfactor'] = self.parameter_5vfactorlineedit.text()
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
        self.datadb["T3_parameter_1"] = talib.T3(
            self.datadb['Close'], timeperiod=int(self.parameter_1timeperiod), vfactor=int(self.parameter_1vfactor))
        self.datadb["T3_parameter_2"] = talib.T3(
            self.datadb['Close'], timeperiod=int(self.parameter_2timeperiod), vfactor=int(self.parameter_2vfactor))
        self.datadb["T3_parameter_3"] = talib.T3(
            self.datadb['Close'], timeperiod=int(self.parameter_3timeperiod), vfactor=int(self.parameter_3vfactor))
        self.datadb["T3_parameter_4"] = talib.T3(
            self.datadb['Close'], timeperiod=int(self.parameter_4timeperiod), vfactor=int(self.parameter_4vfactor))
        self.datadb["T3_parameter_5"] = talib.T3(
            self.datadb['Close'], timeperiod=int(self.parameter_5timeperiod), vfactor=int(self.parameter_5vfactor))
        self.settertoolhistory(self.datadb)

    def entrywidgetedit(self):
        self.buylabel_1_2 = QLabel('Parameters_1 - 2: Golden Cross:')
        self.buylabel_1_2.setMinimumSize(QSize(200, 25))
        self.buylabel_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_1_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_1_2.addItems(['True', 'False'])
        self.buysignalcb_1_2.setCurrentText(str(self.buysignal_1_2))
        self.buysignalcb_1_2.setMinimumSize(QSize(200, 25))
        self.buysignalcb_1_2.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_1_2 = QLabel('Parameters_1 - 2: Death Cross :')
        self.selllabel_1_2.setMinimumSize(QSize(200, 25))
        self.selllabel_1_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_1_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_1_2.addItems(['True', 'False'])
        self.sellsignalcb_1_2.setCurrentText(str(self.sellsignal_1_2))
        self.sellsignalcb_1_2.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_1_2.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_2_3 = QLabel('Parameters_2 - 3: Golden Cross:')
        self.buylabel_2_3.setMinimumSize(QSize(200, 25))
        self.buylabel_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_2_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_2_3.addItems(['True', 'False'])
        self.buysignalcb_2_3.setCurrentText(str(self.buysignal_2_3))
        self.buysignalcb_2_3.setMinimumSize(QSize(200, 25))
        self.buysignalcb_2_3.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_2_3 = QLabel('Parameters_2 - 3: Death Cross :')
        self.selllabel_2_3.setMinimumSize(QSize(200, 25))
        self.selllabel_2_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_2_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_2_3.addItems(['True', 'False'])
        self.sellsignalcb_2_3.setCurrentText(str(self.sellsignal_2_3))
        self.sellsignalcb_2_3.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_2_3.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_3_4 = QLabel('Parameters_3 - 4: Golden Cross:')
        self.buylabel_3_4.setMinimumSize(QSize(200, 25))
        self.buylabel_3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_3_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_3_4.addItems(['True', 'False'])
        self.buysignalcb_3_4.setCurrentText(str(self.buysignal_3_4))
        self.buysignalcb_3_4.setMinimumSize(QSize(200, 25))
        self.buysignalcb_3_4.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_3_4 = QLabel('Parameters_3 - 4: Death Cross :')
        self.selllabel_3_4.setMinimumSize(QSize(200, 25))
        self.selllabel_3_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selllabel_3_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.sellsignalcb_3_4.addItems(['True', 'False'])
        self.sellsignalcb_3_4.setCurrentText(str(self.sellsignal_3_4))
        self.sellsignalcb_3_4.setMinimumSize(QSize(200, 25))
        self.sellsignalcb_3_4.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.buylabel_4_5 = QLabel('Parameters_4 - 5: Golden Cross:')
        self.buylabel_4_5.setMinimumSize(QSize(200, 25))
        self.buylabel_4_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buylabel_4_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.buysignalcb_4_5.addItems(['True', 'False'])
        self.buysignalcb_4_5.setCurrentText(str(self.buysignal_4_5))
        self.buysignalcb_4_5.setMinimumSize(QSize(200, 25))
        self.buysignalcb_4_5.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.selllabel_4_5 = QLabel('Parameters_4 - 5: Death Cross :')
        self.selllabel_4_5.setMinimumSize(QSize(200, 25))
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
        self.tool_dict['T3'] = {}
        self.tool_dict['T3']['Parameters_1 - Parameters_2'] = {}
        self.tool_dict['T3']['Parameters_1 - Parameters_2']['Golden Cross'] = self.buysignalcb_1_2.currentText()
        self.tool_dict['T3']['Parameters_1 - Parameters_2']['Death Cross'] = self.sellsignalcb_1_2.currentText()
        self.tool_dict['T3']['Parameters_2 - Parameters_3'] = {}
        self.tool_dict['T3']['Parameters_2 - Parameters_3']['Golden Cross'] = self.buysignalcb_2_3.currentText()
        self.tool_dict['T3']['Parameters_2 - Parameters_3']['Death Cross'] = self.sellsignalcb_2_3.currentText()
        self.tool_dict['T3']['Parameters_3 - Parameters_4'] = {}
        self.tool_dict['T3']['Parameters_3 - Parameters_4']['Golden Cross'] = self.buysignalcb_3_4.currentText()
        self.tool_dict['T3']['Parameters_3 - Parameters_4']['Death Cross'] = self.sellsignalcb_3_4.currentText()
        self.tool_dict['T3']['Parameters_4 - Parameters_5'] = {}
        self.tool_dict['T3']['Parameters_4 - Parameters_5']['Golden Cross'] = self.buysignalcb_4_5.currentText()
        self.tool_dict['T3']['Parameters_4 - Parameters_5']['Death Cross'] = self.sellsignalcb_4_5.currentText()
        return self.tool_dict

    def uploadentryValue(self):
        self.global_dict = self.getterEntryTechValue()
        tool_dict = self.Entry_tool_dicts()
        self.global_dict.update(tool_dict)
        self.setterEntryTechValue(self.global_dict)
        print(self.getterEntryTechValue())
        QMessageBox.information(None, 'Parameter Saved',
                                'Saved Parameter Setting')
