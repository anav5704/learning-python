def hello ():
    print("Hello World!")
    
def greet(name):
    print("Hello " + str(name))


def sum(num1, num2 = 5):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

def multi(*args): # Makes a tuple
    print(args)

def multi2(**kwargs): # Makes a dictionary
    print(kwargs)


hello()
greet("Anav")
print(sum(5))
multi("Anav", 10, True)
multi2(name = "Anav", age = 10, single = True)
