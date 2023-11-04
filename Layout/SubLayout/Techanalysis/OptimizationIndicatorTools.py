from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.TechAnalysis.Ui_techanalysisindicatorsTool import Ui_TechAnalysis
from Layout.SubLayout.Ta.talib_lib import talib_list
from PyQt6.QtWidgets import QDialog, QMessageBox, QMenu, QLabel, QLineEdit, QFormLayout, QVBoxLayout, QPushButton, QScrollBar, QMessageBox
from PyQt6.QtCore import QSize, Qt
from Global.Value.TechToolParam import TechValue
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets


class OptimizationIndicatorTool(QDialog, Ui_TechAnalysis):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_TechAnalysis()
        self.ui.setupUi(self)
        self.setuptech()

    def mulitbaserange(self, textname, textperm) -> dict:
        Logger().info('Technical indicators Muit Opt Loading')
        if (textperm == 'matype'):
            self.baseoption = {textname: {textperm: {
                'First': 0, 'Last': 9, 'Step': 1}}}
        elif (textperm == 'timeperiod'):
            self.baseoption = {textname: {textperm: {
                'First': 0, 'Last': 100, 'Step': 25}}}
        else:
            self.baseoption = {textname: {textperm: {
                'First': 0, 'Last': 100, 'Step': 25}}}
        return self.baseoption

    def baserange(self, textname) -> dict:
        Logger().info('Technical indicators Base Opt Loading')
        self.baseoption = {textname: {
            'First': 0, 'Last': 100, 'Step': 25}}
        return self.baseoption

    def mulitentrybaserange(self, textname, textperm, textvalue=None):
        Logger().info('Technical indicators Exp Muit Opt Loading')
        self.dict_key_value = self.getterEntryTechValue()[textname][textperm]
        if isinstance(self.dict_key_value, (int, float)):
            self.baseoption = {textname: {textperm: {
                'First': 0, 'Last': 100, 'Step': 25}}}
        elif isinstance(self.dict_key_value, (dict)):
            self.baseoption = {textname: {textperm: {
                textvalue: {'True', 'False', 'Both Test'}}}}
        elif (self.dict_key_value == 'True') or (self.dict_key_value == 'False'):
            self.baseoption = {textname: {
                textperm: {'True', 'False', 'Both Test'}}}
        return self.baseoption

    def checktoolperm_name(self, text):
        Logger().info('Technical indicators Opt indicator Contains')
        self.list = []
        self.tech_tool_key = self.getterTechValue()
        if (self.check_dict_contains_dict(self.tech_tool_key, text) == True):
            self.dict_key_value = self.tech_tool_key[text].keys()
            for permvalue in self.dict_key_value:
                self.list.append(permvalue)
        else:
            self.list.append(text)
        return self.list

    def checkenterperm_name(self, text):
        Logger().info('Technical indicators Opt Exp Contains')
        self.list = []
        self.tech_tool_key = self.getterEntryTechValue()
        if (self.check_dict_contains_dict(self.tech_tool_key, text) == True):
            self.dict_key_value = self.tech_tool_key[text].keys()
            for permvalue in self.dict_key_value:
                self.list.append(permvalue)
        else:
            self.list.append(text)
        return self.list

    def setuptech(self):
        Logger().info('Opt Technical indicators Page Loading')
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
            Logger().info('Opt Technical indicators Page Reload Value')
            self.itemlist = self.getterTechValue()
            self.itemkey = self.itemlist.keys()
            self.ui.toollistWidget.addItems(list(self.itemkey))
        except Exception as e:
            Logger().error(
                f"ERROR in Opt Technical indicators Page Reload Value: {e}")
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
                Logger().info(
                    f'Action "{action.text()}" selected for item "{item.text()}"')

    def deletedictitem(self):
        try:
            Logger().info('Opt Technical indicators Page Del Item')
            self.item = self.listwidgetitem()

            self.dict = self.getterTechValue()
            if (self.item in self.dict):
                del self.dict[self.item]
            self.setterTechValue(self.dict)

            self.Entrydict = self.getterEntryTechValue()
            if (self.item in self.Entrydict):
                del self.Entrydict[self.item]
            self.setterEntryTechValue(self.Entrydict)

            self.rangedict = self.getterEntryRangeTechValue()
            if (self.item in self.rangedict):
                del self.rangedict[self.item]
            self.setterEntryRangeTechValue(self.rangedict)

            self.rangevaldict = self.getterEntryRangeValue()
            if (self.item in self.rangevaldict):
                del self.rangevaldict[self.item]
            self.setterEntryRangeValue(self.rangevaldict)

        except BaseException as e:
            Logger().error(
                f"ERROR in Opt Technical indicators Page Del Item: {e}")
            QMessageBox.warning(None, 'System Error', str(e))

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
        Logger().info('Opt Technical indicators Page Retuen Group')
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
                # self.newdict.remove("APO")
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
            Logger().info('Opt Technical indicators Page insert Item')
            self.text = self.ui.techindicatorstool_combo.currentText()
            if (self.listcheckrepeat(self.text) == False):
                self.insertbaseparam(self.text)
                self.ui.toollistWidget.addItem(self.text)
            else:
                Logger().info('Opt Technical indicators Page insert Item - Select Repeat')
                QMessageBox.warning(None, 'Select Repeat',
                                    'Select the tool Repeat.')
        except Exception as e:
            Logger().error(
                f"ERROR in Opt Technical indicators Page insert Item: {e}")
            QMessageBox.warning(None, 'System Error', str(e))

    def insertbaseparam(self, text):
        try:
            Logger().info('Opt Technical indicators Page insert Base Properties')
            self.returnbase = talib_list()
            self.base = self.returnbase.basereturn(text)
            if (self.base != None):
                self.global_dict = self.getterTechValue()
                self.global_dict.update(self.base)
                self.setterTechValue(self.global_dict)

            self.entrybase = self.returnbase.entry_exit_basereturn(text)
            if (self.entrybase != None):
                self.Entryglobal_dict = self.getterEntryTechValue()
                self.Entryglobal_dict.update(self.entrybase)
                self.setterEntryTechValue(self.Entryglobal_dict)

            self.list = self.checktoolperm_name(text)
            if (len(self.list) > 1):
                for perm in self.list:
                    self.basecase = self.mulitbaserange(text, perm)
                    self.range_dict = self.getterEntryRangeTechValue()
                    if all(key in self.range_dict for key in self.basecase):
                        self.keyvalue = self.basecase[text]
                        self.range_dict[text].update(self.keyvalue)
                        self.setterEntryRangeTechValue(self.range_dict)
                    else:
                        self.range_dict.update(self.basecase)
                        self.setterEntryRangeTechValue(self.range_dict)
            else:
                self.basecase = self.baserange(text)
                self.range_dict = self.getterEntryRangeTechValue()
                self.range_dict.update(self.basecase)
                self.setterEntryRangeTechValue(self.range_dict)

            self.entrylist = self.checkenterperm_name(text)
            self.entryrange_dict = self.getterEntryRangeValue()
            self.Entryglobal_dict = self.getterEntryTechValue()
            if (len(self.entrylist) > 0):
                for perm in self.entrylist:
                    if (isinstance(self.Entryglobal_dict[text][perm], dict)):
                        if text not in self.entryrange_dict:
                            self.entryrange_dict[text] = {}
                        self.sign_valuekey = self.Entryglobal_dict[text][perm].keys(
                        )
                        for sign_value in self.sign_valuekey:
                            self.keyentryvalue = self.mulitentrybaserange(
                                text, perm, textvalue=sign_value)
                            if perm not in self.entryrange_dict[text]:
                                self.entryrange_dict[text][perm] = {}
                            self.entryrange_dict[text][perm].update(
                                self.keyentryvalue[text][perm])
                            self.setterEntryRangeValue(self.entryrange_dict)
                    else:
                        self.entrybaserange = self.mulitentrybaserange(
                            text, perm)
                        if all(key in self.entryrange_dict for key in self.entrybaserange):
                            self.keyentryvalue = self.entrybaserange[text]
                            self.entryrange_dict[text].update(
                                self.keyentryvalue)
                            self.setterEntryRangeValue(self.entryrange_dict)
                        else:
                            self.entryrange_dict.update(self.entrybaserange)
                            self.setterEntryRangeValue(self.entryrange_dict)

        except Exception as e:
            QMessageBox.warning(None, 'System Error', str(e))

    def listwidgetreset(self):
        try:
            Logger().info('Reset Opt Technical indicators Base Properties Widget')
            if (self.clearwidget() == True):
                self.setterTechValue({})
                self.setterEntryTechValue({})
                self.setterEntryRangeTechValue({})
                self.setterEntryRangeValue({})
                self.ui.toollistWidget.clear()
                self.ui.toollistWidget.clearSelection()
                self.ui.toollistWidget.setCurrentItem(None)
        except Exception as msg:
            QMessageBox.warning(None, 'System Error', str(msg))

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
                self.return_Tech_tool_perm(text)
        except Exception as msg:
            Logger().error(f"ERROR in Opt Technical indicators Page Edit: {e}")
            QMessageBox.warning(None, 'System Error', str(msg))

    def return_Tech_tool_perm(self, text):
        self.tech_tool_key = self.getterTechValue()
        if (self.check_dict_contains_dict(self.tech_tool_key, text) == True):
            self.dict_key_value = self.tech_tool_key[text].keys()
            for permvalue in self.dict_key_value:
                self.returnwidget = self.createwidget_setup(
                    text, textname=permvalue)
                self.ui.groupverticalLayout.addLayout(self.returnwidget)
        else:
            self.returnwidget = self.createwidget_setup(text)
            self.ui.groupverticalLayout.addLayout(self.returnwidget)

    def check_dict_contains_dict(self, your_dict, key):
        if isinstance(your_dict.get(key), dict):
            return True
        else:
            return False

    def createwidget_setup(self, textmain, textname=None):
        if (textname == None):
            self.keyvalue = self.getterEntryRangeTechValue()[textmain]
            self.techvalue = self.getterTechValue()[textmain]
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
            self.keyvalue = self.getterEntryRangeTechValue()[
                textmain][textname]
            self.techvalue = self.getterTechValue()[textmain][textname]
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
                textmain, self.__dict__[textmain + textname + 'firstedit'].text(), self.__dict__[textmain + textname + 'nextedit'].text(), self.__dict__[textmain + textname + 'stepedit'].text(), textname))
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
        self.tool_dict[textname]['First'] = float(firstname)
        self.tool_dict[textname]['Last'] = float(lastname)
        self.tool_dict[textname]['Step'] = float(stepname)
        return self.tool_dict

    def uploadRangeValue(self, textmain, firstname, lastname, stepname, textname=None):
        Logger().info('Opt Technical indicators Upload')
        if (float(lastname) < float(firstname)):
            Logger().info('Opt Technical indicators Input Errot')
            QMessageBox.warning(None, 'System Error', 'Input Errot')
        else:
            if (textname == None):
                self.global_dict = self.getterEntryRangeTechValue()
                tool_dict = self.tool_dicts(
                    textmain, firstname, lastname, stepname)
                self.global_dict.update(tool_dict)
                self.setterEntryRangeTechValue(self.global_dict)
                QMessageBox.information(None, 'Parameter Saved',
                                        'Saved Parameter Setting')
            else:
                self.global_dict = self.getterEntryRangeTechValue()
                tool_dict = self.tool_dicts(
                    textname, firstname, lastname, stepname)
                self.global_dict[textmain].update(tool_dict)
                self.setterEntryRangeTechValue(self.global_dict)
                QMessageBox.information(None, 'Parameter Saved',
                                        'Saved Parameter Setting')

    def setterTechValue(self, text):
        TechValue.set_tech_toolperm_var(text)

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

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

    def clearwidget(self):
        Logger().info('Opt Technical indicators Widget')
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
