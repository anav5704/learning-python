x = 2

try:
    print(x)
    if not type(x) is str:
        raise TypeError("Only strings allowed bro")
    
except NameError:
    print("Somethings undefined bro")

except ZeroDivisionError:
    print("Can't divide numbers by 0 bro")

except Exception as error:
    print(error)
else:
    print("No errors bro")

finally:
    print("Try block done bro")