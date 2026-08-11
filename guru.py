def Upper(x):
    for i in x:
        if i.isupper():
            return True
    return False

def vaild(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us:str,psd:str,age:int):
        nonlocal uns
        if us not in uns:
            uns.append(us)
            if 8 <= len(psd) <= 15:
                k = list(filter(lambda x: x in special_char, psd))
                n = psd.isalnum()
                up = Upper(psd)
                # print(k)
                # print(n)
                # print(up)

                if up and n and k:
                    if age >= 18:
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 17"
                else:
                    return "Invalid Password"
            else:
                return "Minimum length of the password is 8 characters"
        else:
            return "Username already exists"
    return inner


@vaild
def register(username,password,age):
    return f"{username}'s Register Successful"

print(register("Nandu","Nandu1403$$",21))
print(register("Siddu","Siddu0314$$",22))


import functools

def ann(func):
    @functools.wraps(func)
    def inner(x,y):
        # print(func.__name__)
        # print(func.__annotations__)
        # print(func.__doc__)
        print(x,y)
        return func(x,y)
    return inner


@ann
def fun(a:int,b:int) -> int:
    """Just adding a Doc for the function"""
    return a+b

print(fun(10,24))
print(fun.__name__)
print(fun.__annotations__)
print(fun.__doc__)
