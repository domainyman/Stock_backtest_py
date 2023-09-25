import talib
from Global.Value.UniversalValue import GlobalValue


class math_operator():
    def __init__(self):
        super().__init__()

    def math_add(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["ADD"] = talib.ADD(self.datadb["High"], self.datadb["Low"])
        self.settertoolhistory(self.datadb)

    def math_div(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["DIV"] = talib.DIV(self.datadb["High"], self.datadb["Low"])
        self.settertoolhistory(self.datadb)

    def math_max(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["MAX"] = talib.MAX(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def math_maxindex(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["MAXINDEX"] = talib.MAXINDEX(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def math_min(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["MIN"] = talib.MIN(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def math_minmax(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["MINMAX_MIN"], self.datadb["MINMAX_MAX"] = talib.MINMAX(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def math_minmaxindex(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["MINMAXINDEX_MINIDX"], self.datadb["MINMAXINDEX_MAXIDX"] = talib.MINMAXINDEX(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def math_mult(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["MULT"] = talib.MULT(
            self.datadb["High"], self.datadb["Low"])
        self.settertoolhistory(self.datadb)

    def math_sub(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["SUB"] = talib.SUB(self.datadb["High"], self.datadb["Low"])
        self.settertoolhistory(self.datadb)

    def math_sum(self, timeperiodtime=30):
        self.datadb = self.gettertoolhistory()
        self.datadb["SUM"] = talib.SUM(
            self.datadb["Close"], timeperiod=int(timeperiodtime))
        self.settertoolhistory(self.datadb)

    def settertoolhistory(self, text):
        GlobalValue.set_TechTool_history_var(text)

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()
