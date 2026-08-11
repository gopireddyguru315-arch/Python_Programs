def login(func):
    def inner():
        un = input("Username: ")
        psd = input("Password: ")
        if un == "Praveen" and psd == "Diya":
            print("Login Successful")
            return func()
        else:
            return "Invalid Credentials"
    
    return inner


@login
def securefile():
    return "Secret File"

print(securefile())

def valid(func):
    def inner(x,y):
        if isinstance(x,int) and isinstance(y,int):
            print(f"Multiplication of {x} & {y}:",end=" ")
            func(x,y)
        else:
            print("Values/Arguments Must be Integers")
    return inner

@valid
def multiply(x,y):
    print(x*y)

multiply(4,5)
multiply('4',5) 

@dec
def greet(name):
    print(f"Hello {name}")

print(greet("Nandu"))

def dec(func):
    def inner(n):
        print("starting this function")
        func(n)
        print("Ending this function")
    return inner