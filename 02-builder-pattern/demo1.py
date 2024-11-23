"""
可以通过建造者模式构建复杂公式
二元一次方程组的定义:
    二元一次方程组是指含有两个未知数（例如x和y），并且所含未知数的项的次数都是1的方程组。每个方程可以化简为ax+by=c的形式
二元一次方程的求根公式为：x1=(-b+(b^2-4ac)^1/2)/2a，x2=(-b-(b^2-4ac)^1/2)/2a，其中a不等于0
"""
from typing import Union


class QiuGenFormulate:
    IRREGULAR_DEFINE_FOR_ER_YUAN = "不满足二元一次方程的定义规范"
    DOUBLE_A = None
    FOUR_A_C = None
    DEI_TA = None
    x1 = None
    x2 = None

    def __init__(self, a: Union[int, float] = None, b: Union[int, float] = None, c: Union[int, float] = None):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def set_a(self, a: Union[int, float]):
        self.a = float(a)

    def set_b(self, b: Union[int, float]):
        self.b = float(b)

    def set_c(self, c: Union[int, float]):
        self.c = float(c)

    def sure_a_regular(self):
        if self.a == 0 or self.b == 0:
            raise Exception(self.IRREGULAR_DEFINE_FOR_ER_YUAN)
        return self

    def double_a(self):
        self.DOUBLE_A = 2 * self.a
        return self

    def four_a_c(self):
        self.FOUR_A_C = 4 * self.a * self.c
        return self

    def dei_ta(self):
        self.DEI_TA = pow((pow(self.b, 2) - self.FOUR_A_C), 0.5)
        return self

    def cal_x1_x2(self):
        self.x1 = round((self.DEI_TA - self.b) / self.DOUBLE_A, 2)
        self.x2 = round((0 - (self.DEI_TA + self.b)) / self.DOUBLE_A, 2)
        return self


if __name__ == "__main__":
    gens = QiuGenFormulate(2, -5, 2)
    gens = gens.sure_a_regular().double_a().four_a_c().dei_ta().cal_x1_x2()
    print("x1:{}, x2:{}".format(gens.x1, gens.x2))
