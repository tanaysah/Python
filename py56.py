# Program to create tuple and find average

n = int(input("Enter number of elements: "))
values = []

for i in range(n):
    num = float(input("Enter number: "))
    values.append(num)

t = tuple(values)

average = sum(t) / n

print("Tuple:", t)
print("Average:", average)