from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.Info.Ui_longbussum import Ui_longbussum
from PyQt6.QtWidgets import QDialog


class LongBusSumPage(QDialog, Ui_longbussum):
    def __init__(self, text):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_longbussum()
        self.ui.setupUi(self)
        self.sum = text
        self.linebox()
        Logger().info('Loading Business Summary')

    def linebox(self):
        self.ui.sum_edit.setText(self.sum)
