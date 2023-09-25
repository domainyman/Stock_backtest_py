class GlobalValue(object):

    symbol = ""
    info = {}
    history = None
    news = []
    TechTool = None
    AATechTool = None

    @staticmethod
    def get_Symbol_static_var():
        print('Get Symbol Name : ' + GlobalValue.symbol)
        return GlobalValue.symbol

    @staticmethod
    def set_Symbol_static_var(value):
        print('Set Symbol Name : ' + value)
        GlobalValue.symbol = value

    @staticmethod
    def get_Symbol_info_var():
        print('Get Symbol Info')
        return GlobalValue.info

    @staticmethod
    def set_Symbol_info_var(value):
        print('Set Symbol Info')
        GlobalValue.info = value

    @staticmethod
    def get_Symbol_history_var():
        print('Get Symbol History')
        return GlobalValue.history

    @staticmethod
    def set_Symbol_history_var(value):
        print('Set Symbol History')
        GlobalValue.history = value

    @staticmethod
    def get_Symbol_new_var():
        print('Get Symbol News')
        return GlobalValue.news

    @staticmethod
    def set_Symbol_new_var(value):
        print('Set Symbol News')
        GlobalValue.news = value

    @staticmethod
    def get_TechTool_history_var():
        # print('Get Tech History')
        return GlobalValue.TechTool

    @staticmethod
    def set_TechTool_history_var(value):
        print('Set Tech History')
        GlobalValue.TechTool = value

    @staticmethod
    def get_AATechTool_history_var():
        print('Get AA_Tech History')
        return GlobalValue.AATechTool

    @staticmethod
    def set_AATechTool_history_var(value):
        print('Set AA_Tech History')
        GlobalValue.AATechTool = value
