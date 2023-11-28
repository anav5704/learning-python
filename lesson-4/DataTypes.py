# Strings

fname = "Anav" # Litieral assignment
lname = "Chand"

print(type(fname)) # str
print(type(fname) == str) # True
print(isinstance(fname, str)) # True

university = str("USP") # Constructor function

print(type(university)) # str
print(type(university) == str) # True
print(isinstance(university, str)) # True

# Concatination

full_name = fname + " " + lname
print(full_name)

# Type Casting

year = str(2023)
print(type(year))   

sentence = "The current year is " + year
print(sentence)

# Multiple Lines

multi = '''
Monday
    Tuesday 
        Wednesday
            Thurday
                Friday
'''
print(multi)

# Escape Characters

quote = "\"You can not learn without making mistakes.\""
print(quote)

# String Methods

myString = "how DO i MAKE you lOVE me?"
print(myString.lower())
print(myString.upper())
print(myString.title())
print(myString.replace("?", " 0_0 ?"))
print(len(myString))

# Making A Lil Menu

print("")
title = "welcome to my store!"
print(title.title().center(50, "-"))
print("Coffee".ljust(48, ".") + "$5".rjust(0))
print("Tea".ljust(48, ".") + "$3".rjust(0))
print("Wine".ljust(48, ".") + "$9".rjust(0))
print("Water".ljust(48, ".") + "$1".rjust(0))
print("")

# Intergers

price = 100 # Interger literal
otherPrice = int(200) # Constructor function
print(price, otherPrice)

# Float

gpa = 3.25
otherGpa = float(4.5)
print(gpa, otherGpa)

# Complex type

comp_num = 5 + 3j
print(comp_num)
print(type(comp_num))
print(comp_num.real)
print(comp_num.imag)

# Math module

import math
print(math.pi, math.tau)
print(math.ceil(gpa))
print(math.floor(gpa))