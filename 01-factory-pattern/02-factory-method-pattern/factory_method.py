"""工厂方法模式"""

from abc import ABC, abstractmethod


class Payment(ABC):
    """ 支付方法的抽象接口  """

    @abstractmethod
    def pay(self, money):
        pass


# ==================== 具体的支付实现 ========================
class WeChatPayment(Payment):
    def __init__(self, **kwargs):
        pay_way_li = ['微信', '微信-银行卡']
        self.pay_type = pay_way_li[0]
        if "KA" in kwargs and kwargs["KA"]:
            self.pay_type = pay_way_li[1]

    def pay(self, money):
        print("您使用[{}]支付了{}元".format(self.pay_type, money))


class AlyPayPayment(Payment):
    def __init__(self, **kwargs):
        pay_way_li = ['支付宝', '支付宝-银行卡', '花呗']
        self.pay_type = pay_way_li[0]
        if "KA" in kwargs and kwargs["KA"]:
            self.pay_type = pay_way_li[1]
        if "HB" in kwargs and kwargs["HB"]:
            self.pay_type = pay_way_li[2]

    def pay(self, money):
        print("您使用[{}]支付了{}元".format(self.pay_type, money))


class ApplePayPayment(Payment):
    def pay(self, money):
        print("您使用[苹果]支付了{}元".format(money))


class YinLianPayPayment(Payment):
    def pay(self, money):
        print("您使用[银联]支付了{}元".format(money))


# ============= 抽象工厂 ===============
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self, payment: str) -> Payment:
        pass


# ============= 工厂的具体实现 ===============
class WeChatPaymentFactory(PaymentFactory):
    def create_payment(self, payment: str = None) -> Payment:
        if payment is None:
            return WeChatPayment()
        elif payment == 'KA':
            return WeChatPayment(KA=True)
        else:
            raise TypeError("微信暂不支持该方式付钱！")


class AlyPayPaymentFactory(PaymentFactory):
    def create_payment(self, payment: str = None) -> Payment:
        if payment is None:
            return AlyPayPayment()
        elif payment == 'HB':
            return AlyPayPayment(HB=True)
        elif payment == 'KA':
            return AlyPayPayment(KA=True)
        else:
            raise TypeError("微信暂不支持该方式付钱！")


class ApplePayPaymentFactory(PaymentFactory):
    def create_payment(self, payment: str = None) -> Payment:
        return ApplePayPayment()


class YinLianPaymentFactory(PaymentFactory):
    def create_payment(self, payment: str = None) -> Payment:
        return YinLianPayPayment()


if __name__ == "__main__":
    f = WeChatPaymentFactory()
    p = f.create_payment()
    p.pay(100)

    p = f.create_payment("KA")
    p.pay(100)

    f = AlyPayPaymentFactory()
    p = f.create_payment()
    p.pay(100)

    p = f.create_payment("KA")
    p.pay(100)

    p = f.create_payment("HB")
    p.pay(100)

    f = ApplePayPaymentFactory()
    p = f.create_payment()
    p.pay(100)

    f = YinLianPaymentFactory()
    p = f.create_payment()
    p.pay(100)
