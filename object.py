# object.py
import importlib

# Dynamically import the 26_11 module
bank_account = importlib.import_module('26_11')

# Create an object and use the methods
obj = bank_account.BankAccount(5000, "Rama")
obj.getData()

obj,deposite(200)
obj.getData()