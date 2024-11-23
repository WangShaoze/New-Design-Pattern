""" 以三角形的例子为例，初步认识建造者模式 """


class SanJaoXinBuilder:
    C = None  # 周长
    S = None  # 面积

    CAN_NOT_DEFINE_ERROR = "不满足三角形定义条件"

    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def set_a(self, a):
        self.a = float(a)
        return self

    def set_b(self, b):
        self.b = float(b)
        return self

    def set_c(self, c):
        self.c = float(c)
        return self

    def is_san_jiao_xing(self):
        return (sum([self.b, self.c]) > self.c) and (sum([self.a, self.b]) > self.c) and (
                sum([self.a, self.c]) > self.b)

    def hai_lun_len(self):
        """通过海伦公式计算出三角形的面积时候会用到的半周长"""
        if self.is_san_jiao_xing():
            return sum([self.a, self.b, self.c]) * 0.5
        else:
            raise Exception(self.CAN_NOT_DEFINE_ERROR)

    def builder(self):
        if not self.is_san_jiao_xing():
            raise Exception(self.CAN_NOT_DEFINE_ERROR)
        p = self.hai_lun_len()
        self.C = 2 * p
        self.S = pow((p - self.a) * (p - self.b) * (p - self.c) * p, 0.5)
        return self

    def __str__(self):
        return "三角形:(a:{}, b:{}, c:{})".format(self.a, self.b, self.c)


if __name__ == "__main__":
    c = SanJaoXinBuilder()
    c = c.set_a(3).set_b(4).set_c(5).builder()
    print("c 这个三角形的 面积:{}, 周长:{}".format(c.S, c.C))
