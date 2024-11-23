"""简单工厂模式"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """ 支付方法的抽象接口  """

    @abstractmethod
    def pay(self, money):
        pass


# ==================== 具体的支付实现 ========================
class WeChatPayment(Payment):
    def __init__(self, pay_type: str = None):
        self.pay_type = pay_type

    def pay(self, money):
        if self.pay_type:
            print("您使用[微信-银行卡]支付了{}元".format(money))
        else:
            print("您使用[微信]支付了{}元".format(money))


class AlyPayPayment(Payment):
    def pay(self, money):
        print("您使用[支付宝]支付了{}元".format(money))


class ApplePayPayment(Payment):
    def pay(self, money):
        print("您使用[苹果]支付了{}元".format(money))


class YinLianPayPayment(Payment):
    def pay(self, money):
        print("您使用[银联]支付了{}元".format(money))


# ============ 工厂 ===========
class PaymentFactory:
    @staticmethod
    def create_payment(payment: str) -> Payment:
        if payment == 'Wechat':
            return WeChatPayment()
        elif payment == 'YinLian':
            return YinLianPayPayment()
        elif payment == 'ApplePay':
            return ApplePayPayment()
        elif payment == 'AlyPay':
            return AlyPayPayment()
        elif payment == 'Ka':
            return WeChatPayment("Ka")
        else:
            raise TypeError('Invalid payment type')


if __name__ == '__main__':
    pf = PaymentFactory()
    wechat = pf.create_payment("Wechat")
    wechat.pay(100)

    p = pf.create_payment("YinLian")
    p.pay(10)

    p = pf.create_payment("ApplePay")
    p.pay(12)

    p = pf.create_payment("AlyPay")
    p.pay(11)

    p = pf.create_payment("Ka")
    p.pay(1900)
