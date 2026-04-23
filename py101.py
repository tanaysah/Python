class Vehicle:
    color = "white"   # class attribute

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# Create object
bus = Bus("School Bus", 180, 12)

print("Vehicle Name:", bus.name)
print("Max Speed:", bus.max_speed)
print("Mileage:", bus.mileage)
print("Color:", bus.color)
print(bus.seating_capacity())