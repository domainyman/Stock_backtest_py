class SegmentationRange(object):

    entryRangelist = []
    techRangelist = []

    @staticmethod
    def get_entryRangelist_var():
        print('Get Entry Range list')
        return SegmentationRange.entryRangelist

    @staticmethod
    def set_techRangelist_var(value):
        print('Set Entry Range list')
        SegmentationRange.entryRangelist = value

    @staticmethod
    def get_techRangelist_var():
        print('Get Tech Range list')
        return SegmentationRange.entryRangelist

    @staticmethod
    def set_techRangelist_var(value):
        print('Set Tech Range list')
        SegmentationRange.entryRangelist = value