# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
            #  - show_full_name
            #  - year_of_birth
            #  - show_initials

class  Student:
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self):
        age=23
        current_year=2023
        year=current_year-age
    return year        

    def show_initials(self):   
        return f"{self.first_name[0]}.{self.last_name[0]}."     


# Car make toyota make(Toyota global) color model speed.

# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

class Car:
    make="Toyota"
    def __init__(self,color,model,speed):
        self.color=color
        self.model=model
        self.speed=speed

    def accelerate(self):
        return f"The acceleration of {self.model} is {self.speed}"
        
    def start_engine(self):
        return f"The engine of {self.make} is Single engine"
    def hired_car(self):
        return f"John hired {self.make} {self.model} of speed {self.speed}.Its colour is {self.color}"    

class Fruit:
    taste="Sweet"
    def __init__(self,color,name,price):
    def buy_fruits(self):
         return f"I bought 10 fruits at the price of {self.price}ksh"

    def make_juice(self):
         return f"I made {self.taste} {self.name} juice"

    def sell_juice(self):
        return f"I sold {self.taste} {self.name} juice at a price of {self.price}ksh per glass"




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