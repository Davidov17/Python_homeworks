# Farm model code
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says Moo!")

    def give_milk(self):
        print(f"{self.name} gives milk.")


class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} says Cluck!")

    def lay_egg(self):
        print(f"{self.name} lays an egg.")


class Sheep(Animal):
    def make_sound(self):
        print(f"{self.name} says Baa!")

    def give_wool(self):
        print(f"{self.name} gives wool.")

# Bank app code
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print("Account created successfully.")
        print(account)

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and amount > 0:
            account.balance += amount
            self.save_to_file()
            print("Deposit successful.")
        else:
            print("Invalid deposit.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and 0 < amount <= account.balance:
            account.balance -= amount
            self.save_to_file()
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        if not os.path.exists("accounts.txt"):
            return
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                self.accounts[int(acc_no)] = Account(int(acc_no), name, float(balance))

# tasks
bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        deposit = float(input("Initial deposit: "))
        bank.create_account(name, deposit)

    elif choice == "2":
        acc = int(input("Account number: "))
        bank.view_account(acc)

    elif choice == "3":
        acc = int(input("Account number: "))
        amount = float(input("Amount: "))
        bank.deposit(acc, amount)

    elif choice == "4":
        acc = int(input("Account number: "))
        amount = float(input("Amount: "))
        bank.withdraw(acc, amount)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
