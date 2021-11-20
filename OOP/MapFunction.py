numbers = ["1", "2", "3", "4", "5"]

#Conventional long method isntead use map.
# This for loop changes string list values to int.
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# add = numbers[2] + 3 #2nd index num is 3
# print(add)    

#map method 
numbers = list(map(int, numbers))
print(map(int, numbers)) #Memory location 
add = numbers[2] + 3 #2nd index num is 3
print(add) 

#********************************

# Using suqare to pass as a argument in map function. This is also how map can be used.
def square(a):
    return a*a

l1 = [1,2,3,4,5,6,7,8,9]
square1 = list((map(square, l1)))
print(square1)

# Here using lambda as a one liner function in order to produce same output.
square2 = list((map(lambda x: x*x, l1)))
print(square2)

#********************************
# Map using function

def sqaureFunc(a):
    return a**2

def cubeFunc(a):
    return a**3

func = [sqaureFunc, cubeFunc]
ls = [2,3,4,5]

for i in ls:
    val = list(map(lambda x: x(i), func)) #calling function form func list and performing task simultaneously.
    print(val)

#********************************    
