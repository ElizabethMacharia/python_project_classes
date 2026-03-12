#bank.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")

    def print_history(self):
        print(f"\n--- {self.owner}'s Transaction History ---")
        for record in self.transaction_history:
            print(record)


def transfer(sender, receiver, amount):
    print(f"\nTransferring ${amount} from {sender.owner} to {receiver.owner}...")
    sender.withdraw(amount)
    receiver.deposit(amount)