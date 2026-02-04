a = float(input("Enter the initial value of 'a': "))
b = float(input("Enter the value of 'b' (Assignment Operator): "))

print(f"\nInitial values: a = {a}, b = {b}")

print(f"\nSimple Assignment (a = b): a is now {b}")

original_a = a
a += b
print(f"Add AND (a += b): a is now {a}")
a = original_a

a -= b
print(f"Subtract AND (a -= b): a is now {a}")
a = original_a

a *= b
print(f"Multiply AND (a *= b): a is now {a}")
a = original_a

a /= b
print(f"Division AND (a /= b): a is now {a}")
a = original_a

a %= b
print(f"Modulus AND (a %= b): a is now {a}")
a = original_a

a **= b
print(f"Exponent AND (a **= b): a is now {a}")
a = original_a

a //= b
print(f"Floor Division AND (a //= b): a is now {a}")