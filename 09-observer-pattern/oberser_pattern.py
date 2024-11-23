"""
观察者模式 -----> 发布订阅模式
"""
from abc import ABCMeta, abstractmethod
from typing import List


class Observer(metaclass=ABCMeta):  # 抽象观察者
    @abstractmethod
    def update(self, notice):
        pass


class Notice:  # 消息制造者类
    def __init__(self):
        self.observers: List[Observer] = []  # 所有加入到通知群

    def follow(self, obs:Observer):
        self.observers.append(obs)  # 点关注

    def unfollow(self, obs:Observer):
        self.observers.remove(obs)  # 点取关

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class BoZhu(Notice):  # 博主  具体的消息制造者
    def __init__(self):
        super().__init__()
        self.__info = None

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, msg):
        self.__info = msg
        self.notify()


class Fans(Observer):  # 具体观察者
    def __init__(self):
        self.__info = None

    def update(self, notice):
        self.__info = notice.info

    def get_message(self):
        return self.__info


if __name__ == "__main__":
    f1 = Fans()
    f2 = Fans()
    f3 = Fans()

    bo_zhu = BoZhu()
    bo_zhu.follow(f1)
    bo_zhu.follow(f2)

    bo_zhu.info = "这是我发布的第一个作品"

    print(f1.get_message())
    print(f2.get_message())
    print(f3.get_message())

    bo_zhu.unfollow(f1)
    bo_zhu.follow(f2)
    bo_zhu.follow(f3)
    bo_zhu.info = "这是我发布的第二个作品"

    print(f1.get_message())
    print(f2.get_message())
    print(f3.get_message())
