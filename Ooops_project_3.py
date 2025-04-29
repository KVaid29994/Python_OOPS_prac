from datetime import datetime

# 🧱 Base class
class BankAccount:
    bank_name = "ABC Bank"  # Class attribute

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Encapsulated variable (protected)

    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"{amount} withdrawn. New balance: {self._balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance

    def account_summary(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self._balance}")
        print(f"Bank: {self.bank_name}")

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def is_banking_day():
        return datetime.today().weekday() < 5  # Mon–Fri are banking days


# 💰 Child class 1 — Inherits & Extends
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest of {interest} added. New balance: {self._balance}")


# 🧾 Child class 2 — Inherits & Overrides withdraw
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
            print(f"{amount} withdrawn (current account). New balance: {self._balance}")
        else:
            print("Overdraft limit exceeded.")


# 🔁 Polymorphism Function
def print_account_details(account):
    account.account_summary()
    print("-----")


# 🎯 Usage

print("✅ Is it a banking day?", BankAccount.is_banking_day())
print()

acc1 = SavingsAccount("Alice", 1000)
acc2 = CurrentAccount("Bob", 500)

acc1.add_interest()
acc2.withdraw(800)

print_account_details(acc1)
print_account_details(acc2)