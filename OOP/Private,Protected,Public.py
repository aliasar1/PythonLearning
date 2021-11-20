class Public1:
    salary = 4000 #Public access modifier

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print(f"Name is {self.name} and age is {self.age}")    

obj = Public1("Ali", 20)
obj.printDetails()
print(obj.salary)  # Calling public attribute

class Private1:
    __privSalary = 10000 # To  make private use __ double underscore

obj1 = Private1()
# print(obj1._privSalary) this will throw error
print(obj1._Private1__privSalary) # This is nhow you can access private member.

class Student:
    
     # protected data members
     _name = None
     _roll = None
     _branch = None
    
     # constructor
     def __init__(self, name, roll, branch): 
          self._name = name
          self._roll = roll
          self._branch = branch
    
     # protected member function  
     def _displayRollAndBranch(self):
 
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
 
 
# derived class
class Geek(Student):
 
       # constructor
       def __init__(self, name, roll, branch):
                Student.__init__(self, name, roll, branch)
         
       # public member function
       def displayDetails(self):
                   
                 # accessing protected data members of super class
                print("Name: ", self._name)
                   
                 # accessing protected member functions of super class
                self._displayRollAndBranch()
 
# creating objects of the derived class       
obj = Geek("R2J", 1706256, "Information Technology")
 
# calling public member functions of the class
obj.displayDetails()
