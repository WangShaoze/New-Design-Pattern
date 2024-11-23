"""
外观模式

"""


class Cpu:
    """定义子类系统的类 ----- 1 """

    def run(self):
        print("CUP 开始工作....")

    def stop(self):
        print("CUP 停止工作....")


class Memory:
    """定义子类系统的类 ----- 2 """

    def run(self):
        print("MEM 开始工作....")

    def stop(self):
        print("MEM 停止工作....")


class Disk:
    """定义子类系统的类 ----- 3 """

    def run(self):
        print("硬盘 开始工作....")

    def stop(self):
        print("硬盘 停止工作....")


class Computer:
    """ 定义外观 """

    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


if __name__ == '__main__':
    computer = Computer()
    computer.run()
    print("正在提供服务......")
    print("正在提供服务......")
    print("正在提供服务......")
    print("正在提供服务......")
    print("正在提供服务......")
    computer.stop()
