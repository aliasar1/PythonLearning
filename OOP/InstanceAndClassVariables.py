class Employee:
    totalLeaves = 10

    # Part 1

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printDetails(self):
        print(f"Employee name is {self.name} and age is {self.age}. Salry is {self.salary}")    

    # Part 1 ends *********************************    

    #Part 2 starts ****************************
    # Class methods as alternative constructor

    # This class method will change value of calss variable.
    @classmethod
    def changeLeaves(cls, leaves):
        cls.totalLeaves = leaves

    # This method is mostly used in filing if we want string sepreatly as name, age, salary 
    @classmethod
    def fromDashes(cls, string):

        # METHOD 1 but have long code approach
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])

        # METHOD 2 same output but simple approach Using *args
        return cls(*string.split("-"))

# static methods are used when we dont want to pass self as parameter and use any class varibales.
    @staticmethod
    def regards(string):
        print(f"Regards, \n{string}")    

        

ali = Employee("Ali", 23, 4000)
ali.printDetails()

# This is the instance variable and its priority is more than class variable if there is any.
ali.totalLeaves = 4 # instance variable
print(ali.totalLeaves)

#To change class variable call it by class name
Employee.totalLeaves = 7
print(Employee.totalLeaves)

# Part 1 ends ****************************

# Part 2 starts *****************************
# Using Class methods as alternative constructor
print("Part 2")
Employee.changeLeaves = 15
print(Employee.changeLeaves)

# Create constructor as pass string with dashes
sam = Employee.fromDashes("Sami-20-5000") #This will save string pass as a part of constructor.
print(sam.name)
print(sam.age)
print(sam.salary)

#Calling static method and passing string as argument.
Employee.regards("Sami")


