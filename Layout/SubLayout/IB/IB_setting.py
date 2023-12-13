from Layout.Method_Class.logger import Logger
from Layout.Ui_Layout.IB.Ui_ib_setting import Ui_ib_setting
from PyQt6.QtWidgets import QDialog, QMessageBox
import json
import os


class IB_setting(QDialog, Ui_ib_setting):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        Logger().info('IB Setting Page Loading')
        self.file_path = 'ib_setting.json'
        self.ui = Ui_ib_setting()
        self.ui.setupUi(self)
        self.setup()

    def setup(self):
        self.ui.IB_SAVE.clicked.connect(self.save)
        self.reload()

    def reload(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.ui.IB_API_textedit.setText(data.get('api', ''))

    def save(self):
        try:
            self.text = self.ui.IB_API_textedit.text()
            data = {
                'api': self.text
            }
            with open('ib_setting.json', 'w') as file:
                json.dump(data, file)
            Logger().info('Saved IB_Setting')
            QMessageBox.information(None, 'Save IB Setting', 'Saved Success')
        except Exception as e:
            Logger().error(f"IB Setting Error : {e}")
            QMessageBox.warning(None, 'System Error', str(e))
