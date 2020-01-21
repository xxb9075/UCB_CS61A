class Account:
    """A bank account that has a non-negative balance."""
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


class Bank:
    """A bank has accounts

    >>> bank = Bank()
    >>> john = bank.open_account("John", 10)
    >>> jack = bank.open_account("Jack", 5, CheckingAccount)
    >>> john. interest
    >>> 0.02
    >>> jack. interest
    >>> 0.01
    >>> bank.pay_interest()
    >>> john.pay_interest()
    >>> john.balance
    >>> 10.2
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind = Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

a = Bank()
