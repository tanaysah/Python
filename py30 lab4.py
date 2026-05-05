'''1
3 3
5 5 5
7 7 7 7
9 9 9 9 9'''

i = 1
num = 1

while i <= 5:
    j = 1
    while j <= i:
        print(num, end=" ")
        j += 1
    print()
    num += 2
    i += 1

