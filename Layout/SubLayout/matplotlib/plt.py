import matplotlib.pyplot as plt
import mplfinance as mpf
import talib
from Global.Value.TechToolParam import TechValue
from Layout.Method_Class.logger import Logger
plt.rcParams['font.size'] = 10


class matplotlib_Canvas():
    def __init__(self, sybmol, data):
        Logger().info('Drawing Photo in Core ')
        # super().__init__()
        self.data = data
        self.sybmol = sybmol
        self.addplot = []
        self.addplotitem()
        self.plot_chart()

    def plot_chart(self):
        mpf.plot(self.data, type='candle', style=self.style(), addplot=self.addplot, volume=True,
                 scale_width_adjustment=dict(volume=0.5, candle=1.15, lines=0.65), xrotation=15, figsize=(12, 8))

    def style(self):
        self.color = mpf.make_marketcolors(
            up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in')
        self.myrcparams = {'xtick.labelsize': 8,
                           'ytick.labelsize': 8, 'axes.labelsize': 8}
        self.mpf_style = mpf.make_mpf_style(marketcolors=self.color, rc=self.myrcparams)
        return self.mpf_style

    def plotitemgroup(self):
        self.paramlist = self.getterTechValue()
        self.paramlistkey = list(self.paramlist.keys())
        self.overlap = []
        self.momentum = []
        self.cycle = []
        self.volatility = []
        self.volume = []
        self.fung = talib.get_function_groups()
        for self.param in self.paramlistkey:
            if (self.param == 'SAREXT' or self.param == 'KDJ'):
                self.momentum.append(self.param)
            elif (self.param in self.fung['Overlap Studies']):
                self.overlap.append(self.param)
            elif (self.param in self.fung['Momentum Indicators']):
                self.momentum.append(self.param)
            elif (self.param in self.fung['Cycle Indicators']):
                self.cycle.append(self.param)
            elif (self.param in self.fung['Volatility Indicators']):
                self.volatility.append(self.param)
            elif (self.param in self.fung['Volume Indicators']):
                self.volume.append(self.param)
        return self.overlap, self.momentum, self.cycle, self.volatility, self.volume

    def checkNanColumn(self, column):
        if self.data[column].isna().all():
            return False
        else:
            return True

    def addplotitem(self):
        # self.paramlist = self.getterTechValue()
        # self.paramlistkey = list(self.paramlist.keys())
        # self.paramlistkey.insert(0, 'volume')
        self.overlap, self.momentum, self.cycle, self.volatility, self.volume = self.plotitemgroup()
        self.merged_list = self.momentum + self.cycle + self.volatility + self.volume
        self.merged_list.insert(0, 'VOLUME')
        # subtract 1 for volume plot
        for i, self.param in enumerate(self.merged_list):
            if (self.param == 'VOLUME'):
                pass
            elif (self.param == 'HT_DCPERIOD'):
                self.add_ht_dcperiod(i)
            elif (self.param == 'HT_DCPHASE'):
                self.add_ht_dchase(i)
            elif (self.param == 'HT_PHASOR'):
                self.add_ht_phasor(i)
            elif (self.param == 'HT_SINE'):
                self.add_ht_sine(i)
            elif (self.param == 'HT_TRENDMODE'):
                self.add_ht_trendmode(i)
            elif (self.param == 'RSI'):
                self.add_rsi(i)
            elif (self.param == 'MACD'):
                self.add_macd(i)
            elif (self.param == 'ADX'):
                self.add_adx(i)
            elif (self.param == 'ADXR'):
                self.add_adxr(i)
            elif (self.param == 'APO'):
                self.add_apo(i)
            elif (self.param == 'AROON'):
                self.add_aroon(i)
            elif (self.param == 'AROONOSC'):
                self.add_aroonosc(i)
            elif (self.param == 'BOP'):
                self.add_bop(i)
            elif (self.param == 'CCI'):
                self.add_cci(i)
            elif (self.param == 'CMO'):
                self.add_cmo(i)
            elif (self.param == 'DX'):
                self.add_dx(i)
            elif (self.param == 'MACDEXT'):
                self.add_macdext(i)
            elif (self.param == 'MACDFIX'):
                self.add_macdfix(i)
            elif (self.param == 'MFI'):
                self.add_mfi(i)
            elif (self.param == 'MINUS_DI'):
                self.add_minus_di(i)
            elif (self.param == 'MINUS_DM'):
                self.add_minus_dm(i)
            elif (self.param == 'MOM'):
                self.add_mom(i)
            elif (self.param == 'PLUS_DI'):
                self.add_plus_di(i)
            elif (self.param == 'PLUS_DM'):
                self.add_plus_dm(i)
            elif (self.param == 'PPO'):
                self.add_ppo(i)
            elif (self.param == 'ROC'):
                self.add_roc(i)
            elif (self.param == 'ROCP'):
                self.add_rocp(i)
            elif (self.param == 'ROCR'):
                self.add_rocr(i)
            elif (self.param == 'ROCR100'):
                self.add_rocr100(i)
            elif (self.param == 'STOCH'):
                self.add_stoch(i)
            elif (self.param == 'STOCHF'):
                self.add_stochf(i)
            elif (self.param == 'STOCHRSI'):
                self.add_stochrsi(i)
            elif (self.param == 'TRIX'):
                self.add_trix(i)
            elif (self.param == 'ULTOSC'):
                self.add_ultosc(i)
            elif (self.param == 'WILLR'):
                self.add_willr(i)
            elif (self.param == 'SAREXT'):
                self.add_sarext(i)
            elif (self.param == 'KDJ'):
                self.add_kdj(i)
            elif (self.param == 'ATR'):
                self.add_atr(i)
            elif (self.param == 'NATR'):
                self.add_natr(i)
            elif (self.param == 'TRANGE'):
                self.add_trange(i)
            elif (self.param == 'AD'):
                self.add_ad(i)
            elif (self.param == 'ADOSC'):
                self.add_adosc(i)
            elif (self.param == 'OBV'):
                self.add_obv(i)
        for self.param in self.overlap:
            if (self.param == 'BBANDS'):
                self.add_bbands()
            elif (self.param == 'DEMA'):
                self.add_dema()
            elif (self.param == 'EMA'):
                self.add_ema()
            elif (self.param == 'HT_TRENDLINE'):
                self.add_ht_trendline()
            elif (self.param == 'KAMA'):
                self.add_kama()
            elif (self.param == 'MA'):
                self.add_ma()
            elif (self.param == 'MAMA'):
                self.add_mama()
            elif (self.param == 'MIDPOINT'):
                self.add_midpoint()
            elif (self.param == 'MIDPRICE'):
                self.add_midprice()
            elif (self.param == 'SAR'):
                self.add_sar()
            elif (self.param == 'SMA'):
                self.add_sma()
            elif (self.param == 'T3'):
                self.add_t3()
            elif (self.param == 'TEMA'):
                self.add_tema()
            elif (self.param == 'TRIMA'):
                self.add_trima()
            elif (self.param == 'WMA'):
                self.add_wma()

    def add_ht_dcperiod(self, i):
        self.data['HT_DCPERIOD'] = self.data['HT_DCPERIOD'].fillna(
            method='ffill')
        if (self.checkNanColumn('HT_DCPERIOD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_DCPERIOD'], panel=i+1, ylabel='HT_DCPERIOD', color='red', width=0.6))

    def add_ht_dchase(self, i):
        self.data['HT_DCPHASE'] = self.data['HT_DCPHASE'].fillna(
            method='ffill')
        if (self.checkNanColumn('HT_DCPHASE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_DCPHASE'], panel=i+1, ylabel='HT_DCPHASE', color='red', width=0.6))

    def add_ht_phasor(self, i):
        self.data['HT_PHASOR_INHPASE'] = self.data['HT_PHASOR_INHPASE'].fillna(
            method='ffill')
        self.data['HT_PHASOR_QUADRATURE'] = self.data['HT_PHASOR_QUADRATURE'].fillna(
            method='ffill')
        if (self.checkNanColumn('HT_PHASOR_INHPASE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_PHASOR_INHPASE'], panel=i+1, ylabel='HT_PHASOR', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('HT_PHASOR_QUADRATURE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_PHASOR_QUADRATURE'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_ht_sine(self, i):
        self.data['SINE'] = self.data['SINE'].fillna(
            method='ffill')
        self.data['LEADSINE'] = self.data['LEADSINE'].fillna(
            method='ffill')
        if (self.checkNanColumn('SINE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SINE'], panel=i+1, ylabel='HT_SINE', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('LEADSINE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['LEADSINE'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_ht_trendmode(self, i):
        self.data['HT_TRENDMODE'] = self.data['HT_TRENDMODE'].fillna(
            method='ffill')
        if (self.checkNanColumn('HT_TRENDMODE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_TRENDMODE'], panel=i+1, ylabel='HT_TRENDMODE', color='red', width=0.6))

    def add_adx(self, i):
        self.data['ADX'] = self.data['ADX'].fillna(
            method='ffill')
        if (self.checkNanColumn('ADX') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ADX'], panel=i+1, ylabel='ADX', color='red', width=0.6))

    def add_adxr(self, i):
        self.data['ADXR'] = self.data['ADXR'].fillna(
            method='ffill')
        if (self.checkNanColumn('ADXR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ADXR'], panel=i+1, ylabel='ADXR', color='red', width=0.6))

    def add_apo(self, i):
        self.data['APO'] = self.data['APO'].fillna(
            method='ffill')
        if (self.checkNanColumn('APO') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['APO'], panel=i+1, ylabel='APO', color='red', width=0.6))

    def add_aroon(self, i):
        self.data['AROON_UP'] = self.data['AROON_UP'].fillna(
            method='ffill')
        self.data['AROON_DOWN'] = self.data['AROON_DOWN'].fillna(
            method='ffill')

        if (self.checkNanColumn('AROON_UP') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['AROON_UP'], panel=i+1, ylabel='AROON', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('AROON_DOWN') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['AROON_DOWN'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_aroonosc(self, i):
        self.data['AROONOSC'] = self.data['AROONOSC'].fillna(
            method='ffill')
        if (self.checkNanColumn('AROONOSC') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['AROONOSC'], panel=i+1, ylabel='AROONOSC', color='red', width=0.6))

    def add_bop(self, i):
        self.data['BOP'] = self.data['BOP'].fillna(
            method='ffill')
        if (self.checkNanColumn('BOP') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['BOP'], panel=i+1, ylabel='BOP', color='red', width=0.6))

    def add_cci(self, i):
        self.data['CCI'] = self.data['CCI'].fillna(
            method='ffill')
        if (self.checkNanColumn('CCI') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['CCI'], panel=i+1, ylabel='CCI', color='red', width=0.6))

    def add_cmo(self, i):
        self.data['CMO'] = self.data['CMO'].fillna(
            method='ffill')
        if (self.checkNanColumn('CMO') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['CMO'], panel=i+1, ylabel='CMO', color='red', width=0.6))

    def add_dx(self, i):
        self.data['DX'] = self.data['DX'].fillna(
            method='ffill')
        if (self.checkNanColumn('DX') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DX'], panel=i+1, ylabel='DX', color='red', width=0.6))

    def add_macd(self, i):
        self.data['MACD'] = self.data['MACD'].fillna(
            method='ffill')
        self.data['MACD_SIGNAL'] = self.data['MACD_SIGNAL'].fillna(
            method='ffill')
        self.data['MACD_HIST'] = self.data['MACD_HIST'].fillna(
            method='ffill')
        # 創建 MACD 指標
        positive_color = 'g'
        negative_color = 'r'
        colors = [positive_color if x >=
                  0 else negative_color for x in self.data['MACD_HIST']]
        if (self.checkNanColumn('MACD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACD'], panel=i+1, ylabel='MACD', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('MACD_SIGNAL') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACD_SIGNAL'], panel=i+1, color='red', width=0.6, secondary_y=False))
        if (self.checkNanColumn('MACD_HIST') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACD_HIST'], type='bar', width=0.6, panel=i+1, color=colors, secondary_y=False))

    def add_macdext(self, i):
        self.data['MACDEXT'] = self.data['MACDEXT'].fillna(
            method='ffill')
        self.data['MACDEXT_SIGNAL'] = self.data['MACDEXT_SIGNAL'].fillna(
            method='ffill')
        self.data['MACDEXT_HIST'] = self.data['MACDEXT_HIST'].fillna(
            method='ffill')
        # 創建 MACD 指標
        positive_color = 'g'
        negative_color = 'r'
        colors = [positive_color if x >=
                  0 else negative_color for x in self.data['MACDEXT_HIST']]
        if (self.checkNanColumn('MACDEXT') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDEXT'], panel=i+1, ylabel='MACDEXT', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('MACDEXT_SIGNAL') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDEXT_SIGNAL'], panel=i+1, color='red', width=0.6, secondary_y=False))
        if (self.checkNanColumn('MACDEXT_HIST') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDEXT_HIST'], type='bar', width=0.6, panel=i+1, color=colors, secondary_y=False))

    def add_macdfix(self, i):
        self.data['MACDFIX'] = self.data['MACDFIX'].fillna(
            method='ffill')
        self.data['MACDFIX_SIGNAL'] = self.data['MACDFIX_SIGNAL'].fillna(
            method='ffill')
        self.data['MACDFIX_HIST'] = self.data['MACDFIX_HIST'].fillna(
            method='ffill')
        # 創建 MACD 指標
        positive_color = 'g'
        negative_color = 'r'
        colors = [positive_color if x >=
                  0 else negative_color for x in self.data['MACDFIX_HIST']]
        if (self.checkNanColumn('MACDFIX') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDFIX'], panel=i+1, ylabel='MACDFIX', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('MACDFIX_SIGNAL') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDFIX_SIGNAL'], panel=i+1, color='red', width=0.6, secondary_y=False))
        if (self.checkNanColumn('MACDFIX_HIST') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MACDFIX_HIST'], type='bar', width=0.6, panel=i+1, color=colors, secondary_y=False))

    def add_mfi(self, i):
        self.data['MFI'] = self.data['MFI'].fillna(
            method='ffill')
        if (self.checkNanColumn('MFI') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MFI'], panel=i+1, ylabel='MFI', color='red', width=0.6))

    def add_minus_di(self, i):
        self.data['MINUS_DI'] = self.data['MINUS_DI'].fillna(
            method='ffill')
        if (self.checkNanColumn('MINUS_DI') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MINUS_DI'], panel=i+1, ylabel='MINUS_DI', color='red', width=0.6))

    def add_minus_dm(self, i):
        self.data['MINUS_DM'] = self.data['MINUS_DM'].fillna(
            method='ffill')
        if (self.checkNanColumn('MINUS_DM') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MINUS_DM'], panel=i+1, ylabel='MINUS_DM', color='red', width=0.6))

    def add_mom(self, i):
        self.data['MOM'] = self.data['MOM'].fillna(
            method='ffill')
        if (self.checkNanColumn('MOM') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MOM'], panel=i+1, ylabel='MOM', color='red', width=0.6))

    def add_rsi(self, i):
        self.data['RSI'] = self.data['RSI'].fillna(
            method='ffill')
        if (self.checkNanColumn('RSI') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['RSI'], panel=i+1, ylabel='RSI', ylim=(0, 100), color='red', width=0.6))

    def add_plus_di(self, i):
        self.data['PLUS_DI'] = self.data['PLUS_DI'].fillna(
            method='ffill')
        if (self.checkNanColumn('PLUS_DI') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['PLUS_DI'], panel=i+1, ylabel='PLUS_DI', color='red', width=0.6))

    def add_plus_dm(self, i):
        self.data['PLUS_DM'] = self.data['PLUS_DM'].fillna(
            method='ffill')
        if (self.checkNanColumn('PLUS_DM') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['PLUS_DM'], panel=i+1, ylabel='PLUS_DM', color='red', width=0.6))

    def add_ppo(self, i):
        self.data['PPO'] = self.data['PPO'].fillna(
            method='ffill')
        if (self.checkNanColumn('PPO') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['PPO'], panel=i+1, ylabel='PPO', color='red', width=0.6))

    def add_roc(self, i):
        self.data['ROC'] = self.data['ROC'].fillna(
            method='ffill')
        if (self.checkNanColumn('ROC') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ROC'], panel=i+1, ylabel='ROC', color='red', width=0.6))

    def add_rocp(self, i):
        self.data['ROCP'] = self.data['ROCP'].fillna(
            method='ffill')
        if (self.checkNanColumn('ROCP') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ROCP'], panel=i+1, ylabel='ROCP', color='red', width=0.6))

    def add_rocr(self, i):
        self.data['ROCR'] = self.data['ROCR'].fillna(
            method='ffill')
        if (self.checkNanColumn('ROCR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ROCR'], panel=i+1, ylabel='ROCR', color='red', width=0.6))

    def add_rocr100(self, i):
        self.data['ROCR100'] = self.data['ROCR100'].fillna(
            method='ffill')
        if (self.checkNanColumn('ROCR100') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ROCR100'], panel=i+1, ylabel='ROCR100', color='red', width=0.6))

    def add_stoch(self, i):
        self.data['STOCH_SLOWK'] = self.data['STOCH_SLOWK'].fillna(
            method='ffill')
        self.data['STOCH_SLOWD'] = self.data['STOCH_SLOWD'].fillna(
            method='ffill')
        if (self.checkNanColumn('STOCH_SLOWK') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCH_SLOWK'], panel=i+1, ylabel='STOCH', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('STOCH_SLOWD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCH_SLOWD'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_stochf(self, i):
        self.data['STOCHF_FASTK'] = self.data['STOCHF_FASTK'].fillna(
            method='ffill')
        self.data['STOCHF_FASTD'] = self.data['STOCHF_FASTD'].fillna(
            method='ffill')
        if (self.checkNanColumn('STOCHF_FASTK') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCHF_FASTK'], panel=i+1, ylabel='STOCHF', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('STOCHF_FASTD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCHF_FASTD'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_stochrsi(self, i):
        self.data['STOCHRSI_SLOWK'] = self.data['STOCHRSI_SLOWK'].fillna(
            method='ffill')
        self.data['STOCHRSI_SLOWD'] = self.data['STOCHRSI_SLOWD'].fillna(
            method='ffill')
        if (self.checkNanColumn('STOCHRSI_SLOWK') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCHRSI_SLOWK'], panel=i+1, ylabel='STOCHRSI', width=0.6, color='yellow', secondary_y=False))
        if (self.checkNanColumn('STOCHRSI_SLOWD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['STOCHRSI_SLOWD'], panel=i+1, color='red', width=0.6, secondary_y=False))

    def add_trix(self, i):
        self.data['TRIX'] = self.data['TRIX'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIX') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIX'], panel=i+1, ylabel='TRIX', color='red', width=0.6))

    def add_ultosc(self, i):
        self.data['ULTOSC'] = self.data['ULTOSC'].fillna(
            method='ffill')
        if (self.checkNanColumn('ULTOSC') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ULTOSC'], panel=i+1, ylabel='ULTOSC', color='red', width=0.6))

    def add_willr(self, i):
        self.data['WILLR'] = self.data['WILLR'].fillna(
            method='ffill')
        if (self.checkNanColumn('WILLR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WILLR'], panel=i+1, ylabel='WILLR', color='red', width=0.6))

    def add_kdj(self, i):
        self.data['KDJ_SLOWK'] = self.data['KDJ_SLOWK'].fillna(
            method='ffill')
        self.data['KDJ_SLOWD'] = self.data['KDJ_SLOWD'].fillna(
            method='ffill')
        self.data['KDJ_SLOWJ'] = self.data['KDJ_SLOWJ'].fillna(
            method='ffill')
        # 創建 KDJ 指標
        if (self.checkNanColumn('KDJ_SLOWK') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KDJ_SLOWK'], panel=i+1, ylabel='KDJ', width=0.6, color='#C4B400', secondary_y=False))
        if (self.checkNanColumn('KDJ_SLOWD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KDJ_SLOWD'], panel=i+1, color='#3D9CC4', width=0.6, secondary_y=False))
        if (self.checkNanColumn('KDJ_SLOWJ') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KDJ_SLOWJ'], panel=i+1, color='#16C444', width=0.6, secondary_y=False))

    def add_bbands(self):
        self.data['BBANDS_UPPERBAND'] = self.data['BBANDS_UPPERBAND'].fillna(
            method='ffill')
        self.data['BBANDS_MIDDLEBAND'] = self.data['BBANDS_MIDDLEBAND'].fillna(
            method='ffill')
        self.data['BBANDS_LOWERBAND'] = self.data['BBANDS_LOWERBAND'].fillna(
            method='ffill')
        # 創建 bbands 指標
        if (self.checkNanColumn('BBANDS_UPPERBAND') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['BBANDS_UPPERBAND'], width=0.6, color='r', secondary_y=False))
        if (self.checkNanColumn('BBANDS_MIDDLEBAND') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['BBANDS_MIDDLEBAND'], color='y', width=0.6, secondary_y=False))
        if (self.checkNanColumn('BBANDS_LOWERBAND') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['BBANDS_LOWERBAND'], width=0.6, color='g', secondary_y=False))

    def add_dema(self):
        self.data['DEMA_parameter_1'] = self.data['DEMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('DEMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DEMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['DEMA_parameter_2'] = self.data['DEMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('DEMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DEMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['DEMA_parameter_3'] = self.data['DEMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('DEMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DEMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['DEMA_parameter_4'] = self.data['DEMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('DEMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DEMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['DEMA_parameter_5'] = self.data['DEMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('DEMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['DEMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_ema(self):
        self.data['EMA_parameter_1'] = self.data['EMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('EMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['EMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['EMA_parameter_2'] = self.data['EMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('EMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['EMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['EMA_parameter_3'] = self.data['EMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('EMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['EMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['EMA_parameter_4'] = self.data['EMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('EMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['EMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['EMA_parameter_5'] = self.data['EMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('EMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['EMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_ht_trendline(self):
        self.data['HT_TRENDLINE'] = self.data['HT_TRENDLINE'].fillna(
            method='ffill')
        if (self.checkNanColumn('HT_TRENDLINE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['HT_TRENDLINE'], color='#AE00AE', width=0.6, secondary_y=False))

    def add_kama(self):
        self.data['KAMA_parameter_1'] = self.data['KAMA_parameter_1'].fillna(
            method='ffill')

        if (self.checkNanColumn('KAMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KAMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['KAMA_parameter_2'] = self.data['KAMA_parameter_2'].fillna(
            method='ffill')

        if (self.checkNanColumn('KAMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KAMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['KAMA_parameter_3'] = self.data['KAMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('KAMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KAMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['KAMA_parameter_4'] = self.data['KAMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('KAMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KAMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['KAMA_parameter_5'] = self.data['KAMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('KAMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['KAMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_ma(self):
        self.data['MA'] = self.data['MA'].fillna(
            method='ffill')
        if (self.checkNanColumn('MA') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MA'], color='#006000', width=0.6, secondary_y=False))

    def add_mama(self):
        self.data['MAMA'] = self.data['MAMA'].fillna(
            method='ffill')
        self.data['MAMA_FAMA'] = self.data['MAMA_FAMA'].fillna(
            method='ffill')
        # 創建 mama 指標
        if (self.checkNanColumn('MAMA') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MAMA'], width=0.6, color='#613030', secondary_y=False))
        if (self.checkNanColumn('MAMA_FAMA') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MAMA_FAMA'], color='#336666', width=0.6, secondary_y=False))

    def add_midpoint(self):
        self.data['MIDPOINT'] = self.data['MIDPOINT'].fillna(
            method='ffill')
        if (self.checkNanColumn('MIDPOINT') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MIDPOINT'], color='#484891', width=0.6, secondary_y=False))

    def add_midprice(self):
        self.data['MIDPRICE'] = self.data['MIDPRICE'].fillna(
            method='ffill')
        if (self.checkNanColumn('MIDPRICE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['MIDPRICE'], color='#642100', width=0.6, secondary_y=False))

    def add_sar(self):
        self.data['SAR'] = self.data['SAR'].fillna(
            method='ffill')
        if (self.checkNanColumn('SAR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SAR'], color='#844200', width=0.6, secondary_y=False))

    def add_sarext(self, i):
        self.data['SAREXT'] = self.data['SAREXT'].fillna(
            method='ffill')
        if (self.checkNanColumn('SAREXT') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SAREXT'], panel=i+1, ylabel='SAREXT', color='#424200', width=0.6))

    def add_sma(self):
        self.data['SMA_parameter_1'] = self.data['SMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('SMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['SMA_parameter_2'] = self.data['SMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('SMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['SMA_parameter_3'] = self.data['SMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('SMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['SMA_parameter_4'] = self.data['SMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('SMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['SMA_parameter_5'] = self.data['SMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('SMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['SMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_t3(self):
        self.data['T3_parameter_1'] = self.data['T3_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('T3_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['T3_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['T3_parameter_2'] = self.data['T3_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('T3_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['T3_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['T3_parameter_3'] = self.data['T3_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('T3_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['T3_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['T3_parameter_4'] = self.data['T3_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('T3_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['T3_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['T3_parameter_5'] = self.data['T3_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('T3_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['T3_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_tema(self):
        self.data['TEMA_parameter_1'] = self.data['TEMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('TEMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TEMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['TEMA_parameter_2'] = self.data['TEMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('TEMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TEMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['TEMA_parameter_3'] = self.data['TEMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('TEMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TEMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['TEMA_parameter_4'] = self.data['TEMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('TEMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TEMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['TEMA_parameter_5'] = self.data['TEMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('TEMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TEMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_trima(self):
        self.data['TRIMA_parameter_1'] = self.data['TRIMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['TRIMA_parameter_2'] = self.data['TRIMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['TRIMA_parameter_3'] = self.data['TRIMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['TRIMA_parameter_4'] = self.data['TRIMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['TRIMA_parameter_5'] = self.data['TRIMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRIMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRIMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_wma(self):
        self.data['WMA_parameter_1'] = self.data['WMA_parameter_1'].fillna(
            method='ffill')
        if (self.checkNanColumn('WMA_parameter_1') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WMA_parameter_1'], color='#C4B700', width=0.6, secondary_y=False))

        self.data['WMA_parameter_2'] = self.data['WMA_parameter_2'].fillna(
            method='ffill')
        if (self.checkNanColumn('WMA_parameter_2') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WMA_parameter_2'], color='#C41C10', width=0.6, secondary_y=False))

        self.data['WMA_parameter_3'] = self.data['WMA_parameter_3'].fillna(
            method='ffill')
        if (self.checkNanColumn('WMA_parameter_3') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WMA_parameter_3'], color='#C43988', width=0.6, secondary_y=False))

        self.data['WMA_parameter_4'] = self.data['WMA_parameter_4'].fillna(
            method='ffill')
        if (self.checkNanColumn('WMA_parameter_4') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WMA_parameter_4'], color='#533FC4', width=0.6, secondary_y=False))

        self.data['WMA_parameter_5'] = self.data['WMA_parameter_5'].fillna(
            method='ffill')
        if (self.checkNanColumn('WMA_parameter_5') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['WMA_parameter_5'], color='#3D9CC4', width=0.6, secondary_y=False))

    def add_atr(self, i):
        self.data['ATR'] = self.data['ATR'].fillna(
            method='ffill')
        if (self.checkNanColumn('ATR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ATR'], panel=i+1, color='r', width=0.6, ylabel='ATR'))

    def add_natr(self, i):
        self.data['NATR'] = self.data['NATR'].fillna(
            method='ffill')
        if (self.checkNanColumn('NATR') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['NATR'], panel=i+1, color='r', width=0.6, ylabel='NATR'))

    def add_trange(self, i):
        self.data['TRANGE'] = self.data['TRANGE'].fillna(
            method='ffill')
        if (self.checkNanColumn('TRANGE') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['TRANGE'], panel=i+1, color='r', width=0.6, ylabel='TRANGE'))

    def add_ad(self, i):
        self.data['AD'] = self.data['AD'].fillna(
            method='ffill')
        if (self.checkNanColumn('AD') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['AD'], panel=i+1, color='r', width=0.6, ylabel='AD'))

    def add_adosc(self, i):
        self.data['ADOSC'] = self.data['ADOSC'].fillna(
            method='ffill')
        if (self.checkNanColumn('ADOSC') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['ADOSC'], panel=i+1, color='r', width=0.6, ylabel='ADOSC'))

    def add_obv(self, i):
        self.data['OBV'] = self.data['OBV'].fillna(
            method='ffill')
        if (self.checkNanColumn('OBV') == True):
            self.addplot.append(mpf.make_addplot(
                self.data['OBV'], panel=i+1, color='r', width=0.6, ylabel='OBV'))

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()
