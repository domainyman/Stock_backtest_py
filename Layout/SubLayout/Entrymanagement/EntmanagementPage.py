from Layout.Ui_Layout.Entrymanagement.Ui_entrymanagement import Ui_EntryManagement
from PyQt6.QtWidgets import QDialog, QMenu, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets
from Layout.SubLayout.Ta.talib_lib import talib_list
from Global.Value.TechToolParam import TechValue


class Entrymanagepage(QDialog, Ui_EntryManagement):
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
                self.returngroup = talib_list()
                self.returnwidget = self.returngroup.entryreturn(text)
                self.ui.EntrygroupverticalLayout.addLayout(self.returnwidget)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

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
