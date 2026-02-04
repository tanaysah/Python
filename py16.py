print("Enter marks of subject 1:")
m1 = int(input())
print("Enter marks of subject 2:")
m2 = int(input())
print("Enter marks of subject 3:")
m3 = int(input())
print("Enter marks of subject 4:")
m4 = int(input())
print("Enter marks of subject 5:")
m5 = int(input())

avg = (m1 + m2 + m3 + m4 + m5) / 5
print("Average marks =", avg)

if 91 <= avg <= 100:
    print("Grade: O")
elif 81 <= avg <= 90:
    print("Grade: A+")
elif 71 <= avg <= 80:
    print("Grade: A")
elif 61 <= avg <= 70:
    print("Grade: B+")
elif 51 <= avg <= 60:
    print("Grade: B")
elif 41 <= avg <= 50:
    print("Grade: C+")
elif 35 <= avg <= 40:
    print("Grade: C")
else:
    print("Fail")
