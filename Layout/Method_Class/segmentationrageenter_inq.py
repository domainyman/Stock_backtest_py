from Global.Value.UniversalValue import GlobalValue
from Global.Value.TechToolParam import TechValue
from Global.Value.SegmentationRangeValue import SegmentationRange
from Global.Value.MoneyManageParam import MoneyValue


class seqmentationrange():
    def __init__(self) -> None:
        pass

    def separationtech(self) -> list:
        self.retlist = []
        self.techrange = self.getterEntryRangeTechValue()
        self.process_dict(self.techrange)

        return self.retlist
    
    def process_dict(self,dictionary):
        for key, value in dictionary.items():
            print(key + ":")
            if isinstance(value, dict):
                self.process_dict(value)
            else:
                print(value)


    def seqment_tech_dict(self, dicttech, permkey) -> list:
        self.first = None
        self.last = None
        self.step = None
        self.targetdict = dicttech[permkey]
        for perm in self.targetdict:
            if (perm == "First"):
                self.first = dicttech[permkey][perm]
            elif (perm == "Last"):
                self.last = dicttech[permkey][perm]
            elif (perm == "Step"):
                self.step = dicttech[permkey][perm]
        self.techlist = range(self.first, self.last, self.step)
        return list(self.techlist)

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
