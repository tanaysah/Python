name=input("Enter string: ")
name=name.upper()

for char in name:
    if char.isalpha():
        count=name.count(char)
        print(count, end="")
    else:
        printa
