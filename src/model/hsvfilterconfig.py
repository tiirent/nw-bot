from model.hsvfilter import HsvFilter

class HsvFilterConfig:

    @staticmethod
    def getReelFilter():
        return HsvFilter(0, 217, 0, 179, 255, 255, 0, 0, 0, 0)

    @staticmethod
    def getFishIconFilter():
        return HsvFilter(0, 0, 0, 179, 3, 255, 0, 0, 0, 0)

    @staticmethod
    def getSuccessFilter():
        return HsvFilter(0, 0, 165, 173, 49, 255, 0, 0, 0, 0)