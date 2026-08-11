 class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"

    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "balance" and value < 0:
            raise ValueError("Balance cannot be negative")
        object.__setattr__(self, name, value)


a1 = BankAccount("Guru", 10000)
a2 = BankAccount("Ravi", 7000)

print(a1)
print(a2)

a1.deposit(2000)
a2.withdraw(1000)

print("A1 + A2 =", a1 + a2)
print("A1 - A2 =", a1 - a2)
print("Same balance:", a1 == a2)
print("A1 lower:", a1 < a2)

print(a1.balance)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.price} x {self.quantity}"

    def __add__(self, other):
        return self.total_price() + other.total_price()

    def __mul__(self, number):
        return self.price * number

    def __gt__(self, other):
        return self.total_price() > other.total_price()

    def __eq__(self, other):
        return self.price == other.price

    def __getattr__(self, name):
        return "Attribute not found"

    def __setattr__(self, name, value):
        if name == "price" and value < 0:
            raise ValueError("Price cannot be negative")
        object.__setattr__(self, name, value)


p1 = Product("Laptop", 50000, 2)
p2 = Product("Phone", 30000, 3)

print(p1)
print(p2)

print("Total prices added:", p1 + p2)
print("Laptop price x 3:", p1 * 3)

print("P1 greater:", p1 > p2)
print("Same price:", p1 == p2)

print(p1.color)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return f"{self.name}: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks

    def __truediv__(self, number):
        return self.marks / number

    def __ge__(self, other):
        return self.marks >= other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "marks" and not 0 <= value <= 100:
            raise ValueError("Marks must be between 0 and 100")
        object.__setattr__(self, name, value)


s1 = Student("Guru", 85)
s2 = Student("Ravi", 70)

print(s1)
print("Grade:", s1.grade())

print("Total marks:", s1 + s2)
print("Average of Guru marks:", s1 / 2)

print("Guru >= Ravi:", s1 >= s2)
print("Guru < Ravi:", s1 < s2)

print(s1.marks)



class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __str__(self):
        return f"Length: {self.length}, Breadth: {self.breadth}"

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __getattr__(self, name):
        return "Attribute not found"

    def __setattr__(self, name, value):
        if name in ["length", "breadth"] and value <= 0:
            raise ValueError("Length and breadth must be positive")
        object.__setattr__(self, name, value)


r1 = Rectangle(10, 5)
r2 = Rectangle(8, 4)

print(r1)
print(r2)

print("Area:", r1.area())
print("Added areas:", r1 + r2)
print("Subtracted areas:", r1 - r2)
print("Same area:", r1 == r2)
print("R1 greater:", r1 > r2)

print(r1.color)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def __str__(self):
        return f"{self.name}: {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __mul__(self, months):
        return self.salary * months

    def __ne__(self, other):
        return self.salary != other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "salary" and value < 10000:
            raise ValueError("Salary cannot be below 10000")
        object.__setattr__(self, name, value)


e1 = Employee("Guru", 30000)
e2 = Employee("Ravi", 40000)

print(e1)
print("Annual salary:", e1.annual_salary())

print("Combined salary:", e1 + e2)
print("Six months salary:", e1 * 6)

print("Not equal:", e1 != e2)
print("E1 <= E2:", e1 <= e2)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def reading_time(self):
        return self.pages * 2

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __add__(self, other):
        return self.pages + other.pages

    def __floordiv__(self, days):
        return self.pages // days

    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        return self.title == other.title

    def __getattr__(self, name):
        return "Book attribute not found"

    def __setattr__(self, name, value):
        if name == "title" and value == "":
            raise ValueError("Title cannot be empty")

        if name == "pages" and value <= 0:
            raise ValueError("Pages must be positive")

        object.__setattr__(self, name, value)


b1 = Book("Python", "Guido", 300)
b2 = Book("Java", "James", 400)

print(b1)
print("Reading time:", b1.reading_time(), "minutes")

print("Total pages:", b1 + b2)
print("Pages per day:", b1 // 10)

print("B1 greater:", b1 > b2)
print("Same title:", b1 == b2)

print(b1.price)



class CartItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def final_amount(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.item_name}: {self.quantity} x {self.price}"

    def __add__(self, other):
        return self.final_amount() + other.final_amount()

    def __mod__(self, discount):
        return self.final_amount() % discount

    def __lt__(self, other):
        return self.final_amount() < other.final_amount()

    def __ge__(self, other):
        return self.quantity >= other.quantity

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "quantity" and value < 1:
            raise ValueError("Quantity must be at least 1")
        object.__setattr__(self, name, value)


c1 = CartItem("Laptop", 50000, 2)
c2 = CartItem("Mouse", 1000, 3)

print(c1)
print("Final amount:", c1.final_amount())

print("Combined amount:", c1 + c2)
print("Remainder:", c1 % 1000)

print("C1 < C2:", c1 < c2)
print("C1 quantity >= C2:", c1 >= c2)


class TimeDuration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def total_minutes(self):
        return self.hours * 60 + self.minutes

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"

    def __add__(self, other):
        total = self.total_minutes() + other.total_minutes()

        hours = total // 60
        minutes = total % 60

        return TimeDuration(hours, minutes)

    def __sub__(self, other):
        total = self.total_minutes() - other.total_minutes()

        hours = total // 60
        minutes = total % 60

        return TimeDuration(hours, minutes)

    def __eq__(self, other):
        return self.total_minutes() == other.total_minutes()

    def __gt__(self, other):
        return self.total_minutes() > other.total_minutes()

    def __getattr__(self, name):
        return "Invalid attribute"

    def __setattr__(self, name, value):
        if name == "minutes" and not 0 <= value <= 59:
            raise ValueError("Minutes must be between 0 and 59")

        object.__setattr__(self, name, value)


t1 = TimeDuration(2, 30)
t2 = TimeDuration(1, 45)

print(t1)
print("Total minutes:", t1.total_minutes())

print("Addition:", t1 + t2)
print("Subtraction:", t1 - t2)

print("Equal:", t1 == t2)
print("Greater:", t1 > t2)

print(t1.seconds)


class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def upgrade_ram(self, extra_ram):
        self.ram += extra_ram

    def __str__(self):
        return f"{self.brand}, RAM: {self.ram}GB, Price: {self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, quantity):
        return self.price * quantity

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.ram == other.ram

    def __getattribute__(self, name):
        print("Accessing:", name)
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name in ["ram", "price"] and value <= 0:
            raise ValueError("RAM and price must be positive")

        object.__setattr__(self, name, value)


l1 = Laptop("Dell", 8, 50000)
l2 = Laptop("HP", 16, 60000)

print(l1)
print(l2)

l1.upgrade_ram(8)

print("After RAM upgrade:", l1)

print("Added prices:", l1 + l2)
print("Bulk price:", l1 * 5)

print("L1 cheaper:", l1 < l2)
print("Same RAM:", l1 == l2)

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(self.name, "attacked", enemy.name)

    def __str__(self):
        return f"{self.name}: Health={self.health}, Attack={self.attack_power}"

    def __add__(self, other):
        return self.attack_power + other.attack_power

    def __sub__(self, other):
        return self.health - other.attack_power

    def __gt__(self, other):
        return self.health > other.health

    def __eq__(self, other):
        return self.attack_power == other.attack_power

    def __getattr__(self, name):
        return "Player stat not available"

    def __setattr__(self, name, value):
        if name == "health" and value < 0:
            value = 0

        object.__setattr__(self, name, value)


p1 = Player("Guru", 100, 30)
p2 = Player("Ravi", 80, 20)

print(p1)
print(p2)

p1.attack(p2)

print("After attack:")
print(p2)

print("Combined attack power:", p1 + p2)
print("Health difference:", p1 - p2)

print("P1 has greater health:", p1 > p2)
print("Same attack power:", p1 == p2)

print(p1.mana)
