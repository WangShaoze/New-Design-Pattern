"""

Python 的模块本身就是 单例模式

"""

from demo1 import demo1_singleton
from demo2 import demo2_singleton

if __name__ == '__main__':
    s = demo1_singleton
    s.set_a(10)
    s.set_b(30)
    print(s)

    s = demo2_singleton
    s.set_a(1)
    s.set_b(3)
    print(s)
