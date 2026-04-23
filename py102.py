class Account:
    def __init__(self, initial_amount):
        self.__balance = initial_amount   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance


# Test
ac = Account(1000)

ac.deposit(500)
ac.withdraw(300)
ac.withdraw(2000)  # invalid

print("Final Balance:", ac.get_balance())