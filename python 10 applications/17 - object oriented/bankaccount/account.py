from time import sleep
from datetime import datetime

class Account():
    def __init__(self, accttype, owner, acctname, initial = 0):
        self.type = accttype
        self.owner = owner
        self.balance = initial
        self.created = datetime.now().strftime('%Y-%m-%d')
        self.balance_record = self.created + " " + owner + " " + acctname + " Balance.txt"
        with open(self.balance_record, 'w') as file:
            file.write(str(datetime.now().strftime('%Y/%m/%d %H:%M:%S')) + " - Initial balance: " + str(self.balance) + " dollars\n")

    def created_when(self):
        print("This account was opened on " + str(self.created) + ".")

    def check_balance(self):
        print("Current Balance: " + str(self.balance))

    def check_type(self):
        print("This is a " + self.type + " account.")

    def deposit(self, amount):
        self.balance += amount
        with open(self.balance_record, 'a+') as file:
            file.write(str(datetime.now().strftime('%Y/%m/%d %H:%M:%S')) + " - Deposit: " + str(amount) + " dollars\n")
            self.write_balance(file)

    def write_balance(self, file):
        file.write("                      Current balance: " + str(self.balance) + " dollars\n")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds. Maximum amount you can withdraw: ' + str(self.balance) + " dollars")
        else:
            self.balance -= amount
            with open(self.balance_record, "a+") as file:
                file.write(str(datetime.now().strftime('%Y/%m/%d %H:%M:%S')) + " - Withdrawal: " + str(amount) + " dollars \n")
                self.write_balance(file)


acct = Account('Savings', 'Austin Atwood', 'Savings Account', 500)
acct.created_when()
acct.check_balance()
acct.check_type()
acct.deposit(25)

acct.withdraw(513)