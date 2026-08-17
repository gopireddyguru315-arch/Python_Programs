# create a base class A with m1 and m2 methods and sub class B with m3 method.create a object fro both the class and call the methods

class A:
    def m1(self):
        print("Method m1")

    def m2(self):
        print("Method m2")

class B(A):
    def m3(self):
        print("Method m3")

a = A()
a.m1()
a.m2()

b = B()
b.m1()
b.m2()
b.m3()


class A:
    def m1(self):
        print("Method m1 from class A")
    
    def m2(self):
        print("Method m2 from class A")

class B(A):
    def m3(self):
        print("Method m3 from class B")

obj_a = A()
obj_a.m1()
obj_a.m2()

obj_b = B()
obj_b.m1()  
obj_b.m2()  
obj_b.m3()  

class A:
    def m1(self):
        print("m1 A class A")
    
    def m2(self):
        print("Method m2 from class A")




#create a class land_animal with method "berry" create a class water_animal with method "water" and create a subclass frog that inherits both the classes  with method "living" that calls both being and water methods.    
class Land_animal:
    def being(self):
        print("Land Animal")

class Water_animal:
    def water(self):
        print("Water Animal")

        

class Frog(Land_animal, Water_animal):
    def living(self):
        self.being()
        self.water()
        print("both")
f=Frog()
f.living()

