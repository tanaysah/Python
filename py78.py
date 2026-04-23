class Student:
    def __init__(self, name, sap, marks):
        self.name = name
        self.sap = sap
        self.marks = marks

    def percentage(self):
        return sum(self.marks)/3

    def result(self):
        return "Pass" if all(m > 40 for m in self.marks) else "Fail"

    def display(self):
        print(self.name, self.percentage(), self.result())

def class_avg(students):
    return sum(s.percentage() for s in students)/len(students)