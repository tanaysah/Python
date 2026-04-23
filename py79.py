class A:
    def show(self):
        print("A")

class B(A):
    def show2(self):
        print("B")

obj = B()
obj.show()
obj.show2()