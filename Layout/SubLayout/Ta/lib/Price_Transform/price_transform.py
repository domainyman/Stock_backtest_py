import talib
from Global.Value.UniversalValue import GlobalValue


class price_transform():
    def __init__(self):
        super().__init__()

    def price_transform_Average_Price(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["AVGPRICE"] = talib.AVGPRICE(
            self.datadb["Open"], self.datadb["High"], self.datadb["Low"], self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def price_transform_Median_Price(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["MEDPRICE"] = talib.MEDPRICE(
            self.datadb["High"], self.datadb["Low"])
        self.settertoolhistory(self.datadb)

    def price_transform_Typical_Price(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["TYPPRICE"] = talib.TYPPRICE(
            self.datadb["High"], self.datadb["Low"], self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def price_transform_Weighted_Close_Price(self):
        self.datadb = self.gettertoolhistory()
        self.datadb["WCLPRICE"] = talib.WCLPRICE(
            self.datadb["High"], self.datadb["Low"], self.datadb["Close"])
        self.settertoolhistory(self.datadb)

    def settertoolhistory(self, text):
        GlobalValue.set_TechTool_history_var(text)

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()
