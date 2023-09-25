import talib
from Global.Value.TechToolParam import TechValue
from Global.Value.UniversalValue import GlobalValue


class math_transform():
    def __init__(self):
        super().__init__()

    def math_ACOS(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["ACOS"] = talib.ACOS(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_ASIN(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["ASIN"] = talib.ASIN(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_ATAN(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["ATAN"] = talib.ATAN(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_CEIL(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["CEIL"] = talib.CEIL(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_COS(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["COS"] = talib.COS(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_COSH(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["COSH"] = talib.COSH(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_EXP(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["EXP"] = talib.EXP(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_FLOOR(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["FLOOR"] = talib.FLOOR(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_LN(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["LN"] = talib.LN(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_LOG10(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["LOG10"] = talib.LOG10(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_SIN(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["SIN"] = talib.SIN(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_SINH(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["SINH"] = talib.SINH(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_SQRT(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["SQRT"] = talib.SQRT(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_TAN(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["TAN"] = talib.TAN(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def math_TANH(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["TANH"] = talib.TANH(self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def settertoolhistory(self, text):
        GlobalValue.set_TechTool_history_var(text)

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()
