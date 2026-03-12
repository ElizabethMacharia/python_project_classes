#error handling
class BankAccount:
    def __init__(self, owner, balance =0 ):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        try:
            if not isinstance(amount,(int, float)):
                raise TypeError("deposit amount must be a number")
            if amount<=0:
                raise ValueError("deposit amount must be positive")
            self.balance+=amount
            self.transaction_history.append (f"deposited $ {amount}")
            print(f"{self.owner} deposited ${amount}. New balance is $ {self.balance}")
        except TypeError as e:
            print(F"x Error!:{e}")
        except ValueError as e:
            print(f"x Error: {e}")

    def withdraw(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise TypeError("Amount must be a number")
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                raise ValueError(f"insufficient fund!. Balance is {self.balance}")
            
            self.balance-=amount
            self.transaction_history.append(f"withdrew ${amount}")
            print(f"{self.owner} withdrew ${amount}. New balance is ${self.balance}")
        except TypeError as e:
            print(f"X Error!: {e}")
        except ValueError as e:
            print(f"X Error!: {e}")
    
    def print_history(self):
        print(f"\n---{self.owner}'s Transaction history----")
        for record in self.transaction_history:
            print(record)

def transfer(sender, receiver, amount):
        print(f"\n---initiating transfer of $ {amount}---")
        try:
            if amount> sender.balance:
               raise ValueError (F"insufficient funds in {sender.owner}'s account")
            sender.balance-= amount
            receiver.balance+= amount
        except ValueError as e:
            print(f"transfer failed! {e}")
        else:
            print(f"sucessfuly transferred $ {amount}")
            print(f"{sender.owner}'s balance is {sender.balance}")
            print(f"{receiver.owner}'s balance is {receiver.balance}")
        finally:
            print("----Transfer completed successfully-----")
            

alice = BankAccount("Alice", 1000)
bob = BankAccount("bob", 500)

alice.deposit("500")
alice.deposit(2000)
alice.deposit(-200)

