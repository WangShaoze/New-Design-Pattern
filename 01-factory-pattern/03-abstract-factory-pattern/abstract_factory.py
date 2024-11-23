"""抽象工厂模式"""

from abc import ABCMeta, abstractmethod


# =========== 抽象产品 =============
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class Os(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# =========== 抽象工厂 =============
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# =============== 具体产品 ======= 实现产品接口==
class OppoShell(PhoneShell):
    def show_shell(self):
        print("该手机是OPPO手机")


class HuaWeiShell(PhoneShell):
    def show_shell(self):
        print("该手机是HuaWei手机")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("该手机是Apple手机")


class LongXinCPU(CPU):
    def show_cpu(self):
        print("cpu is: [龙兴]CPU")


class KunPengCPU(CPU):
    def show_cpu(self):
        print("cpu is: [鲲鹏]CPU")


class HaiSiCPU(CPU):
    def show_cpu(self):
        print("cpu is: [海思]CPU")


class XiaoLongCPU(CPU):
    def show_cpu(self):
        print("cpu is: [晓龙]CPU")


class LianFaKeCPU(CPU):
    def show_cpu(self):
        print("cpu is: [联发科]CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("cpu is: [苹果]CPU")


class HongMengOs(Os):
    def show_os(self):
        print("os is:[鸿蒙] os")


class WindowsOs(Os):
    def show_os(self):
        print("os is:[Windows] os")


class LinuxOs(Os):
    def show_os(self):
        print("os is:[Linux] os")


class AndroidOs(Os):
    def show_os(self):
        print("os is:[安卓] os")


class IOSOs(Os):
    def show_os(self):
        print("os is:[IOS] os")


class AppleOs(Os):
    def show_os(self):
        print("os is:[苹果] os")


# 工厂实现工厂接口
class HuaWeiFactory(PhoneFactory):
    def make_shell(self):
        return HuaWeiShell()

    def make_cpu(self):
        return HaiSiCPU()

    def make_os(self):
        return HongMengOs()


class OppoFactory(PhoneFactory):
    def make_shell(self):
        return OppoShell()

    def make_cpu(self):
        return XiaoLongCPU()

    def make_os(self):
        return AndroidOs()


class AppleFactory(PhoneFactory):
    def make_shell(self):
        return AppleShell()

    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return AppleOs()


# 客户端的手机类
class Phone:
    def __init__(self, shell: PhoneShell, os: Os, cpu: CPU):
        self.shell = shell
        self.os = os
        self.cpu = cpu

    def show_info(self):
        print("手机信息:")
        self.shell.show_shell()
        self.os.show_os()
        self.cpu.show_cpu()


# 定义一个制作手机的类
def make_phone(pf: PhoneFactory):
    return Phone(pf.make_shell(), pf.make_os(), pf.make_cpu())


if __name__ == "__main__":
    phone = make_phone(HuaWeiFactory())
    phone.show_info()
    print("=====+++=====")

    phone = make_phone(AppleFactory())
    phone.show_info()
    print("=====+++=====")

    phone = make_phone(OppoFactory())
    phone.show_info()
    print("=====+++=====")
