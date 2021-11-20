class Calculator:

    def __init__(self, x):
        self.x = x

    def square(self):
        print(f"The square of {self.x} is {self.x ** 2}")

    def cube(self):
        print(f"The cube of {self.x} is {self.x ** 3}")

    def root(self):
        print(f"The square root of {self.x} is {self.x ** 0.5}")

    @staticmethod
    def greet():
        print("Hello")    

value1 = Calculator(4)
value1.square()
value1.cube()
value1.root()
value1.greet()

