from abc import ABC, abstractmethod

# ABC is used to pass as argument to make any class abstract.
# abstractmethod decorator is used to make a method abstract. (Implemented by every class.)
# abstract class is base class and object cannot be made of that class.

class Shape(ABC):

    @abstractmethod
    def calcArea(self):
        pass

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcArea(self):
        return self.a * self.b

class Square(Shape):

    def __init__(self, a):
        self.a = a

    def calcArea(self):
        return self.a * self.a    

        
rec = Rectangle(5,10)
print(rec.calcArea())

sq = Square(4)
print(sq.calcArea())




