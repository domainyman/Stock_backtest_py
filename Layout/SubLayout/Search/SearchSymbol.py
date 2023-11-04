import yfinance as yf
from PyQt6.QtWidgets import QMessageBox
import pandas as pd
from datetime import datetime, timedelta
import re
from Layout.Method_Class.logger import Logger


class Tickersearch:

    def __init__(self, text):
        self.texts = text

    def tickerchecking(self):
        try:
            # 创建 Ticker 对象
            self.ticker = None
            self.ticker = yf.Ticker(self.texts)
            print('Checking Symbol : ' + self.texts)
            # 检查是否可用
            if self.ticker.history_metadata is not None:
                print('股票代碼 : ' + self.texts + ' 可用')
                return True
            else:
                print('股票代码不可用')
                QMessageBox.warning(None, 'Error Ticker Symbol', '股票代碼不可用')
                return False
        except Exception as e:
            Logger().error(f"YF.Ticker Checking: {e}")
            QMessageBox.warning(None, 'System Error', str(e))
            return False

    def tickerinfo(self):
        self.ticker = yf.Ticker(self.texts)
        Logger().info('YF.Ticker Loading')
        return self.ticker.info

    def tickerhisory(self, kwargs):
        self.ticker = yf.Ticker(self.texts)
        Logger().info('YF.History Loading')
        self.kwargs = self.re_data_add_30d(kwargs)
        data = self.ticker.history(**self.kwargs)
        return data

    def tickernew(self):
        self.ticker = yf.Ticker(self.texts)
        Logger().info('YF.News Loading')
        return self.ticker.news

    def re_data_add_30d(self, kwargs):
        if 'period' in kwargs:
            period = kwargs['period']
            match = re.match(r'(\d+)([yYmMdD])', period)

            if match:
                num = int(match.group(1))
                unit = match.group(2).lower()

                if unit == 'y':
                    num_days = num * 365
                elif unit == 'm':
                    num_days = num * 30
                elif unit == 'd':
                    num_days = num

                period = (datetime.now() - timedelta(days=num_days)) - \
                    timedelta(days=30)
                kwargs['start'] = period.strftime('%Y-%m-%d')
                kwargs['end'] = datetime.now().strftime('%Y-%m-%d')
                del kwargs['period']
        return kwargs
