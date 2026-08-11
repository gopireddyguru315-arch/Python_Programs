class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 40


s1 = Student("Guru", 75)
s2 = Student("Nandini", 35)

print(s1.name, "Passed" if s1.is_passed() else "Failed")
print(s2.name, "Passed" if s2.is_passed() else "Failed")

class Employee:
    company_name = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


e1 = Employee("Guru")
e2 = Employee("Ravi")

print(e1.company_name)
print(e2.company_name)

Employee.change_company("Microsoft")

print(e1.company_name)
print(e2.company_name)\

class MathOps:

    @staticmethod
    def is_even(num):
        return num % 2 == 0


print(MathOps.is_even(10))

m = MathOps()
print(m.is_even(7))


class Car:
    wheels = 4

    def __init__(self, mileage):
        self.mileage = mileage

    def display_specs(self):
        print("Mileage:", self.mileage)
        print("Wheels:", self.wheels)

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels


c1 = Car(20)
c2 = Car(25)

c1.display_specs()
c2.display_specs()

Car.change_wheels(6)

print("After changing wheels:")

c1.display_specs()
c2.display_specs()

class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def show_conversion(self):
        fahrenheit = self.to_fahrenheit(self.celsius)

        print("Celsius:", self.celsius)
        print("Fahrenheit:", fahrenheit)


t = Temperature(25)
t.show_conversion()


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3

if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")

if Book.is_valid_title("Java"):
    b2 = Book.from_string("Java-James Gosling")

print(b1.title, "-", b1.author)
print(b2.title, "-", b2.author)

print("Total books:", Book.total_books)


class Employee:
    bonus_rate = 0.1

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)

    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate

    @staticmethod
    def is_valid_salary(sal):
        return sal > 0


e1 = Employee("Guru", 30000)
e2 = Employee("Ravi", 40000)

print("Before bonus update:")
print(e1.name, e1.final_salary())
print(e2.name, e2.final_salary())

Employee.update_bonus(0.2)

print("\nAfter bonus update:")
print(e1.name, e1.final_salary())
print(e2.name, e2.final_salary())

print("\nSalary validation:")
print(Employee.is_valid_salary(30000))
print(Employee.is_valid_salary(-5000))

class Course:
    total_students = 0

    def __init__(self, student_name):
        self.student_name = student_name

    def enroll(self):
        Course.total_students += 1
        print(self.student_name, "enrolled")

    @classmethod
    def show_total(cls):
        print("Total students:", cls.total_students)

    @staticmethod
    def is_eligible(age):
        return age >= 18


c1 = Course("Guru")
c2 = Course("Ravi")
c3 = Course("Nandini")

print(Course.is_eligible(20))

c1.enroll()
c2.enroll()
c3.enroll()

Course.show_total()


class BankAccount:
    bank_name = "ABC Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(amount, "deposited")
        else:
            print("Invalid amount")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount):
        return amount > 0


a1 = BankAccount("Guru", 10000)

print("Bank:", BankAccount.bank_name)
print("Holder:", a1.holder)
print("Balance:", a1.balance)

a1.deposit(5000)

print("New Balance:", a1.balance)

BankAccount.change_bank_name("XYZ Bank")

print("New Bank Name:", BankAccount.bank_name)

print(BankAccount.validate_amount(100))
print(BankAccount.validate_amount(-50))

class Student:
    passing_marks = 40

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks

    @staticmethod
    def grade_category(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


s1 = Student("Guru", 75)
s2 = Student("Ravi", 45)

print(s1.name, "Grade:", Student.grade_category(s1.marks))
print(s2.name, "Grade:", Student.grade_category(s2.marks))

s1.result()
s2.result()

Student.update_passing_marks(50)

print("\nAfter updating passing marks to 50:")

s1.result()
s2.result()

print(s1.name, "Grade:", Student.grade_category(s1.marks))
print(s2.name, "Grade:", Student.grade_category(s2.marks))