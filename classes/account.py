# Car make toyota make(Toyota global) color model speed.

# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them    
class Account:
    bank="KCB" 
    def __init__(self,account_name,deposit,withdraw): 
        self.account_name=account_name
        self.deposit=deposit
        self.withdraw=withdraw  
    def balance(self):
    def open_account(self):
        return f"I created a new {self.bank} named {self.account_name}"
    def deposit(self): 
        return f"{self.account_name} made {self.deposit} in {self.bank}"  