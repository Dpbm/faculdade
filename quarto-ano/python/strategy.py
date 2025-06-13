from abc import ABC, abstractmethod
from random import randint

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagmento de {amount:.2f} com cartão de crédito")

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagmento de {amount:.2f} com PayPal")

class PixPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processando pagmento de {amount:.2f} com Pix")


class PaymentProcessor:
    def __init__(self):
        # by default the payment is done using credit card
        self.set_strategy(CreditCardPayment())

    def set_strategy(self,strategy):
        self.strategy = strategy

    def pay(self,amount):
        self.strategy.process_payment(amount)

if __name__ == "__main__":
    context = PaymentProcessor()
    
    print("---Realizando pagamentos com diversos meios de pagamento---")
    for strategy_class in [CreditCardPayment, PayPalPayment, PixPayment]:
        strategy = strategy_class()
        context.set_strategy(strategy)
        context.pay(randint(10, 1000))