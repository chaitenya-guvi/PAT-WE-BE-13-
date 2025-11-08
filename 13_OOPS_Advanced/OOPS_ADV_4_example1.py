class Payment:
    def process(self):
        raise NotImplementedError("Subclass must implement this method")

class CreditCardPayment(Payment):
    def process(self):
        return "Processing credit card payment"

class UpiPayment(Payment):
    def process(self):
        return "Processing UPI payment"

def complete_payment(payment_method):
    print(payment_method.process())

complete_payment(CreditCardPayment())
complete_payment(UpiPayment())
