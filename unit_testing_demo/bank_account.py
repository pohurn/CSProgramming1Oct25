# Create a BankAccount class.
class BankAccount:

    # Constructor.
    def __init__(self, balance=0):

        # Store the current account balance.
        self.balance = balance


    # Deposit money.
    def deposit(self, amount):

        # Increase the balance.
        self.balance = self.balance + amount


    # Withdraw money.
    def withdraw(self, amount):

        # Reduce the balance.
        self.balance = self.balance - amount


