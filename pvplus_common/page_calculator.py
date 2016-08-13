# coding:utf-8


class PageCalculator():
    @staticmethod
    def start(pindex: int, psize: int) -> int:
        return (pindex - 1) * psize

    @staticmethod
    def end(pindex: int, psize: int) -> int:
        return pindex * psize



