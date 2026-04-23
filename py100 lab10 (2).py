class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

# Test case
emp1 = Employee("Mohandas", "Gandhi", 50000)

print("First Name:", emp1.first)
print("Last Name:", emp1.last)
print("Pay:", emp1.pay)
print("Email:", emp1.email)