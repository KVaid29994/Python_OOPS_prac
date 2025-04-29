class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public attribute
        self._account_number = "123456789"  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000)

# Accessing public attribute
print(account.owner)  # Output: Alice

# Accessing protected attribute (not recommended, but possible)
print(account._account_number)  # Output: 123456789

# Accessing private attribute (will raise an AttributeError)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Using public methods to interact with the private attribute
account.deposit(500)  # Output: Deposited 500. New balance is 1500.
account.withdraw(200)  # Output: Withdrew 200. New balance is 1300.
print(account.get_balance())  # Output: 1300
