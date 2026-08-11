def greet():
    print("hello!")
say_hello = greet
say_hello()

def outer():
    message = "i am the outer function"
    def inner():
        print(message)
    inner()
outer()

def display (name, /):
	print(name)
display("Jhon")

def display (*, message):
	print (message)
display(message = 'Hello')	

def add (a, b, /, *, c, d):
	print (a + b + c + d)
add (2, 4, c = 8, d = 6)	
