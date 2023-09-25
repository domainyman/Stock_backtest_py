# Form implementation generated from reading ui file 'd:\Python\Stock_py\Ui_File\moneymanagement.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MoneyManagement(object):
    def setupUi(self, MoneyManagement):
        MoneyManagement.setObjectName("MoneyManagement")
        MoneyManagement.resize(1000, 630)
        MoneyManagement.setMinimumSize(QtCore.QSize(1000, 630))
        MoneyManagement.setMaximumSize(QtCore.QSize(1000, 630))
        MoneyManagement.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MoneyManagement)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_38 = QtWidgets.QLabel(parent=MoneyManagement)
        self.label_38.setMinimumSize(QtCore.QSize(200, 25))
        self.label_38.setMaximumSize(QtCore.QSize(100, 25))
        self.label_38.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.label_38.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout.addWidget(self.label_38)
        self.money_management_group_combo = QtWidgets.QComboBox(parent=MoneyManagement)
        self.money_management_group_combo.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.money_management_group_combo.setFont(font)
        self.money_management_group_combo.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.money_management_group_combo.setObjectName("money_management_group_combo")
        self.horizontalLayout.addWidget(self.money_management_group_combo)
        self.money_management_item_combo = QtWidgets.QComboBox(parent=MoneyManagement)
        self.money_management_item_combo.setMinimumSize(QtCore.QSize(0, 25))
        self.money_management_item_combo.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.money_management_item_combo.setObjectName("money_management_item_combo")
        self.horizontalLayout.addWidget(self.money_management_item_combo)
        self.Btn_mm_add = QtWidgets.QPushButton(parent=MoneyManagement)
        self.Btn_mm_add.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_mm_add.setMaximumSize(QtCore.QSize(100, 25))
        self.Btn_mm_add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_mm_add.setObjectName("Btn_mm_add")
        self.horizontalLayout.addWidget(self.Btn_mm_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toollistWidget = QtWidgets.QListWidget(parent=MoneyManagement)
        self.toollistWidget.setMaximumSize(QtCore.QSize(470, 16777215))
        self.toollistWidget.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.toollistWidget.setObjectName("toollistWidget")
        self.horizontalLayout_2.addWidget(self.toollistWidget)
        self.widget = QtWidgets.QWidget(parent=MoneyManagement)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupverticalLayout = QtWidgets.QVBoxLayout()
        self.groupverticalLayout.setObjectName("groupverticalLayout")
        self.verticalLayout_3.addLayout(self.groupverticalLayout)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Btn_mm_reset = QtWidgets.QPushButton(parent=MoneyManagement)
        self.Btn_mm_reset.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_mm_reset.setMaximumSize(QtCore.QSize(1000, 25))
        self.Btn_mm_reset.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_mm_reset.setObjectName("Btn_mm_reset")
        self.horizontalLayout_4.addWidget(self.Btn_mm_reset)
        self.Btn_mm_enter = QtWidgets.QPushButton(parent=MoneyManagement)
        self.Btn_mm_enter.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_mm_enter.setMaximumSize(QtCore.QSize(1000, 25))
        self.Btn_mm_enter.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_mm_enter.setObjectName("Btn_mm_enter")
        self.horizontalLayout_4.addWidget(self.Btn_mm_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(MoneyManagement)
        QtCore.QMetaObject.connectSlotsByName(MoneyManagement)

    def retranslateUi(self, MoneyManagement):
        _translate = QtCore.QCoreApplication.translate
        MoneyManagement.setWindowTitle(_translate("MoneyManagement", "Select Model Managementl For Analysis"))
        self.label_38.setText(_translate("MoneyManagement", "Select Model Management"))
        self.Btn_mm_add.setText(_translate("MoneyManagement", "Add"))
        self.Btn_mm_reset.setText(_translate("MoneyManagement", "RESET"))
        self.Btn_mm_enter.setText(_translate("MoneyManagement", " Enter to Quit the application"))
