import numpy as np
from prettytable import PrettyTable
import pandas as pd
from Ui_File.Ui_test import Ui_test
from PyQt6.QtWidgets import QDialog, QMessageBox, QMenu,QApplication, QMainWindow, QHeaderView, QFileDialog, QMessageBox,QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QDesktopServices
from Global.Value.TechToolParam import TechValue
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6 import QtWidgets
import sys

class test(QDialog, Ui_test):

    def __init__(self):
        super().__init__()
        self.ui = Ui_test()
        self.ui.setupUi(self)
        self.techrange = [{'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 1}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {
            'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 7}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 80, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 90, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 60, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 1}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 10}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 20}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}, {'TechRange': {'RSI': 14}, 'EntryRange': {'RSI': {'HIGH': 70, 'LOW': 30}}, 'return_item': None, 'positions': None, 'transactions': None, 'gross_lev': None}]
        self.eatableviewsetup(self.eatableviewModelsetup(self.eaheader(self.techrange), self.eatabledata(self.techrange)))

    def eatableviewsetup(self, model):
        self.ui.ea_tableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)

        self.ui.ea_tableView.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.ea_tableView.verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.ea_tableView.setStyleSheet(
            "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")
        self.ui.ea_tableView.setModel(model)

    def eatableviewModelsetup(self, HeaderLabel, data):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(HeaderLabel)
        for officer in data:
            tech_range = officer['TechRange']
            entry_range = officer['EntryRange']
            self.techrange = QStandardItem(str(tech_range))
            self.entryrange = QStandardItem(str(entry_range))
            self.model.appendRow([self.techrange, self.entryrange])
        return self.model

    def eacolumnCount(self):
        return len(self.eatabledata(self.techrange))

    def eaheader(self,headler):
        return headler[0].keys()

    def newsheaderRow(self):
        return len(self.eaheader())

    def eatabledata(self, text):
        self.eatext = text
        ea_list = [{'TechRange': officer.get('TechRange'), 'EntryRange': officer.get('EntryRange')} for officer in self.eatext if 'TechRange' in officer and 'EntryRange' in officer]
        return ea_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = test()
    win.show()
    sys.exit(app.exec())