#LAB 8C

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def display(self):
        print("Name:", self.first, self.last)
        print("Pay:", self.pay)
        print("Email:", self.email)


# Test
emp = Employee("Mohandas", "Gandhi", 50000)
emp.display()