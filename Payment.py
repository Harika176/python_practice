from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPaymentr(Payment):
    def pay(self,amount):
        print("Paid",amount,"using Credit Card")
class UPIPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")
class CashPayment(Payment):
    def pay(self,amount):
        print("Paid",amount,"using Cash")
p1=CreditCardPaymentr()
p2=UPIPayment()
p3=CashPayment()
p1.pay(1000)
p2.pay(500)
p3.pay(200)