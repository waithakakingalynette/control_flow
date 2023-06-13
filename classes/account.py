# Car make toyota make(Toyota global) color model speed.

# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them  
# Add attributes deposits and withdrawals in the init method which are empty lists by 
# default and another attribute loan_balance which is zero by default.
# Add a method check_balance which returns the account’s balance
# Update the deposit method to append each withdrawal transaction to the deposits 
# list. Each transaction should be in form of a dictionary like this  
{
   "amount": amount,
   "narration": “deposit”
}

# Update the withdrawal method to append each withdrawal transaction to the 
# withdrawals list. Each transaction should be in form of a dictionary like like this 
{
   "amount": amount,
   "narration": “withdrawal”
}

# Add a new method  print_statement which combines both deposits and withdrawals 
# into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500 

# Add a borrow_loan method which allows a customer to borrow if they meet these 
# conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance

# Add a transfer method which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the 
# requested amount from the current account to the passed account. The transfer is 
# accomplished by reducing the current account balance and depositing the requested amount 
# to the passed account

class Account:
    bank = "KCB"
    def __init__(self, account_name, deposits=[], withdrawals=[], loan_balance=0,current_balance):
        self.account_name = account_name
        self.deposits = deposits
        self.withdrawals = withdrawals
        self.loan_balance = loan_balance
    
    def open_account(self):
        return f"I created a new {self.bank} account named {self.account_name}."
    
    def deposit(self, amount):
        self.deposits.append(amount)
        return f"{self.account_name} made a deposit of {amount} in {self.bank}."
         self.transactions.append(('deposit', amount))

    
    def withdraw(self, amount):
        self.withdrawals.append(amount)
        return f"{self.account_name} withdrew {amount} from {self.bank}."
        self.transactions.append(('deposit', amount))

    def check_balance(self):
        balance = sum(self.deposits) - sum(self.withdrawals) - self.loan_balance
        return f"The balance of {self.account_name}'s {self.bank} account is {balance}."

    def print_statement(self):    
        for transaction in transactions:
            print(f'{transaction[0]} - {transaction[1]}')

    def borrow_loan(self):
         if self.loan_balance > 0:
            print("Sorry you have an already outstanding loan.")
            else:
                print("")
            return

        elif amount <= 100:
            print("The loan amount requested is less than 100.")
            return

        elif len(self.deposits) < 10:
            print("Sorry, you  must have made at least 10 deposits.")
            return

        total_deposits = sum(self.deposits)
        elif amount > total_deposits / 3:
            print("Loan amount cannot be more than 1/3 of total deposits.")
            return

        self.loan_balance += amount
        print("Congratulations, ${amount}, you have acquired your loan")

    def repay_loan(self):    
        if amount > self.loan_balance:
            self.current_balance += amount-self.loan_balance
        else:
            self.loan_balance -=amount 

    def money_transfer(self):           