import talib
from Layout.SubLayout.Ta.lib.Momentum.adx import adx
from Layout.SubLayout.Ta.lib.Momentum.adxr import adxr
from Layout.SubLayout.Ta.lib.Momentum.apo import apo
from Layout.SubLayout.Ta.lib.Momentum.aroon import aroon
from Layout.SubLayout.Ta.lib.Momentum.aroonosc import aroonosc
from Layout.SubLayout.Ta.lib.Momentum.bop import bop
from Layout.SubLayout.Ta.lib.Momentum.cci import cci
from Layout.SubLayout.Ta.lib.Momentum.cmo import cmo
from Layout.SubLayout.Ta.lib.Momentum.dx import dx
from Layout.SubLayout.Ta.lib.Momentum.rsi import rsi
from Layout.SubLayout.Ta.lib.Momentum.macd import macd
from Layout.SubLayout.Ta.lib.Momentum.macdext import macdext
from Layout.SubLayout.Ta.lib.Momentum.macdfix import macdfix
from Layout.SubLayout.Ta.lib.Momentum.mfi import mfi
from Layout.SubLayout.Ta.lib.Momentum.minus_di import minusdi
from Layout.SubLayout.Ta.lib.Momentum.minus_dm import minusdm
from Layout.SubLayout.Ta.lib.Momentum.mom import mom
from Layout.SubLayout.Ta.lib.Momentum.plus_di import plusdi
from Layout.SubLayout.Ta.lib.Momentum.plus_dm import plusdm
from Layout.SubLayout.Ta.lib.Momentum.ppo import ppo
from Layout.SubLayout.Ta.lib.Momentum.roc import roc
from Layout.SubLayout.Ta.lib.Momentum.rocp import rocp
from Layout.SubLayout.Ta.lib.Momentum.rocr import rocr
from Layout.SubLayout.Ta.lib.Momentum.rocr100 import rocr100
from Layout.SubLayout.Ta.lib.Momentum.stoch import stoch
from Layout.SubLayout.Ta.lib.Momentum.stochf import stochf
from Layout.SubLayout.Ta.lib.Momentum.stochrsi import stochrsi
from Layout.SubLayout.Ta.lib.Momentum.trix import trix
from Layout.SubLayout.Ta.lib.Momentum.ultosc import ultosc
from Layout.SubLayout.Ta.lib.Momentum.willr import willr
from Layout.SubLayout.Ta.lib.Momentum.kdj import kdj
from Layout.SubLayout.Ta.lib.Cycle.ht_dcperiod import ht_dcperiod
from Layout.SubLayout.Ta.lib.Cycle.ht_dcphase import ht_dcphase
from Layout.SubLayout.Ta.lib.Cycle.ht_phasor import ht_phasor
from Layout.SubLayout.Ta.lib.Cycle.ht_sine import ht_sine
from Layout.SubLayout.Ta.lib.Cycle.ht_trendmode import ht_trendmode
from Layout.SubLayout.Ta.lib.Overlap_Studies.bbands import bbands
from Layout.SubLayout.Ta.lib.Overlap_Studies.dema import dema
from Layout.SubLayout.Ta.lib.Overlap_Studies.mavp import mavp
from Layout.SubLayout.Ta.lib.Overlap_Studies.sarext import sarext
from Layout.SubLayout.Ta.lib.Overlap_Studies.ema import ema
from Layout.SubLayout.Ta.lib.Overlap_Studies.ht_trendline import ht_trendline
from Layout.SubLayout.Ta.lib.Overlap_Studies.kama import kama
from Layout.SubLayout.Ta.lib.Overlap_Studies.ma import ma
from Layout.SubLayout.Ta.lib.Overlap_Studies.mama import mama
from Layout.SubLayout.Ta.lib.Overlap_Studies.midpoint import midpoint
from Layout.SubLayout.Ta.lib.Overlap_Studies.midprice import midprice
from Layout.SubLayout.Ta.lib.Overlap_Studies.sar import sar
from Layout.SubLayout.Ta.lib.Overlap_Studies.sarext import sarext
from Layout.SubLayout.Ta.lib.Overlap_Studies.sma import sma
from Layout.SubLayout.Ta.lib.Overlap_Studies.t3 import t3
from Layout.SubLayout.Ta.lib.Overlap_Studies.tema import tema
from Layout.SubLayout.Ta.lib.Overlap_Studies.trima import trima
from Layout.SubLayout.Ta.lib.Overlap_Studies.wma import wma
from Layout.SubLayout.Ta.lib.Volatility_Indicator.atr import atr
from Layout.SubLayout.Ta.lib.Volatility_Indicator.natr import natr
from Layout.SubLayout.Ta.lib.Volatility_Indicator.trange import trange
from Layout.SubLayout.Ta.lib.Volume_Indicator.ad import ad
from Layout.SubLayout.Ta.lib.Volume_Indicator.adosc import adosc
from Layout.SubLayout.Ta.lib.Volume_Indicator.obv import obv
from Layout.SubLayout.matplotlib.plt import matplotlib_Canvas
from Global.Value.UniversalValue import GlobalValue
from Global.Value.TechToolParam import TechValue


class talib_list():
    def __init__(self):
        super().__init__()

    def takeparam(self, data, text):
        if text in data:
            self.param = data[text]
            print(self.param)
            return self.param
        else:
            print(f"Error: {text} is not a valid key in data.")
            return None

    def all_functions(self):
        list = talib.get_functions()
        return list

    def all_funtionsgroupkey(self):
        lists = talib.get_function_groups()
        keys_list = [""] + list(lists.keys())
        return keys_list

    def all_funtion(self):
        list = talib.get_function_groups()
        return list

    def allgroup_subfunction(self, text):
        lists = self.all_funtion()
        list = lists[text]
        return list

    """Cycle Indicators"""
    """HT_DCPERIOD"""

    def ht_dcperiod(self):
        return ht_dcperiod()

    def ht_dcperiodgroup(self):
        self.widget = ht_dcperiod()
        layout = self.widget.widgetedit()
        return layout

    def ht_dcperiodbase(self):
        return ht_dcperiod().base()

    def ht_dcperiodcalculate(self):
        self.value = ht_dcperiod()
        self.value.calculate()

    def ht_dcperiodentry_exit_base(self):
        return ht_dcperiod().entry_exit_base()

    def ht_dcperiodcheckentry(self, testitemrow):
        self.value = ht_dcperiod()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_dcperiodcheckexit(self, testitem):
        self.value = ht_dcperiod()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_dcperiodentry(self):
        self.value = ht_dcperiod()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_DCPERIOD"""
    """HT_DCPHASE"""

    def ht_dchase(self):
        return ht_dcphase()

    def ht_dchasegroup(self):
        self.widget = ht_dcphase()
        layout = self.widget.widgetedit()
        return layout

    def ht_dchasebase(self):
        return ht_dcphase().base()

    def ht_dchasecalculate(self):
        self.value = ht_dcphase()
        self.value.calculate()

    def ht_dchaseentry_exit_base(self):
        return ht_dcphase().entry_exit_base()

    def ht_dchasecheckentry(self, testitemrow):
        self.value = ht_dcphase()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_dchasecheckexit(self, testitem):
        self.value = ht_dcphase()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_dchaseentry(self):
        self.value = ht_dcphase()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_DCPERIOD"""
    """HT_PHASOR"""

    def ht_phasor(self):
        return ht_phasor()

    def ht_phasorgroup(self):
        self.widget = ht_phasor()
        layout = self.widget.widgetedit()
        return layout

    def ht_phasorbase(self):
        return ht_phasor().base()

    def ht_phasorcalculate(self):
        self.value = ht_phasor()
        self.value.calculate()

    def ht_phasorentry_exit_base(self):
        return ht_phasor().entry_exit_base()

    def ht_phasorcheckentry(self, testitemrow):
        self.value = ht_phasor()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_phasorcheckexit(self, testitem):
        self.value = ht_phasor()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_phasorentry(self):
        self.value = ht_phasor()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_PHASOR"""

    """HT_SINE"""

    def ht_sine(self):
        return ht_sine()

    def ht_sinegroup(self):
        self.widget = ht_sine()
        layout = self.widget.widgetedit()
        return layout

    def ht_sinebase(self):
        return ht_sine().base()

    def ht_sinecalculate(self):
        self.value = ht_sine()
        self.value.calculate()

    def ht_sineentry_exit_base(self):
        return ht_sine().entry_exit_base()

    def ht_sinecheckentry(self, testitemrow):
        self.value = ht_sine()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_sinecheckexit(self, testitem):
        self.value = ht_sine()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_sineentry(self):
        self.value = ht_sine()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_SINE"""
    """HT_TRENDMODE"""

    def ht_trendmode(self):
        return ht_trendmode()

    def ht_trendmodegroup(self):
        self.widget = ht_trendmode()
        layout = self.widget.widgetedit()
        return layout

    def ht_trendmodebase(self):
        return ht_trendmode().base()

    def ht_trendmodecalculate(self):
        self.value = ht_trendmode()
        self.value.calculate()

    def ht_trendmodeentry_exit_base(self):
        return ht_trendmode().entry_exit_base()

    def ht_trendmodecheckentry(self, testitemrow):
        self.value = ht_trendmode()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_trendmodecheckexit(self, testitem):
        self.value = ht_trendmode()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_trendmodeentry(self):
        self.value = ht_trendmode()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_TRENDMODE"""
    """Cycle Indicators"""

    """Momentum  cle Indicators"""

    """ADX"""

    def adx(self):
        return adx()

    def adxgroup(self):
        self.widget = adx()
        layout = self.widget.widgetedit()
        return layout

    def adxbase(self):
        return adx().base()

    def adxcalculate(self):
        self.value = adx()
        self.value.calculate()

    def adxentry_exit_base(self):
        return adx().entry_exit_base()

    def adxcheckentry(self, testitemrow):
        self.value = adx()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def adxcheckexit(self, testitem):
        self.value = adx()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def adxentry(self):
        self.value = adx()
        layout = self.value.entrywidgetedit()
        return layout
    """ADX"""
    """ADXR"""

    def adxr(self):
        return adxr()

    def adxrgroup(self):
        self.widget = adxr()
        layout = self.widget.widgetedit()
        return layout

    def adxrbase(self):
        return adxr().base()

    def adxrcalculate(self):
        self.value = adxr()
        self.value.calculate()

    def adxrentry_exit_base(self):
        return adxr().entry_exit_base()

    def adxrcheckentry(self, testitemrow):
        self.value = adxr()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def adxrcheckexit(self, testitem):
        self.value = adxr()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def adxrentry(self):
        self.value = adxr()
        layout = self.value.entrywidgetedit()
        return layout
    """ADXR"""
    """APO"""

    def apo(self):
        return apo()

    def apogroup(self):
        self.widget = apo()
        layout = self.widget.widgetedit()
        return layout

    def apobase(self):
        return apo().base()

    def apocalculate(self):
        self.value = apo()
        self.value.calculate()

    def apoentry_exit_base(self):
        return apo().entry_exit_base()

    def apocheckentry(self, testitemrow):
        self.value = apo()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def apocheckexit(self, testitem):
        self.value = apo()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def apoentry(self):
        self.value = apo()
        layout = self.value.entrywidgetedit()
        return layout
    """APO"""
    """AROON"""

    def aroon(self):
        return aroon()

    def aroongroup(self):
        self.widget = aroon()
        layout = self.widget.widgetedit()
        return layout

    def aroonbase(self):
        return aroon().base()

    def arooncalculate(self):
        self.value = aroon()
        self.value.calculate()

    def aroonentry_exit_base(self):
        return aroon().entry_exit_base()

    def arooncheckentry(self, testitemrow):
        self.value = aroon()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def arooncheckexit(self, testitem):
        self.value = aroon()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def aroonentry(self):
        self.value = aroon()
        layout = self.value.entrywidgetedit()
        return layout
    """AROON"""
    """AROONOSC"""

    def aroonosc(self):
        return aroonosc()

    def aroonoscgroup(self):
        self.widget = aroonosc()
        layout = self.widget.widgetedit()
        return layout

    def aroonoscbase(self):
        return aroonosc().base()

    def aroonosccalculate(self):
        self.value = aroonosc()
        self.value.calculate()

    def aroonoscentry_exit_base(self):
        return aroonosc().entry_exit_base()

    def aroonosccheckentry(self, testitemrow):
        self.value = aroonosc()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def aroonosccheckexit(self, testitem):
        self.value = aroonosc()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def aroonoscentry(self):
        self.value = aroonosc()
        layout = self.value.entrywidgetedit()
        return layout
    """AROONOSC"""
    """BOP"""

    def bop(self):
        return bop()

    def bopgroup(self):
        self.widget = bop()
        layout = self.widget.widgetedit()
        return layout

    def bopbase(self):
        return bop().base()

    def bopcalculate(self):
        self.value = bop()
        self.value.calculate()

    def bopcentry_exit_base(self):
        return bop().entry_exit_base()

    def bopcheckentry(self, testitemrow):
        self.value = bop()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def bopcheckexit(self, testitem):
        self.value = bop()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def bopentry(self):
        self.value = bop()
        layout = self.value.entrywidgetedit()
        return layout
    """BOP"""
    """CCI"""

    def cci(self):
        return cci()

    def ccigroup(self):
        self.widget = cci()
        layout = self.widget.widgetedit()
        return layout

    def ccibase(self):
        return cci().base()

    def ccicalculate(self):
        self.value = cci()
        self.value.calculate()

    def ccicentry_exit_base(self):
        return cci().entry_exit_base()

    def ccicheckentry(self, testitemrow):
        self.value = cci()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ccicheckexit(self, testitem):
        self.value = cci()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ccientry(self):
        self.value = cci()
        layout = self.value.entrywidgetedit()
        return layout
    """CCI"""
    """CMO"""

    def cmo(self):
        return cci()

    def cmogroup(self):
        self.widget = cmo()
        layout = self.widget.widgetedit()
        return layout

    def cmobase(self):
        return cmo().base()

    def cmocalculate(self):
        self.value = cmo()
        self.value.calculate()

    def cmocentry_exit_base(self):
        return cmo().entry_exit_base()

    def cmocheckentry(self, testitemrow):
        self.value = cmo()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def cmocheckexit(self, testitem):
        self.value = cmo()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def cmoentry(self):
        self.value = cmo()
        layout = self.value.entrywidgetedit()
        return layout
    """CMO"""
    """DX"""

    def dx(self):
        return dx()

    def dxgroup(self):
        self.widget = dx()
        layout = self.widget.widgetedit()
        return layout

    def dxbase(self):
        return dx().base()

    def dxcalculate(self):
        self.value = dx()
        self.value.calculate()

    def dxcentry_exit_base(self):
        return dx().entry_exit_base()

    def dxcheckentry(self, testitemrow):
        self.value = dx()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def dxcheckexit(self, testitem):
        self.value = dx()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def dxentry(self):
        self.value = dx()
        layout = self.value.entrywidgetedit()
        return layout
    """DX"""
    """MACD"""

    def macd(self):
        return macd()

    def macdgroup(self):
        self.widget = macd()
        layout = self.widget.widgetedit()
        return layout

    def macdbase(self):
        return macd().base()

    def macdcalculate(self):
        self.value = macd()
        self.value.calculate()

    def macdentry_exit_base(self):
        return macd().entry_exit_base()

    def macdcheckentry(self, testitemrow):
        self.value = macd()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def macdcheckexit(self, testitem):
        self.value = macd()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def macdentry(self):
        self.value = macd()
        layout = self.value.entrywidgetedit()
        return layout

    """MACD"""
    """MACDEXT"""

    def macdext(self):
        return macdext()

    def macdextgroup(self):
        self.widget = macdext()
        layout = self.widget.widgetedit()
        return layout

    def macdextbase(self):
        return macdext().base()

    def macdextcalculate(self):
        self.value = macdext()
        self.value.calculate()

    def macdextentry_exit_base(self):
        return macdext().entry_exit_base()

    def macdextcheckentry(self, testitemrow):
        self.value = macdext()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def macdextcheckexit(self, testitem):
        self.value = macdext()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def macdextentry(self):
        self.value = macdext()
        layout = self.value.entrywidgetedit()
        return layout

    """MACDEXT"""
    """MACDFIX"""

    def macdfix(self):
        return macdfix()

    def macdfixgroup(self):
        self.widget = macdfix()
        layout = self.widget.widgetedit()
        return layout

    def macdfixbase(self):
        return macdfix().base()

    def macdfixcalculate(self):
        self.value = macdfix()
        self.value.calculate()

    def macdfixentry_exit_base(self):
        return macdfix().entry_exit_base()

    def macdfixcheckentry(self, testitemrow):
        self.value = macdfix()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def macdfixcheckexit(self, testitem):
        self.value = macdfix()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def macdfixentry(self):
        self.value = macdfix()
        layout = self.value.entrywidgetedit()
        return layout

    """MACDFIX"""
    """MFI"""

    def mfi(self):
        return mfi()

    def mfigroup(self):
        self.widget = mfi()
        layout = self.widget.widgetedit()
        return layout

    def mfibase(self):
        return mfi().base()

    def mficalculate(self):
        self.value = mfi()
        self.value.calculate()

    def mfientry_exit_base(self):
        return mfi().entry_exit_base()

    def mficheckentry(self, testitemrow):
        self.value = mfi()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def mficheckexit(self, testitem):
        self.value = mfi()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def mfientry(self):
        self.value = mfi()
        layout = self.value.entrywidgetedit()
        return layout

    """MFI"""
    """MINUS_DI"""

    def minus_di(self):
        return minusdi()

    def minus_digroup(self):
        self.widget = minusdi()
        layout = self.widget.widgetedit()
        return layout

    def minus_dibase(self):
        return minusdi().base()

    def minus_dicalculate(self):
        self.value = minusdi()
        self.value.calculate()

    def minusdientry_exit_base(self):
        return minusdi().entry_exit_base()

    def minusdicheckentry(self, testitemrow):
        self.value = minusdi()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def minusdicheckexit(self, testitem):
        self.value = minusdi()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def minusdientry(self):
        self.value = minusdi()
        layout = self.value.entrywidgetedit()
        return layout

    """MINUS_DI"""

    """MINUS_DM"""

    def minus_dm(self):
        return minusdm()

    def minus_dmgroup(self):
        self.widget = minusdm()
        layout = self.widget.widgetedit()
        return layout

    def minus_dmbase(self):
        return minusdm().base()

    def minus_dmcalculate(self):
        self.value = minusdm()
        self.value.calculate()

    def minus_dmentry_exit_base(self):
        return minusdm().entry_exit_base()

    def minus_dmcheckentry(self, testitemrow):
        self.value = minusdm()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def minus_dmcheckexit(self, testitem):
        self.value = minusdm()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def minus_dmentry(self):
        self.value = minusdm()
        layout = self.value.entrywidgetedit()
        return layout

    """MINUS_DM"""

    """MOM"""

    def mom(self):
        return mom()

    def momgroup(self):
        self.widget = mom()
        layout = self.widget.widgetedit()
        return layout

    def mombase(self):
        return mom().base()

    def momcalculate(self):
        self.value = mom()
        self.value.calculate()

    def momentry_exit_base(self):
        return mom().entry_exit_base()

    def momcheckentry(self, testitemrow):
        self.value = mom()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def momcheckexit(self, testitem):
        self.value = mom()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def momentry(self):
        self.value = mom()
        layout = self.value.entrywidgetedit()
        return layout

    """MOM"""
    """RSI"""

    def rsi(self):
        return rsi()

    def rsigroup(self):
        self.widget = rsi()
        layout = self.widget.widgetedit()
        return layout

    def rsibase(self):
        return rsi().base()

    def rsicalculate(self):
        self.value = rsi()
        self.value.calculate()

    def rsientry_exit_base(self):
        return rsi().entry_exit_base()

    def rsicheckentry(self, testitemrow):
        self.value = rsi()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def rsicheckexit(self, testitem):
        self.value = rsi()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def rsientry(self):
        self.value = rsi()
        layout = self.value.entrywidgetedit()
        return layout

    """RSI"""
    """PLUS_DI"""

    def plusdi(self):
        return plusdi()

    def plusdigroup(self):
        self.widget = plusdi()
        layout = self.widget.widgetedit()
        return layout

    def plusdibase(self):
        return plusdi().base()

    def plusdicalculate(self):
        self.value = plusdi()
        self.value.calculate()

    def plusdientry_exit_base(self):
        return plusdi().entry_exit_base()

    def plusdicheckentry(self, testitemrow):
        self.value = plusdi()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def plusdicheckexit(self, testitem):
        self.value = plusdi()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def plusdientry(self):
        self.value = plusdi()
        layout = self.value.entrywidgetedit()
        return layout

    """PLUS_DI"""
    """PLUS_DM"""

    def plusdm(self):
        return plusdm()

    def plusdmgroup(self):
        self.widget = plusdm()
        layout = self.widget.widgetedit()
        return layout

    def plusdmbase(self):
        return plusdm().base()

    def plusdmcalculate(self):
        self.value = plusdm()
        self.value.calculate()

    def plusdmentry_exit_base(self):
        return plusdm().entry_exit_base()

    def plusdmcheckentry(self, testitemrow):
        self.value = plusdm()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def plusdmcheckexit(self, testitem):
        self.value = plusdm()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def plusdmentry(self):
        self.value = plusdm()
        layout = self.value.entrywidgetedit()
        return layout

    """PLUS_DM"""
    """PPO"""

    def ppo(self):
        return ppo()

    def ppogroup(self):
        self.widget = ppo()
        layout = self.widget.widgetedit()
        return layout

    def ppobase(self):
        return ppo().base()

    def ppocalculate(self):
        self.value = ppo()
        self.value.calculate()

    def ppoentry_exit_base(self):
        return ppo().entry_exit_base()

    def ppocheckentry(self, testitemrow):
        self.value = ppo()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ppocheckexit(self, testitem):
        self.value = ppo()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ppoentry(self):
        self.value = ppo()
        layout = self.value.entrywidgetedit()
        return layout

    """PPO"""
    """ROC"""

    def roc(self):
        return roc()

    def rocgroup(self):
        self.widget = roc()
        layout = self.widget.widgetedit()
        return layout

    def rocbase(self):
        return roc().base()

    def roccalculate(self):
        self.value = roc()
        self.value.calculate()

    def rocentry_exit_base(self):
        return roc().entry_exit_base()

    def roccheckentry(self, testitemrow):
        self.value = roc()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def roccheckexit(self, testitem):
        self.value = roc()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def rocentry(self):
        self.value = roc()
        layout = self.value.entrywidgetedit()
        return layout

    """ROC"""
    """ROCP"""

    def rocp(self):
        return rocp()

    def rocpgroup(self):
        self.widget = rocp()
        layout = self.widget.widgetedit()
        return layout

    def rocpbase(self):
        return rocp().base()

    def rocpcalculate(self):
        self.value = rocp()
        self.value.calculate()

    def rocpentry_exit_base(self):
        return rocp().entry_exit_base()

    def rocpcheckentry(self, testitemrow):
        self.value = rocp()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def rocpcheckexit(self, testitem):
        self.value = rocp()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def rocpentry(self):
        self.value = rocp()
        layout = self.value.entrywidgetedit()
        return layout

    """ROCP"""
    """ROCR"""

    def rocr(self):
        return rocr()

    def rocrgroup(self):
        self.widget = rocr()
        layout = self.widget.widgetedit()
        return layout

    def rocrbase(self):
        return rocr().base()

    def rocrcalculate(self):
        self.value = rocr()
        self.value.calculate()

    def rocrentry_exit_base(self):
        return rocr().entry_exit_base()

    def rocrcheckentry(self, testitemrow):
        self.value = rocr()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def rocrcheckexit(self, testitem):
        self.value = rocr()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def rocrentry(self):
        self.value = rocr()
        layout = self.value.entrywidgetedit()
        return layout

    """ROCR"""
    """ROCR100"""

    def rocr100(self):
        return rocr100()

    def rocr100group(self):
        self.widget = rocr100()
        layout = self.widget.widgetedit()
        return layout

    def rocr100base(self):
        return rocr100().base()

    def rocr100calculate(self):
        self.value = rocr100()
        self.value.calculate()

    def rocr100entry_exit_base(self):
        return rocr100().entry_exit_base()

    def rocr100checkentry(self, testitemrow):
        self.value = rocr100()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def rocr100checkexit(self, testitem):
        self.value = rocr100()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def rocr100entry(self):
        self.value = rocr100()
        layout = self.value.entrywidgetedit()
        return layout

    """ROCR100"""
    """STOCH"""

    def stoch(self):
        return stoch()

    def stochgroup(self):
        self.widget = stoch()
        layout = self.widget.widgetedit()
        return layout

    def stochbase(self):
        return stoch().base()

    def stochcalculate(self):
        self.value = stoch()
        self.value.calculate()

    def stochentry_exit_base(self):
        return stoch().entry_exit_base()

    def stochcheckentry(self, testitemrow):
        self.value = stoch()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def stochcheckexit(self, testitem):
        self.value = stoch()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def stochentry(self):
        self.value = stoch()
        layout = self.value.entrywidgetedit()
        return layout

    """STOCH"""
    """STOCHF"""

    def stochf(self):
        return stochf()

    def stochfgroup(self):
        self.widget = stochf()
        layout = self.widget.widgetedit()
        return layout

    def stochfbase(self):
        return stochf().base()

    def stochfcalculate(self):
        self.value = stochf()
        self.value.calculate()

    def stochfentry_exit_base(self):
        return stochf().entry_exit_base()

    def stochfcheckentry(self, testitemrow):
        self.value = stochf()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def stochfcheckexit(self, testitem):
        self.value = stochf()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def stochfentry(self):
        self.value = stochf()
        layout = self.value.entrywidgetedit()
        return layout

    """STOCHF"""
    """STOCHRSI"""

    def stochrsi(self):
        return stochrsi()

    def stochrsigroup(self):
        self.widget = stochrsi()
        layout = self.widget.widgetedit()
        return layout

    def stochrsibase(self):
        return stochrsi().base()

    def stochrsicalculate(self):
        self.value = stochrsi()
        self.value.calculate()

    def stochrsientry_exit_base(self):
        return stochrsi().entry_exit_base()

    def stochrsicheckentry(self, testitemrow):
        self.value = stochrsi()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def stochrsicheckexit(self, testitem):
        self.value = stochrsi()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def stochrsientry(self):
        self.value = stochrsi()
        layout = self.value.entrywidgetedit()
        return layout

    """STOCHRSI"""
    """TRIX"""

    def trix(self):
        return trix()

    def trixgroup(self):
        self.widget = trix()
        layout = self.widget.widgetedit()
        return layout

    def trixbase(self):
        return trix().base()

    def trixcalculate(self):
        self.value = trix()
        self.value.calculate()

    def trixentry_exit_base(self):
        return trix().entry_exit_base()

    def trixcheckentry(self, testitemrow):
        self.value = trix()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def trixcheckexit(self, testitem):
        self.value = trix()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def trixentry(self):
        self.value = trix()
        layout = self.value.entrywidgetedit()
        return layout

    """TRIX"""
    """ULTOSC"""

    def ultosc(self):
        return ultosc()

    def ultoscgroup(self):
        self.widget = ultosc()
        layout = self.widget.widgetedit()
        return layout

    def ultoscbase(self):
        return ultosc().base()

    def ultosccalculate(self):
        self.value = ultosc()
        self.value.calculate()

    def ultoscentry_exit_base(self):
        return ultosc().entry_exit_base()

    def ultosccheckentry(self, testitemrow):
        self.value = ultosc()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ultosccheckexit(self, testitem):
        self.value = ultosc()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ultoscentry(self):
        self.value = ultosc()
        layout = self.value.entrywidgetedit()
        return layout

    """ULTOSC"""
    """WILLR"""

    def willr(self):
        return willr()

    def willrgroup(self):
        self.widget = willr()
        layout = self.widget.widgetedit()
        return layout

    def willrbase(self):
        return willr().base()

    def willrcalculate(self):
        self.value = willr()
        self.value.calculate()

    def willrentry_exit_base(self):
        return willr().entry_exit_base()

    def willrcheckentry(self, testitemrow):
        self.value = willr()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def willrcheckexit(self, testitem):
        self.value = willr()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def willrentry(self):
        self.value = willr()
        layout = self.value.entrywidgetedit()
        return layout

    """WILLR"""

    """MAVP"""

    def mavp(self):
        return mavp()

    def mavpgroup(self):
        self.widget = mavp()
        layout = self.widget.widgetedit()
        return layout

    def mavpbase(self):
        return mavp().base()

    def mavpcalculate(self):
        self.value = mavp()
        self.value.calculate()

    def mavpentry_exit_base(self):
        return mavp().entry_exit_base()

    def mavpcheckentry(self, testitemrow):
        self.value = mavp()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def mavpcheckexit(self, testitem):
        self.value = mavp()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def mavpentry(self):
        self.value = mavp()
        layout = self.value.entrywidgetedit()
        return layout

    """MAVP"""

    """bbands"""

    def bbands(self):
        return bbands()

    def bbandsgroup(self):
        self.widget = bbands()
        layout = self.widget.widgetedit()
        return layout

    def bbandsbase(self):
        return bbands().base()

    def bbandscalculate(self):
        self.value = bbands()
        self.value.calculate()

    def bbandsentry_exit_base(self):
        return bbands().entry_exit_base()

    def bbandscheckentry(self, testitemrow):
        self.value = bbands()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def bbandscheckexit(self, testitem):
        self.value = bbands()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def bbandsentry(self):
        self.value = bbands()
        layout = self.value.entrywidgetedit()
        return layout

    """bbands"""
    """DEMA"""

    def dema(self):
        return dema()

    def demagroup(self):
        self.widget = dema()
        layout = self.widget.widgetedit()
        return layout

    def demabase(self):
        return dema().base()

    def demacalculate(self):
        self.value = dema()
        self.value.calculate()

    def demaentry_exit_base(self):
        return dema().entry_exit_base()

    def demacheckentry(self, testitemrow):
        self.value = dema()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def demacheckexit(self, testitem):
        self.value = dema()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def demaentry(self):
        self.value = dema()
        layout = self.value.entrywidgetedit()
        return layout

    """DEMA"""
    """EMA"""

    def ema(self):
        return ema()

    def emagroup(self):
        self.widget = ema()
        layout = self.widget.widgetedit()
        return layout

    def emabase(self):
        return ema().base()

    def emacalculate(self):
        self.value = ema()
        self.value.calculate()

    def emaentry_exit_base(self):
        return ema().entry_exit_base()

    def emacheckentry(self, testitemrow):
        self.value = ema()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def emacheckexit(self, testitem):
        self.value = ema()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def emaentry(self):
        self.value = ema()
        layout = self.value.entrywidgetedit()
        return layout

    """EMA"""

    """HT_TRENDLINE"""

    def ht_trendline(self):
        return ht_trendline()

    def ht_trendlinegroup(self):
        self.widget = ht_trendline()
        layout = self.widget.widgetedit()
        return layout

    def ht_trendlinebase(self):
        return ht_trendline().base()

    def ht_trendlinecalculate(self):
        self.value = ht_trendline()
        self.value.calculate()

    def ht_trendlineentry_exit_base(self):
        return ht_trendline().entry_exit_base()

    def ht_trendlinecheckentry(self, testitemrow):
        self.value = ht_trendline()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def ht_trendlinecheckexit(self, testitem):
        self.value = ht_trendline()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def ht_trendlineentry(self):
        self.value = ht_trendline()
        layout = self.value.entrywidgetedit()
        return layout

    """HT_TRENDLINE"""
    """KAMA"""

    def kama(self):
        return kama()

    def kamagroup(self):
        self.widget = kama()
        layout = self.widget.widgetedit()
        return layout

    def kamabase(self):
        return kama().base()

    def kamacalculate(self):
        self.value = kama()
        self.value.calculate()

    def kamaentry_exit_base(self):
        return kama().entry_exit_base()

    def kamacheckentry(self, testitemrow):
        self.value = kama()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def kamacheckexit(self, testitem):
        self.value = kama()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def kamaentry(self):
        self.value = kama()
        layout = self.value.entrywidgetedit()
        return layout

    """KAMA"""
    """MA"""

    def ma(self):
        return ma()

    def magroup(self):
        self.widget = ma()
        layout = self.widget.widgetedit()
        return layout

    def mabase(self):
        return ma().base()

    def macalculate(self):
        self.value = ma()
        self.value.calculate()

    def maentry_exit_base(self):
        return ma().entry_exit_base()

    def macheckentry(self, testitemrow):
        self.value = ma()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def macheckexit(self, testitem):
        self.value = ma()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def maentry(self):
        self.value = ma()
        layout = self.value.entrywidgetedit()
        return layout

    """MA"""
    """MAMA"""

    def mama(self):
        return mama()

    def mamagroup(self):
        self.widget = mama()
        layout = self.widget.widgetedit()
        return layout

    def mamabase(self):
        return mama().base()

    def mamacalculate(self):
        self.value = mama()
        self.value.calculate()

    def mamaentry_exit_base(self):
        return mama().entry_exit_base()

    def mamacheckentry(self, testitemrow):
        self.value = mama()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def mamacheckexit(self, testitem):
        self.value = mama()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def mamaentry(self):
        self.value = mama()
        layout = self.value.entrywidgetedit()
        return layout

    """MAMA"""
    """MIDPOINT"""

    def midpoint(self):
        return midpoint()

    def midpointgroup(self):
        self.widget = midpoint()
        layout = self.widget.widgetedit()
        return layout

    def midpointbase(self):
        return midpoint().base()

    def midpointcalculate(self):
        self.value = midpoint()
        self.value.calculate()

    def midpointentry_exit_base(self):
        return midpoint().entry_exit_base()

    def midpointcheckentry(self, testitemrow):
        self.value = midpoint()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def midpointcheckexit(self, testitem):
        self.value = midpoint()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def midpointentry(self):
        self.value = midpoint()
        layout = self.value.entrywidgetedit()
        return layout

    """MIDPOINT"""
    """MIDPRICE"""

    def midprice(self):
        return midprice()

    def midpricegroup(self):
        self.widget = midprice()
        layout = self.widget.widgetedit()
        return layout

    def midpricebase(self):
        return midprice().base()

    def midpricecalculate(self):
        self.value = midprice()
        self.value.calculate()

    def midpriceentry_exit_base(self):
        return midprice().entry_exit_base()

    def midpricecheckentry(self, testitemrow):
        self.value = midprice()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def midpricecheckexit(self, testitem):
        self.value = midprice()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def midpriceentry(self):
        self.value = midprice()
        layout = self.value.entrywidgetedit()
        return layout

    """MIDPRICE"""
    """SAR"""

    def sar(self):
        return sar()

    def sargroup(self):
        self.widget = sar()
        layout = self.widget.widgetedit()
        return layout

    def sarbase(self):
        return sar().base()

    def sarcalculate(self):
        self.value = sar()
        self.value.calculate()

    def sarentry_exit_base(self):
        return sar().entry_exit_base()

    def sarcheckentry(self, testitemrow):
        self.value = sar()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def sarcheckexit(self, testitem):
        self.value = sar()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def sarentry(self):
        self.value = sar()
        layout = self.value.entrywidgetedit()
        return layout

    """SAR"""
    """SAREXT"""

    def sarext(self):
        return sarext()

    def sarextgroup(self):
        self.widget = sarext()
        layout = self.widget.widgetedit()
        return layout

    def sarextbase(self):
        return sarext().base()

    def sarextcalculate(self):
        self.value = sarext()
        self.value.calculate()

    def sarextentry_exit_base(self):
        return sarext().entry_exit_base()

    def sarextcheckentry(self, testitemrow):
        self.value = sarext()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def sarextcheckexit(self, testitem):
        self.value = sarext()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def sarextentry(self):
        self.value = sarext()
        layout = self.value.entrywidgetedit()
        return layout

    """SAREXT"""
    """SMA"""

    def sma(self):
        return sma()

    def smagroup(self):
        self.widget = sma()
        layout = self.widget.widgetedit()
        return layout

    def smabase(self):
        return sma().base()

    def smacalculate(self):
        self.value = sma()
        self.value.calculate()

    def smaentry_exit_base(self):
        return sma().entry_exit_base()

    def smacheckentry(self, testitemrow):
        self.value = sma()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def smacheckexit(self, testitem):
        self.value = sma()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def smaentry(self):
        self.value = sma()
        layout = self.value.entrywidgetedit()
        return layout

    """SMA"""
    """T3"""

    def t3(self):
        return t3()

    def t3group(self):
        self.widget = t3()
        layout = self.widget.widgetedit()
        return layout

    def t3base(self):
        return t3().base()

    def t3calculate(self):
        self.value = t3()
        self.value.calculate()

    def t3entry_exit_base(self):
        return t3().entry_exit_base()

    def t3checkentry(self, testitemrow):
        self.value = t3()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def t3checkexit(self, testitem):
        self.value = t3()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def t3entry(self):
        self.value = t3()
        layout = self.value.entrywidgetedit()
        return layout

    """T3"""
    """TEMA"""

    def tema(self):
        return tema()

    def temagroup(self):
        self.widget = tema()
        layout = self.widget.widgetedit()
        return layout

    def temabase(self):
        return tema().base()

    def temacalculate(self):
        self.value = tema()
        self.value.calculate()

    def temaentry_exit_base(self):
        return tema().entry_exit_base()

    def temacheckentry(self, testitemrow):
        self.value = tema()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def temacheckexit(self, testitem):
        self.value = tema()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def temaentry(self):
        self.value = tema()
        layout = self.value.entrywidgetedit()
        return layout

    """TEMA"""
    """TRIMA"""

    def trima(self):
        return trima()

    def trimagroup(self):
        self.widget = trima()
        layout = self.widget.widgetedit()
        return layout

    def trimabase(self):
        return trima().base()

    def trimacalculate(self):
        self.value = trima()
        self.value.calculate()

    def trimaentry_exit_base(self):
        return trima().entry_exit_base()

    def trimacheckentry(self, testitemrow):
        self.value = trima()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def trimacheckexit(self, testitem):
        self.value = trima()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def trimaentry(self):
        self.value = trima()
        layout = self.value.entrywidgetedit()
        return layout

    """TEMA"""
    """WMA"""

    def wma(self):
        return wma()

    def wmagroup(self):
        self.widget = wma()
        layout = self.widget.widgetedit()
        return layout

    def wmabase(self):
        return wma().base()

    def wmacalculate(self):
        self.value = wma()
        self.value.calculate()

    def wmaentry_exit_base(self):
        return wma().entry_exit_base()

    def wmacheckentry(self, testitemrow):
        self.value = wma()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def wmacheckexit(self, testitem):
        self.value = wma()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def wmaentry(self):
        self.value = wma()
        layout = self.value.entrywidgetedit()
        return layout

    """WMA"""
    """kdj"""

    def kdj(self):
        return kdj()

    def kdjgroup(self):
        self.widget = kdj()
        layout = self.widget.widgetedit()
        return layout

    def kdjbase(self):
        return kdj().base()

    def kdjcalculate(self):
        self.value = kdj()
        self.value.calculate()

    def kdjentry_exit_base(self):
        return kdj().entry_exit_base()

    def kdjcheckentry(self, testitemrow):
        self.value = kdj()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def kdjcheckexit(self, testitem):
        self.value = kdj()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def kdjentry(self):
        self.value = kdj()
        layout = self.value.entrywidgetedit()
        return layout

    """kdj"""

    """atr"""

    def atr(self):
        return atr()

    def atrgroup(self):
        self.widget = atr()
        layout = self.widget.widgetedit()
        return layout

    def atrbase(self):
        return atr().base()

    def atrcalculate(self):
        self.value = atr()
        self.value.calculate()

    def atrentry_exit_base(self):
        return atr().entry_exit_base()

    def atrcheckentry(self, testitemrow):
        self.value = atr()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def atrcheckexit(self, testitem):
        self.value = atr()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def atrentry(self):
        self.value = atr()
        layout = self.value.entrywidgetedit()
        return layout

    """atr"""
    """natr"""

    def natr(self):
        return natr()

    def natrgroup(self):
        self.widget = natr()
        layout = self.widget.widgetedit()
        return layout

    def natrbase(self):
        return natr().base()

    def natrcalculate(self):
        self.value = natr()
        self.value.calculate()

    def natrentry_exit_base(self):
        return natr().entry_exit_base()

    def natrcheckentry(self, testitemrow):
        self.value = natr()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def natrcheckexit(self, testitem):
        self.value = natr()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def natrentry(self):
        self.value = natr()
        layout = self.value.entrywidgetedit()
        return layout

    """natr"""
    """trange"""

    def trange(self):
        return trange()

    def trangegroup(self):
        self.widget = trange()
        layout = self.widget.widgetedit()
        return layout

    def trangebase(self):
        return trange().base()

    def trangecalculate(self):
        self.value = trange()
        self.value.calculate()

    def trangeentry_exit_base(self):
        return trange().entry_exit_base()

    def trangecheckentry(self, testitemrow):
        self.value = trange()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def trangecheckexit(self, testitem):
        self.value = trange()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def trangeentry(self):
        self.value = trange()
        layout = self.value.entrywidgetedit()
        return layout

    """trange"""
    """obv"""

    def obv(self):
        return obv()

    def obvgroup(self):
        self.widget = obv()
        layout = self.widget.widgetedit()
        return layout

    def obvbase(self):
        return obv().base()

    def obvcalculate(self):
        self.value = obv()
        self.value.calculate()

    def obventry_exit_base(self):
        return obv().entry_exit_base()

    def obvcheckentry(self, testitemrow):
        self.value = obv()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def obvcheckexit(self, testitem):
        self.value = obv()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def obventry(self):
        self.value = obv()
        layout = self.value.entrywidgetedit()
        return layout

    """obv"""
    """ad"""

    def ad(self):
        return ad()

    def adgroup(self):
        self.widget = ad()
        layout = self.widget.widgetedit()
        return layout

    def adbase(self):
        return ad().base()

    def adcalculate(self):
        self.value = ad()
        self.value.calculate()

    def adentry_exit_base(self):
        return ad().entry_exit_base()

    def adcheckentry(self, testitemrow):
        self.value = ad()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def adcheckexit(self, testitem):
        self.value = ad()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def adentry(self):
        self.value = ad()
        layout = self.value.entrywidgetedit()
        return layout

    """ad"""
    """adosc"""

    def adosc(self):
        return adosc()

    def adoscgroup(self):
        self.widget = adosc()
        layout = self.widget.widgetedit()
        return layout

    def adoscbase(self):
        return adosc().base()

    def adosccalculate(self):
        self.value = adosc()
        self.value.calculate()

    def adoscentry_exit_base(self):
        return adosc().entry_exit_base()

    def adosccheckentry(self, testitemrow):
        self.value = adosc()
        self.en = self.value.Check_Entry(testitemrow)
        return self.en

    def adosccheckexit(self, testitem):
        self.value = adosc()
        self.en = self.value.Check_Exit(testitem)
        return self.en

    def adoscentry(self):
        self.value = adosc()
        layout = self.value.entrywidgetedit()
        return layout

    """adosc"""
    """Return"""

    def groupreturn(self, text):
        try:
            if (text == "HT_DCPERIOD"):
                return self.ht_dcperiodgroup()
            elif (text == "HT_DCPHASE"):
                return self.ht_dchasegroup()
            elif (text == "HT_PHASOR"):
                return self.ht_phasorgroup()
            elif (text == "HT_SINE"):
                return self.ht_sinegroup()
            elif (text == "HT_TRENDMODE"):
                return self.ht_trendmodegroup()
            elif (text == "ADX"):
                return self.adxgroup()
            elif (text == "ADXR"):
                return self.adxrgroup()
            elif (text == "RSI"):
                return self.rsigroup()
            elif (text == "MACD"):
                return self.macdgroup()
            elif (text == "APO"):
                return self.apogroup()
            elif (text == "AROON"):
                return self.aroongroup()
            elif (text == "AROONOSC"):
                return self.aroonoscgroup()
            elif (text == "BOP"):
                return self.bopgroup()
            elif (text == "CCI"):
                return self.ccigroup()
            elif (text == "CMO"):
                return self.cmogroup()
            elif (text == "DX"):
                return self.dxgroup()
            elif (text == "MACDEXT"):
                return self.macdextgroup()
            elif (text == "MACDFIX"):
                return self.macdfixgroup()
            elif (text == "MFI"):
                return self.mfigroup()
            elif (text == "MINUS_DI"):
                return self.minus_digroup()
            elif (text == "MINUS_DM"):
                return self.minus_dmgroup()
            elif (text == "MOM"):
                return self.momgroup()
            elif (text == "PLUS_DI"):
                return self.plusdigroup()
            elif (text == "PLUS_DM"):
                return self.plusdmgroup()
            elif (text == "PPO"):
                return self.ppogroup()
            elif (text == "ROC"):
                return self.rocgroup()
            elif (text == "ROCP"):
                return self.rocpgroup()
            elif (text == "ROCR"):
                return self.rocrgroup()
            elif (text == "ROCR100"):
                return self.rocr100group()
            elif (text == "STOCH"):
                return self.stochgroup()
            elif (text == "STOCHF"):
                return self.stochfgroup()
            elif (text == "STOCHRSI"):
                return self.stochrsigroup()
            elif (text == "TRIX"):
                return self.trixgroup()
            elif (text == "ULTOSC"):
                return self.ultoscgroup()
            elif (text == "WILLR"):
                return self.willrgroup()
            elif (text == "MAVP"):
                return self.mavpgroup()
            elif (text == "BBANDS"):
                return self.bbandsgroup()
            elif (text == "DEMA"):
                return self.demagroup()
            elif (text == "EMA"):
                return self.emagroup()
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlinegroup()
            elif (text == "KAMA"):
                return self.kamagroup()
            elif (text == "MA"):
                return self.magroup()
            elif (text == "MAMA"):
                return self.mamagroup()
            elif (text == "MIDPOINT"):
                return self.midpointgroup()
            elif (text == "MIDPRICE"):
                return self.midpricegroup()
            elif (text == "SAR"):
                return self.sargroup()
            elif (text == "SAREXT"):
                return self.sarextgroup()
            elif (text == "SMA"):
                return self.smagroup()
            elif (text == "T3"):
                return self.t3group()
            elif (text == "TEMA"):
                return self.temagroup()
            elif (text == "TRIMA"):
                return self.trimagroup()
            elif (text == "WMA"):
                return self.wmagroup()
            elif (text == "KDJ"):
                return self.kdjgroup()
            elif (text == "ATR"):
                return self.atrgroup()
            elif (text == "NATR"):
                return self.natrgroup()
            elif (text == "TRANGE"):
                return self.trangegroup()
            elif (text == "AD"):
                return self.adgroup()
            elif (text == "ADOSC"):
                return self.adoscgroup()
            elif (text == "OBV"):
                return self.obvgroup()
        except BaseException as msg:
            print(str(msg))

    def basereturn(self, text):
        try:
            if (text == "RSI"):
                return self.rsibase()
            elif (text == "MACD"):
                return self.macdbase()
            elif (text == "HT_DCPERIOD"):
                return self.ht_dcperiodbase()
            elif (text == "HT_DCPHASE"):
                return self.ht_dchasebase()
            elif (text == "HT_PHASOR"):
                return self.ht_phasorbase()
            elif (text == "HT_SINE"):
                return self.ht_sinebase()
            elif (text == "HT_TRENDMODE"):
                return self.ht_trendmodebase()
            elif (text == "ADX"):
                return self.adxbase()
            elif (text == "ADXR"):
                return self.adxrbase()
            elif (text == "APO"):
                return self.apobase()
            elif (text == "AROON"):
                return self.aroonbase()
            elif (text == "AROONOSC"):
                return self.aroonoscbase()
            elif (text == "BOP"):
                return self.bopbase()
            elif (text == "CCI"):
                return self.ccibase()
            elif (text == "CMO"):
                return self.cmobase()
            elif (text == "DX"):
                return self.dxbase()
            elif (text == "MACDEXT"):
                return self.macdextbase()
            elif (text == "MACDFIX"):
                return self.macdfixbase()
            elif (text == "MFI"):
                return self.mfibase()
            elif (text == "MINUS_DI"):
                return self.minus_dibase()
            elif (text == "MINUS_DM"):
                return self.minus_dmbase()
            elif (text == "MOM"):
                return self.mombase()
            elif (text == "PLUS_DI"):
                return self.plusdibase()
            elif (text == "PLUS_DM"):
                return self.plusdmbase()
            elif (text == "PPO"):
                return self.ppobase()
            elif (text == "ROC"):
                return self.rocbase()
            elif (text == "ROCP"):
                return self.rocpbase()
            elif (text == "ROCR"):
                return self.rocrbase()
            elif (text == "ROCR100"):
                return self.rocr100base()
            elif (text == "STOCH"):
                return self.stochbase()
            elif (text == "STOCHF"):
                return self.stochfbase()
            elif (text == "STOCHRSI"):
                return self.stochrsibase()
            elif (text == "TRIX"):
                return self.trixbase()
            elif (text == "ULTOSC"):
                return self.ultoscbase()
            elif (text == "WILLR"):
                return self.willrbase()
            elif (text == "MAVP"):
                return self.mavpbase()
            elif (text == "BBANDS"):
                return self.bbandsbase()
            elif (text == "DEMA"):
                return self.demabase()
            elif (text == "EMA"):
                return self.emabase()
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlinebase()
            elif (text == "KAMA"):
                return self.kamabase()
            elif (text == "MA"):
                return self.mabase()
            elif (text == "MAMA"):
                return self.mamabase()
            elif (text == "MIDPOINT"):
                return self.midpointbase()
            elif (text == "MIDPRICE"):
                return self.midpricebase()
            elif (text == "SAR"):
                return self.sarbase()
            elif (text == "SAREXT"):
                return self.sarextbase()
            elif (text == "SMA"):
                return self.smabase()
            elif (text == "T3"):
                return self.t3base()
            elif (text == "TEMA"):
                return self.temabase()
            elif (text == "TRIMA"):
                return self.trimabase()
            elif (text == "WMA"):
                return self.wmabase()
            elif (text == "KDJ"):
                return self.kdjbase()
            elif (text == "ATR"):
                return self.atrbase()
            elif (text == "NATR"):
                return self.natrbase()
            elif (text == "TRANGE"):
                return self.trangebase()
            elif (text == "AD"):
                return self.adbase()
            elif (text == "ADOSC"):
                return self.adoscbase()
            elif (text == "OBV"):
                return self.obvbase()
        except BaseException as msg:
            print(str(msg))

    def entry_exit_basereturn(self, text):
        try:
            if (text == "RSI"):
                return self.rsientry_exit_base()
            elif (text == "MACD"):
                return self.macdentry_exit_base()
            elif (text == "HT_DCPERIOD"):
                return self.ht_dcperiodentry_exit_base()
            elif (text == "HT_DCPHASE"):
                return self.ht_dchaseentry_exit_base()
            elif (text == "HT_PHASOR"):
                return self.ht_phasorentry_exit_base()
            elif (text == "HT_SINE"):
                return self.ht_sineentry_exit_base()
            elif (text == "HT_TRENDMODE"):
                return self.ht_trendmodeentry_exit_base()
            elif (text == "ADX"):
                return self.adxentry_exit_base()
            elif (text == "ADXR"):
                return self.adxrentry_exit_base()
            elif (text == "APO"):
                return self.apoentry_exit_base()
            elif (text == "AROON"):
                return self.aroonentry_exit_base()
            elif (text == "AROONOSC"):
                return self.aroonoscentry_exit_base()
            elif (text == "BOP"):
                return self.bopcentry_exit_base()
            elif (text == "CCI"):
                return self.ccicentry_exit_base()
            elif (text == "CMO"):
                return self.cmocentry_exit_base()
            elif (text == "DX"):
                return self.dxcentry_exit_base()
            elif (text == "MACDEXT"):
                return self.macdextentry_exit_base()
            elif (text == "MACDFIX"):
                return self.macdfixentry_exit_base()
            elif (text == "MFI"):
                return self.mfientry_exit_base()
            elif (text == "MINUS_DI"):
                return self.minusdientry_exit_base()
            elif (text == "MINUS_DM"):
                return self.minus_dmentry_exit_base()
            elif (text == "MOM"):
                return self.momentry_exit_base()
            elif (text == "PLUS_DI"):
                return self.plusdientry_exit_base()
            elif (text == "PLUS_DM"):
                return self.plusdmentry_exit_base()
            elif (text == "PPO"):
                return self.ppoentry_exit_base()
            elif (text == "ROC"):
                return self.rocentry_exit_base()
            elif (text == "ROCP"):
                return self.rocpentry_exit_base()
            elif (text == "ROCR"):
                return self.rocrentry_exit_base()
            elif (text == "ROCR100"):
                return self.rocr100entry_exit_base()
            elif (text == "STOCH"):
                return self.stochentry_exit_base()
            elif (text == "STOCHF"):
                return self.stochfentry_exit_base()
            elif (text == "STOCHRSI"):
                return self.stochrsientry_exit_base()
            elif (text == "TRIX"):
                return self.trixentry_exit_base()
            elif (text == "ULTOSC"):
                return self.ultoscentry_exit_base()
            elif (text == "WILLR"):
                return self.willrentry_exit_base()
            elif (text == "MAVP"):
                return self.mavpentry_exit_base()
            elif (text == "BBANDS"):
                return self.bbandsentry_exit_base()
            elif (text == "DEMA"):
                return self.demaentry_exit_base()
            elif (text == "EMA"):
                return self.emaentry_exit_base()
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlineentry_exit_base()
            elif (text == "KAMA"):
                return self.kamaentry_exit_base()
            elif (text == "MA"):
                return self.maentry_exit_base()
            elif (text == "MAMA"):
                return self.mamaentry_exit_base()
            elif (text == "MIDPOINT"):
                return self.midpointentry_exit_base()
            elif (text == "MIDPRICE"):
                return self.midpriceentry_exit_base()
            elif (text == "SAR"):
                return self.sarentry_exit_base()
            elif (text == "SAREXT"):
                return self.sarextentry_exit_base()
            elif (text == "SMA"):
                return self.smaentry_exit_base()
            elif (text == "T3"):
                return self.t3entry_exit_base()
            elif (text == "TEMA"):
                return self.temaentry_exit_base()
            elif (text == "TRIMA"):
                return self.trimaentry_exit_base()
            elif (text == "WMA"):
                return self.wmaentry_exit_base()
            elif (text == "KDJ"):
                return self.kdjentry_exit_base()
            elif (text == "ATR"):
                return self.atrentry_exit_base()
            elif (text == "NATR"):
                return self.natrentry_exit_base()
            elif (text == "TRANGE"):
                return self.trangeentry_exit_base()
            elif (text == "AD"):
                return self.adentry_exit_base()
            elif (text == "ADOSC"):
                return self.adoscentry_exit_base()
            elif (text == "OBV"):
                return self.obventry_exit_base()
        except BaseException as msg:
            print(str(msg))

    def entry_turn(self, text, testitemrow):
        try:
            if (text == "RSI"):
                return self.rsicheckentry(testitemrow)
            elif (text == "MACD"):
                return self.macdcheckentry(testitemrow)
            elif (text == "HT_DCPERIOD"):
                return self.ht_dcperiodcheckentry(testitemrow)
            elif (text == "HT_DCPHASE"):
                return self.ht_dchasecheckentry(testitemrow)
            elif (text == "HT_PHASOR"):
                return self.ht_phasorcheckentry(testitemrow)
            elif (text == "HT_SINE"):
                return self.ht_sinecheckentry(testitemrow)
            elif (text == "HT_TRENDMODE"):
                return self.ht_trendmodecheckentry(testitemrow)
            elif (text == "ADX"):
                return self.adxcheckentry(testitemrow)
            elif (text == "ADXR"):
                return self.adxrcheckentry(testitemrow)
            elif (text == "APO"):
                return self.apocheckentry(testitemrow)
            elif (text == "AROON"):
                return self.arooncheckentry(testitemrow)
            elif (text == "AROONOSC"):
                return self.aroonosccheckentry(testitemrow)
            elif (text == "BOP"):
                return self.bopcheckentry(testitemrow)
            elif (text == "CCI"):
                return self.ccicheckentry(testitemrow)
            elif (text == "CMO"):
                return self.cmocheckentry(testitemrow)
            elif (text == "DX"):
                return self.dxcheckentry(testitemrow)
            elif (text == "MACDEXT"):
                return self.macdextcheckentry(testitemrow)
            elif (text == "MACDFIX"):
                return self.macdfixcheckentry(testitemrow)
            elif (text == "MFI"):
                return self.mficheckentry(testitemrow)
            elif (text == "MINUS_DI"):
                return self.minusdicheckentry(testitemrow)
            elif (text == "MINUS_DM"):
                return self.minus_dmcheckentry(testitemrow)
            elif (text == "MOM"):
                return self.momcheckentry(testitemrow)
            elif (text == "PLUS_DI"):
                return self.plusdicheckentry(testitemrow)
            elif (text == "PLUS_DM"):
                return self.plusdmcheckentry(testitemrow)
            elif (text == "PPO"):
                return self.ppocheckentry(testitemrow)
            elif (text == "ROC"):
                return self.roccheckentry(testitemrow)
            elif (text == "ROCP"):
                return self.rocpcheckentry(testitemrow)
            elif (text == "ROCR"):
                return self.rocrcheckentry(testitemrow)
            elif (text == "ROCR100"):
                return self.rocr100checkentry(testitemrow)
            elif (text == "STOCH"):
                return self.stochcheckentry(testitemrow)
            elif (text == "STOCHF"):
                return self.stochfcheckentry(testitemrow)
            elif (text == "STOCHRSI"):
                return self.stochrsicheckentry(testitemrow)
            elif (text == "TRIX"):
                return self.trixcheckentry(testitemrow)
            elif (text == "ULTOSC"):
                return self.ultosccheckentry(testitemrow)
            elif (text == "WILLR"):
                return self.willrcheckentry(testitemrow)
            elif (text == "MAVP"):
                return self.mavpcheckentry(testitemrow)
            elif (text == "KDJ"):
                return self.kdjcheckentry(testitemrow)
            elif (text == "BBANDS"):
                return self.bbandscheckentry(testitemrow)
            elif (text == "DEMA"):
                return self.demacheckentry(testitemrow)
            elif (text == "EMA"):
                return self.emacheckentry(testitemrow)
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlinecheckentry(testitemrow)
            elif (text == "KAMA"):
                return self.kamacheckentry(testitemrow)
            elif (text == "MA"):
                return self.macheckentry(testitemrow)
            elif (text == "MAMA"):
                return self.mamacheckentry(testitemrow)
            elif (text == "MIDPOINT"):
                return self.midpointcheckentry(testitemrow)
            elif (text == "MIDPRICE"):
                return self.midpricecheckentry(testitemrow)
            elif (text == "SAR"):
                return self.sarcheckentry(testitemrow)
            elif (text == "SAREXT"):
                return self.sarextcheckentry(testitemrow)
            elif (text == "SMA"):
                return self.smacheckentry(testitemrow)
            elif (text == "T3"):
                return self.t3checkentry(testitemrow)
            elif (text == "TEMA"):
                return self.temacheckentry(testitemrow)
            elif (text == "TRIMA"):
                return self.trimacheckentry(testitemrow)
            elif (text == "WMA"):
                return self.wmacheckentry(testitemrow)
            elif (text == "ATR"):
                return self.atrcheckentry(testitemrow)
            elif (text == "NATR"):
                return self.natrcheckentry(testitemrow)
            elif (text == "TRANGE"):
                return self.trangecheckentry(testitemrow)
            elif (text == "OBV"):
                return self.obvcheckentry(testitemrow)
            elif (text == "AD"):
                return self.adcheckentry(testitemrow)
            elif (text == "ADOSC"):
                return self.adosccheckentry(testitemrow)
        except BaseException as msg:
            print(str(msg))

    def exit_turn(self, text, testitem):
        try:
            if (text == "RSI"):
                return self.rsicheckexit(testitem)
            elif (text == "MACD"):
                return self.macdcheckexit(testitem)
            elif (text == "HT_DCPERIOD"):
                return self.ht_dcperiodcheckexit(testitem)
            elif (text == "HT_DCPHASE"):
                return self.ht_dchasecheckexit(testitem)
            elif (text == "HT_PHASOR"):
                return self.ht_phasorcheckexit(testitem)
            elif (text == "HT_SINE"):
                return self.ht_sinecheckexit(testitem)
            elif (text == "ADX"):
                return self.adxcheckexit(testitem)
            elif (text == "ADXR"):
                return self.adxrcheckexit(testitem)
            elif (text == "APO"):
                return self.apocheckexit(testitem)
            elif (text == "AROON"):
                return self.arooncheckexit(testitem)
            elif (text == "AROONOSC"):
                return self.aroonosccheckexit(testitem)
            elif (text == "BOP"):
                return self.bopcheckexit(testitem)
            elif (text == "CCI"):
                return self.ccicheckexit(testitem)
            elif (text == "CMO"):
                return self.cmocheckexit(testitem)
            elif (text == "DX"):
                return self.dxcheckexit(testitem)
            elif (text == "MACDEXT"):
                return self.macdextcheckexit(testitem)
            elif (text == "MACDFIX"):
                return self.macdfixcheckexit(testitem)
            elif (text == "MFI"):
                return self.mficheckexit(testitem)
            elif (text == "MINUS_DI"):
                return self.minusdicheckexit(testitem)
            elif (text == "MINUS_DM"):
                return self.minus_dmcheckexit(testitem)
            elif (text == "MOM"):
                return self.momcheckexit(testitem)
            elif (text == "PLUS_DI"):
                return self.plusdicheckexit(testitem)
            elif (text == "PLUS_DM"):
                return self.plusdmcheckexit(testitem)
            elif (text == "PPO"):
                return self.ppocheckexit(testitem)
            elif (text == "ROC"):
                return self.roccheckexit(testitem)
            elif (text == "ROCP"):
                return self.rocpcheckexit(testitem)
            elif (text == "ROCR"):
                return self.rocrcheckexit(testitem)
            elif (text == "ROCR100"):
                return self.rocr100checkexit(testitem)
            elif (text == "STOCH"):
                return self.stochcheckexit(testitem)
            elif (text == "STOCHF"):
                return self.stochfcheckexit(testitem)
            elif (text == "STOCHRSI"):
                return self.stochrsicheckexit(testitem)
            elif (text == "TRIX"):
                return self.trixcheckexit(testitem)
            elif (text == "ULTOSC"):
                return self.ultosccheckexit(testitem)
            elif (text == "WILLR"):
                return self.willrcheckexit(testitem)
            elif (text == "MAVP"):
                return self.mavpcheckexit(testitem)
            elif (text == "KDJ"):
                return self.kdjcheckexit(testitem)
            elif (text == "BBANDS"):
                return self.bbandscheckexit(testitem)
            elif (text == "DEMA"):
                return self.demacheckexit(testitem)
            elif (text == "EMA"):
                return self.emacheckexit(testitem)
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlinecheckexit(testitem)
            elif (text == "KAMA"):
                return self.kamacheckexit(testitem)
            elif (text == "MA"):
                return self.macheckexit(testitem)
            elif (text == "MAMA"):
                return self.mamacheckexit(testitem)
            elif (text == "MIDPOINT"):
                return self.midpointcheckexit(testitem)
            elif (text == "MIDPRICE"):
                return self.midpricecheckexit(testitem)
            elif (text == "SAR"):
                return self.sarcheckexit(testitem)
            elif (text == "SAREXT"):
                return self.sarextcheckexit(testitem)
            elif (text == "SMA"):
                return self.smacheckexit(testitem)
            elif (text == "T3"):
                return self.t3checkexit(testitem)
            elif (text == "TEMA"):
                return self.temacheckexit(testitem)
            elif (text == "TRIMA"):
                return self.trimacheckexit(testitem)
            elif (text == "WMA"):
                return self.wmacheckexit(testitem)
            elif (text == "ATR"):
                return self.atrcheckexit(testitem)
            elif (text == "NATR"):
                return self.natrcheckexit(testitem)
            elif (text == "TRANGE"):
                return self.trangecheckexit(testitem)
            elif (text == "OBV"):
                return self.obvcheckexit(testitem)
            elif (text == "AD"):
                return self.adcheckexit(testitem)
            elif (text == "ADOSC"):
                return self.adosccheckexit(testitem)
        except BaseException as msg:
            print(str(msg))

    def entryreturn(self, text):
        try:
            if (text == "RSI"):
                return self.rsientry()
            elif (text == "MACD"):
                return self.macdentry()
            elif (text == "HT_DCPERIOD"):
                return self.ht_dcperiodentry()
            elif (text == "HT_DCPHASE"):
                return self.ht_dchaseentry()
            elif (text == "HT_PHASOR"):
                return self.ht_phasorentry()
            elif (text == "HT_SINE"):
                return self.ht_sineentry()
            elif (text == "HT_TRENDMODE"):
                return self.ht_trendmodeentry()
            elif (text == "ADX"):
                return self.adxentry()
            elif (text == "ADXR"):
                return self.adxrentry()
            elif (text == "APO"):
                return self.apoentry()
            elif (text == "AROON"):
                return self.aroonentry()
            elif (text == "AROONOSC"):
                return self.aroonoscentry()
            elif (text == "CCI"):
                return self.ccientry()
            elif (text == "CMO"):
                return self.cmoentry()
            elif (text == "DX"):
                return self.dxentry()
            elif (text == "MACDEXT"):
                return self.macdextentry()
            elif (text == "MACDFIX"):
                return self.macdfixentry()
            elif (text == "MFI"):
                return self.mfientry()
            elif (text == "MINUS_DI"):
                return self.minusdientry()
            elif (text == "MINUS_DM"):
                return self.minus_dmentry()
            elif (text == "MOM"):
                return self.momentry()
            elif (text == "PLUS_DI"):
                return self.plusdientry()
            elif (text == "PLUS_DM"):
                return self.plusdmentry()
            elif (text == "PPO"):
                return self.ppoentry()
            elif (text == "ROC"):
                return self.rocentry()
            elif (text == "ROCP"):
                return self.rocpentry()
            elif (text == "ROCR"):
                return self.rocrentry()
            elif (text == "ROCR100"):
                return self.rocr100entry()
            elif (text == "STOCH"):
                return self.stochentry()
            elif (text == "STOCHF"):
                return self.stochfentry()
            elif (text == "STOCHRSI"):
                return self.stochrsientry()
            elif (text == "TRIX"):
                return self.trixentry()
            elif (text == "ULTOSC"):
                return self.ultoscentry()
            elif (text == "WILLR"):
                return self.willrentry()
            elif (text == "MAVP"):
                return self.mavpentry()
            elif (text == "KDJ"):
                return self.kdjentry()
            elif (text == "BBANDS"):
                return self.bbandsentry()
            elif (text == "DEMA"):
                return self.demaentry()
            elif (text == "EMA"):
                return self.emaentry()
            elif (text == "HT_TRENDLINE"):
                return self.ht_trendlineentry()
            elif (text == "KAMA"):
                return self.kamaentry()
            elif (text == "MA"):
                return self.maentry()
            elif (text == "MAMA"):
                return self.mamaentry()
            elif (text == "MIDPOINT"):
                return self.midpointentry()
            elif (text == "MIDPRICE"):
                return self.midpriceentry()
            elif (text == "SAR"):
                return self.sarentry()
            elif (text == "SAREXT"):
                return self.sarextentry()
            elif (text == "SMA"):
                return self.smaentry()
            elif (text == "T3"):
                return self.t3entry()
            elif (text == "TEMA"):
                return self.temaentry()
            elif (text == "TRIMA"):
                return self.trimaentry()
            elif (text == "WMA"):
                return self.wmaentry()
            elif (text == "ATR"):
                return self.atrentry()
            elif (text == "NATR"):
                return self.natrentry()
            elif (text == "TRANGE"):
                return self.trangeentry()
            elif (text == "OBV"):
                return self.obventry()
            elif (text == "AD"):
                return self.adentry()
            elif (text == "ADOSC"):
                return self.adoscentry()
        except BaseException as msg:
            print(str(msg))

    def calculatereturn(self, text):
        try:
            if (text == "RSI"):
                self.rsicalculate()
            elif (text == "MACD"):
                self.macdcalculate()
            elif (text == "HT_DCPERIOD"):
                self.ht_dcperiodcalculate()
            elif (text == "HT_DCPHASE"):
                self.ht_dchasecalculate()
            elif (text == "HT_PHASOR"):
                self.ht_phasorcalculate()
            elif (text == "HT_SINE"):
                self.ht_sinecalculate()
            elif (text == "HT_TRENDMODE"):
                self.ht_trendmodecalculate()
            elif (text == "ADX"):
                self.adxcalculate()
            elif (text == "ADXR"):
                self.adxrcalculate()
            elif (text == "APO"):
                self.apocalculate()
            elif (text == "AROON"):
                self.arooncalculate()
            elif (text == "AROONOSC"):
                self.aroonosccalculate()
            elif (text == "BOP"):
                self.bopcalculate()
            elif (text == "CCI"):
                self.ccicalculate()
            elif (text == "CMO"):
                self.cmocalculate()
            elif (text == "DX"):
                self.dxcalculate()
            elif (text == "MACDEXT"):
                self.macdextcalculate()
            elif (text == "MACDFIX"):
                self.macdfixcalculate()
            elif (text == "MFI"):
                self.mficalculate()
            elif (text == "MINUS_DI"):
                self.minus_dicalculate()
            elif (text == "MINUS_DM"):
                self.minus_dmcalculate()
            elif (text == "MOM"):
                self.momcalculate()
            elif (text == "PLUS_DI"):
                self.plusdicalculate()
            elif (text == "PLUS_DM"):
                self.plusdmcalculate()
            elif (text == "PPO"):
                self.ppocalculate()
            elif (text == "ROC"):
                self.roccalculate()
            elif (text == "ROCP"):
                self.rocpcalculate()
            elif (text == "ROCR"):
                self.rocrcalculate()
            elif (text == "ROCR100"):
                self.rocr100calculate()
            elif (text == "STOCH"):
                self.stochcalculate()
            elif (text == "STOCHF"):
                self.stochfcalculate()
            elif (text == "STOCHRSI"):
                self.stochrsicalculate()
            elif (text == "TRIX"):
                self.trixcalculate()
            elif (text == "ULTOSC"):
                self.ultosccalculate()
            elif (text == "WILLR"):
                self.willrcalculate()
            elif (text == "MAVP"):
                """ERROR"""
                self.mavpcalculate()
            elif (text == "BBANDS"):
                self.bbandscalculate()
            elif (text == "DEMA"):
                self.demacalculate()
            elif (text == "EMA"):
                self.emacalculate()
            elif (text == "HT_TRENDLINE"):
                self.ht_trendlinecalculate()
            elif (text == "KAMA"):
                self.kamacalculate()
            elif (text == "MA"):
                self.macalculate()
            elif (text == "MAMA"):
                self.mamacalculate()
            elif (text == "MIDPOINT"):
                self.midpointcalculate()
            elif (text == "MIDPRICE"):
                self.midpricecalculate()
            elif (text == "SAR"):
                self.sarcalculate()
            elif (text == "SAREXT"):
                self.sarextcalculate()
            elif (text == "SMA"):
                self.smacalculate()
            elif (text == "T3"):
                self.t3calculate()
            elif (text == "TEMA"):
                self.temacalculate()
            elif (text == "TRIMA"):
                self.trimacalculate()
            elif (text == "WMA"):
                self.wmacalculate()
            elif (text == "KDJ"):
                self.kdjcalculate()
            elif (text == "ATR"):
                self.atrcalculate()
            elif (text == "NATR"):
                self.natrcalculate()
            elif (text == "TRANGE"):
                self.trangecalculate()
            elif (text == "AD"):
                self.adcalculate()
            elif (text == "ADOSC"):
                self.adosccalculate()
            elif (text == "OBV"):
                self.obvcalculate()
        except BaseException as msg:
            print(str(msg))

    # def baselist(self, text):
    #     self.basechecklist = ["ADX", "ADXR", "APO", "AROON", "AROONOSC", "BOP", "CCI", "CMO", "DX", "RSI", "MACD", "MACDEXT", "MACDFIX", "MFI",
    #                           "MINUS_DI", "MINUS_DM", "MOM", "PLUS_DI", "PLUS_DM", "PPO", "ROC", "ROCP", "ROCR", "ROCR100", "STOCH", "STOCHF",
    #                           "STOCHRSI", "TRIX", "ULTOSC", "WILLR", "HT_DCPERIOD", "HT_DCPHASE", "HT_PHASOR", "HT_SINE", "HT_TRENDMODE",
    #                           "BBANDS", "DEMA", "EMA", "HT_TRENDLINE", "KAMA", "MIDPOINT", "MIDPRICE", "SAR", "MAMA",
    #                           "SAREXT", "SMA", "T3", "TEMA", "TRIMA", "WMA", "KDJ", "ATR", "NATR", "TRANGE", "AD", "ADOSC", "OBV"]
    #     if text in self.basechecklist:
    #         return True
    #     else:
    #         return False

    def matplotlib_main(self):
        matplotlib_Canvas(self.gettersymbolinfo(), self.gettertoolhistory())

    def gettersymbolinfo(self):
        return GlobalValue.get_Symbol_info_var()

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()

    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

    def gettersymbol(self):
        return GlobalValue.get_Symbol_static_var()

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()
