from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.Info.Ui_companyOfficers import Ui_CompanyOfficers
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QDialog, QHeaderView


class CompanyOfficerPage(QDialog, Ui_CompanyOfficers):
    def __init__(self, text):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_CompanyOfficers()
        self.ui.setupUi(self)
        self.companyOfficerstext = text
        self.tableviewsetup(self.tableviewModelsetup(
            self.header(), self.tabledata()))
        Logger().info('Loading Company Summary')

    def tableviewModelsetup(self, HeaderLabel, data):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(HeaderLabel)
        for officer in data:
            item_name = QStandardItem(officer['name'])
            item_title = QStandardItem(officer['title'])
            item_total_pay = QStandardItem(str(officer['totalPay']))
            item_year_born = QStandardItem(str(officer['yearBorn']))
            self.model.appendRow(
                [item_name, item_title,  item_total_pay, item_year_born])
        return self.model

    def tableviewsetup(self, model):
        self.ui.officertableview.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.ui.officertableview.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.officertableview.verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.officertableview.setStyleSheet(
            "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")
        self.ui.officertableview.setModel(model)

    def columnCount(self):
        return len(self.tabledata())

    def header(self):
        header = ["Name", "Title", "TotalPay", "YearBorn"]
        return header

    def headerRow(self):
        return len(self.header())

    def tablekey(self):
        for d in self.companyOfficerstext:
            keys = list(d.keys())
            print(keys)

    def tabledata(self):
        new_list = [{'name': officer.get('name'), 'title': officer.get('title'), 'totalPay': officer.get('totalPay'), 'yearBorn': officer.get(
            'yearBorn')} for officer in self.companyOfficerstext if 'name' in officer and 'title' in officer]
        return new_list
