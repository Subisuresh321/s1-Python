class BankAccount():
    def __init__(self, account_number, account_name, type,balance=0):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__balance=balance
        self.__type=type
        
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
    
    def balance(self):
        return self.__balance
    
    def details(self):
        return f"Account Number: {self.__account_number}\nAccount Name: {self.__account_name}\nAccount Type : {self.__type}"

basil=BankAccount(1234,"basil","savings")

subi=BankAccount(12345,"subi","minimum balance")

basil.deposit(2900)
basil.withdraw(1200)

subi.deposit(5000)

print(basil.balance())
print(subi.balance())  

print(basil.details())
print(subi.details())