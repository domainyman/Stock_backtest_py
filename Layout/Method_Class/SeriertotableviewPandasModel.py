from PyQt6.QtCore import QSize, Qt, QAbstractTableModel

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
