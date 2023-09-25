class MoneyValue(object):

    model = None
    money_perm = {}

    @staticmethod
    def get_model_name_var():
        print('Get Model Name Management Perm')
        return MoneyValue.model

    @staticmethod
    def set_model_name_var(value):
        print('Set Model Name Management Perm')
        MoneyValue.model = value

    @staticmethod
    def get_model_perm_var():
        print('Get Model Value Management Perm')
        return MoneyValue.money_perm

    @staticmethod
    def set_model_perm_var(value):
        print('Set Money Value Management Perm')
        MoneyValue.money_perm = value
