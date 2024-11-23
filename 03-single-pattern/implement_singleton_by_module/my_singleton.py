"""

Python模块本身就是一个天然的单例模式。模块在第一次导入时被初始化，之后再次导入时直接返回已经加载的模块。

"""


class Singleton:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def __str__(self):
        if self.a is None:
            self.a = 0
        if self.b is None:
            self.b = 0
        return "实例id:{}, 求和计算:[{},{}]={}".format(id(self), self.a, self.b, sum([self.a, self.b]))


singleton = Singleton()
