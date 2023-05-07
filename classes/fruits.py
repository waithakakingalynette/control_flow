# Car make toyota make(Toyota global) color model speed.

# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them    
class Fruit:
    taste="Sweet"
    def __init__(self,color,name,price):
    def buy_fruits(self):
         return f"I bought 10 fruits at the price of {self.price}ksh"

    def make_juice(self):
         return f"I made {self.taste} {self.name} juice"

    def sell_juice(self):
        return f"I sold {self.taste} {self.name} juice at a price of {self.price}ksh per glass"
