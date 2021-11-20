class A:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # These are operators overloading, these operators are already defined.******
    def __add__(self, other):
        return self.salary + other.salary

    # we can also use it to concate two strings passed as objects.
    def __add__(self, other):
        return self.name + other.name    

    # divide salaries.
    def __truediv__(self, other):
        return self.salary / other.salary    
    #********************************

    # These are dunder methods.

    # This will help us to return string as we want.
    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.salary})"    

    # str is given priority if there is no string repr will be called if made otherwise object location will be printed. Eg: print(ali)
    def __str__(self):
        return f"Name is {self.name} and age is {self.age}. Salart is {self.salary}"      

ali = A("Ali", 20, 20000)
amin = A("Amin", 24, 40000)
# print(ali + amin) This will throw error as it will get confuse what it should add from class variables.
print(ali + amin) #This will return salary addition of both objs.
print(ali / amin) #This will return salary division of both objs.
print(ali + amin) # This will return name  AliAmin.

print(ali) # format mentioned in str will be printed as it is given priority,
print(str(ali))
print(repr(ali)) #withoud creating repr method it will return object loation.


