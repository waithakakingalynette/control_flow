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
