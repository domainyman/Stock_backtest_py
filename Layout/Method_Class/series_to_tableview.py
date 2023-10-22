from PyQt6.QtWidgets import QApplication, QTableView
from PyQt6.QtCore import QAbstractTableModel, Qt
import pandas as pd

class SeriesPandastotableviewModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.data = data

    def rowCount(self, parent=None):
        return self.data.shape[0]

    def columnCount(self, parent=None):
        return self.data.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return str(self.data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.data.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self.data.index[section])
        return None