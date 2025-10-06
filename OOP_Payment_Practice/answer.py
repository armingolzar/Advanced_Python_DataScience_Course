from abc import ABC, abstractmethod

# ----- Abstraction -----
class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount  # Encapsulation: private attribute

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount
        else:
            raise ValueError("Amount must be positive.")

    @abstractmethod
    def process_payment(self):
        """Process the payment. Must be implemented by subclasses."""
        pass


# ----- Inheritance + Encapsulation -----
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.__card_number = card_number  # private for security

    def get_masked_card(self):
        return "****-****-****-" + self.__card_number[-4:]

    def process_payment(self):
        return f"Processing Credit Card payment of ${self.get_amount()} from {self.get_masked_card()}"


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.__email = email

    def process_payment(self):
        return f"Processing PayPal payment of ${self.get_amount()} from {self.__email}"


class CryptoPayment(Payment):
    def __init__(self, amount, wallet_address):
        super().__init__(amount)
        self.__wallet_address = wallet_address

    def process_payment(self):
        return f"Processing Crypto payment of ${self.get_amount()} from wallet {self.__wallet_address[:6]}..."


# ----- Polymorphism in Action -----
class PaymentProcessor:
    def __init__(self):
        self.payments = []

    def add_payment(self, payment: Payment):
        self.payments.append(payment)

    def process_all(self):
        for p in self.payments:
            print(p.process_payment())  # Calls correct method dynamically


# ----- Testing -----
if __name__ == "__main__":
    processor = PaymentProcessor()

    cc = CreditCardPayment(150, "1234567812345678")
    paypal = PayPalPayment(200, "user@example.com")
    crypto = CryptoPayment(500, "0xabc123def456")

    processor.add_payment(cc)
    processor.add_payment(paypal)
    processor.add_payment(crypto)

    processor.process_all()

    # Test Encapsulation
    print("\nTesting encapsulation:")
    cc.set_amount(300)
    print(cc.process_payment())
