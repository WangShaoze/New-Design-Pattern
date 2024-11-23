"""

3.单例模式(通过装饰器实现)
特点：在类加载的时候就立即创建实例，不管之后是否会用到这个实例，就像一个饥饿的人迫不及待地把食物准备好一样，所以称为 “饿汉式”

"""


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton  # AddClass = singleton(AddClass)
class AddClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return "实例：{} add[{},{}]={}".format(id(self), self.a, self.b, self.a + self.b)


@singleton
class ExchangeClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def reuslt(self):
        self.a, self.b = self.b, self.a

    def __str__(self):
        self.reuslt()
        return "a:{}, b:{}".format(self.a, self.b)


if __name__ == '__main__':
    add = AddClass(12, 34)
    print(add.get_sum())

    add = AddClass(12, 35)
    print(add.get_sum())

    s = ExchangeClass(23, 89)
    print(s)

    s = ExchangeClass(34, 12)
    print(s)
