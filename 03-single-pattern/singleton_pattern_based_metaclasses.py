"""
4. 基于元类的单例模式
特点：利用 Python 的元类（metaclass）特性来控制类的创建过程，从而实现单例模式，这种方式相对比较高级一些。
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == '__main__':
    # 使用示例
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # 输出 True
