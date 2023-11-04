from Layout.Method_Class.logger import Logger


class TechValue(object):

    tool_perm = {}
    Entry_perm = {}
    range_perm = {}
    range_entry_perm = {}

    @classmethod
    def get_tech_toolperm_var(cls):
        Logger().info(f"Get Technical indicator properties: {cls.tool_perm}")
        return cls.tool_perm

    @classmethod
    def set_tech_toolperm_var(cls,value):
        Logger().info(f"Set Technical indicator properties: {value}")
        cls.tool_perm = value

    @classmethod
    def get_tech_Entry_var(cls):
        Logger().info(f"Get Exp properties: {cls.Entry_perm}")
        return cls.Entry_perm

    @classmethod
    def set_tech_Entry_var(cls,value):
        Logger().info(f"Set Technical indicator properties: {value}")
        cls.Entry_perm = value
##

    @classmethod
    def get_tech_range_perm(cls):
        Logger().info(f"Get Technical indicator Range : {cls.range_perm}")
        return cls.range_perm

    @classmethod
    def set_tech_range_perm(cls,value):
        Logger().info(f"Set Technical indicator Range: {value}")
        cls.range_perm = value

##
    @classmethod
    def get_entry_range_perm(cls):
        Logger().info(f"Get Exp Range : {cls.range_entry_perm}")
        return cls.range_entry_perm

    @classmethod
    def set_entry_range_perm(cls,value):
        Logger().info(f"Set Exp Range: {value}")
        cls.range_entry_perm = value
