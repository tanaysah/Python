class Vehicle:
    color = "white"   # class attribute

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# Child class
class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# Object
bus = Bus("School Bus", 120, 12)

print("Color:", bus.color)
print("Max Speed:", bus.max_speed)
print("Mileage:", bus.mileage)
print(bus.seating_capacity())