class BankAccount:
    def __init__(self, initial_amt, acc_holder):
        self.balance = initial_amt  # Corrected '=' and changed variable name
        self.name = acc_holder  # Corrected variable name
        print("Account is created")
        print(f"Account created for {self.name} with balance {self.balance:.2f}")
        
    def getData(self):
        print(f"Account '{self.name}' has balance: {self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully.")
        self.getData()
        print("Thank You!")

'''
print("Creation of simple application")

class BankAcc:
    def __init__(self, initial_amt, acc_holder):
        self.balance = initial_amt
        self.name = acc_holder
        print("Account created")
        print(f"Account created for: {self.name} with opening balance = {self.balance}")
'''

