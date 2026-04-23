class Account:
    def __init__(self, initial_amount):
        self.__balance = initial_amount   # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


# Test
ac = Account(1000)
ac.deposit(500)
ac.withdraw(200)

print("Balance:", ac.get_balance())