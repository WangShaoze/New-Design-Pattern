"""
2. 线程安全的懒汉式单例模式（使用锁）
特点：同样是在第一次使用时创建实例，不过通过加锁机制保证了在多线程环境下的安全性，避免多个线程同时创建实例的问题
"""

import threading


class Singleton:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # cls.__lock.acquire()
        # if not cls.__instance:
        #     cls.__instance = super().__new__(cls)
        #     cls.__lock.release()
        # return cls.__instance
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                # cls.__instance = object.__new__(cls)
        return cls.__instance


class Number(Singleton):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return str("实例内存地址:{}, 实例的属性a:{}".format(id(self), self.a))


if __name__ == '__main__':

    # 多线程测试示例
    def test_singleton(num: int):
        s = Number(num)

        print("线程{}:{}, Number instance:{}".format(num, id(s), s))


    threads = [threading.Thread(target=test_singleton, args=(u,)) for u in range(160)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
