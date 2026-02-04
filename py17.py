print("Enter '1' number for True, or '0' for False.")
a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))

condition_a = bool(a)
condition_b = bool(b)

print(f"\nA is {condition_a}, B is {condition_b}")


print(f"\nA AND B result: {condition_a and condition_b}")

print(f"A OR B result: {condition_a or condition_b}")

print(f"NOT A result: {not condition_a}")
print(f"NOT B result: {not condition_b}")