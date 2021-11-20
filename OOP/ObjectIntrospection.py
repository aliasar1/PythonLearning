import inspect
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

Shivansh=Employee("Ali","Asar")

def insp(emp):
     inspect.isclass(emp)
     while True:
       print(dir(emp))
       break

print("Enter Employee name: ", end="")    
emp=input()
insp(emp)