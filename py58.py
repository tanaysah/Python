# Program to store name and city

n = int(input("Enter number of persons: "))
students = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

print("Names:")
for name in students.keys():
    print(name)


print("Cities:")
for city in students.values():
    print(city)

print("Student Details:")
for name, city in students.items():
    print(name, "lives in", city)

city_count = {}
for city in students.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Students in each city:")
for city, count in city_count.items():
    print(city, ":", count)