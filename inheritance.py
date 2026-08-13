class user:
    def __init__(self,n,a,g,dob):
        self.name =n
        self.age = a
        self.gender = g
        self.dob = dob

    def login(self):
        print("Login successful.")

    def logout(self):
        print("Logout successful.")

class Instagram(user):
    def post(self):
        print(f"{self.name} post")
        print("Got 1L likes.")

i1 = Instagram(n="Nandu", a=21, g="Female", dob="01-03-2005")
i1.post()
i1.login()
i1.logout()


class Restaurants:
    def __init__(self,name,rating,address):
        self.name = name
        self.rating = rating
        self.address = address

    def display_menu(self):
        print("All dishes are non-veg only")

class Swiggy(user, Restaurants):
    def display(self):
        print("User details")
s1=Swiggy("prathyu",21,"female","01-08-2004")
s1.login()
s1.logout()
s1.display()
s1.display_menu()


class Bank(user):
    Name = "RBI"
    def guidelines(self):
        print("Beware of scammer and call xxx")
class BhimUPI(Bank):
    def payments(self,amount):
        print(f"{amount} has been paid through UPI")
b1 = BhimUPI(n="Nandu", a=21, g="Female", dob="01-03-2005")
b2 =Bank(n="Vidhya", a=25, g="Female", dob="01-01-2000")
