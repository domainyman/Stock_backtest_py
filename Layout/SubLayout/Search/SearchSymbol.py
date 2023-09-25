import yfinance as yf
from PyQt6.QtWidgets import QMessageBox
import pandas as pd
from datetime import datetime


class Tickersearch:

    def __init__(self, text):
        self.texts = text

    def tickerchecking(self):
        try:
            # 创建 Ticker 对象
            self.ticker = yf.Ticker(self.texts)
            print('Checking Symbol : ' + self.texts)

            # 检查是否可用
            info = self.ticker.info
            if info is not None:
                print('股票代碼 : ' + self.texts + ' 可用')
                return True
            else:
                print('股票代码不可用')
                QMessageBox.warning(None, 'Error Ticker Symbol', '股票代碼不可用')
                return False
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                    'System Error !' + str(msg))
            return False

    def tickerinfo(self):
        self.ticker = yf.Ticker(self.texts)
        return self.ticker.info

    def tickerhisory(self, kwargs):
        self.ticker = yf.Ticker(self.texts)
        data = self.ticker.history(**kwargs)
        return data

    def tickernew(self):
        self.ticker = yf.Ticker(self.texts)
        return self.ticker.news
