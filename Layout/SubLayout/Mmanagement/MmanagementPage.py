from Layout.Ui_Layout.Moneymanagement.Ui_moneymanagement import Ui_MoneyManagement
from PyQt6.QtWidgets import QDialog, QMessageBox, QMenu, QLabel, QLabel, QFormLayout, QVBoxLayout, QPushButton, QComboBox
from Global.Value.MoneyManageParam import MoneyValue
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets
import functools
import numpy as np


class Moneymanagepage(QDialog, Ui_MoneyManagement):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_MoneyManagement()
        self.ui.setupUi(self)
        self.setup()

    def FromOrderReturn(self, text):
        try:
            if (text == "Cash"):
                return self.setcash()
            elif (text == "Commission"):
                return self.setcommission()
            elif (text == "Sizers"):
                return self.setsizers()

        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def setcash(self):
        return {
            "$1000": 1000,
            "$10000": 10000,
            "$100000": 100000,
            "$1000000": 1000000
        }

    def setcommission(self):
        return {
            "0.0": 0.0,
            "0.0005": 0.0005,
            "0.005": 0.005,
            "0.01": 0.01,
            "0.1": 0.1,
            "1": 1
        }

    def setsizers(self):
        return {
            "100%": 100,
            "90%": 90,
            "80%": 80,
            "70%": 70,
            "60%": 60,
            "50%": 50,
            "40%": 40,
            "30%": 30,
            "20%": 20,
            "10%": 10
        }

    def FromSignals(self):
        return {
            "Cash": 10000,
            "Commission": 0.0,
            "Sizers" : 90
        }

    def grouplist(self):
        item = ["", "Portfolio Model"]
        return item

    def InitialModelitem(self):
        item = ["", "From_Signals()"]
        return item

    def combochange(self):
        self.text = self.ui.money_management_group_combo.currentText()
        self.mmgroupsub(self.text)

    def mmgroupsub(self, text):
        if (text == ""):
            self.subclearcombo()
        else:
            self.subclearcombo()
            print(text)
            if (text == "Portfolio Model"):
                self.itemmodeldict = self.InitialModelitem()
                self.ui.money_management_item_combo.addItems(
                    self.itemmodeldict)

    def subclearcombo(self):
        self.ui.money_management_item_combo.clear()

    def setup(self):
        self.reloadvalue()
        self.ui.money_management_group_combo.addItems(self.grouplist())
        self.ui.Btn_mm_add.clicked.connect(self.addmdoellist)
        self.ui.Btn_mm_reset.clicked.connect(self.listwidgetreset)
        self.ui.toollistWidget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.toollistWidget.customContextMenuRequested.connect(
            self.showContextMenu)
        self.ui.money_management_group_combo.currentTextChanged.connect(
            self.combochange)
        self.ui.Btn_mm_enter.clicked.connect(self.close)

    def reloadvalue(self):
        try:
            self.itemkey = self.getterModelValue().keys()
            self.ui.toollistWidget.addItems(list(self.itemkey))
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def addmdoellist(self):
        self.listwidgetreset()
        self.text = self.ui.money_management_item_combo.currentText()
        self.setterModeParamlValue(self.text)
        if (self.text == "From_Signals()"):
            self.setterModelValue(self.FromSignals())
            self.ui.toollistWidget.addItems(self.FromSignals().keys())

    def listwidgetreset(self):
        try:
            if (self.clearwidget() == True):
                self.setterModelValue({})
                self.ui.toollistWidget.clear()
                self.ui.toollistWidget.clearSelection()
                self.ui.toollistWidget.setCurrentItem(None)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def showContextMenu(self, pos):
        item = self.ui.toollistWidget.itemAt(pos)
        if item is not None:
            menu = QMenu("Meun", self)
            self.e = QAction("Edit")
            # self.d = QAction("Delete")
            menu.addAction(self.e)
            # menu.addAction(self.d)
            action = menu.exec(self.mapToGlobal(pos))
            if action == self.e:
                print("Opening Edit...")
                self.editedit(self.ui.toollistWidget.currentItem().text())
                # Your code here
            # if action == self.d:
            #     print("Opening Del...")
                # self.deletedictitem()
                # if (self.clearwidget() == True):
                #     self.deletelistitem(self.listcurrentRow())
                # Your code here
            if action is not None:
                print(
                    f'Action "{action.text()}" selected for item "{item.text()}"')

    def editedit(self, text):
        try:
            if (self.clearwidget() == True):
                self.returnwidget = self.widgetreturn(text)
                self.ui.groupverticalLayout.addLayout(self.returnwidget)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def widgetreturn(self, text):
        # self.itemlist = self.getterModeParamlValue()
        value = self.getterModelValue()[text]
        return self.widgetLayout(text, value)

    def find_key(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None

    def widgetLayout(self, text, para):
        self.textLabel = text
        self.parameter = para
        self.label = QLabel('Parameter :')
        self.label.setMinimumSize(QSize(150, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.comboBox = QComboBox()
        keyfun = self.FromOrderReturn(self.textLabel)
        keys = keyfun.keys()
        for key in keys:
            self.comboBox.addItem(str(key))
        result = self.find_key(keyfun, self.parameter)

        index = self.comboBox.findText(str(result))
        self.comboBox.setCurrentIndex(index)
        self.comboBox.setMinimumSize(QSize(200, 25))
        self.comboBox.setStyleSheet(
            "background-color: rgb(40, 40, 40);\n""color: rgb(255, 255, 255);")
        self.formlayout = QFormLayout()
        self.formlayout.addRow(self.label, self.comboBox)
        self.button = QPushButton('Submit')
        self.button.clicked.connect(
            functools.partial(self.uploadValue, self.textLabel))
        self.button.setMinimumSize(QSize(200, 25))
        self.button.setStyleSheet(
            "color: rgb(255, 255, 255);\n""background-color: rgb(25, 69, 85);")
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formlayout)
        self.layout.addWidget(self.button)
        return self.layout

    def uploadValue(self, labelkey):
        try:
            self.tool_dict = {}
            self.global_dict = self.getterModelValue()
            self.item = self.FromOrderReturn(labelkey)
            self.textcm = self.comboBox.currentText()
            if (self.textcm == "None"):
                self.tool_dict[labelkey] = None
            else:
                self.tool_dict[labelkey] = self.item[self.textcm]
            self.global_dict.update(self.tool_dict)
            self.setterModelValue(self.global_dict)
            print(self.getterModelValue())
            QMessageBox.information(None, 'Parameter Saved',
                                    'Saved Parameter Setting')
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def clearwidget(self):
        layout = self.ui.groupverticalLayout  # 要清除的 QVBoxLayout
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

    def setterModeParamlValue(self, text):
        MoneyValue.set_model_name_var(text)

    def getterModeParamlValue(self):
        return MoneyValue.get_model_name_var()

    def setterModelValue(self, text):
        MoneyValue.set_model_perm_var(text)

    def getterModelValue(self):
        return MoneyValue.get_model_perm_var()
