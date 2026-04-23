#LAB 8
class Student:
    def __init__(self, name, sap, marks):
        self.name = name
        self.sap = sap
        self.marks = marks

    def display(self):
        print(self.name, self.sap, self.marks)

students = []

for _ in range(3):
    name = input("Name: ")
    sap = input("SAP: ")
    marks = list(map(int, input("Marks (3): ").split()))
    students.append(Student(name, sap, marks))

for s in students:
    s.display()