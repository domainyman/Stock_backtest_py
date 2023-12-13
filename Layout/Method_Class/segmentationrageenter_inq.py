from Global.Value.UniversalValue import GlobalValue
from Global.Value.TechToolParam import TechValue
from Global.Value.SegmentationRangeValue import SegmentationRange
from Global.Value.MoneyManageParam import MoneyValue
import numpy as np
from prettytable import PrettyTable
import pandas as pd

from Layout.Method_Class.logger import Logger



class seqmentationrange_conv():
    def __init__(self) -> None:
        pass

    def meshgrid_conv(self,combinations_np):
        self.combinations_nps = np.array(combinations_np, dtype=object)
        meshgrid_result = np.meshgrid(*self.combinations_nps)
        self.combinations = np.array(meshgrid_result).T.reshape(-1, len(self.combinations_nps))    
        return self.combinations
        

class seqmentationrange_inq():

    def __init__(self) -> None:
        self.techrange = self.getterEntryRangeTechValue()
        Logger().info(f'seqmentationrange inq {self.techrange}')

    def separationtech(self) -> None:
        try:
            self.matchlist = []
            for tech in self.techrange.keys():
                self.tech_list_perm = self.process_dict(self.techrange[tech])
                if (self.check_instance(self.tech_list_perm, list) == True):
                    self.tech_list_perm_core = self.rebuilding_structure(
                        tech, self.tech_list_perm)
                    self.signresult = self.dict_building_perm(
                        tech, self.tech_list_perm_core)
                    self.matchlist.append(self.signresult)
                elif (self.check_instance(self.tech_list_perm, dict) == True):
                    self.tech_dictlist_perm_core = self.rebuildlist_to_permlist(
                        self.tech_list_perm)
                    self.combination = self.combinations_data(
                        self.tech_dictlist_perm_core)
                    self.rebuild_technames = self.rebuild_techname(
                        tech, self.combination)
                    self.feild_dict = self.rebuilding_feild_name(
                        tech, self.rebuild_technames)
                    self.matchlist.append(self.feild_dict)
            self.combinations = self.combinations_data(self.matchlist)
            self.table = self.PrettyTabletest(
                self.field_name(self.matchlist), self.combinations)
            Logger().info(f'seqmentationrange_inq Table {self.table}')
            self.csv_loading_tech(self.table,self.field_name(self.matchlist))
            return self.combinations
        except Exception as e:
            Logger().error(f"ERROR in seqmentationrange inq Table: {e}")

    def field_name(self, input_list):
        return [list(dic[0].keys())[0] for dic in input_list]

    def PrettyTabletest(self, field, list_core):
        field_names = field
        table = PrettyTable()
        table.field_names = field_names
        for combination in list_core:
            table.add_row(combination)
        return table

    def csv_loading_tech(self, table, field):
        df = pd.DataFrame(table.__dict__['_rows'], columns=field)
        df.to_csv('combinations_tech.csv', index=False)

    def combinations_data(self, combinations_np):
        self.combinations_nps = np.array(combinations_np, dtype=object)
        combinations = np.array(np.meshgrid(
            *self.combinations_nps)).T.reshape(-1, len(self.combinations_nps))
        return combinations

    def rebuild_techname(self, perm_name, tech_list) -> list:
        self.new_list = []
        self.tech_lists = tech_list.tolist()
        self.perm_names = perm_name
        for i in range(len(self.tech_lists)):
            self.merged_dict = {}
            for dictionary in self.tech_lists[i]:
                self.merged_dict.update(dictionary)
            self.new_list.append(self.merged_dict)
        return self.new_list

    def rebuildlist_to_permlist(self, tech_dict_perm) -> list:
        self.radon = []
        self.tech_dict_perm = tech_dict_perm
        self.tech_dict_perms = self.tech_dict_perm.keys()
        for perm in self.tech_dict_perms:
            self.listperm = self.tech_dict_perm[perm]
            if (self.listperm == []):
                self.dictname = []
                result = self.rebuilding_structure(perm, 0)
                self.dictname.append(result)
                self.radon.append(self.dictname)
            else:
                self.dictname = []
                for i in range(len(self.listperm)):
                    result = self.rebuilding_structure(perm, self.listperm[i])
                    self.dictname.append(result)
                self.radon.append(self.dictname)
        return self.radon

    def process_dict(self, dictionary) -> list:
        self.dictionarys = dictionary
        self.keys = self.dictionarys.keys()
        if (self.check_perm(self.keys) == False):
            self.rebuildlists = {}
            for key in self.keys:
                if (isinstance(self.dictionarys[key], dict) == True) and (self.check_perm(self.dictionarys[key]) == True):
                    self.techseqperm = self.seqment_tech_dict(
                        self.dictionarys[key])
                    # self.techseqperm = self.resetzore_to_one(self.techseqperm)
                    self.techseqperm = self.rm_duplicates_list(
                        self.techseqperm)
                    self.rebuildlist = self.rebuilding_structure(
                        key, self.techseqperm)
                    self.rebuildlists.update(self.rebuildlist)

            return self.rebuildlists

        else:
            self.techseqperm = self.seqment_tech_dict(dictionary)
            # self.techseqperm = self.resetzore_to_one(self.techseqperm)
            self.techseqperm = self.rm_duplicates_list(self.techseqperm)
            return self.techseqperm

    def check_instance(self, dict, type):
        if (isinstance(dict, type)):
            return True
        else:
            return False

    def check_perm(self, dict_list) -> bool:
        if list(dict_list) == ['First', 'Last', 'Step']:
            return True
        else:
            return False

    def seqment_tech_dict(self, dicttech) -> list:
        self.first = None
        self.last = None
        self.step = None
        self.targetdict = dicttech
        for perm in self.targetdict:
            if (perm == "First"):
                self.first = dicttech[perm]
            elif (perm == "Last"):
                self.last = dicttech[perm]
            elif (perm == "Step"):
                self.step = dicttech[perm]
        if (self.first == 0) and (self.last == 0) and (self.step == 0):
            return []
        else:
            self.techlist = np.arange(self.first, self.last, self.step, dtype=np.float64).round(3)
            return list(self.techlist)

    def rebuilding_structure(self, key, dict_structure):
        return {key: dict_structure}

    def dict_building_perm(self, key, list_structure):
        return sorted([{key: value} for value in list_structure[key]], key=lambda x: x[key])

    def reset_structure(self, reset_list):
        return [item for sublist in reset_list for item in sublist]

    def rebuilding_sort(self, keys, list_data):
        return sorted(list_data, key=lambda x: x[keys])

    def rebuilding_feild_name(self, key, dictname):
        self.dictnames = dictname
        self.keys = key
        self.new_list = []
        for value in self.dictnames:
            self.new_list.append({self.keys: value})
        return self.new_list

    def rm_duplicates_list(self, list_dup):
        return list(set(list_dup))

    def resetzore_to_one(self, list_step) -> list:
        for i in range(len(list_step)):
            if list_step[i] == 0:
                list_step[i] = 1
        return list_step

    ##########################
    def setterEntryRangeTechValue(self, text):
        TechValue.set_tech_range_perm(text)

    def getterEntryRangeTechValue(self):
        return TechValue.get_tech_range_perm()

    def setterEntryRangeValue(self, text):
        TechValue.set_entry_range_perm(text)

    def getterEntryRangeValue(self):
        return TechValue.get_entry_range_perm()


class seqmentationrange_entry():

    def __init__(self):
        self.techrange = self.getterEntryRangeValue()
        Logger().info(f'seqmentationrange Exp {self.techrange}')

    def separationtech(self) -> None:
        try:
            self.matchlist = []
            for tech in self.techrange.keys():
                self.tech_list_perm = self.process_dict(tech, self.techrange)
                self.combination = self.combinations_data(self.tech_list_perm)
                self.rebuild_technames = self.rebuild_techname(
                    tech, self.combination)
                self.feild_dict = self.rebuilding_feild_name(
                    tech, self.rebuild_technames)
                self.matchlist.append(self.feild_dict)
            self.combinations = self.combinations_data(self.matchlist)
            self.table = self.PrettyTabletest(
                self.field_name(self.matchlist), self.combinations)
            Logger().info(f'seqmentationrange Exp Table {self.table}')
            self.csv_loading_entry(self.table,self.field_name(self.matchlist))
            return self.combinations
        except Exception as e:
            Logger().error(f"ERROR in seqmentationrange Exp Table: {e}")

    def field_name(self, input_list):
        return [list(dic[0].keys())[0] for dic in input_list]

    def PrettyTabletest(self, field, list_core):
        field_names = field
        table = PrettyTable()
        table.field_names = field_names
        for combination in list_core:
            table.add_row(combination)
        return table

    def csv_loading_entry(self, table, field):
        df = pd.DataFrame(table.__dict__['_rows'], columns=field)
        df.to_csv('combinations_entry.csv', index=False)

    def combinations_data(self, combinations_np):
        self.combinations_nps = np.array(combinations_np, dtype=object)
        combinations = np.array(np.meshgrid(
            *self.combinations_nps)).T.reshape(-1, len(self.combinations_nps))
        return combinations

    def rebuild_techname(self, perm_name, tech_list) -> list:
        self.new_list = []
        self.tech_lists = tech_list.tolist()
        self.perm_names = perm_name
        for i in range(len(self.tech_lists)):
            self.merged_dict = {}
            for dictionary in self.tech_lists[i]:
                self.merged_dict.update(dictionary)
            self.new_list.append(self.merged_dict)
        return self.new_list

    def rebuildlist_to_permlist(self, tech_dict_perm) -> list:
        self.radon = []
        self.tech_dict_perm = tech_dict_perm
        self.tech_dict_perms = self.tech_dict_perm.keys()
        for perm in self.tech_dict_perms:
            self.listperm = self.tech_dict_perm[perm]
            if (self.listperm == []):
                self.dictname = []
                result = self.rebuilding_structure(perm, 0)
                self.dictname.append(result)
                self.radon.append(self.dictname)
            else:
                self.dictname = []
                for i in range(len(self.listperm)):
                    result = self.rebuilding_structure(perm, self.listperm[i])
                    self.dictname.append(result)
                self.radon.append(self.dictname)
        return self.radon

    def process_dict(self, keydict, dictionary) -> list:
        self.dictionarys = dictionary[keydict]
        self.keys = self.dictionarys.keys()
        self.rebuildlists = []
        for key in self.keys:
            self.rebuildlist = self.group_option(key, self.dictionarys)
            self.rebuildlists.append(self.rebuildlist)
        return self.rebuildlists

    def group_option(self, key, value):
        self.values = value[key]
        if (self.values == 'Both Test'):
            self.techseqpermfinal = [{key: 'True'}, {key: 'False'}]
        elif (self.values == 'True'):
            self.techseqpermfinal = [{key: 'True'}]
        elif (self.values == 'False'):
            self.techseqpermfinal = [{key: 'False'}]
        elif (list(self.values.keys()) == ['First', 'Last', 'Step']):
            self.techseqperm = self.seqment_tech_dict(self.values)
            # self.techseqperm = self.resetzore_to_one(self.techseqperm)
            self.techseqperm = self.rm_duplicates_list(self.techseqperm)
            self.techseqpermfinal = [self.rebuilding_structure(
                key, techseqperm) for techseqperm in self.techseqperm]
        elif (list(self.values.keys()) == ['GOLDEN CROSS', 'Death Cross']):
            self.techseqperm = self.seqment_techTrue_F_dict(self.values)
            self.combination = self.combinations_data(self.techseqperm)
            self.merged_dict = self.merged_dict_data(self.combination)
            self.techseqpermfinal = [self.rebuilding_structure(
                key, techseqperm) for techseqperm in self.merged_dict]
        return self.techseqpermfinal

    def merged_dict_data(self, data) -> list:
        merged_data = []
        for item in data:
            merged_data.append({**item[0], **item[1]})
        return merged_data

    def check_instance(self, dict, type):
        if (isinstance(dict, type)):
            return True
        else:
            return False

    def check_perm(self, dict_list) -> bool:
        if list(dict_list) == ['First', 'Last', 'Step']:
            return True
        else:
            return False

    def seqment_tech_dict(self, dicttech) -> list:
        self.first = None
        self.last = None
        self.step = None
        self.targetdict = dicttech
        for perm in self.targetdict:
            if (perm == "First"):
                self.first = dicttech[perm]
            elif (perm == "Last"):
                self.last = dicttech[perm]
            elif (perm == "Step"):
                self.step = dicttech[perm]
        if (self.first == 0) and (self.last == 0) and (self.step == 0):
            return []
        else:
            self.techlist = np.arange(self.first, self.last, self.step, dtype=np.float64).round(3)
            return list(self.techlist)

    def seqment_techTrue_F_dict(self, dicttech) -> list:
        self.GOLDEN_CROSS = None
        self.Death_Cross = None
        self.targetdict = dicttech
        for perm in list(self.targetdict.keys()):
            if (perm == "GOLDEN CROSS"):
                self.GOLDEN_CROSS_item = self.targetdict[perm]
                if (self.GOLDEN_CROSS_item == 'Both Test'):
                    self.GOLDEN_CROSS = [{perm: 'True'}, {perm: 'False'}]
                elif (self.GOLDEN_CROSS_item == 'True'):
                    self.GOLDEN_CROSS = [{perm: 'True'}]
                elif (self.GOLDEN_CROSS_item == 'False'):
                    self.GOLDEN_CROSS = [{perm: 'False'}]
            elif (perm == "Death Cross"):
                self.Death_Cross_item = self.targetdict[perm]
                if (self.Death_Cross_item == 'Both Test'):
                    self.Death_Cross = [{perm: 'True'}, {perm: 'False'}]
                elif (self.Death_Cross_item == 'True'):
                    self.Death_Cross = [{perm: 'True'}]
                elif (self.Death_Cross_item == 'False'):
                    self.Death_Cross = [{perm: 'False'}]
        self.techlist = [self.GOLDEN_CROSS, self.Death_Cross]
        return self.techlist

    def rebuilding_structure(self, key, dict_structure):
        return {key: dict_structure}

    def dict_building_perm(self, key, list_structure):
        return sorted([{key: value} for value in list_structure[key]], key=lambda x: x[key])

    def reset_structure(self, reset_list):
        return [item for sublist in reset_list for item in sublist]

    def rebuilding_sort(self, keys, list_data):
        return sorted(list_data, key=lambda x: x[keys])

    def rebuilding_feild_name(self, key, dictname):
        self.dictnames = dictname
        self.keys = key
        self.new_list = []
        for value in self.dictnames:
            self.new_list.append({self.keys: value})
        return self.new_list

    def rm_duplicates_list(self, list_dup):
        return list(set(list_dup))

    def resetzore_to_one(self, list_step) -> list:
        for i in range(len(list_step)):
            if list_step[i] == 0:
                list_step[i] = 1
        return list_step

    def setterEntryRangeTechValue(self, text):
        TechValue.set_tech_range_perm(text)

    def getterEntryRangeTechValue(self):
        return TechValue.get_tech_range_perm()

    def setterEntryRangeValue(self, text):
        TechValue.set_entry_range_perm(text)

    def getterEntryRangeValue(self):
        return TechValue.get_entry_range_perm()


