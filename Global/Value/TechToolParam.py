class TechValue(object):

    tool_perm = {}
    Entry_perm = {}
    range_perm = {}

    @staticmethod
    def get_tech_toolperm_var():
        print('Get Tech Tool Perm')
        return TechValue.tool_perm

    @staticmethod
    def set_tech_toolperm_var(value):
        print('Set Tech Tool Perm')
        TechValue.tool_perm = value

    @staticmethod
    def get_tech_Entry_var():
        print('Get Entry Tech Perm')
        return TechValue.Entry_perm

    @staticmethod
    def set_tech_Entry_var(value):
        print('Set Entry Tech Perm')
        TechValue.Entry_perm = value

    @staticmethod
    def get_tech_range_perm():
        print('Get Tool Range Tech Perm')
        return TechValue.range_perm

    @staticmethod
    def set_tech_range_perm(value):
        print('Set Tool Range Tech Perm')
        TechValue.range_perm = value
