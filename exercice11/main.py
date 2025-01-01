class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder: str = account_holder
        self.balance: float = balance

    def deposit(self, amount: float):
        self.balance += amount
        self.display_balance()

    def withdraw(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            self.display_balance()
        else:
            print("Vous ne pouvez pas retirer il n'y a pas asser d'argent")

    def display_balance(self):
        print(f"{self.account_holder} - Balance: {self.balance}")


BankAccount = BankAccount("Clément", 100)
BankAccount.deposit(300)
BankAccount.withdraw(100)