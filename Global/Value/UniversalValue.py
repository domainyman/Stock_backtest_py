from Layout.Method_Class.logger import Logger

class GlobalValue:
    symbol = ""
    info = {}
    history = None
    news = []
    TechTool = None

    @classmethod
    def get_Symbol_static_var(cls):
        Logger().info(f"Get Symbol Name: {cls.symbol}")
        return cls.symbol

    @classmethod
    def set_Symbol_static_var(cls, value):
        Logger().info(f"Set Symbol Name: {value}")
        cls.symbol = value

    @classmethod
    def get_Symbol_info_var(cls):
        Logger().info(f"Get Symbol Info: {cls.info}")
        return cls.info

    @classmethod
    def set_Symbol_info_var(cls, value):
        Logger().info(f"Set Symbol Info: {value}")
        cls.info = value

    @classmethod
    def get_Symbol_history_var(cls):
        Logger().info(f"Get Symbol History: {cls.history}")
        return cls.history

    @classmethod
    def set_Symbol_history_var(cls, value):
        Logger().info(f"Set Symbol History: {value}")
        cls.history = value

    @classmethod
    def get_Symbol_new_var(cls):
        Logger().info(f"Get Symbol News: {cls.news}")
        return cls.news

    @classmethod
    def set_Symbol_new_var(cls, value):
        Logger().info(f"Set Symbol News: {value}")
        cls.news = value

    @classmethod
    def get_TechTool_history_var(cls):
        Logger().info(f"Get Symbol Stock History")
        return cls.TechTool

    @classmethod
    def set_TechTool_history_var(cls, value):
        Logger().info(f"Set Symbol Stock History")
        cls.TechTool = value