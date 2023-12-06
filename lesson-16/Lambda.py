# Lambda

squared = lambda num: num  * num
print(squared(10))

addTwo = lambda num: num + 2
print(addTwo(98))

sum = lambda a, b: a + b
print(sum(50, 50))

def funBuilder(x):
    return lambda num: num + x

addTen = funBuilder(10)
addFive = funBuilder(5)

print(addTen(5), addTwo(5))


# Higher order functions

numbers = [ 1, 2, 4, 5 ]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

from functools import  reduce

total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)