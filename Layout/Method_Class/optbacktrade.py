from Global.Value.UniversalValue import GlobalValue
from Global.Value.TechToolParam import TechValue
from Global.Value.MoneyManageParam import MoneyValue
from Layout.SubLayout.Ta.talib_lib import talib_list
import webbrowser
import quantstats as qs
import pytz
import backtrader as bt
import numpy as np
np.seterr(invalid='ignore')


class bt_enter_exit(bt.Strategy):
    # list of parameters which are configurable for the strategy
    def __init__(self):
        pass

    def next(self):
        current_close = self.data.close[0]
        current_datetime = self.data.datetime.datetime()
        row = basesetup().df_row(current_datetime, current_close)
        row = row.squeeze()
        self.entry = basesetup().tran_entry(row)
        self.exit = basesetup().tran_exit(row)
        if not self.position:  # not in the market
            if (self.entry == True) & (self.exit == False):
                self.buy()  # enter long

        elif (self.exit == True) & (self.entry == False):
            self.close()  # close long position


class optcerebrosetup():
    def __init__(self):
        self.cerebro = bt.Cerebro()
        self.cerebro.adddata(self.btfeel())
        self.cerebro.addstrategy(bt_enter_exit)
        self.cerebro.addobserver(bt.observers.DrawDown)
        self.cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
        self.loopperm()
        results = self.cerebro.run()
        portfolio_stats = results[0].analyzers.getbyname('pyfolio')
        self.returns, self.positions, self.transactions, self.gross_lev = portfolio_stats.get_pf_items()
        self.return_prof = qs.stats.avg_return(self.returns)
        self.return_cagr = qs.stats.cagr(self.returns)
        self.return_sharpe_ratio = qs.stats.sharpe(self.returns)
        self.return_risk_return_ratio = qs.stats.risk_return_ratio(self.returns)
        # qs.reports.html(
        #     returns, output='Stock Sentiment Report.html', title='Stock Sentiment')
        # webbrowser.open('Stock Sentiment Report.html')
        # self.cerebro.plot()

    def opt_file(self):
        return self.return_prof, self.return_cagr, self.return_sharpe_ratio, self.return_risk_return_ratio

    def returns_return_prof(self):
        return self.return_prof

    def returns_return_cagr(self):
        return self.return_cagr

    def returns_return_sharpe_ratio(self):
        return self.return_sharpe_ratio

    def returns_return_risk_return_ratio(self):
        return self.return_risk_return_ratio

    def returns_file(self):
        return self.returns, self.positions, self.transactions, self.gross_lev

    def btfeel(self):
        return bt.feeds.PandasData(dataname=self.gettertoolhistory())

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()

    def setcash(self, dollar):
        self.cerebro.broker.setcash(dollar)

    def setcommission(self, commissionfee):
        self.cerebro.broker.setcommission(commission=commissionfee)

    def setsizers(self, sizer):
        self.cerebro.addsizer(bt.sizers.PercentSizer, percents=sizer)

    def loopperm(self):
        for perm in list(self.getterModelValue().keys()):
            self.setperm(perm)

    def setperm(self, text):
        self.value = self.getterModelValue()
        if (text == 'Cash'):
            self.setcash(self.value[text])
        elif (text == 'Commission'):
            self.setcommission(self.value[text])
        elif (text == 'Sizers'):
            self.setsizers(self.value[text])

    def getterModelValue(self):
        return MoneyValue.get_model_perm_var()


class basesetup():
    def __init__(self):
        pass

    def df_row(self, datatime, close):
        self.df = self.gettertoolhistory()
        self.converted_dt = self.conv_date_to_America_New_York(datatime)
        selected_rows = self.df.loc[(self.df['Close'] == close) & (
            self.df.index == self.converted_dt)]
        print(selected_rows)
        return selected_rows

    def conv_date_to_America_New_York(self, datetime):
        dt_without_tz = pytz.utc.localize(datetime)
        converted_dt = dt_without_tz.astimezone(
            pytz.timezone('America/New_York'))
        return converted_dt

    def tran_entry(self, row):
        self.entry_exit_tran = self.getterEntryTechValue()
        self.entry_exit_trankeys = list(self.entry_exit_tran.keys())
        self.Checklist = []
        for param in self.entry_exit_trankeys:
            self.entryCheck = self.check_entery_para(
                param, row)
            self.Checklist.append(self.entryCheck)
        if (all(self.Checklist)):
            return True
        else:
            return False

    def tran_exit(self, row):
        self.exit_exit_trankeys = list(self.getterEntryTechValue().keys())
        self.Checklist = []
        for param in self.exit_exit_trankeys:
            self.exitCheck = self.check_exit_para(
                param, row)
            self.Checklist.append(self.exitCheck)
        if (all(self.Checklist)):
            return True
        else:
            return False

    def check_entery_para(self, testname, testitemrow):
        self.name = testname
        self.libret = talib_list()
        self.entryCheck = self.libret.entry_turn(self.name, testitemrow)
        return self.entryCheck

    def check_exit_para(self, testname, testitem):
        self.name = testname
        self.libret = talib_list()
        self.entryCheck = self.libret.exit_turn(self.name, testitem)
        return self.entryCheck

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()
