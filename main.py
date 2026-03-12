# main.py
import bank                        # import the whole module

alice = bank.BankAccount("alice",100000)
bob = bank.BankAccount("bob", 500000)

alice.withdraw(50000)
alice.deposit(25000)
bank.transfer(alice, bob, 30000)
bob.deposit(500000)
bank.transfer(bob, alice, 100000)
bob.withdraw(70000)
alice.print_history
bob.print_history

from bank import BankAccount, transfer
alice = BankAccount("alice", 100000)
bob = BankAccount("bob", 30000)

bank.transfer(bob, alice, 10000)