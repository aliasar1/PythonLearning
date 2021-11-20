# The reduce(fun,seq) function is used to apply a particular function passed in its argument 
# to all of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.


# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


#****************************************************************

l1 = [1,2,3,4]
print(functools.reduce(lambda a,b : a+b, l1))

import operator

# Or we can use operators as a function by importing operator module.

print(functools.reduce(operator.add, l1))
print(functools.reduce(operator.sub, l1))
print(functools.reduce(operator.mul, l1))
