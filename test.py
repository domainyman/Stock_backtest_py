import numpy as np
from prettytable import PrettyTable
import pandas as pd


class test:

    def __init__(self):
        self.techrange = {'RSI': {'HIGH': {'First': 0, 'Last': 100, 'Step': 25}, 'LOW': {'First': 0, 'Last': 100, 'Step': 25}},
                          'MACD': {'GOLDEN CROSS': 'Both Test', 'Death Cross': 'Both Test'}}

    def separationtech(self) -> None:
        try:
            self.matchlist = []
            for tech in self.techrange.keys():
                self.tech_list_perm = self.process_dict(self.techrange[tech])
                # print(tech,self.tech_list_perm)
                # if (self.check_instance(self.tech_list_perm, dict)):
                #     print("******dict*******")
                #     self.tech_dictlist_perm_core = self.rebuildlist_to_permlist(
                #         self.tech_list_perm)
                #     self.combination = self.combinations_data(
                #         self.tech_dictlist_perm_core)
                #     self.rebuild_technames = self.rebuild_techname(
                #         tech, self.combination)
                #     self.feild_dict = self.rebuilding_feild_name(
                #         tech, self.rebuild_technames)
                #     self.matchlist.append(self.feild_dict)
            # self.matchlist = self.reset_structure(self.matchlist)
            # self.combinations = self.combinations_data(self.matchlist)
            # self.table = self.PrettyTabletest(
            #     self.field_name(self.matchlist), self.combinations)
            # print(self.table)
            # self.csv_loading(self.table,self.field_name(self.matchlist))
            return self.matchlist
        except Exception as e:
            print(e)

    def field_name(self, input_list):
        return [list(dic[0].keys())[0] for dic in input_list]

    def PrettyTabletest(self, field, list_core):
        field_names = field
        table = PrettyTable()
        table.field_names = field_names
        for combination in list_core:
            table.add_row(combination)
        return table

    def csv_loading(self, table, field):
        df = pd.DataFrame(table.__dict__['_rows'], columns=field)
        df.to_csv('combinations.csv', index=False)

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
        self.rebuildlists = {}
        for key in self.keys:
            self.group_option(self.dictionarys[key])
        #             self.techseqperm = self.seqment_tech_dict(
        #                 self.dictionarys[key])
        #             self.techseqperm = self.resetzore_to_one(self.techseqperm)
        #             self.techseqperm = self.rm_duplicates_list(
        #                 self.techseqperm)
        #             self.rebuildlist = self.rebuilding_structure(
        #                 key, self.techseqperm)
        #             self.rebuildlists.update(self.rebuildlist)

        #     return self.rebuildlists

        # else:
        #     self.techseqperm = self.seqment_tech_dict(dictionary)
        #     self.techseqperm = self.resetzore_to_one(self.techseqperm)
        #     self.techseqperm = self.rm_duplicates_list(self.techseqperm)
        #     return self.techseqperm

    def group_option(self, value):
        self.values = value
        if (self.values == 'Both Test'):
            print("TURE")
        elif (list(self.values.keys()) == ['First', 'Last', 'Step']):
            self.techseqperm = self.seqment_tech_dict(self.values)
            self.techseqperm = self.resetzore_to_one(self.techseqperm)
            self.techseqperm = self.rm_duplicates_list(self.techseqperm)
            print(self.techseqperm)

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
            self.techlist = range(self.first, self.last, self.step)
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


if __name__ == "__main__":
    test().separationtech()
