import numpy as np


class test:

    def __init__(self):
        self.techrange = {
            'ADX': {
                'First': 0,
                'Last': 100,
                'Step': 25
            },
            'BBANDS': {
                'timeperiod': {
                    'First': 0,
                    'Last': 100,
                    'Step': 25
                },
                'nbdevup': {
                    'First': 0,
                    'Last': 0,
                    'Step': 0
                },
                'nbdevdn': {
                    'First': 0,
                    'Last': 0,
                    'Step': 0
                },
                'matype': {
                    'First': 0,
                    'Last': 8,
                    'Step': 1
                }
            }
        }

    def separationtech(self) -> None:
        for tech in self.techrange.keys():
            self.tech_list_perm = self.process_dict(self.techrange[tech])
            if (self.check_instance(self.tech_list_perm, list)):
                self.tech_list_perm_core = self.rebuilding_structure(
                    tech, self.tech_list_perm)
                result = self.dict_building_perm(
                    tech, self.tech_list_perm_core)
                print(self.tech_list_perm_core)
            elif (self.check_instance(self.tech_list_perm, dict)):
                self.tech_dictlist_perm_core = self.rebuildlist_to_permlist(
                    self.tech_list_perm)
                print(self.tech_dictlist_perm_core)

    def rebuildlist_to_permlist(self, tech_dict_perm):
        self.radon = []
        self.tech_dict_perm = tech_dict_perm
        self.tech_dict_perms = self.tech_dict_perm.keys()
        for perm in self.tech_dict_perms:
            self.listperm = self.tech_dict_perm[perm]
            if (self.listperm == []):
                result = self.rebuilding_structure(perm, 0)
                self.radon.append(result)
            else:
                result = self.rebuilding_structure(perm, self.listperm)
                self.radon.append(result)
                # for i in range(len(self.listperm)):
                # result =self.rebuilding_structure(perm,self.listperm[i])
                # self.radon.append(result)

        return self.radon

    def process_dict(self, dictionary) -> list:
        self.dictionarys = dictionary
        self.keys = self.dictionarys.keys()
        if (self.check_perm(self.keys) == False):
            self.rebuildlists = {}
            for key in self.keys:
                if (isinstance(self.dictionarys[key], dict)) and (self.check_perm(self.dictionarys[key]) == True):
                    self.techseqperm = self.seqment_tech_dict(
                        self.dictionarys[key])
                    self.techseqperm = self.resetzore_to_one(self.techseqperm)
                    self.techseqperm = self.rm_duplicates_list(
                        self.techseqperm)
                    self.rebuildlist = self.rebuilding_structure(
                        key, self.techseqperm)
                    self.rebuildlists.update(self.rebuildlist)

            return self.rebuildlists

        else:
            self.techseqperm = self.seqment_tech_dict(dictionary)
            self.techseqperm = self.resetzore_to_one(self.techseqperm)
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
            self.techlist = range(self.first, self.last, self.step)
            return list(self.techlist)

    def rebuilding_structure(self, key, dict_structure):
        return {key: dict_structure}

    def dict_building_perm(self, key, list_structure):
        return [{key: value} for value in list_structure[key]]

    def rm_duplicates_list(self, list_dup):
        return list(set(list_dup))

    def resetzore_to_one(self, list_step) -> list:
        for i in range(len(list_step)):
            if list_step[i] == 0:
                list_step[i] = 1
        return list_step


if __name__ == "__main__":
    test().separationtech()
