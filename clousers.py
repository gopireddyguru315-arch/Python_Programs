def electricity(rate_per_unit):

    def bill(units):
        total = rate_per_unit * units
        print("Electricity Bill:", total)

    return bill


e = electricity(5)
e(100)

def salary(bonus):

    def total_salary(basic_salary):
        total = basic_salary + bonus
        print("Total Salary:", total)

    return total_salary


s = salary(5000)
s(30000)


def discount(percent):

    def final_price(price):
        discount_amount = price * percent / 100
        final = price - discount_amount

        print("Final Price:", final)

    return final_price


d = discount(10)
d(1000)

def bank_account(balance):

    def withdraw(amount):
        balance_remaining = balance - amount
        print("Remaining Balance:", balance_remaining)

    return withdraw


account = bank_account(10000)
account(3000)

def movie(movie_name):

    def booking(person_name):
        print(person_name, "booked a ticket for", movie_name)

    return booking


m = movie("Avengers")
m("Guru")

def multiplier(number):

    def multiply(other_number):
        result = number * other_number
        print("Multiplication:", result)

    return multiply


m = multiplier(5)
m(10)


def restaurant(food_item):

    def order(quantity):
        print("Food Item:", food_item)
        print("Quantity:", quantity)

    return order


r = restaurant("Pizza")
r(2)

def create_password(password):

    def check_password(another_password):

        if password == another_password:
            print("Access Granted")
        else:
            print("Access Denied")

    return check_password


p = create_password("python123")

p("python123")
p("hello123")

def shopping_cart(item_name):

    def cart(quantity, price_per_item):
        total_price = quantity * price_per_item

        print("Item Name:", item_name)
        print("Quantity:", quantity)
        print("Total Price:", total_price)

    return cart


cart = shopping_cart("Laptop")
cart(2, 50000)

def counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count:", count)

    return increment


c = counter()

c()
c()
c()
c()
c()