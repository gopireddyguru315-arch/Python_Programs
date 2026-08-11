class Student:
    total_students = 0
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

    def result(self):
        if self.marks >= Student.passing_marks:
            return "Pass"
        else:
            return "Fail"

    @classmethod
    def curve_marks(cls, percentage):
        cls.curve_percentage = percentage

    @staticmethod
    def grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"


s1 = Student("Guru", 65)
s2 = Student("Ravi", 75)
s3 = Student("Nandini", 85)

for student in [s1, s2, s3]:
    student.marks += student.marks * 10 / 100

print("Updated Results:")

for student in [s1, s2, s3]:
    print(student.name,
          student.marks,
          Student.grade(student.marks),
          student.result())

print("Total Students:", Student.total_students)

class Product:
    tax_rate = 0.10

    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    def final_price(self):
        return self.base_price + (self.base_price * Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate

    @staticmethod
    def is_valid_price(price):
        return 0 <= price <= 1000000


p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)

print("Before tax change:")
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())

Product.change_tax_rate(0.18)

print("\nAfter tax change:")
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())

print("\nPrice Validation:")
print(Product.is_valid_price(50000))
print(Product.is_valid_price(-100))


class Employee:
    min_experience = 3

    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department

    def is_eligible(self):
        return self.experience >= Employee.min_experience

    @classmethod
    def update_criteria(cls, new_experience):
        cls.min_experience = new_experience

    @staticmethod
    def valid_department(department):
        return department in ["HR", "Tech", "Admin"]


e1 = Employee("Guru", 2, "Tech")
e2 = Employee("Ravi", 5, "HR")
e3 = Employee("Nandini", 4, "Admin")

print("Before changing criteria:")

for e in [e1, e2, e3]:
    print(e.name, e.is_eligible())

Employee.update_criteria(4)

print("\nAfter changing criteria:")

for e in [e1, e2, e3]:
    print(e.name, e.is_eligible())

print("\nDepartment Validation:")
print(Employee.valid_department("Tech"))
print(Employee.valid_department("Sales"))


class Loan:
    interest_rate = 0.10

    def __init__(self, borrower, principal):
        self.borrower = borrower
        self.principal = principal

    def total_payable(self):
        interest = self.principal * Loan.interest_rate
        return self.principal + interest

    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @staticmethod
    def is_eligible(salary):
        return salary > 30000


l1 = Loan("Guru", 100000)
l2 = Loan("Ravi", 200000)

print("Before rate change:")
print(l1.borrower, l1.total_payable())
print(l2.borrower, l2.total_payable())

Loan.update_interest_rate(0.12)

print("\nAfter rate change:")
print(l1.borrower, l1.total_payable())
print(l2.borrower, l2.total_payable())

print("\nEligibility:")
print("Guru:", Loan.is_eligible(40000))
print("Ravi:", Loan.is_eligible(25000))


class Course:
    total_courses = 0
    min_duration = 4

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.enrolled_students = []
        Course.total_courses += 1

    def enroll(self, student):
        self.enrolled_students.append(student)

    @classmethod
    def update_min_duration(cls, new_duration):
        cls.min_duration = new_duration

    @staticmethod
    def valid_duration(duration):
        return 0 < duration <= 100


c1 = Course("Python", 6)
c2 = Course("Machine Learning", 10)

c1.enroll("Guru")
c1.enroll("Ravi")

c2.enroll("Nandini")

print(c1.title, c1.enrolled_students)
print(c2.title, c2.enrolled_students)

Course.update_min_duration(8)

print("\nMinimum Duration:", Course.min_duration)

print("Python valid:", c1.duration >= Course.min_duration)
print("ML valid:", c2.duration >= Course.min_duration)

print("Duration check:", Course.valid_duration(10))
print("Duration check:", Course.valid_duration(-5))

print("Total Courses:", Course.total_courses)


class Vehicle:
    service_rate = 5

    def __init__(self, model, kilometers_run, service_history):
        self.model = model
        self.kilometers_run = kilometers_run
        self.service_history = service_history

    def service_charge(self):
        return self.kilometers_run * Vehicle.service_rate

    @classmethod
    def update_service_rate(cls, new_rate):
        cls.service_rate = new_rate

    @staticmethod
    def eligible_for_service(age):
        return age <= 15


v1 = Vehicle("Honda City", 20000, [])
v2 = Vehicle("Toyota", 30000, [])

print("Before rate change:")
print(v1.model, v1.service_charge())
print(v2.model, v2.service_charge())

Vehicle.update_service_rate(8)

print("\nAfter rate change:")
print(v1.model, v1.service_charge())
print(v2.model, v2.service_charge())

print("\nEligibility:")
print("Honda:", Vehicle.eligible_for_service(10))
print("Toyota:", Vehicle.eligible_for_service(18))



class Inventory:
    total_items = 0
    min_stock = 5

    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        if quantity > 0:
            self.stock[item] = self.stock.get(item, 0) + quantity
            Inventory.total_items += quantity

    def remove_stock(self, item, quantity):
        if item in self.stock and quantity <= self.stock[item]:
            self.stock[item] -= quantity
            Inventory.total_items -= quantity

    @classmethod
    def update_threshold(cls, new_threshold):
        cls.min_stock = new_threshold

    @staticmethod
    def below_threshold(quantity):
        return quantity < Inventory.min_stock


i1 = Inventory()
i2 = Inventory()

i1.add_stock("Laptop", 10)
i1.add_stock("Mouse", 3)

i2.add_stock("Keyboard", 8)

print("Inventory 1:", i1.stock)
print("Inventory 2:", i2.stock)

i1.remove_stock("Laptop", 2)

print("\nAfter removing:")
print(i1.stock)

Inventory.update_threshold(6)

print("\nNew Minimum Stock:", Inventory.min_stock)

print("Mouse below threshold:",
      Inventory.below_threshold(i1.stock["Mouse"]))

print("Laptop below threshold:",
      Inventory.below_threshold(i1.stock["Laptop"]))

print("Total Items:", Inventory.total_items)


class HotelRoom:
    base_price = 2000

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    def total_bill(self):
        return self.nights_booked * HotelRoom.base_price

    @classmethod
    def change_base_price(cls, new_price):
        cls.base_price = new_price

    @staticmethod
    def valid_nights(nights):
        return isinstance(nights, int) and nights > 0


r1 = HotelRoom(101, 3, "Guru")
r2 = HotelRoom(102, 5, "Ravi")

print("Before price change:")
print(r1.guest_name, r1.total_bill())
print(r2.guest_name, r2.total_bill())

HotelRoom.change_base_price(2500)

print("\nAfter price change:")
print(r1.guest_name, r1.total_bill())
print(r2.guest_name, r2.total_bill())

print("\nValidation:")
print(HotelRoom.valid_nights(3))
print(HotelRoom.valid_nights(-2))
print(HotelRoom.valid_nights(2.5))

class LibraryMember:
    active_members = 0
    borrowing_limit = 3

    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0
        LibraryMember.active_members += 1

    def borrow_book(self, title):
        if not LibraryMember.is_valid_title(title):
            print("Invalid book title")
            return

        if self.books_borrowed < LibraryMember.borrowing_limit:
            self.books_borrowed += 1
            print(self.name, "borrowed", title)
        else:
            print(self.name, "reached borrowing limit")

    @classmethod
    def update_limit(cls, new_limit):
        cls.borrowing_limit = new_limit

    @staticmethod
    def is_valid_title(title):
        return isinstance(title, str) and 1 <= len(title.strip()) <= 100


m1 = LibraryMember("Guru")
m2 = LibraryMember("Ravi")

m1.borrow_book("Python Programming")
m1.borrow_book("Machine Learning")

m2.borrow_book("Data Science")

LibraryMember.update_limit(5)

print("\nNew borrowing limit:", LibraryMember.borrowing_limit)

m1.borrow_book("Artificial Intelligence")

print("\nBooks borrowed:")
print(m1.name, m1.books_borrowed)
print(m2.name, m2.books_borrowed)

print("\nTitle validation:")
print(LibraryMember.is_valid_title("Python"))
print(LibraryMember.is_valid_title(""))

class Member:
    bmi_limit = 25

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def is_fit(self):
        return self.calculate_bmi() <= Member.bmi_limit

    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit

    @staticmethod
    def valid_input(height, weight):
        return (
            isinstance(height, (int, float)) and
            isinstance(weight, (int, float)) and
            height > 0 and
            weight > 0
        )


m1 = Member("Guru", 1.70, 60)
m2 = Member("Ravi", 1.75, 90)

print("Before BMI limit change:")

for m in [m1, m2]:
    print(m.name)
    print("BMI:", round(m.calculate_bmi(), 2))
    print("Fit:", m.is_fit())

Member.update_bmi_limit(27)

print("\nAfter BMI limit change:")

for m in [m1, m2]:
    print(m.name)
    print("BMI:", round(m.calculate_bmi(), 2))
    print("Fit:", m.is_fit())

print("\nInput Validation:")
print(Member.valid_input(1.70, 60))
print(Member.valid_input(-1.70, 60))


