"""
This file defines two parent classes: Customer and Account.
We will use them later to demonstrate multiple inheritance.
"""

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def show_customer_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")


"""
- BankMember can access attributes and methods from both parent classes.

Concept:
----------
When a class inherits from multiple parent classes, 
it gets access to all their methods and attributes.

Python follows something called the MRO (Method Resolution Order)
to decide which parent’s method to call first if there are name conflicts.

In this example, since there are no conflicting method names,
both parent methods will be accessible directly.
"""

class BankMember(Customer, Account):
    def __init__(self, name, customer_id, account_number, balance):
        # Call both parent class constructors using their class names
        Customer.__init__(self, name, customer_id)
        Account.__init__(self, account_number, balance)

    def show_member_details(self):
        print("=== Bank Member Details ===")
        self.show_customer_info()
        self.show_account_info()


# creating an object of BankMember
member1 = BankMember("Alice", "C001", "SB1001", 50000)

# display all details
member1.show_member_details()
