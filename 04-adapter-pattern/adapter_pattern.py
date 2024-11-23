"""
适配器模式
"""
from abc import ABCMeta, abstractmethod


# =============== 内部系统顶层接口 ========================
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# =============== 内部系统支付产品 ========================
class WeChatPayment(Payment):
    def pay(self, money):
        print("正在使用微信支付{}元".format(money))


class AlyPayPayment(Payment):
    def pay(self, money):
        print("正在使用支付宝支付{}元".format(money))


# =============== 外部系统支付产品 ========================
class YinLianPayment:
    def cost(self, money):
        print("正在使用银联支付{}元".format(money))


class ApplePayment:
    def cost(self, money):
        print("正在使用苹果支付{}元".format(money))


# =============== 外部系统适配器 ========================
class YinLianPaymentAdapter(Payment, YinLianPayment):  # 多继承的方式实现适配器
    def pay(self, money):
        YinLianPayment().cost(money)


class CostPaymentAdapter(Payment):  # 通过组合的模式实现适配
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


# =============== Client ========================
def pay(payment: Payment, money):
    payment.pay(money)


if __name__ == '__main__':
    pay(WeChatPayment(), 220)
    pay(AlyPayPayment(), 220)
    pay(YinLianPaymentAdapter(), 220)
    pay(CostPaymentAdapter(YinLianPayment()), 220)
    pay(CostPaymentAdapter(ApplePayment()), 220)
