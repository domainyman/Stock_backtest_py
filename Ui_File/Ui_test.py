# Form implementation generated from reading ui file 'd:\Python\Stock_py\Ui_File\test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName("test")
        test.resize(1095, 706)
        test.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(test)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ea_tableView = QtWidgets.QTableView(parent=test)
        self.ea_tableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ea_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.ea_tableView.setObjectName("ea_tableView")
        self.verticalLayout_2.addWidget(self.ea_tableView)

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)

    def retranslateUi(self, test):
        _translate = QtCore.QCoreApplication.translate
        test.setWindowTitle(_translate("test", "Select Indicators Tool For Analysis"))
