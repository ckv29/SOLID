from abc import ABC, abstractclassmethod

class Customer(ABC):
    @abstractclassmethod
    def calculate_discount(self, order_total):
        pass


class regular(Customer):
    def calculate_discount(self,order_total):
        return order_total * 0.05  # 5% скидка для постоянных клиентов


class vip(Customer):
    def calculate_discount(self,order_total):
        return order_total * 0.15  # 15% скидка для VIP-клиентов


class new(Customer):
    def calculate_discount(self,order_total):
        return order_total * 0.02  # 2% скидка для новых клиентов



r = regular()
print(r.calculate_discount(100))

v = vip()
print(vip.calculate_discount(100))

n = new()
print(n.calculate_discount(100))