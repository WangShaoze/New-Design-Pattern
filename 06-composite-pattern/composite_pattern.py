"""
组合模式

组合模式是一种结构型设计模式，它允许你将对象组合成树形结构来表示 “部分 - 整体” 的层次关系。
组合模式使得用户对单个对象和组合对象的使用具有一致性。


"""
from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    """抽象组件"""

    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    """点 ---- 叶子组件"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'点({self.x}, {self.y})'

    def draw(self):
        print(str(self))


class Line(Graphic):
    """线 ---- 叶子组件"""

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"线({self.p1}, {self.p1})"

    def draw(self):
        print(str(self))


class Circle(Graphic):
    """圆 --- 叶子组件"""

    def __init__(self, r):
        self.r = r

    def __str__(self):
        return "半径为{}圆".format(self.r)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    """符合组件"""

    def __init__(self, iterable: List[Graphic]):
        self.children = []
        for i in iterable:
            self.add(i)

    def add(self, p: Graphic):
        self.children.append(p)

    def draw(self):
        print("===================复合图形===================")
        for child in self.children:
            child.draw()
        print("===================复合图形===================")
        print()


if __name__ == '__main__':
    p1 = Point(12, 43)
    p2 = Point(12, 48)
    l1 = Line(p1, p2)
    l2 = Line(Point(32, 43), Point(32, 48))
    pic1 = Picture([l1, p1, p2, l2, Circle(4)])
    pic1.draw()

    p1.draw()
    p2.draw()

    l1.draw()
    l2.draw()

    c = Circle(12)
    c1 = Circle(12)
    c.draw()
    c1.draw()

    pic2 = Picture([l1, l2])
    pic2.draw()

    pic3 = Picture([pic1, pic2])
    pic3.draw()
