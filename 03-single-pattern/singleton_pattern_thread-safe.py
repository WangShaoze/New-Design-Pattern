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


if __name__ == '__main__':

    # 多线程测试示例
    def test_singleton(num: int):
        s = Singleton()
        print("线程{}:{}".format(num, id(s)))

    threads = [threading.Thread(target=test_singleton, args=(u,)) for u in range(160)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
