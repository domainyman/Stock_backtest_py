from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.TechAnalysis.Ui_techanalysisindicatorsTool import Ui_TechAnalysis
from Layout.SubLayout.Ta.talib_lib import talib_list
from PyQt6.QtWidgets import QDialog, QMessageBox, QMenu
from Global.Value.TechToolParam import TechValue
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets


class TechAnalysispage(QDialog, Ui_TechAnalysis):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_TechAnalysis()
        self.ui.setupUi(self)
        self.setuptech()

    def setuptech(self):
        self.reloadvalue()
        self.ui.techgroupindicatorstool_combo.addItems(self.techtool_list())
        self.ui.Btn_add.clicked.connect(self.techtaddlist)
        self.ui.Btn_reset.clicked.connect(self.listwidgetreset)
        self.ui.toollistWidget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.toollistWidget.customContextMenuRequested.connect(
            self.showContextMenu)
        self.ui.techgroupindicatorstool_combo.currentTextChanged.connect(
            self.combochange)
        self.ui.Btn_enter.clicked.connect(self.close)

    def reloadvalue(self):
        try:
            Logger().info('Technical indicators Page Loading')
            self.itemlist = self.getterTechValue()
            self.itemkey = self.itemlist.keys()
            self.ui.toollistWidget.addItems(list(self.itemkey))
        except Exception as e:
            Logger().error(f"ERROR in Technical indicators Page: {e}")
            QMessageBox.warning(None, 'System Error', str(e))

    def showContextMenu(self, pos):
        item = self.ui.toollistWidget.itemAt(pos)
        if item is not None:
            menu = QMenu("Meun", self)
            self.e = QAction("Edit")
            self.d = QAction("Delete")
            menu.addAction(self.e)
            menu.addAction(self.d)
            action = menu.exec(self.mapToGlobal(pos))
            if action == self.e:
                self.indicatoredit(self.ui.toollistWidget.currentItem().text())
                # Your code here
            if action == self.d:
                self.deletedictitem()
                if (self.clearwidget() == True):
                    self.deletelistitem(self.listcurrentRow())
                # Your code here
            if action is not None:
                Logger().info(f'Action "{action.text()}" selected for item "{item.text()}"')


    def deletedictitem(self):
        try:
            Logger().info('Technical indicators Page Del Item')
            self.item = self.listwidgetitem()
            self.dict = self.getterTechValue()
            if (self.item in self.dict):
                del self.dict[self.item]
            self.setterTechValue(self.dict)

            self.Entrydict = self.getterEntryTechValue()
            if (self.item in self.Entrydict):
                del self.Entrydict[self.item]
            self.setterEntryTechValue(self.Entrydict)

        except Exception as e:
            Logger().error(f"ERROR in Technical indicators Page Del Item: {e}")
            QMessageBox.warning(None, 'System Error',str(e))

    def techtool_list(self):
        self.listkey = ["", "Cycle Indicators", "Momentum Indicators",
                        "Overlap Studies", "Volatility Indicators", "Volume Indicators"]
        self.list = talib_list()
        self.text = self.list.all_funtionsgroupkey()
        return self.listkey

    def combochange(self):
        self.text = self.ui.techgroupindicatorstool_combo.currentText()
        self.techgroupindicatorstoolsub(self.text)

    def techgroupindicatorstoolsub(self, text):
        Logger().info('Add Group Technical indicators ')
        if (text == ""):
            self.subcombo()
        else:
            self.newdict = []
            self.subcombo()
            self.list = talib_list()
            self.dict = self.list.allgroup_subfunction(text)
            for item in self.dict:
                self.newdict.append(item)
            if (text == 'Momentum Indicators'):
                self.newdict.append("KDJ")
            elif (text == 'Overlap Studies'):
                self.newdict.remove('MAVP')
                self.newdict.remove('MA')
            self.ui.techindicatorstool_combo.addItems(self.newdict)

    def subcombo(self):
        self.ui.techindicatorstool_combo.clear()

    def listcurrentRow(self):
        index = self.ui.toollistWidget.currentIndex()
        return index.row()

    def deletelistitem(self, index):
        self.ui.toollistWidget.takeItem(index)

    def techtaddlist(self):
        try:
            Logger().info('Add Technical indicators ')
            self.text = self.ui.techindicatorstool_combo.currentText()
            if (self.listcheckrepeat(self.text) == False):
                self.insertbaseparam(self.text)
                self.ui.toollistWidget.addItem(self.text)

            else:
                Logger().info('Select Technical indicators Repeat')
                QMessageBox.warning(None, 'Select Repeat',
                                    'Select the tool Repeat.')
        except Exception as msg:
            QMessageBox.warning(None, 'System Error', str(msg))

    def insertbaseparam(self, text):
        try:
            Logger().info('Add Technical indicators item ')
            self.returnbase = talib_list()
            self.base = self.returnbase.basereturn(text)
            self.global_dict = self.getterTechValue()
            self.global_dict.update(self.base)
            self.setterTechValue(self.global_dict)
            self.entrybase = self.returnbase.entry_exit_basereturn(text)
            if (self.entrybase != None):
                self.Entryglobal_dict = self.getterEntryTechValue()
                self.Entryglobal_dict.update(self.entrybase)
                self.setterEntryTechValue(self.Entryglobal_dict)
        except Exception as e:
            Logger().error(f"ERROR in insert Technical indicators Page : {e}")
            QMessageBox.warning(None, 'System Error',str(e))

    def listwidgetreset(self):
        try:
            Logger().info('Technical indicators Page Widget Reset Loading')
            if (self.clearwidget() == True):
                self.setterTechValue({})
                self.setterEntryTechValue({})
                self.ui.toollistWidget.clear()
                self.ui.toollistWidget.clearSelection()
                self.ui.toollistWidget.setCurrentItem(None)
        except Exception as e:
            Logger().error(f"ERROR in Technical indicators Page Widget Reset : {e}")
            QMessageBox.warning(None, 'System Error',str(e))

    def listwidgetitem(self):
        return self.ui.toollistWidget.currentItem().text()

    def listcheckrepeat(self, text):
        self.items = []
        for index in range(self.ui.toollistWidget.count()):
            self.items.append(self.ui.toollistWidget.item(index).text())
        if (text in self.items):
            return True
        else:
            return False

    def indicatoredit(self, text):
        try:
            Logger().info('Opening Edit...')
            if (self.clearwidget() == True):
                self.returngroup = talib_list()
                self.returnwidget = self.returngroup.groupreturn(text)
                self.ui.groupverticalLayout.addLayout(self.returnwidget)
        except Exception as e:
            Logger().error(f"ERROR in Technical indicators Page Edit: {e}")
            QMessageBox.warning(None, 'System Error', str(e))

    def setterTechValue(self, text):
        TechValue.set_tech_toolperm_var(text)

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

    def setterEntryTechValue(self, text):
        TechValue.set_tech_Entry_var(text)

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()

    def clearwidget(self):
        Logger().info('Technical indicators Widget')
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

