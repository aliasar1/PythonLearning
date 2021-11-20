class Employee:

    increment = 1.5

    def __init__(self, sal):
        self.salary = sal

    @property
    def salaryAfterIncrement(self):   
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.salary = sal*self.increment


emp = Employee(1000)
print(emp.salaryAfterIncrement)

