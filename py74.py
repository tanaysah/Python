# a. Keyword
def greet(name, msg):
    print(name, msg)

greet(name="Tanay", msg="Hello")

# b. Default
def greet2(name="Guest"):
    print("Hello", name)

greet2()

# c. Variable length
def total(*nums):
    print(sum(nums))

total(1,2,3,4)