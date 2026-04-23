# Program to count occurrence of values in range 0-3
#Lab 07
n = int(input("Enter number of values: "))

count = {0:0, 1:0, 2:0, 3:0}

for i in range(n):
    val = int(input("Enter value (0-3): "))
    if val in count:
        count[val] += 1
    else:
        print("Invalid input")

print("Occurrences:")
for key in count:
    print(key, "occurred", count[key], "times")