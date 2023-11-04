from concurrent.futures import ProcessPoolExecutor, as_completed
import talib
import quantstats as qs
import pytz
import backtrader as bt
import numpy as np
import multiprocessing
import numba
from Layout.Method_Class.logger import Logger
np.seterr(invalid='ignore')


class Dataset:
    tool_perm = {}
    Entry_perm = {}
    history = None

    @staticmethod
    def get__var():
        # print('Get Tech Tool Perm')
        return Dataset.tool_perm, Dataset.Entry_perm, Dataset.history

    @staticmethod
    def set_var(toolperm, entryperm, history):
        # print('Set Tech Tool Perm')
        Dataset.tool_perm = toolperm
        Dataset.Entry_perm = entryperm
        Dataset.history = history


class bt_enter_exit(bt.Strategy):
    # list of parameters which are configurable for the strategy

    def next(self):
        current_close = self.data.close[0]
        current_datetime = self.data.datetime.datetime()
        self.entry, self.exit = basesetup().proc(current_datetime, current_close)
        if not self.position:  # not in the market
            if (self.entry == True) & (self.exit == False):
                self.buy()  # enter long

        elif (self.exit == True) & (self.entry == False):
            self.close()  # close long position


class optcerebrosetup:
    def __init__(self, datadb, modelValue):
        self.modelValue = modelValue
        # self.modelValue = {'Cash': 10000, 'Commission': 0.0, 'Sizers': 90}
        self.cerebro = bt.Cerebro()
        self.db = self.btfeel(datadb)
        self.cerebro.adddata(self.db)
        self.cerebro.addstrategy(bt_enter_exit)
        self.cerebro.addobserver(bt.observers.DrawDown)
        self.cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
        self.loopperm()
        results = self.cerebro.run()
        portfolio_stats = results[0].analyzers.getbyname('pyfolio')
        self.returns, self.positions, self.transactions, self.gross_lev = portfolio_stats.get_pf_items()
        self.retuen_comp = qs.stats.comp(self.returns)
        self.return_cagr = qs.stats.cagr(self.returns)
        self.return_sharpe_ratio = qs.stats.sharpe(self.returns)
        self.return_risk_return_ratio = qs.stats.risk_return_ratio(
            self.returns)

    def opt_file(self):
        return self.retuen_comp, self.return_cagr, self.return_sharpe_ratio, self.return_risk_return_ratio

    def returns_retuen_comp(self):
        return self.retuen_comp

    def returns_return_prof(self):
        return qs.stats.avg_return(self.returns)

    def returns_return_cagr(self):
        return self.return_cagr

    def returns_return_sharpe_ratio(self):
        return self.return_sharpe_ratio

    def returns_return_risk_return_ratio(self):
        return self.return_risk_return_ratio

    def returns_file(self):
        return self.returns, self.positions, self.transactions, self.gross_lev

    def btfeel(self, datadb):
        return bt.feeds.PandasData(dataname=datadb)

    def setcash(self, dollar):
        self.cerebro.broker.setcash(dollar)

    def setcommission(self, commissionfee):
        self.cerebro.broker.setcommission(commission=commissionfee)

    def setsizers(self, sizer):
        self.cerebro.addsizer(bt.sizers.PercentSizer, percents=sizer)

    def loopperm(self):
        for perm in list(self.modelValue.keys()):
            self.setperm(perm)

    def setperm(self, text):
        self.value = self.modelValue
        if (text == 'Cash'):
            self.setcash(self.value[text])
        elif (text == 'Commission'):
            self.setcommission(self.value[text])
        elif (text == 'Sizers'):
            self.setsizers(self.value[text])


class tread_p_task:

    def __init__(self, mesh_conv, toolhistory, modelValue):
        Logger().info('Running Tread Quantstats Backtest.')
        self.mesh_conv = mesh_conv
        self.toolhistory = toolhistory
        self.modelValue = modelValue

    def processes(self):
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            results = list(executor.map(self.task, self.mesh_conv, [
                           self.toolhistory]*len(self.mesh_conv)))
        return results

    def task(self, mesh_conv, toolhistory):
        try:
            TechValue, EntryTechValue = self.split_data(mesh_conv)
            datadb = self.calculateinter(TechValue, toolhistory)
            self.setterret_profo_var(TechValue, EntryTechValue, datadb)
            self.return_sharpe_ratio = optcerebrosetup(datadb, self.modelValue)
            self.return_prof, self.return_cagr, self.return_sharpe_ratio, self.return_risk_return_ratio = self.return_sharpe_ratio.opt_file()
            return [TechValue, EntryTechValue, self.return_prof, self.return_cagr, self.return_sharpe_ratio, self.return_risk_return_ratio]
        except:
            return []

    def split_data(self, mesh_conv):
        return mesh_conv[0], mesh_conv[1]

    def calculateinter(self, TechValue, toolhistory):
        datadb = toolhistory
        TechValuekey = list(TechValue.keys())
        for param in TechValuekey:
            pr = param_return()
            returndatadb = pr.param_cal_return(
                model='cal', param=param, TechValue=TechValue, toolhistory=toolhistory)
            datadb = returndatadb
        return datadb

    def setterret_profo_var(self, toolpermm, entryperm, history):
        Dataset.set_var(toolpermm, entryperm, history)

    def getterret_profo_var(self):
        return Dataset.get__var()


class param_return:

    def param_cal_return(self, model, param, TechValue=None, toolhistory=None, row=None, entryTechValue=None):
        methods = {
            "RSI": rsi_inq,
            "MACD": macd_inq,
            "HT_DCPERIOD": ht_dc_inq,
            "HT_DCPHASE": ht_dchase_inq,
            "HT_PHASOR": ht_phasor_inq,
            "HT_SINE": ht_sine_inq,
            "HT_TRENDMODE": ht_trendmode_inq,
            "ADX": adx_inq,
            "ADXR": adxr_inq,
            "APO": apo_inq,
            "AROON": aroon_inq,
            "AROONOSC": aroonosc_inq,
            "BOP": bop_inq,
            "CCI": cci_inq,
            "CMO": cmo_inq,
            "DX": dx_inq,
            "MACDEXT": macdext_inq,
            "MACDFIX": macdfix_inq,
            "MFI": mfi_inq,
            "MINUS_DI": minus_di_inq,
            "MINUS_DM": minus_dm_inq,
            "MOM": mom_inq,
            "PLUS_DI": plusdi_inq,
            "PLUS_DM": plusdm_inq,
            "PPO": ppo_inq,
            "ROC": roc_inq,
            "ROCP": rocp_inq,
            "ROCR": rocr_inq,
            "ROCR100": rocr100_inq,
            "STOCH": stoch_inq,
            "STOCHF": stochf_inq,
            "STOCHRSI": stochrsi_inq,
            "TRIX": trix_inq,
            "ULTOSC": ultosc_inq,
            "WILLR": willr_inq,
            "MAVP": mavp_inq,
            "BBANDS": bbands_inq,
            "DEMA": dema_inq,
            "EMA": ema_inq,
            "HT_TRENDLINE": ht_trendline_inq,
            "KAMA": kama_inq,
            "MA": ma_inq,
            "MAMA": mama_inq,
            "MIDPOINT": midpoint_inq,
            "MIDPRICE": midprice_inq,
            "SAR": sar_inq,
            "SAREXT": sarext_inq,
            "SMA": sma_inq,
            "T3": t3_inq,
            "TEMA": tema_inq,
            "TRIMA": trima_inq,
            "WMA": wma_inq,
            "KDJ": kdj_inq,
            "ATR": atr_inq,
            "NATR": natr_inq,
            "TRANGE": trange_inq,
            "AD": ad_inq,
            "ADOSC": adosc_inq,
            "OBV": obv_inq
        }
        if (model == 'cal'):
            if param in methods:
                return methods[param]().calculate(TechValue=TechValue, toolhistory=toolhistory)

        if (model == 'enter'):
            if param in methods:
                return methods[param]().entry(row=row, entryTechValue=entryTechValue, toolhistory=toolhistory)
        if (model == 'exit'):
            if param in methods:
                return methods[param]().exit(row=row, entryTechValue=entryTechValue, toolhistory=toolhistory)


class basesetup:
    def __init__(self):
        pass

    def proc(self, current_datetime, current_close):
        tool_perm, Entry_perm, history = self.getterret_profo_var()
        rows = self.df_row(current_datetime, current_close, history)
        rows = rows.squeeze()
        self.entry = self.tran_entry(
            row=rows, entryTechValue=Entry_perm, toolhistory=history)
        self.exit = self.tran_exit(
            row=rows, entryTechValue=Entry_perm, toolhistory=history)
        return self.entry, self.exit

    def df_row(self, datatime, close, toolhistory):
        self.df = toolhistory
        self.converted_dt = self.conv_date_to_America_New_York(datatime)
        selected_rows = self.df.loc[(self.df['Close'] == close) & (
            self.df.index == self.converted_dt)]
        return selected_rows

    def conv_date_to_America_New_York(self, datetime):
        dt_without_tz = pytz.utc.localize(datetime)
        converted_dt = dt_without_tz.astimezone(
            pytz.timezone('America/New_York'))
        return converted_dt

    def tran_entry(self, row, entryTechValue, toolhistory):
        self.entry_exit_trankeys = list(entryTechValue.keys())
        self.Checklist = []
        for param in self.entry_exit_trankeys:
            self.entryCheck = param_return().param_cal_return(
                model='enter', param=param, row=row, entryTechValue=entryTechValue, toolhistory=toolhistory)
            self.Checklist.append(self.entryCheck)
        if (all(self.Checklist)):
            return True
        else:
            return False

    def tran_exit(self, row, entryTechValue, toolhistory):
        self.exit_exit_trankeys = list(entryTechValue.keys())
        self.Checklist = []
        for param in self.exit_exit_trankeys:
            self.exitCheck = param_return().param_cal_return(
                model='exit', param=param, row=row, entryTechValue=entryTechValue, toolhistory=toolhistory)
            self.Checklist.append(self.exitCheck)
        if (all(self.Checklist)):
            return True
        else:
            return False

    def getterret_profo_var(self):
        return Dataset.get__var()


class rsi_inq():
    def calculate(self, TechValue, toolhistory):
        if (TechValue['RSI'] == 0):
            TechValue['RSI'] = 2
        datadb = toolhistory
        self.parameter = TechValue['RSI']
        datadb["RSI"] = talib.RSI(
            datadb["Close"], timeperiod=int(TechValue['RSI']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['RSI']
        self.entryba = entryTechValue['RSI']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['RSI']
        self.entryba = entryTechValue['RSI']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False


class macd_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MACD"], datadb["MACD_SIGNAL"], datadb["MACD_HIST"] = talib.MACD(datadb['Close'], fastperiod=int(TechValue['MACD']['fastperiod']), slowperiod=int(
            TechValue['MACD']['slowperiod']), signalperiod=int(TechValue['MACD']['signalperiod']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MACD']['GOLDEN CROSS']
        self.MACDitem = row.loc['MACD']
        self.MACD_SIGNALitem = row.loc['MACD_SIGNAL']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MACD']['Death Cross']
        self.MACDitem = row.loc['MACD']
        self.MACD_SIGNALitem = row.loc['MACD_SIGNAL']
        if (self.exitba == 'True'):
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem)):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class ht_dc_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["HT_DCPERIOD"] = talib.HT_DCPERIOD(datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_DCPERIOD']
        self.entryba = entryTechValue['HT_DCPERIOD']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_DCPERIOD']
        self.exitba = entryTechValue['HT_DCPERIOD']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ht_dchase_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["HT_DCPHASE"] = talib.HT_DCPHASE(datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_DCPHASE']
        self.entryba = entryTechValue['HT_DCPHASE']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_DCPHASE']
        self.exitba = entryTechValue['HT_DCPHASE']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ht_phasor_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["HT_PHASOR_INHPASE"], datadb["HT_PHASOR_QUADRATURE"] = talib.HT_PHASOR(
            datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['HT_PHASOR']['GOLDEN CROSS']
        self.HT_PHASORitem = row.loc['HT_PHASOR_INHPASE']
        self.HT_PHASOR_QUADRATUREitem = row.loc['HT_PHASOR_QUADRATURE']
        if (self.entryba == 'True'):
            if float(self.HT_PHASORitem) > float(self.HT_PHASOR_QUADRATUREitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.HT_PHASORitem) < float(self.HT_PHASOR_QUADRATUREitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['HT_PHASOR']['Death Cross']
        self.HT_PHASORitem = row.loc['HT_PHASOR_INHPASE']
        self.HT_PHASOR_QUADRATUREitem = row.loc['HT_PHASOR_QUADRATURE']
        if (self.exitba == 'True'):
            if float(self.HT_PHASORitem) < float(self.HT_PHASOR_QUADRATUREitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.HT_PHASORitem) > float(self.HT_PHASOR_QUADRATUREitem):
                return True
            else:
                return False


class ht_sine_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["SINE"], datadb["LEADSINE"] = talib.HT_SINE(datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['SINE']
        self.entryba = entryTechValue['HT_SINE']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['SINE']
        self.exitba = entryTechValue['HT_SINE']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ht_trendmode_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["HT_TRENDMODE"] = talib.HT_TRENDMODE(datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_TRENDMODE']
        self.entryba = entryTechValue['HT_TRENDMODE']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['HT_TRENDMODE']
        self.exitba = entryTechValue['HT_TRENDMODE']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class adx_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ADX"] = talib.ADX(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['ADX']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ADX']
        self.entryba = entryTechValue['ADX']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ADX']
        self.exitba = entryTechValue['ADX']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class adxr_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ADXR"] = talib.ADXR(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['ADXR']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ADXR']
        self.entryba = entryTechValue['ADXR']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ADXR']
        self.exitba = entryTechValue['ADXR']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class apo_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["APO"] = talib.APO(datadb['Close'], fastperiod=int(TechValue['APO']['fastperiod']), slowperiod=int(
            TechValue['APO']['slowperiod']), matype=int(TechValue['APO']['matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['APO']
        self.entryba = entryTechValue['APO']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['APO']
        self.exitba = entryTechValue['APO']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class aroon_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["AROON_UP"], datadb["AROON_DOWN"] = talib.AROON(
            datadb["High"], datadb["Low"], timeperiod=int(TechValue['AROON']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['AROON']['GOLDEN CROSS']
        self.item = row.loc['AROON_UP']
        self.SIGNALitem = row.loc['AROON_DOWN']
        if (self.entryba == 'True'):
            if float(self.item) > float(self.SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.item) < float(self.SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['AROON']['Death Cross']
        self.item = row.loc['AROON_UP']
        self.SIGNALitem = row.loc['AROON_DOWN']
        if (self.exitba == 'True'):
            if float(self.item) < float(self.SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.item) > float(self.SIGNALitem):
                return True
            else:
                return False


class aroonosc_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["AROONOSC"] = talib.AROONOSC(
            datadb["High"], datadb["Low"], timeperiod=int(TechValue['AROONOSC']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['AROONOSC']
        self.entryba = entryTechValue['AROONOSC']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['AROONOSC']
        self.exitba = entryTechValue['AROONOSC']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class bop_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["BOP"] = talib.BOP(
            datadb["Open"], datadb["High"], datadb["Low"], datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['BOP']
        self.entryba = entryTechValue['BOP']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['BOP']
        self.exitba = entryTechValue['BOP']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class cci_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["CCI"] = talib.CCI(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['CCI']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['CCI']
        self.entryba = entryTechValue['CCI']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['CCI']
        self.exitba = entryTechValue['CCI']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class cmo_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["CMO"] = talib.CMO(
            datadb["Close"], timeperiod=int(TechValue['CMO']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['CMO']
        self.entryba = entryTechValue['CMO']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['CMO']
        self.exitba = entryTechValue['CMO']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class dx_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["DX"] = talib.DX(datadb["High"], datadb["Low"],
                                datadb["Close"], timeperiod=int(TechValue['DX']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['DX']
        self.entryba = entryTechValue['DX']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['DX']
        self.exitba = entryTechValue['DX']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class macdext_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MACDEXT"], datadb["MACDEXT_SIGNAL"], datadb["MACDEXT_HIST"] = talib.MACDEXT(datadb['Close'], fastperiod=int(TechValue['MACDEXT']['fastperiod']), fastmatype=int(TechValue['MACDEXT']['fastmatype']), slowperiod=int(
            TechValue['MACDEXT']['slowperiod']), slowmatype=int(TechValue['MACDEXT']['slowmatype']), signalperiod=int(TechValue['MACDEXT']['signalperiod']), signalmatype=int(TechValue['MACDEXT']['signalmatype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MACDEXT']['GOLDEN CROSS']
        self.MACDitem = row.loc['MACDEXT']
        self.MACD_SIGNALitem = row.loc['MACDEXT_SIGNAL']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MACDEXT']['Death Cross']
        self.MACDitem = row.loc['MACDEXT']
        self.MACD_SIGNALitem = row.loc['MACDEXT_SIGNAL']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class macdfix_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MACDFIX"], datadb["MACDFIX_SIGNAL"], datadb["MACDFIX_HIST"] = talib.MACDFIX(
            datadb["Close"], signalperiod=int(TechValue['MACDFIX']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MACDFIX']['GOLDEN CROSS']
        self.MACDitem = row.loc['MACDFIX']
        self.MACD_SIGNALitem = row.loc['MACDFIX_SIGNAL']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MACDFIX']['Death Cross']
        self.MACDitem = row.loc['MACDFIX']
        self.MACD_SIGNALitem = row.loc['MACDFIX_SIGNAL']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class mfi_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MFI"] = talib.MFI(datadb["High"], datadb["Low"], datadb["Close"],
                                  datadb["Volume"], timeperiod=int(TechValue['MFI']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MFI']
        self.entryba = entryTechValue['MFI']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MFI']
        self.exitba = entryTechValue['MFI']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class minus_di_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MINUS_DI"] = talib.MINUS_DI(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['MINUS_DI']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MINUS_DI']
        self.entryba = entryTechValue['MINUS_DI']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MINUS_DI']
        self.exitba = entryTechValue['MINUS_DI']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class minus_dm_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MINUS_DM"] = talib.MINUS_DM(
            datadb["High"], datadb["Low"], timeperiod=int(TechValue['MINUS_DM']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MINUS_DI']
        self.entryba = entryTechValue['MINUS_DI']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MINUS_DI']
        self.exitba = entryTechValue['MINUS_DI']['LOW']
        if (float(self.item) < float(self.exitba)):
            return True
        else:
            return False


class mom_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MOM"] = talib.MOM(
            datadb["Close"], timeperiod=int(TechValue['MOM']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MOM']
        self.entryba = entryTechValue['MOM']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MOM']
        self.exitba = entryTechValue['MOM']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class plusdi_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["PLUS_DI"] = talib.PLUS_DI(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['PLUS_DI']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PLUS_DI']
        self.entryba = entryTechValue['PLUS_DI']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PLUS_DI']
        self.exitba = entryTechValue['PLUS_DI']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class plusdm_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["PLUS_DM"] = talib.PLUS_DM(
            datadb["High"], datadb["Low"], timeperiod=int(TechValue['PLUS_DM']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PLUS_DM']
        self.entryba = entryTechValue['PLUS_DM']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PLUS_DM']
        self.exitba = entryTechValue['PLUS_DM']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ppo_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["PPO"] = talib.PPO(datadb['Close'], fastperiod=int(TechValue['PPO']['fastperiod']), slowperiod=int(
            TechValue['PPO']['slowperiod']), matype=int(TechValue['PPO']['matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PPO']
        self.entryba = entryTechValue['PPO']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['PPO']
        self.exitba = entryTechValue['PPO']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class roc_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ROC"] = talib.ROC(
            datadb["Close"], timeperiod=int(TechValue['ROC']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROC']
        self.entryba = entryTechValue['ROC']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROC']
        self.exitba = entryTechValue['ROC']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class rocp_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ROCP"] = talib.ROCP(
            datadb["Close"], timeperiod=int(TechValue['ROCP']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCP']
        self.entryba = entryTechValue['ROCP']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCP']
        self.exitba = entryTechValue['ROCP']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class rocr_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ROCR"] = talib.ROCR(
            datadb["Close"], timeperiod=int(TechValue['ROCR']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCR']
        self.entryba = entryTechValue['ROCR']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCR']
        self.exitba = entryTechValue['ROCR']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class rocr100_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ROCR100"] = talib.ROCR100(
            datadb["Close"], timeperiod=int(TechValue['ROCR100']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCR100']
        self.entryba = entryTechValue['ROCR100']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ROCR100']
        self.exitba = entryTechValue['ROCR100']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class stoch_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["STOCH_SLOWK"], datadb["STOCH_SLOWD"] = talib.STOCH(datadb['High'], datadb['Low'], datadb['Close'], fastk_period=int(TechValue['STOCH']['fastk_period']), slowk_period=int(
            TechValue['STOCH']['slowk_period']), slowk_matype=int(TechValue['STOCH']['slowk_matype']), slowd_period=int(TechValue['STOCH']['slowd_period']), slowd_matype=int(TechValue['STOCH']['slowd_matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['STOCH']['GOLDEN CROSS']
        self.MACDitem = row.loc['STOCH_SLOWK']
        self.MACD_SIGNALitem = row.loc['STOCH_SLOWD']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['STOCH']['Death Cross']
        self.MACDitem = row.loc['STOCH_SLOWK']
        self.MACD_SIGNALitem = row.loc['STOCH_SLOWD']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class stochf_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["STOCHF_FASTK"], datadb["STOCHF_FASTD"] = talib.STOCHF(datadb['High'], datadb['Low'], datadb['Close'], fastk_period=int(
            TechValue['STOCHF']['fastk_period']), fastd_period=int(TechValue['STOCHF']['fastd_period']), fastd_matype=int(TechValue['STOCHF']['fastd_matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['STOCHF']['GOLDEN CROSS']
        self.MACDitem = row.loc['STOCHF_FASTK']
        self.MACD_SIGNALitem = row.loc['STOCHF_FASTD']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['STOCHF']['Death Cross']
        self.MACDitem = row.loc['STOCHF_FASTK']
        self.MACD_SIGNALitem = row.loc['STOCHF_FASTD']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class stochrsi_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["STOCHRSI_SLOWK"], datadb["STOCHRSI_SLOWD"] = talib.STOCHRSI(datadb['Close'], timeperiod=int(TechValue['STOCHRSI']['timeperiod']), fastk_period=int(
            TechValue['STOCHRSI']['fastk_period']), fastd_period=int(TechValue['STOCHRSI']['fastd_period']), fastd_matype=int(TechValue['STOCHRSI']['fastd_matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['STOCHRSI']['GOLDEN CROSS']
        self.MACDitem = row.loc['STOCHRSI_SLOWK']
        self.MACD_SIGNALitem = row.loc['STOCHRSI_SLOWD']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['STOCHRSI']['Death Cross']
        self.MACDitem = row.loc['STOCHRSI_SLOWK']
        self.MACD_SIGNALitem = row.loc['STOCHRSI_SLOWD']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class trix_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["TRIX"] = talib.TRIX(
            datadb["Close"], timeperiod=int(TechValue['TRIX']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['TRIX']
        self.entryba = entryTechValue['TRIX']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['TRIX']
        self.exitba = entryTechValue['TRIX']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ultosc_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ULTOSC"] = talib.ULTOSC(datadb['High'], datadb['Low'], datadb['Close'], timeperiod1=int(
            TechValue['ULTOSC']['timeperiod1']), timeperiod2=int(TechValue['ULTOSC']['timeperiod2']), timeperiod3=int(TechValue['ULTOSC']['timeperiod3']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ULTOSC']
        self.entryba = entryTechValue['ULTOSC']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ULTOSC']
        self.exitba = entryTechValue['ULTOSC']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class willr_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["WILLR"] = talib.WILLR(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['WILLR']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['WILLR']
        self.entryba = entryTechValue['WILLR']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['WILLR']
        self.exitba = entryTechValue['WILLR']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class mavp_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        periods = None
        datadb["MAVP"] = talib.MAVP(datadb['Close'], periods, minperiod=int(TechValue['MAVP']['minperiod']), maxperiod=int(
            TechValue['MAVP']['maxperiod']), matype=int(TechValue['MAVP']['matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MAVP']
        self.entryba = entryTechValue['MAVP']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['MAVP']
        self.exitba = entryTechValue['MAVP']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class bbands_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["BBANDS_UPPERBAND"], datadb["BBANDS_MIDDLEBAND"], datadb["BBANDS_LOWERBAND"] = talib.BBANDS(
            datadb['Close'], timeperiod=int(TechValue['BBANDS']['timeperiod']), nbdevup=int(TechValue['BBANDS']['nbdevup']), nbdevdn=int(TechValue['BBANDS']['nbdevdn']), matype=int(TechValue['BBANDS']['matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['BBANDS']['BBANDS_UPPERBAND']
        self.MACDitem = row.loc['Close']
        self.MACD_SIGNALitem = row.loc['BBANDS_UPPERBAND']
        self.entryMIDDLEBAND = row.loc['BBANDS_MIDDLEBAND']
        if (self.entryba == 'True'):
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem) and float(self.MACDitem) < float(self.entryMIDDLEBAND)):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if (float(self.MACDitem) > float(self.MACD_SIGNALitem) and float(self.MACDitem) > float(self.entryMIDDLEBAND)):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['BBANDS']['BBANDS_LOWERBAND']
        self.MACDitem = row.loc['Close']
        self.MACD_SIGNALitem = row.loc['BBANDS_LOWERBAND']
        self.entryMIDDLEBAND = row.loc['BBANDS_MIDDLEBAND']
        if (self.exitba == 'True'):
            if (float(self.MACDitem) > float(self.MACD_SIGNALitem) and float(self.MACDitem) > float(self.entryMIDDLEBAND)):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if (float(self.MACDitem) < float(self.MACD_SIGNALitem) and float(self.MACDitem) < float(self.entryMIDDLEBAND)):
                return True
            else:
                return False


class dema_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["DEMA_parameter_1"] = talib.DEMA(
            datadb["Close"], timeperiod=int(TechValue['DEMA']['Parameters_1']))
        datadb["DEMA_parameter_2"] = talib.DEMA(
            datadb["Close"], timeperiod=int(TechValue['DEMA']['Parameters_2']))
        datadb["DEMA_parameter_3"] = talib.DEMA(
            datadb["Close"], timeperiod=int(TechValue['DEMA']['Parameters_3']))
        datadb["DEMA_parameter_4"] = talib.DEMA(
            datadb["Close"], timeperiod=int(TechValue['DEMA']['Parameters_4']))
        datadb["DEMA_parameter_5"] = talib.DEMA(
            datadb["Close"], timeperiod=int(TechValue['DEMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['DEMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['DEMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['DEMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['DEMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        self.p1 = row.loc['DEMA_parameter_1']
        self.p2 = row.loc['DEMA_parameter_2']
        self.p3 = row.loc['DEMA_parameter_3']
        self.p4 = row.loc['DEMA_parameter_4']
        self.p5 = row.loc['DEMA_parameter_5']
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['DEMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['DEMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['DEMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['DEMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        self.p1 = row.loc['DEMA_parameter_1']
        self.p2 = row.loc['DEMA_parameter_2']
        self.p3 = row.loc['DEMA_parameter_3']
        self.p4 = row.loc['DEMA_parameter_4']
        self.p5 = row.loc['DEMA_parameter_5']
        ####
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class ema_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["EMA_parameter_1"] = talib.EMA(
            datadb["Close"], timeperiod=int(TechValue['EMA']['Parameters_1']))
        datadb["EMA_parameter_2"] = talib.EMA(
            datadb["Close"], timeperiod=int(TechValue['EMA']['Parameters_2']))
        datadb["EMA_parameter_3"] = talib.EMA(
            datadb["Close"], timeperiod=int(TechValue['EMA']['Parameters_3']))
        datadb["EMA_parameter_4"] = talib.EMA(
            datadb["Close"], timeperiod=int(TechValue['EMA']['Parameters_4']))
        datadb["EMA_parameter_5"] = talib.EMA(
            datadb["Close"], timeperiod=int(TechValue['EMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['EMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['EMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['EMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['EMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['EMA_parameter_1']
        self.p2 = row.loc['EMA_parameter_2']
        self.p3 = row.loc['EMA_parameter_3']
        self.p4 = row.loc['EMA_parameter_4']
        self.p5 = row.loc['EMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['EMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['EMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['EMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['EMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['EMA_parameter_1']
        self.p2 = row.loc['EMA_parameter_2']
        self.p3 = row.loc['EMA_parameter_3']
        self.p4 = row.loc['EMA_parameter_4']
        self.p5 = row.loc['EMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class ht_trendline_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["HT_TRENDLINE"] = talib.HT_TRENDLINE(datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['HT_TRENDLINE']['GOLDEN CROSS']
        self.MACDitem = row.loc['HT_TRENDLINE']
        self.MACD_SIGNALitem = row.loc['Close']
        if (self.entryba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['HT_TRENDLINE']['Death Cross']
        self.MACDitem = row.loc['HT_TRENDLINE']
        self.MACD_SIGNALitem = row.loc['Close']
        if (self.exitba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class kama_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["KAMA_parameter_1"] = talib.KAMA(
            datadb["Close"], timeperiod=int(TechValue['KAMA']['Parameters_1']))
        datadb["KAMA_parameter_2"] = talib.KAMA(
            datadb["Close"], timeperiod=int(TechValue['KAMA']['Parameters_2']))
        datadb["KAMA_parameter_3"] = talib.KAMA(
            datadb["Close"], timeperiod=int(TechValue['KAMA']['Parameters_3']))
        datadb["KAMA_parameter_4"] = talib.KAMA(
            datadb["Close"], timeperiod=int(TechValue['KAMA']['Parameters_4']))
        datadb["KAMA_parameter_5"] = talib.KAMA(
            datadb["Close"], timeperiod=int(TechValue['KAMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['KAMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['KAMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['KAMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['KAMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['KAMA_parameter_1']
        self.p2 = row.loc['KAMA_parameter_2']
        self.p3 = row.loc['KAMA_parameter_3']
        self.p4 = row.loc['KAMA_parameter_4']
        self.p5 = row.loc['KAMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['KAMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['KAMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['KAMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['KAMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['KAMA_parameter_1']
        self.p2 = row.loc['KAMA_parameter_2']
        self.p3 = row.loc['KAMA_parameter_3']
        self.p4 = row.loc['KAMA_parameter_4']
        self.p5 = row.loc['KAMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class ma_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MA"] = talib.MA(datadb['Close'], timeperiod=int(
            TechValue['MA']['timeperiod']), matype=int(TechValue['MA']['matype']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        return True

    def exit(self, row, entryTechValue, toolhistory=None):
        return True


class mama_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MAMA"], datadb["MAMA_FAMA"] = talib.MAMA(
            datadb['Close'], fastlimit=float(TechValue['MAMA']['fastlimit']), slowlimit=float(TechValue['MAMA']['slowlimit']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MAMA']['GOLDEN CROSS']
        self.MACDitem = row.loc['MAMA']
        self.MACD_SIGNALitem = row.loc['MAMA_FAMA']
        if (self.entryba == 'True'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MAMA']['Death Cross']
        self.MACDitem = row.loc['MAMA']
        self.MACD_SIGNALitem = row.loc['MAMA_FAMA']
        if (self.exitba == 'True'):
            if float(self.MACDitem) < float(self.MACD_SIGNALitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MACDitem) > float(self.MACD_SIGNALitem):
                return True
            else:
                return False


class midpoint_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MIDPOINT"] = talib.MIDPOINT(
            datadb["Close"], timeperiod=int(TechValue['MIDPOINT']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MIDPOINT']['GOLDEN CROSS']
        self.MIDPOINTitem = row.loc['MIDPOINT']
        self.Highitem = row.loc['High']
        self.Lowitem = row.loc['Low']
        self.MIditem = (float(self.Highitem) + float(self.Lowitem))/2
        if (self.entryba == 'True'):
            if float(self.MIDPOINTitem) < float(self.MIditem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MIDPOINTitem) > float(self.MIditem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MIDPOINT']['Death Cross']
        self.MIDPOINTitem = row.loc['MIDPOINT']
        self.Highitem = row.loc['High']
        self.Lowitem = row.loc['Low']
        self.MIditem = (float(self.Highitem) + float(self.Lowitem))/2
        if (self.exitba == 'True'):
            if float(self.MIDPOINTitem) > float(self.MIditem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MIDPOINTitem) < float(self.MIditem):
                return True
            else:
                return False


class midprice_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["MIDPRICE"] = talib.MIDPRICE(
            datadb["High"], datadb["Low"], timeperiod=int(TechValue['MIDPRICE']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['MIDPRICE']['GOLDEN CROSS']
        self.MIDPOINTitem = row.loc['MIDPRICE']
        self.Highitem = row.loc['High']
        self.Lowitem = row.loc['Low']
        self.MIditem = (float(self.Highitem) + float(self.Lowitem))/2
        if (self.entryba == 'True'):
            if float(self.MIDPOINTitem) < float(self.MIditem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MIDPOINTitem) > float(self.MIditem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['MIDPRICE']['Death Cross']
        self.MIDPOINTitem = row.loc['MIDPRICE']
        self.Highitem = row.loc['High']
        self.Lowitem = row.loc['Low']
        self.MIditem = (float(self.Highitem) + float(self.Lowitem))/2
        if (self.exitba == 'True'):
            if float(self.MIDPOINTitem) > float(self.MIditem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MIDPOINTitem) < float(self.MIditem):
                return True
            else:
                return False


class sar_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["SAR"] = talib.SAR(datadb['High'], datadb['Low'], acceleration=float(
            TechValue['SAR']['acceleration']), maximum=float(TechValue['SAR']['maximum']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.entryba = entryTechValue['SAR']['GOLDEN CROSS']
        self.MIDPOINTitem = row.loc['SAR']
        self.Closeitem = row.loc['Close']
        if (self.entryba == 'True'):
            if float(self.MIDPOINTitem) < float(self.Closeitem):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if float(self.MIDPOINTitem) > float(self.Closeitem):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.exitba = entryTechValue['SAR']['Death Cross']
        self.MIDPOINTitem = row.loc['SAR']
        self.Closeitem = row.loc['Close']
        if (self.exitba == 'True'):
            if float(self.MIDPOINTitem) > float(self.Closeitem):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if float(self.MIDPOINTitem) < float(self.Closeitem):
                return True
            else:
                return False


class sarext_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["SAREXT"] = talib.SAREXT(datadb['High'], datadb['Low'], startvalue=float(TechValue['SAREXT']['startvalue']), offsetonreverse=float(TechValue['SAREXT']['offsetonreverse']), accelerationinitlong=float(TechValue['SAREXT']['accelerationinitlong']), accelerationlong=float(
            TechValue['SAREXT']['accelerationlong']), accelerationmaxlong=float(TechValue['SAREXT']['accelerationmaxlong']), accelerationinitshort=float(TechValue['SAREXT']['accelerationinitshort']), accelerationshort=float(TechValue['SAREXT']['accelerationshort']), accelerationmaxshort=float(TechValue['SAREXT']['accelerationmaxshort']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['SAREXT']
        self.entryba = entryTechValue['SAREXT']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['SAREXT']
        self.exitba = entryTechValue['SAREXT']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class sma_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["SMA_parameter_1"] = talib.SMA(
            datadb["Close"], timeperiod=int(TechValue['SMA']['Parameters_1']))
        datadb["SMA_parameter_2"] = talib.SMA(
            datadb["Close"], timeperiod=int(TechValue['SMA']['Parameters_2']))
        datadb["SMA_parameter_3"] = talib.SMA(
            datadb["Close"], timeperiod=int(TechValue['SMA']['Parameters_3']))
        datadb["SMA_parameter_4"] = talib.SMA(
            datadb["Close"], timeperiod=int(TechValue['SMA']['Parameters_4']))
        datadb["SMA_parameter_5"] = talib.SMA(
            datadb["Close"], timeperiod=int(TechValue['SMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['SMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['SMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['SMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['SMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['SMA_parameter_1']
        self.p2 = row.loc['SMA_parameter_2']
        self.p3 = row.loc['SMA_parameter_3']
        self.p4 = row.loc['SMA_parameter_4']
        self.p5 = row.loc['SMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['SMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['SMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['SMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['SMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['SMA_parameter_1']
        self.p2 = row.loc['SMA_parameter_2']
        self.p3 = row.loc['SMA_parameter_3']
        self.p4 = row.loc['SMA_parameter_4']
        self.p5 = row.loc['SMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class t3_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["T3_parameter_1"] = talib.T3(datadb['Close'], timeperiod=int(
            TechValue['T3']['parameter_1timeperiod']), vfactor=int(TechValue['T3']['parameter_1vfactor']))
        datadb["T3_parameter_2"] = talib.T3(datadb['Close'], timeperiod=int(
            TechValue['T3']['parameter_2timeperiod']), vfactor=int(TechValue['T3']['parameter_2vfactor']))
        datadb["T3_parameter_3"] = talib.T3(datadb['Close'], timeperiod=int(
            TechValue['T3']['parameter_3timeperiod']), vfactor=int(TechValue['T3']['parameter_3vfactor']))
        datadb["T3_parameter_4"] = talib.T3(datadb['Close'], timeperiod=int(
            TechValue['T3']['parameter_4timeperiod']), vfactor=int(TechValue['T3']['parameter_4vfactor']))
        datadb["T3_parameter_5"] = talib.T3(datadb['Close'], timeperiod=int(
            TechValue['T3']['parameter_5timeperiod']), vfactor=int(TechValue['T3']['parameter_5vfactor']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['T3'][
            'Parameters_1 - Parameters_2']['Golden Cross']
        self.parameters_2_Parameters_3 = entryTechValue['T3'][
            'Parameters_2 - Parameters_3']['Golden Cross']
        self.parameters_3_Parameters_4 = entryTechValue['T3'][
            'Parameters_3 - Parameters_4']['Golden Cross']
        self.parameters_4_Parameters_5 = entryTechValue['T3'][
            'Parameters_4 - Parameters_5']['Golden Cross']
        self.p1 = row.loc['T3_parameter_1']
        self.p2 = row.loc['T3_parameter_2']
        self.p3 = row.loc['T3_parameter_3']
        self.p4 = row.loc['T3_parameter_4']
        self.p5 = row.loc['T3_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['T3'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['T3'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['T3'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['T3'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['T3_parameter_1']
        self.p2 = row.loc['T3_parameter_2']
        self.p3 = row.loc['T3_parameter_3']
        self.p4 = row.loc['T3_parameter_4']
        self.p5 = row.loc['T3_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class tema_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["TEMA_parameter_1"] = talib.TEMA(
            datadb["Close"], timeperiod=int(TechValue['TEMA']['Parameters_1']))
        datadb["TEMA_parameter_2"] = talib.TEMA(
            datadb["Close"], timeperiod=int(TechValue['TEMA']['Parameters_2']))
        datadb["TEMA_parameter_3"] = talib.TEMA(
            datadb["Close"], timeperiod=int(TechValue['TEMA']['Parameters_3']))
        datadb["TEMA_parameter_4"] = talib.TEMA(
            datadb["Close"], timeperiod=int(TechValue['TEMA']['Parameters_4']))
        datadb["TEMA_parameter_5"] = talib.TEMA(
            datadb["Close"], timeperiod=int(TechValue['TEMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['TEMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['TEMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['TEMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['TEMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['TEMA_parameter_1']
        self.p2 = row.loc['TEMA_parameter_2']
        self.p3 = row.loc['TEMA_parameter_3']
        self.p4 = row.loc['TEMA_parameter_4']
        self.p5 = row.loc['TEMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['TEMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['TEMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['TEMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['TEMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['TEMA_parameter_1']
        self.p2 = row.loc['TEMA_parameter_2']
        self.p3 = row.loc['TEMA_parameter_3']
        self.p4 = row.loc['TEMA_parameter_4']
        self.p5 = row.loc['TEMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class trima_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["TRIMA_parameter_1"] = talib.TRIMA(
            datadb["Close"], timeperiod=int(TechValue['TRIMA']['Parameters_1']))
        datadb["TRIMA_parameter_2"] = talib.TRIMA(
            datadb["Close"], timeperiod=int(TechValue['TRIMA']['Parameters_2']))
        datadb["TRIMA_parameter_3"] = talib.TRIMA(
            datadb["Close"], timeperiod=int(TechValue['TRIMA']['Parameters_3']))
        datadb["TRIMA_parameter_4"] = talib.TRIMA(
            datadb["Close"], timeperiod=int(TechValue['TRIMA']['Parameters_4']))
        datadb["TRIMA_parameter_5"] = talib.TRIMA(
            datadb["Close"], timeperiod=int(TechValue['TRIMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['TRIMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['TRIMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['TRIMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['TRIMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['TRIMA_parameter_1']
        self.p2 = row.loc['TRIMA_parameter_2']
        self.p3 = row.loc['TRIMA_parameter_3']
        self.p4 = row.loc['TRIMA_parameter_4']
        self.p5 = row.loc['TRIMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['TRIMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['TRIMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['TRIMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['TRIMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['TRIMA_parameter_1']
        self.p2 = row.loc['TRIMA_parameter_2']
        self.p3 = row.loc['TRIMA_parameter_3']
        self.p4 = row.loc['TRIMA_parameter_4']
        self.p5 = row.loc['TRIMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class wma_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["WMA_parameter_1"] = talib.WMA(
            datadb["Close"], timeperiod=int(TechValue['WMA']['Parameters_1']))
        datadb["WMA_parameter_2"] = talib.WMA(
            datadb["Close"], timeperiod=int(TechValue['WMA']['Parameters_2']))
        datadb["WMA_parameter_3"] = talib.WMA(
            datadb["Close"], timeperiod=int(TechValue['WMA']['Parameters_3']))
        datadb["WMA_parameter_4"] = talib.WMA(
            datadb["Close"], timeperiod=int(TechValue['WMA']['Parameters_4']))
        datadb["WMA_parameter_5"] = talib.WMA(
            datadb["Close"], timeperiod=int(TechValue['WMA']['Parameters_5']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['WMA'][
            'Parameters_1 - Parameters_2']['GOLDEN CROSS']
        self.parameters_2_Parameters_3 = entryTechValue['WMA'][
            'Parameters_2 - Parameters_3']['GOLDEN CROSS']
        self.parameters_3_Parameters_4 = entryTechValue['WMA'][
            'Parameters_3 - Parameters_4']['GOLDEN CROSS']
        self.parameters_4_Parameters_5 = entryTechValue['WMA'][
            'Parameters_4 - Parameters_5']['GOLDEN CROSS']
        self.p1 = row.loc['WMA_parameter_1']
        self.p2 = row.loc['WMA_parameter_2']
        self.p3 = row.loc['WMA_parameter_3']
        self.p4 = row.loc['WMA_parameter_4']
        self.p5 = row.loc['WMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) > float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) < float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) > float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) < float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) > float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) < float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) > float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) < float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.parameters_1_Parameters_2 = entryTechValue['WMA'][
            'Parameters_1 - Parameters_2']['Death Cross']
        self.parameters_2_Parameters_3 = entryTechValue['WMA'][
            'Parameters_2 - Parameters_3']['Death Cross']
        self.parameters_3_Parameters_4 = entryTechValue['WMA'][
            'Parameters_3 - Parameters_4']['Death Cross']
        self.parameters_4_Parameters_5 = entryTechValue['WMA'][
            'Parameters_4 - Parameters_5']['Death Cross']
        self.p1 = row.loc['WMA_parameter_1']
        self.p2 = row.loc['WMA_parameter_2']
        self.p3 = row.loc['WMA_parameter_3']
        self.p4 = row.loc['WMA_parameter_4']
        self.p5 = row.loc['WMA_parameter_5']

        P_1_2 = None
        P_2_3 = None
        P_3_4 = None
        P_4_5 = None
        if float(self.p1) < float(self.p2):
            P_1_2 = 'True'
        elif float(self.p1) > float(self.p2):
            P_1_2 = 'False'
            ####
        if float(self.p2) < float(self.p3):
            P_2_3 = 'True'
        elif float(self.p2) > float(self.p3):
            P_2_3 = 'False'
            ####
        if float(self.p3) < float(self.p4):
            P_3_4 = 'True'
        elif float(self.p3) > float(self.p4):
            P_3_4 = 'False'
            ####
        if float(self.p4) < float(self.p5):
            P_4_5 = 'True'
        elif float(self.p4) > float(self.p5):
            P_4_5 = 'False'

        if (self.parameters_1_Parameters_2 == P_1_2) and (self.parameters_2_Parameters_3 == P_2_3) and (self.parameters_3_Parameters_4 == P_3_4) and (self.parameters_4_Parameters_5 == P_4_5):
            return True
        else:
            return False


class kdj_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["KDJ_SLOWK"], datadb["KDJ_SLOWD"] = talib.STOCH(datadb['High'], datadb['Low'], datadb['Close'], fastk_period=int(TechValue['KDJ']['fastk_period']), slowk_period=int(
            TechValue['KDJ']['slowk_period']), slowk_matype=int(TechValue['KDJ']['slowk_matype']), slowd_period=int(TechValue['KDJ']['slowd_period']), slowd_matype=int(TechValue['KDJ']['slowd_matype']))
        datadb['KDJ_SLOWJ'] = 3*datadb['KDJ_SLOWK']-2*datadb['KDJ_SLOWD']
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['KDJ_SLOWJ']
        self.entryba = entryTechValue['KDJ']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['KDJ_SLOWJ']
        self.exitba = entryTechValue['KDJ']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class atr_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ATR"] = talib.ATR(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['ATR']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ATR']
        self.entryba = entryTechValue['ATR']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['ATR']
        self.exitba = entryTechValue['ATR']['LOW']
        if (float(self.item) < float(self.exitba)):
            return True
        else:
            return False


class natr_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["NATR"] = talib.NATR(
            datadb["High"], datadb["Low"], datadb["Close"], timeperiod=int(TechValue['NATR']))
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['NATR']
        self.entryba = entryTechValue['NATR']['HIGH']
        if (float(self.item) > float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['NATR']
        self.exitba = entryTechValue['NATR']['LOW']
        if (float(self.item) < float(self.exitba)):
            return True
        else:
            return False


class trange_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["TRANGE"] = talib.TRANGE(
            datadb["High"], datadb["Low"], datadb["Close"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['TRANGE']
        self.entryba = entryTechValue['TRANGE']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['TRANGE']
        self.exitba = entryTechValue['TRANGE']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False


class ad_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["AD"] = talib.AD(datadb["High"], datadb["Low"],
                                datadb["Close"], datadb["Volume"])
        return datadb

    def get_db_for_entry_exit(self, testitem, toolhistory):
        self.ChecklistClose = []
        self.ChecklistAD = []
        self.df = toolhistory
        self.targetindex = testitem
        for i in range(1, 3):
            previous_close = self.df.shift(i).loc[(self.df['AD'] == self.targetindex['AD']) & (
                self.df['Close'] == self.targetindex['Close'])].head(1)
            # Add 'Close' values to self.Checklist
            if not previous_close.empty:
                self.ChecklistClose.append(previous_close['Close'].iloc[0])
                self.ChecklistAD.append(previous_close['AD'].iloc[0])
            else:
                break
        return self.ChecklistClose, self.ChecklistAD

    def Check_AD_CLOSE_RELAT(self, rel, new):
        self.new = new
        self.rel = rel
        if (self.rel != []):
            close_0 = self.rel[0]
            if (float(self.new) > float(close_0)):
                return "111"
            elif (float(self.new) < float(close_0)):
                return "000"
            else:
                return "Unknown"
        else:
            return "Unknown"

    def entry(self, row, entryTechValue, toolhistory):
        self.entryba = entryTechValue['AD']['Bottom Divergence']
        self.itemclose = row.loc['Close']
        self.itemad = row.loc['AD']
        self.oldclose, self.oldad = self.get_db_for_entry_exit(
            row, toolhistory)
        self.close_test = self.Check_AD_CLOSE_RELAT(
            self.oldclose, self.itemclose)
        self.ad_test = self.Check_AD_CLOSE_RELAT(self.oldad, self.itemad)
        if (self.entryba == 'True'):
            if (self.close_test == "000" and self.ad_test == "111"):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if (self.close_test == "111" and self.ad_test == "000"):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory):
        self.exitba = entryTechValue['AD']['Top Divergence']
        self.itemclose = row.loc['Close']
        self.itemad = row.loc['AD']
        self.oldclose, self.oldad = self.get_db_for_entry_exit(
            row, toolhistory)
        self.close_test = self.Check_AD_CLOSE_RELAT(
            self.oldclose, self.itemclose)
        self.ad_test = self.Check_AD_CLOSE_RELAT(self.oldad, self.itemad)
        if (self.exitba == 'True'):
            if (self.close_test == "111" and self.ad_test == "000"):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if (self.close_test == "000" and self.ad_test == "111"):
                return True
            else:
                return False


class adosc_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["ADOSC"] = talib.ADOSC(
            datadb['High'], datadb['Low'], datadb['Close'], datadb['Volume'], fastperiod=int(TechValue['ADOSC']['fastperiod']), slowperiod=int(TechValue['ADOSC']['slowperiod']))
        return datadb

    def get_db_for_entry_exit(self, testitem, toolhistory):
        self.ChecklistClose = []
        self.ChecklistAD = []
        self.df = toolhistory
        self.targetindex = testitem
        for i in range(1, 3):
            self.adoscitem = self.targetindex['ADOSC']
            if (self.adoscitem != np.nan):
                previous_close = self.df.shift(i).loc[(self.df['ADOSC'] == self.targetindex['ADOSC']) & (
                    self.df['Close'] == self.targetindex['Close'])].head(1)
                # Add 'Close' values to self.Checklist
                if not previous_close.empty:
                    self.ChecklistClose.append(previous_close['Close'].iloc[0])
                    self.ChecklistAD.append(previous_close['ADOSC'].iloc[0])
            else:
                break
        return self.ChecklistClose, self.ChecklistAD

    def CheckMathis(self, item):
        self.math = item
        if (self.math > 0):
            return "1"
        elif (self.math < 0):
            return "0"
        else:
            return "-"

    def Check_RELAT(self, relclose, newclose, relad, newad):
        self.relclose = relclose
        self.relad = relad

        if (self.relad != [] and self.relclose != []):

            if (self.CheckMathis(newad) == "0" and self.CheckMathis(self.relad[0]) == "1"):
                return "111"
            elif (self.CheckMathis(newad) == "1" and self.CheckMathis(self.relad[0]) == "0"):
                return "000"
            else:
                return "Unknown"
        else:
            return "Unknown"

    def entry(self, row, entryTechValue, toolhistory):
        self.entryba = entryTechValue['ADOSC']['GOLDEN CROSS']
        self.itemclose = row.loc['Close']
        self.itemADOSC = row.loc['ADOSC']
        self.oldclose, self.oldad = self.get_db_for_entry_exit(
            row, toolhistory)
        self.ad_test = self.Check_RELAT(
            self.oldclose, self.itemclose, self.oldad, self.itemADOSC)
        if (self.entryba == 'True'):
            if (self.ad_test == "111"):
                return True
            else:
                return False
        elif (self.entryba == 'False'):
            if (self.ad_test == "000"):
                return True
            else:
                return False

    def exit(self, row, entryTechValue, toolhistory):
        self.exitba = entryTechValue['ADOSC']['Death Cross']
        self.itemclose = row.loc['Close']
        self.itemADOSC = row.loc['ADOSC']
        self.oldclose, self.oldad = self.get_db_for_entry_exit(
            row, toolhistory)
        self.ad_test = self.Check_RELAT(
            self.oldclose, self.itemclose, self.oldad, self.itemADOSC)
        if (self.exitba == 'True'):
            if (self.ad_test == "000"):
                return True
            else:
                return False
        elif (self.exitba == 'False'):
            if (self.ad_test == "111"):
                return True
            else:
                return False


class obv_inq():
    def calculate(self, TechValue, toolhistory):
        datadb = toolhistory
        datadb["OBV"] = talib.OBV(datadb["Close"], datadb["Volume"])
        return datadb

    def entry(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['OBV']
        self.entryba = entryTechValue['OBV']['LOW']
        if (float(self.item) < float(self.entryba)):
            return True
        else:
            return False

    def exit(self, row, entryTechValue, toolhistory=None):
        self.item = row.loc['OBV']
        self.exitba = entryTechValue['OBV']['HIGH']
        if (float(self.item) > float(self.exitba)):
            return True
        else:
            return False
