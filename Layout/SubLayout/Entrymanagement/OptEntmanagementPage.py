from Layout.Ui_Layout.Entrymanagement.Ui_entrymanagement import Ui_EntryManagement
from PyQt6.QtWidgets import QDialog, QMenu, QMessageBox, QLabel, QLineEdit, QFormLayout, QVBoxLayout, QComboBox, QPushButton, QScrollBar, QMessageBox
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets
from Layout.SubLayout.Ta.talib_lib import talib_list
from Global.Value.TechToolParam import TechValue


class optEntrymanagepage(QDialog, Ui_EntryManagement):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_EntryManagement()
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        self.reloadvalue()
        self.btn()

    def btn(self):
        self.ui.Btn_Entrymm_reset.clicked.connect(self.listwidgetreset)
        self.ui.EntrytoollistWidget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.EntrytoollistWidget.customContextMenuRequested.connect(
            self.showContextMenu)
        self.ui.Btn_Entrymm_enter.clicked.connect(self.close)

    def listwidgetreset(self):
        try:
            if (self.clearwidget() == True):
                self.setterTechValue({})
                self.setterEntryTechValue({})
                self.setterEntryRangeTechValue({})
                self.setterEntryRangeValue({})
                self.ui.EntrytoollistWidget.clear()
                self.ui.EntrytoollistWidget.clearSelection()
                self.ui.EntrytoollistWidget.setCurrentItem(None)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def showContextMenu(self, pos):
        item = self.ui.EntrytoollistWidget.itemAt(pos)
        if item is not None:
            menu = QMenu("Meun", self)
            self.e = QAction("Edit")
            # self.d = QAction("Delete")
            menu.addAction(self.e)
            # menu.addAction(self.d)
            action = menu.exec(self.mapToGlobal(pos))
            if action == self.e:
                print("Opening Edit...")
                self.indicatoredit(
                    self.ui.EntrytoollistWidget.currentItem().text())
                # Your code here
            # if action == self.d:
            #     print("Opening Del...")
            #     self.deletedictitem()
            #     if (self.clearwidget() == True):
            #         self.deletelistitem(self.listcurrentRow())
                # Your code here
            if action is not None:
                print(
                    f'Action "{action.text()}" selected for item "{item.text()}"')

    def listcurrentRow(self):
        index = self.ui.EntrytoollistWidget.currentIndex()
        return index.row()

    def deletelistitem(self, index):
        self.ui.EntrytoollistWidget.takeItem(index)

    def clearwidget(self):
        try:
            layout = self.ui.EntrygroupverticalLayout  # 要清除的 QVBoxLayout
            for i in reversed(range(layout.count())):  # 從後往前迭代佈局中的元素
                item = layout.itemAt(i)
                if isinstance(item, QtWidgets.QVBoxLayout):  # 如果是 QVBoxLayout，遞迴清除其中的元素
                    for j in reversed(range(item.count())):
                        sub_item = item.itemAt(j)
                        # 如果是 QFormLayout，清除其中的 QPushButton 和 QLabel
                        if isinstance(sub_item, QtWidgets.QFormLayout):
                            for k in reversed(range(sub_item.count())):
                                form_item = sub_item.itemAt(k)
                                if isinstance(form_item.widget(), (QtWidgets.QPushButton, QtWidgets.QLabel, QtWidgets.QLineEdit, QtWidgets.QComboBox)):
                                    widget = form_item.widget()
                                    sub_item.removeWidget(widget)
                                    widget.setParent(None)
                        elif item.itemAt(j).widget() is not None:
                            widget = item.itemAt(j).widget()
                            item.removeWidget(widget)
                            widget.setParent(None)
            return True
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))
            return False

    def indicatoredit(self, text):
        try:
            if (self.clearwidget() == True):
                self.return_Tech_tool_perm(text)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def return_Tech_tool_perm(self, text):
        self.tech_tool_key = self.getterEntryTechValue()
        if (self.check_dict_contains_dict(self.tech_tool_key, text) == True):
            self.dict_key_value = self.tech_tool_key[text].keys()
            for permvalue in self.dict_key_value:
                self.dictbool = self.check_dict_contains_true(
                    self.tech_tool_key, text, permvalue)
                if (self.dictbool == "Bool"):
                    self.returnwidget = self.createboolwidget_setup(
                        text, textname=permvalue)
                    self.ui.EntrygroupverticalLayout.addLayout(
                        self.returnwidget)
                elif (self.dictbool == "Int"):
                    self.returnwidget = self.createstepwidget_setup(
                        text, textname=permvalue)
                    self.ui.EntrygroupverticalLayout.addLayout(
                        self.returnwidget)
                elif (self.dictbool == "Dict"):
                    self.dict_list = self.tech_tool_key[text][permvalue].keys()
                    for per in self.dict_list:
                        self.returnwidget = self.createdictboolwidget_setup(
                            text, textname=permvalue, textcontext=per)
                        self.ui.EntrygroupverticalLayout.addLayout(
                            self.returnwidget)

    def check_dict_contains_dict(self, your_dict, key):
        if isinstance(your_dict.get(key), dict):
            return True
        else:
            return False

    def check_dict_contains_true(self, your_dict, text, permvalue):
        values = your_dict[text][permvalue]
        if (values == 'True') or (values == 'False'):
            return "Bool"
        elif (isinstance(values, int)):
            return "Int"
        elif (isinstance(values, dict)):
            return "Dict"

    def createdictboolwidget_setup(self, textmain, textname=None, textcontext=None):
        if (textname is not None) and (textcontext is not None):
            self.keyvalue = self.getterEntryRangeValue(
            )[textmain][textname][textcontext]
            self.techvalue = self.getterEntryTechValue(
            )[textmain][textname][textcontext]
            # main
            self.__dict__[textmain + textname + textcontext +
                          'mainlabel'] = QLabel(textcontext)
            self.__dict__[textmain + textname + textcontext +
                          'mainlabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[textmain + textname + textcontext +
                          'mainlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + textcontext + 'mainlabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname + textcontext +
                          'dfvalue'] = QLabel(str(textname) + ' Parameter : ' + str(self.techvalue))
            self.__dict__[textmain + textname + textcontext +
                          'dfvalue'].setMinimumSize(QSize(100, 25))
            self.__dict__[textmain + textname + textcontext +
                          'dfvalue'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + textcontext + 'dfvalue'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname + textcontext +
                          'boolparameter'] = self.keyvalue
            self.__dict__[textmain + textname + textcontext +
                          'boollabel'] = QLabel('Bool :')
            self.__dict__[textmain + textname + textcontext +
                          'boollabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[textmain + textname + textcontext +
                          'boollabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + textcontext + 'boollabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname + textcontext +
                          'booledit'] = QComboBox()
            self.item = ['', 'Both Test', 'False', 'True']
            self.__dict__[textmain + textname + textcontext +
                          'booledit'].addItems(self.item)
            if (self.keyvalue == {'True', 'False', 'Both Test'}):
                index = self.__dict__[textmain +
                                      textname + textcontext + 'booledit'].findText(str(''))
                self.__dict__[textmain + textname + textcontext +
                              'booledit'].setCurrentIndex(index)
            else:
                index = self.__dict__[textmain + textname + textcontext +
                                      'booledit'].findText(str(self.keyvalue))
                self.__dict__[textmain + textname + textcontext +
                              'booledit'].setCurrentIndex(index)
            self.__dict__[textmain + textname + textcontext +
                          'booledit'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + textname + textcontext + 'booledit'].setStyleSheet(
                "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

            self.__dict__[textmain + textname +
                          textcontext + 'formlayout'] = QFormLayout()
            self.__dict__[textmain + textname + textcontext + 'formlayout'].addRow(
                self.__dict__[textmain + textname + textcontext + 'mainlabel'], self.__dict__[textmain + textname + textcontext + 'dfvalue'])
            self.__dict__[textmain + textname + textcontext + 'formlayout'].addRow(self.__dict__[
                textmain + textname + textcontext + 'boollabel'], self.__dict__[textmain + textname + textcontext + 'booledit'])

            self.__dict__[textmain + textname + textcontext +
                          'button'] = QPushButton('Submit')
            self.__dict__[textmain + textname + textcontext + 'button'].clicked.connect(lambda: self.uploadboolvaluedict(
                textmain, self.__dict__[textmain + textname + textcontext + 'booledit'].currentText(), textname=textname, textcontext=textcontext))
            self.__dict__[textmain + textname + textcontext +
                          'button'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + textname + textcontext + 'button'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname +
                          textcontext + 'layout'] = QVBoxLayout()
            self.__dict__[textmain + textname + textcontext + 'layout'].addLayout(
                self.__dict__[textmain + textname + textcontext + 'formlayout'])
            self.__dict__[textmain + textname + textcontext +
                          'layout'].addWidget(self.__dict__[textmain + textname + textcontext + 'button'])
            return self.__dict__[textmain + textname + textcontext + 'layout']

    def createboolwidget_setup(self, textmain, textname=None):
        if (textname == None):
            pass
        else:
            self.keyvalue = self.getterEntryRangeValue()[textmain][textname]
            self.techvalue = self.getterEntryTechValue()[textmain][textname]
            # main
            self.__dict__[textmain + textname +
                          'mainlabel'] = QLabel(textname)
            self.__dict__[textmain + textname +
                          'mainlabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[textmain + textname +
                          'mainlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + 'mainlabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname +
                          'dfvalue'] = QLabel('Parameter : ' + str(self.techvalue))
            self.__dict__[textmain + textname +
                          'dfvalue'].setMinimumSize(QSize(100, 25))
            self.__dict__[textmain + textname +
                          'dfvalue'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + 'dfvalue'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname +
                          'boolparameter'] = self.keyvalue
            self.__dict__[textmain + textname +
                          'boollabel'] = QLabel('Bool :')
            self.__dict__[textmain + textname +
                          'boollabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[textmain + textname +
                          'boollabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + 'boollabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname +
                          'booledit'] = QComboBox()
            self.item = ['', 'Both Test', 'False', 'True']
            self.__dict__[textmain + textname +
                          'booledit'].addItems(self.item)
            if (self.keyvalue == {'True', 'False', 'Both Test'}):
                index = self.__dict__[textmain +
                                      textname + 'booledit'].findText(str(''))
                self.__dict__[textmain + textname +
                              'booledit'].setCurrentIndex(index)
            else:
                index = self.__dict__[textmain + textname +
                                      'booledit'].findText(str(self.keyvalue))
                self.__dict__[textmain + textname +
                              'booledit'].setCurrentIndex(index)
            self.__dict__[textmain + textname +
                          'booledit'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + textname + 'booledit'].setStyleSheet(
                "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")

            self.__dict__[textmain + textname + 'formlayout'] = QFormLayout()
            self.__dict__[textmain + textname + 'formlayout'].addRow(
                self.__dict__[textmain + textname + 'mainlabel'], self.__dict__[textmain + textname + 'dfvalue'])
            self.__dict__[textmain + textname + 'formlayout'].addRow(self.__dict__[
                textmain + textname + 'boollabel'], self.__dict__[textmain + textname + 'booledit'])

            self.__dict__[textmain + textname +
                          'button'] = QPushButton('Submit')
            self.__dict__[textmain + textname + 'button'].clicked.connect(lambda: self.uploadboolvalue(
                textmain, self.__dict__[textmain + textname + 'booledit'].currentText(), textname=textname))
            self.__dict__[textmain + textname +
                          'button'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + textname + 'button'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname + 'layout'] = QVBoxLayout()
            self.__dict__[textmain + textname + 'layout'].addLayout(
                self.__dict__[textmain + textname + 'formlayout'])
            self.__dict__[textmain + textname +
                          'layout'].addWidget(self.__dict__[textmain + textname + 'button'])
            return self.__dict__[textmain + textname + 'layout']

    def createstepwidget_setup(self, textmain, textname=None):
        if (textname == None):
            self.keyvalue = self.getterEntryRangeValue()[textmain]
            self.techvalue = self.getterEntryTechValue()[textmain]
            self.__dict__[textmain + 'mainlabel'] = QLabel(textmain)
            self.__dict__[textmain +
                          'mainlabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[
                textmain + 'mainlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + 'mainlabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain +
                          'dfvalue'] = QLabel('Parameter : ' + str(self.techvalue))
            self.__dict__[textmain +
                          'dfvalue'].setMinimumSize(QSize(100, 25))
            self.__dict__[
                textmain + 'dfvalue'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + 'dfvalue'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            for perm in self.keyvalue:
                if (perm == "First"):
                    self.__dict__[textmain +
                                  'Firstparameter'] = self.keyvalue['First']
                    self.__dict__[textmain + 'firstlabel'] = QLabel('First :')
                    self.__dict__[textmain +
                                  'firstlabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[
                        textmain + 'firstlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + 'firstlabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + 'firstedit'] = QLineEdit()
                    self.__dict__[
                        textmain + 'firstedit'].setText(str(self.__dict__[textmain + 'Firstparameter']))
                    self.__dict__[textmain +
                                  'firstedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + 'firstedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        ###############################
                elif (perm == "Last"):
                    self.__dict__[textmain +
                                  'Lastparameter'] = self.keyvalue['Last']
                    self.__dict__[textmain + 'nextlabel'] = QLabel('Last :')
                    self.__dict__[textmain +
                                  'nextlabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[
                        textmain + 'nextlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + 'nextlabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + 'nextedit'] = QLineEdit()
                    self.__dict__[
                        textmain + 'nextedit'].setText(str(self.__dict__[textmain + 'Lastparameter']))
                    self.__dict__[textmain +
                                  'nextedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + 'nextedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        ################################
                elif (perm == "Step"):
                    self.__dict__[textmain +
                                  'Stepparameter'] = self.keyvalue['Step']
                    self.__dict__[textmain + 'steplabel'] = QLabel('Step :')
                    self.__dict__[textmain +
                                  'steplabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[
                        textmain + 'steplabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + 'steplabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + 'stepedit'] = QLineEdit()
                    self.__dict__[
                        textmain + 'stepedit'].setText(str(self.__dict__[textmain + 'Stepparameter']))
                    self.__dict__[textmain +
                                  'stepedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + 'stepedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
            ########################
            self.__dict__[textmain + 'formlayout'] = QFormLayout()
            self.__dict__[
                textmain + 'formlayout'].addRow(self.__dict__[textmain + 'mainlabel'], self.__dict__[textmain + 'dfvalue'])
            self.__dict__[textmain + 'formlayout'].addRow(
                self.__dict__[textmain + 'firstlabel'], self.__dict__[textmain + 'firstedit'])
            self.__dict__[textmain + 'formlayout'].addRow(
                self.__dict__[textmain + 'nextlabel'], self.__dict__[textmain + 'nextedit'])
            self.__dict__[textmain + 'formlayout'].addRow(
                self.__dict__[textmain + 'steplabel'], self.__dict__[textmain + 'stepedit'])

            self.__dict__[textmain + 'button'] = QPushButton('Submit')
            self.__dict__[textmain + 'button'].clicked.connect(lambda: self.uploadRangeValue(
                textmain, self.__dict__[textmain + 'firstedit'].text(), self.__dict__[textmain + 'nextedit'].text(), self.__dict__[textmain + 'stepedit'].text()))
            self.__dict__[textmain + 'button'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + 'button'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + 'layout'] = QVBoxLayout()
            self.__dict__[
                textmain + 'layout'].addLayout(self.__dict__[textmain + 'formlayout'])
            self.__dict__[
                textmain + 'layout'].addWidget(self.__dict__[textmain + 'button'])
            return self.__dict__[textmain + 'layout']
        else:
            self.keyvalue = self.getterEntryRangeValue()[textmain][textname]
            self.techvalue = self.getterEntryTechValue()[textmain][textname]
            # main
            self.__dict__[textmain + textname +
                          'mainlabel'] = QLabel(textname)
            self.__dict__[textmain + textname +
                          'mainlabel'].setMinimumSize(QSize(150, 25))
            self.__dict__[textmain + textname +
                          'mainlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + 'mainlabel'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname +
                          'dfvalue'] = QLabel('Parameter : ' + str(self.techvalue))
            self.__dict__[textmain + textname +
                          'dfvalue'].setMinimumSize(QSize(100, 25))
            self.__dict__[textmain + textname +
                          'dfvalue'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.__dict__[textmain + textname + 'dfvalue'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            for perm in self.keyvalue:
                if (perm == "First"):
                    self.__dict__[textmain + textname +
                                  'Firstparameter'] = self.keyvalue['First']
                    self.__dict__[textmain + textname +
                                  'firstlabel'] = QLabel('First :')
                    self.__dict__[textmain + textname +
                                  'firstlabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[textmain + textname +
                                  'firstlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + textname + 'firstlabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + textname +
                                  'firstedit'] = QLineEdit()
                    self.__dict__[textmain + textname +
                                  'firstedit'].setText(str(self.__dict__[textmain + textname + 'Firstparameter']))
                    self.__dict__[textmain + textname +
                                  'firstedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + textname + 'firstedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        ###############################
                elif (perm == "Last"):
                    self.__dict__[textmain + textname +
                                  'Lastparameter'] = self.keyvalue['Last']
                    self.__dict__[textmain + textname +
                                  'nextlabel'] = QLabel('Last :')
                    self.__dict__[textmain + textname +
                                  'nextlabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[textmain + textname +
                                  'nextlabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + textname + 'nextlabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + textname +
                                  'nextedit'] = QLineEdit()
                    self.__dict__[textmain + textname +
                                  'nextedit'].setText(str(self.__dict__[textmain + textname + 'Lastparameter']))
                    self.__dict__[textmain + textname +
                                  'nextedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + textname + 'nextedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        ################################
                elif (perm == "Step"):
                    self.__dict__[textmain + textname +
                                  'Stepparameter'] = self.keyvalue['Step']
                    self.__dict__[textmain + textname +
                                  'steplabel'] = QLabel('Step :')
                    self.__dict__[textmain + textname +
                                  'steplabel'].setMinimumSize(QSize(150, 25))
                    self.__dict__[textmain + textname +
                                  'steplabel'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.__dict__[textmain + textname + 'steplabel'].setStyleSheet(
                        "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
                    self.__dict__[textmain + textname +
                                  'stepedit'] = QLineEdit()
                    self.__dict__[textmain + textname +
                                  'stepedit'].setText(str(self.__dict__[textmain + textname + 'Stepparameter']))
                    self.__dict__[textmain + textname +
                                  'stepedit'].setMinimumSize(QSize(200, 25))
                    self.__dict__[textmain + textname + 'stepedit'].setStyleSheet(
                        "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
            ########################
            self.__dict__[textmain + textname + 'formlayout'] = QFormLayout()
            self.__dict__[textmain + textname + 'formlayout'].addRow(
                self.__dict__[textmain + textname + 'mainlabel'], self.__dict__[textmain + textname + 'dfvalue'])
            self.__dict__[textmain + textname + 'formlayout'].addRow(self.__dict__[
                textmain + textname + 'firstlabel'], self.__dict__[textmain + textname + 'firstedit'])
            self.__dict__[textmain + textname + 'formlayout'].addRow(self.__dict__[
                textmain + textname + 'nextlabel'], self.__dict__[textmain + textname + 'nextedit'])
            self.__dict__[textmain + textname + 'formlayout'].addRow(self.__dict__[
                textmain + textname + 'steplabel'], self.__dict__[textmain + textname + 'stepedit'])

            self.__dict__[textmain + textname +
                          'button'] = QPushButton('Submit')
            self.__dict__[textmain + textname + 'button'].clicked.connect(lambda: self.uploadRangeValue(
                textmain, self.__dict__[textmain + textname + 'firstedit'].text(), self.__dict__[textmain + textname + 'nextedit'].text(), self.__dict__[textmain + textname + 'stepedit'].text(), textname=textname))
            self.__dict__[textmain + textname +
                          'button'].setMinimumSize(QSize(200, 25))
            self.__dict__[textmain + textname + 'button'].setStyleSheet(
                "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
            self.__dict__[textmain + textname + 'layout'] = QVBoxLayout()
            self.__dict__[textmain + textname + 'layout'].addLayout(
                self.__dict__[textmain + textname + 'formlayout'])
            self.__dict__[textmain + textname +
                          'layout'].addWidget(self.__dict__[textmain + textname + 'button'])
            return self.__dict__[textmain + textname + 'layout']

    def tool_dicts(self, textname, firstname, lastname, stepname):
        self.tool_dict = {}
        self.tool_dict[textname] = {}
        self.tool_dict[textname]['First'] = int(firstname)
        self.tool_dict[textname]['Last'] = int(lastname)
        self.tool_dict[textname]['Step'] = int(stepname)
        return self.tool_dict

    def bool_dicts(self, textname, boolname):
        self.tool_dict = {}
        self.tool_dict[textname] = {}
        self.tool_dict[textname] = boolname
        return self.tool_dict

    def bool_dictsbool(self, textname, boolname,textcontext):
        self.tool_dict = {}
        self.tool_dict[textname] = {}
        self.tool_dict[textname][textcontext] = {}
        self.tool_dict[textname][textcontext]  = boolname
        return self.tool_dict

    def uploadRangeValue(self, textmain, firstname, lastname, stepname, textname=None):
        if (textname == None):
            self.global_dict = self.getterEntryRangeValue()
            tool_dict = self.tool_dicts(
                textmain, firstname, lastname, stepname)
            self.global_dict.update(tool_dict)
            self.setterEntryRangeValue(self.global_dict)
            print(self.getterEntryRangeValue())
            QMessageBox.information(None, 'Parameter Saved',
                                    'Saved Parameter Setting')
        else:
            self.global_dict = self.getterEntryRangeValue()
            tool_dict = self.tool_dicts(
                textname, firstname, lastname, stepname)
            self.global_dict[textmain].update(tool_dict)
            self.setterEntryRangeValue(self.global_dict)
            print(self.getterEntryRangeValue())
            QMessageBox.information(None, 'Parameter Saved',
                                    'Saved Parameter Setting')

    def uploadboolvalue(self, textmain, boolname, textname=None):
        if (boolname == ''):
            QMessageBox.information(None, 'Input Error',
                                    'Input Can not None')
        else:
            if (textname == None):
                self.global_dict = self.getterEntryRangeValue()
                tool_dict = self.bool_dicts(
                    textmain, boolname)
                self.global_dict.update(tool_dict)
                self.setterEntryRangeValue(self.global_dict)
                print(self.getterEntryRangeValue())
                QMessageBox.information(None, 'Parameter Saved',
                                        'Saved Parameter Setting')
            else:
                self.global_dict = self.getterEntryRangeValue()
                tool_dict = self.bool_dicts(
                    textname, boolname)
                self.global_dict[textmain].update(tool_dict)
                self.setterEntryRangeValue(self.global_dict)
                print(self.getterEntryRangeValue())
                QMessageBox.information(None, 'Parameter Saved',
                                        'Saved Parameter Setting')

    def uploadboolvaluedict(self, textmain, boolname, textname=None,textcontext=None):
        if (boolname == ''):
            QMessageBox.information(None, 'Input Error',
                                    'Input Can not None')
        else:
            if(textname is not None)and (textcontext is not None):
                self.global_dict = self.getterEntryRangeValue()
                # self.tool_dict = self.bool_dictsbool(
                #     textname, boolname,textcontext)
                self.global_dict[textmain][textname][textcontext]=boolname
                # self.global_dict[textmain].update(self.tool_dict)
                self.setterEntryRangeValue(self.global_dict)
                print(self.getterEntryRangeValue())
                QMessageBox.information(None, 'Parameter Saved',
                                        'Saved Parameter Setting')

    def listwidgetitem(self):
        return self.ui.EntrytoollistWidget.currentItem().text()

    def deletedictitem(self):
        try:
            self.item = self.listwidgetitem()
            self.dict = self.getterEntryTechValue()
            if (self.item in self.dict):
                del self.dict[self.item]
            self.setterEntryTechValue(self.dict)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def reloadvalue(self):
        self.itemlist = self.getterTechValue()
        self.itemkey = self.itemlist.keys()
        self.ui.EntrytoollistWidget.addItems(list(self.itemkey))

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

    def setterTechValue(self, text):
        TechValue.set_tech_toolperm_var(text)

    def setterEntryTechValue(self, text):
        TechValue.set_tech_Entry_var(text)

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()

    def setterEntryRangeTechValue(self, text):
        TechValue.set_tech_range_perm(text)

    def getterEntryRangeTechValue(self):
        return TechValue.get_tech_range_perm()

    def setterEntryRangeValue(self, text):
        TechValue.set_entry_range_perm(text)

    def getterEntryRangeValue(self):
        return TechValue.get_entry_range_perm()
