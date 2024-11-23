from demo1 import demo1_singleton
from demo2 import demo2_singleton

if __name__ == '__main__':
    s = demo1_singleton
    s.set_a(10)
    s.set_b(30)
    print(s)

    s1 = demo2_singleton
    s1.set_a(1)
    s1.set_b(3)
    print(s1)
