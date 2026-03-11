
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficent funds")
        else:
            self.balance-= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
    def getbalance(self):
        return f"{self.owner}'s balance : $ {self.balance}"

alice = BankAccount("alice", 1000)
bob = BankAccount("bob")

alice.deposit(2000)
bob.deposit(1000)
alice.withdraw(2500)
bob.withdraw(800)

print(bob.getbalance())

#create a savings account thats like a bank account and also earns interest

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance+=interest
        print(f"interest applied! New Balance :{self.balance:.2f}")

carol = SavingsAccount("carol", 10000, 0.1)
carol.deposit(1000)
carol.apply_interest()

class TransactionHistrory(BankAccount):
    def __init__(self, owner, balance=0,):
        super().__init__(owner, balance)
        self.transaction_history = []

    def deposit(self, amount):
        super().deposit(amount)
        self.transaction_history.append 
        print(f"deposited $ {amount}")

    def withdraw(self, amount):
        super().withdraw(amount)
        self.transaction_history.append
        print(f"withdrew & {amount}")
    def print_history(self):
        print(f"\n---{self.owner}'s Transacation History---")
        for record in TransactionHistrory:
            print(record)

alice =TransactionHistrory("alice", 10000)
alice.deposit(12000)
alice.withdraw(20000)
alice.deposit(50000)
alice.print_history


    
        

