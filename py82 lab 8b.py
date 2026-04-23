class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def display(self):
        print(f"{self.r} + {self.i}i")

    def add(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def sub(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def mul(self, other):
        r = self.r*other.r - self.i*other.i
        i = self.r*other.i + self.i*other.r
        return Complex(r, i)
#creating two complex number
c1 = Complex(2,3)
c2 = Complex(4,5)

c3 = c1.add(c2)
c3.display()