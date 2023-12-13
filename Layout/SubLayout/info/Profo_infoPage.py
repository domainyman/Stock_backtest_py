from PyQt6.QtGui import QStandardItemModel, QStandardItem, QMouseEvent
from PyQt6.QtWidgets import QDialog, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHeaderView, QFileDialog, QMessageBox
from Global.Value.UniversalValue import GlobalValue
from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.Info.Ui_prof_pf import Ui_Profo_info


class Profo_info(QDialog, Ui_Profo_info):
    def __init__(self, TechValue, EntryTechValue, Info_tableView, Positions_tableView, Transactions_tableView):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_Profo_info()
        self.ui.setupUi(self)
        Logger().info('EA Auto Analyis Profo_info Loading')
        self.TechValuetext = TechValue
        self.EntryTechValuetext = EntryTechValue
        self.Profo_infotext = Info_tableView
        self.Positions_tableViewtext = Positions_tableView
        self.Transactions_tableViewtext = Transactions_tableView
        self.tableview = [self.ui.Positions_tableView,
                          self.ui.Transactions_tableView]

        self.tableviewsetup(self.tableview)
        self.setuploading()

    def setuploading(self):
        self.info_tableview(self.TechValuetext, self.EntryTechValuetext)
        self.positions_tableview(self.Positions_tableViewtext)
        self.transactions_tableview(self.Transactions_tableViewtext)
        self.ui.profo_csv.clicked.connect(self.techanalysisenterdownloadcsv)

    def tableviewsetup(self, tableview):
        for item in tableview:
            item.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch)
            item.horizontalHeader().setStyleSheet(
                "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
            item.verticalHeader().setStyleSheet(
                "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
            item.setStyleSheet(
                "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")

    def info_tableview(self, TechValue, EntryTechValue):
        self.ui.tach_vale_label.setText(
            f"Technical indicators : {TechValue} .  Strategy indicators : {EntryTechValue}")

    def positions_tableview(self, positions):
        positionsmodel = QStandardItemModel()
        # Add 1 for the index column
        positionsmodel.setColumnCount(len(positions.columns) + 1)
        # Include "Index" in the header labels
        header_labels = ["Index"] + positions.columns.tolist()
        positionsmodel.setHorizontalHeaderLabels(header_labels)

        for row in range(len(positions)):
            # Add index value as the first item in each row
            data = [QStandardItem(str(positions.index[row]))]
            data += [QStandardItem(str(positions.iloc[row, col]))
                     for col in range(len(positions.columns))]
            positionsmodel.appendRow(data)
        self.ui.Positions_tableView.setModel(positionsmodel)

    def transactions_tableview(self, transactions):
        transactionsmodel = QStandardItemModel()
        transactionsmodel.setColumnCount(len(transactions.columns) + 1)
        # Include "Index" in the header labels
        header_labels = ["Index"] + transactions.columns.tolist()
        transactionsmodel.setHorizontalHeaderLabels(header_labels)
        for row in range(len(transactions)):
            data = [QStandardItem(str(transactions.index[row]))]
            data += [QStandardItem(str(transactions.iloc[row, col]))
                     for col in range(len(transactions.columns))]
            transactionsmodel.appendRow(data)
        self.ui.Transactions_tableView.setModel(transactionsmodel)

    def techanalysisenterdownloadcsv(self):
        try:
            self.tickerhistorydownload(self.gettertoolhistory())
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def tickerhistorydownload(self, pdtext):
        try:
            if (pdtext is not None):
                # create and show the file dialog
                self.file_dialog = QFileDialog()
                self.file_path, _ = self.file_dialog.getSaveFileName(
                    filter='CSV files (*.csv);;All files (*.*)')
                # save the DataFrame to the CSV file
                if self.file_path:
                    pdtext.to_csv(self.file_path)
                    QMessageBox.information(
                        None, 'Save Completed', f'The file has been saved to:\n{self.file_path}')

        except:
            print("except ! Please select the option that requires history")
            QMessageBox.warning(None, 'Error Ticker History',
                                'Please select the option that requires history.')

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.setWindowState(Qt.WindowState.WindowMaximized)
        else:
            super().mouseDoubleClickEvent(event)
