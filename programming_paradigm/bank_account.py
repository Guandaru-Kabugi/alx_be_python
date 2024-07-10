class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0
        
    def deposit(self, amount):
        self.account_balance+=amount
        return amount
    def withdraw(self, amount):
        if amount <=self.account_balance:
            return True
        return False
    def display_balance(self):
        print(f"Your current account balance is {self.account_balance}.")