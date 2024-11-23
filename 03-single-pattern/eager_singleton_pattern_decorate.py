"""

2. 饿汉式单例模式(通过装饰器实现)
特点：在类加载的时候就立即创建实例，不管之后是否会用到这个实例，就像一个饥饿的人迫不及待地把食物准备好一样，所以称为 “饿汉式”

"""


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class AddClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return "实例：{} add[{},{}]={}".format(id(self), self.a, self.b, self.a + self.b)


@singleton
class SumClass:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return "实例：{} sum[{},{}]={}".format(id(self), self.a, self.b, self.a + self.b)


if __name__ == '__main__':
    mc = AddClass(1, 2)
    print(mc.get_sum())
    mc = AddClass(109, 1)
    print(mc.get_sum())

    mc = SumClass(1, 2)
    print(mc.get_sum())
    mc = SumClass(109, 1)
    print(mc.get_sum())
