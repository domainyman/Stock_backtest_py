class SegmentationRange(object):

    ret_profo = []

    
###############

    @staticmethod
    def get_ret_profo_var():
        # print('Get ret_profo list')
        return SegmentationRange.ret_profo

    @staticmethod
    def set_ret_profo_var(value):
        # print('Set ret_profo list')
        SegmentationRange.ret_profo = value

    @staticmethod
    def add_ret_profo_var(value):
        # print('Add ret_profo list')
        SegmentationRange.ret_profo.append(value)