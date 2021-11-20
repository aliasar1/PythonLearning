class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Dogs barks BHOW BHOW!")

dog = Dogs()
dog.bark()        
