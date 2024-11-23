"""
1.单例模式（线程不安全）
特点：只有在第一次使用这个实例的时候才去创建它，比较 “懒”，等到真正需要了才行动，不过这种简单的实现方式在多线程环境下是不安全的。
"""


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            # cls.__instance = object.__new__(cls)
        return cls.__instance


class Number(Singleton):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return str("实例内存地址:{}, 实例的属性a:{}".format(id(self), self.a))


"""
这里的 __instance 初始化为 None，当第一次调用 Singleton 类来创建实例时，发现 __instance 是 None，
就会创建一个新的实例并赋值给它，后续再调用创建实例时，就直接返回已经存在的这个实例了。

但在多线程并发调用创建实例的场景下，可能会出现多个线程同时判断 __instance 为 None，进而都去创建实例，就破坏了单例的特性了。
"""

if __name__ == '__main__':
    # # 使用示例
    # s1 = Singleton()
    # s2 = Singleton()
    # print(s1 is s2)  # 正常情况下输出 True，但在多线程环境可能有问题

    a = Number(12)
    print(a)
    b = Number(1)
    print(b)
