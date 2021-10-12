from hsvfilter import HsvFilter

class HsvFilterConfig:

    # @staticmethod
    # def getTrentoFilter():
    #     return HsvFilter(11, 89, 205, 31, 200, 255, 79, 0, 0, 4)

    @staticmethod
    def getKidMannieFilter():
        return HsvFilter(0, 29, 255, 0, 255, 255, 0, 4, 0, 0)

    @staticmethod
    def getArrowFilter():
        return HsvFilter(26, 252, 0, 30, 255, 255, 0, 0, 0, 0)

    # @staticmethod
    # def getWatchFilter():
    #     return HsvFilter(19, 0, 193, 38, 33, 255, 0, 0, 20, 0)

    @staticmethod
    def getWatchFilter():
        return HsvFilter(103, 63, 11, 133, 151, 219, 52, 0, 0, 42)

    @staticmethod
    def getTrentoFilter():
        return HsvFilter(83, 104, 219, 105, 192, 248, 24, 81, 0, 0)

    @staticmethod
    def getWraithFilter():
        return HsvFilter(0, 0, 217, 145, 37, 255, 0, 0, 0, 0)

    # @staticmethod
    # def getWeedFilter():
    #     return HsvFilter(52,45,90,76,209,227,0,0,0,32)

    @staticmethod
    def getWeedFilter():
        return HsvFilter(0,0,219,179,29,254,0,0,34,0)
