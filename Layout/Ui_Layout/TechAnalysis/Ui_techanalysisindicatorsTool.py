# Form implementation generated from reading ui file 'd:\Python\Stock_py\Ui_File\techanalysisindicatorsTool.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TechAnalysis(object):
    def setupUi(self, TechAnalysis):
        TechAnalysis.setObjectName("TechAnalysis")
        TechAnalysis.resize(1095, 702)
        TechAnalysis.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TechAnalysis)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_38 = QtWidgets.QLabel(parent=TechAnalysis)
        self.label_38.setMinimumSize(QtCore.QSize(200, 25))
        self.label_38.setMaximumSize(QtCore.QSize(100, 25))
        self.label_38.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.label_38.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout.addWidget(self.label_38)
        self.techgroupindicatorstool_combo = QtWidgets.QComboBox(parent=TechAnalysis)
        self.techgroupindicatorstool_combo.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.techgroupindicatorstool_combo.setFont(font)
        self.techgroupindicatorstool_combo.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.techgroupindicatorstool_combo.setObjectName("techgroupindicatorstool_combo")
        self.horizontalLayout.addWidget(self.techgroupindicatorstool_combo)
        self.techindicatorstool_combo = QtWidgets.QComboBox(parent=TechAnalysis)
        self.techindicatorstool_combo.setMinimumSize(QtCore.QSize(0, 25))
        self.techindicatorstool_combo.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.techindicatorstool_combo.setObjectName("techindicatorstool_combo")
        self.horizontalLayout.addWidget(self.techindicatorstool_combo)
        self.Btn_add = QtWidgets.QPushButton(parent=TechAnalysis)
        self.Btn_add.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_add.setMaximumSize(QtCore.QSize(100, 25))
        self.Btn_add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_add.setObjectName("Btn_add")
        self.horizontalLayout.addWidget(self.Btn_add)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toollistWidget = QtWidgets.QListWidget(parent=TechAnalysis)
        self.toollistWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.toollistWidget.setStyleSheet("background-color: rgb(47, 47, 47);\n"
"border-color: rgb(47, 47, 47);\n"
"color: rgb(255, 255, 255);")
        self.toollistWidget.setObjectName("toollistWidget")
        self.horizontalLayout_2.addWidget(self.toollistWidget)
        self.widget = QtWidgets.QWidget(parent=TechAnalysis)
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
        self.Btn_reset = QtWidgets.QPushButton(parent=TechAnalysis)
        self.Btn_reset.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_reset.setMaximumSize(QtCore.QSize(1000, 25))
        self.Btn_reset.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_reset.setObjectName("Btn_reset")
        self.horizontalLayout_4.addWidget(self.Btn_reset)
        self.Btn_enter = QtWidgets.QPushButton(parent=TechAnalysis)
        self.Btn_enter.setMinimumSize(QtCore.QSize(100, 25))
        self.Btn_enter.setMaximumSize(QtCore.QSize(1000, 25))
        self.Btn_enter.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 69, 85);")
        self.Btn_enter.setObjectName("Btn_enter")
        self.horizontalLayout_4.addWidget(self.Btn_enter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(TechAnalysis)
        QtCore.QMetaObject.connectSlotsByName(TechAnalysis)

    def retranslateUi(self, TechAnalysis):
        _translate = QtCore.QCoreApplication.translate
        TechAnalysis.setWindowTitle(_translate("TechAnalysis", "Select Indicators Tool For Analysis"))
        self.label_38.setText(_translate("TechAnalysis", "Select Indicators Tool"))
        self.Btn_add.setText(_translate("TechAnalysis", "Add"))
        self.Btn_reset.setText(_translate("TechAnalysis", "RESET"))
        self.Btn_enter.setText(_translate("TechAnalysis", " Enter to Quit the application"))