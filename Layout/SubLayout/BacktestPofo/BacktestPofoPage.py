from Layout.Ui_Layout.Ui_Backtest_Pofo.Ui_pofo_data import Ui_Portfolio_Data
from Layout.Ui_Layout.Entrymanagement.Ui_entrymanagement import Ui_EntryManagement
from PyQt6.QtWidgets import QDialog, QHeaderView
from Global.Value.MoneyManageParam import MoneyValue
from PyQt6.QtCore import QSize, Qt, QAbstractTableModel
from PyQt6.QtGui import QAction
from PyQt6 import QtCore, QtGui, QtWidgets


class BacktestPofopage(QDialog, Ui_Portfolio_Data):
    def __init__(self, data):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_Portfolio_Data()
        self.ui.setupUi(self)
        self.dataf = data
        self.setup()

    def setup(self):
        self.reloadvalue()
        self.btn()

    def reloadvalue(self):
        model = PandasModel(self.dataf.stats())
        self.newstableviewsetup(model)

    def btn(self):
        self.ui.Backtest_Btn_enter.clicked.connect(self.close)

    def newstableviewsetup(self, model):
        self.ui.backtestpofotableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
        self.ui.backtestpofotableView.horizontalHeader().setStretchLastSection(True)
        self.ui.backtestpofotableView.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.backtestpofotableView.verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.backtestpofotableView.setStyleSheet(
            "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")
        self.ui.backtestpofotableView.setModel(model)


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.data = data

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                if index.column() == 0:
                    return str(self.data.index[index.row()])
                elif index.column() == 1:
                    return str(self.data.iloc[index.row()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                if section == 0:
                    return "Name"
                elif section == 1:
                    return "Value"
            elif orientation == Qt.Orientation.Vertical:
                return str(section + 1)
        return None
