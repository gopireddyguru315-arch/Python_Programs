class A:
    def m1(self):
        print("A class")
class B(A):
    def m2(self):
        print("B class")
        super().m1()

b1=B()
b1.m1()
B.mro()

class user:
    def order(self):
        print("Ordered Pasta")
class restaurant(user):
    def order(self):
        super().order()
        print("Order Received")

R1=restaurant()
R1.order()

class swiggy(restaurant):
    def order(self):
        super().order()
        print("Delivery partner assigned")

s1=swiggy()
s1.order()
r1=restaurant()
r1.order()
