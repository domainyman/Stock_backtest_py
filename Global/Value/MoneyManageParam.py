from Layout.Method_Class.logger import Logger


class MoneyValue(object):

    model = None
    money_perm = {}

    @classmethod
    def get_model_name_var(cls):
        Logger().info(f"Get Model Name: {cls.model}")
        return MoneyValue.model

    @classmethod
    def set_model_name_var(cls, value):
        Logger().info(f"Set Model Name: {value}")
        MoneyValue.model = value

    @classmethod
    def get_model_perm_var(cls):
        Logger().info(f"Get Model Perm: {cls.money_perm}")
        return MoneyValue.money_perm

    @classmethod
    def set_model_perm_var(cls, value):
        Logger().info(f"Set Model Perm: {value}")
        MoneyValue.money_perm = value
