import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_deposit(self):

        # Create an account.
        account = BankAccount(1000)

        # Deposit 500.
        account.deposit(500)

        # Expected balance = 1500.
        self.assertEqual(account.balance, 1500)


    def test_withdraw(self):

        # Create another account.
        account = BankAccount(1000)

        # Withdraw 200.
        account.withdraw(200)

        # Expected balance = 800.
        self.assertEqual(account.balance, 800)


if __name__ == "__main__":

    unittest.main()