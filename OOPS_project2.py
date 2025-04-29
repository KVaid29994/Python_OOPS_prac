# Parent class representing a general Bank Account
class BankAccount:
    total_accounts = 0  # Class variable to track total number of accounts created

    def __init__(self, account_holder, balance=0):
        """Constructor: initializes account holder name and balance."""
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1  # Increment total accounts when a new account is created

    def deposit(self, amount):
        """Instance method: Deposits the given amount into the account after validation."""
        if self.validate_amount(amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Instance method: Withdraws the given amount if it’s valid and available."""
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal.")

    @classmethod
    def get_total_accounts(cls):
        """Class method: Returns the total number of accounts created."""
        return cls.total_accounts

    @staticmethod
    def validate_amount(amount):
        """Static method: Validates that the amount is positive."""
        return amount > 0

# Child class representing a Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        """Constructor: Initializes savings account with interest rate."""
        super().__init__(account_holder, balance)  # Call parent constructor
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Instance method: Applies interest to the balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")

# Child class representing a Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        """Constructor: Initializes current account with overdraft limit."""
        super().__init__(account_holder, balance)  # Call parent constructor
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Overridden withdraw method: Allows overdraft up to a limit."""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded.")

# ------------------------
# Usage (how the classes work)
# ------------------------

# Create a savings account
acc1 = SavingsAccount("Alice", 1000)
acc1.deposit(500)        # Deposit money
acc1.apply_interest()    # Apply interest

# Create a current account
acc2 = CurrentAccount("Bob", 300)
acc2.withdraw(700)       # Withdraw money with overdraft facility

# Check total number of accounts created
print("Total accounts created:", BankAccount.get_total_accounts())
