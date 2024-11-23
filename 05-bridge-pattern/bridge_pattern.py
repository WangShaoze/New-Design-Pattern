"""
桥模式:
    方便一个事物的多个维度扩展

    球 :
        维度1 形状（球体， 椭球体）
        维度2 弹力 （弱弹力，强弹力）
        维度3 条纹
    通过实现不同维度就可得到不同的球，如篮球、排球、橄榄球

    需求: 使用细线画一个绿色的圆
    平面事物:
        第一个维度: 形状  （圆形）
        第二个维度: 颜色  （绿色）
        第三个维度: 粗细  （细线）
"""

from abc import ABCMeta, abstractmethod


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Thickness(metaclass=ABCMeta):
    @abstractmethod
    def discript(self, shape):
        pass


class Shape(metaclass=ABCMeta):
    def __init__(self, color: Color, thickness: Thickness):
        self.color = color
        self.thickness = thickness

    @abstractmethod
    def draw(self):
        pass


class Green(Color):
    def paint(self, shape):
        return "绿"


class Red(Color):
    def paint(self, shape):
        return "红"


class Black(Color):
    def paint(self, shape):
        return "黑"


class ThinLine(Thickness):
    def discript(self, shape):
        return "细"


class ThickLine(Thickness):
    def discript(self, shape):
        return "粗"


class Circle(Shape):
    def draw(self):
        print("用{}线画{}色圆".format(self.thickness.discript(self), self.color.paint(self)))


class Rectangle(Shape):
    def draw(self):
        print("用{}线画{}色正方形".format(self.thickness.discript(self), self.color.paint(self)))


class Heart(Shape):
    def draw(self):
        print("用{}线画{}色心形".format(self.thickness.discript(self), self.color.paint(self)))


if __name__ == "__main__":
    c = Circle(Green(), ThinLine())
    c.draw()

    r = Rectangle(Green(), ThinLine())
    r.draw()

    r = Rectangle(Red(), ThinLine())
    r.draw()

    r = Rectangle(Red(), ThickLine())
    r.draw()

    c = Circle(Green(), ThickLine())
    c.draw()

    h = Heart(Red(), ThickLine())
    h.draw()

    h = Heart(Black(), ThickLine())
    h.draw()
