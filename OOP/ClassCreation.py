class Programmer:
    company = "Microsoft"

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def getInfo(self):
        print(f"The name of pragrammer is {self.name}. The company is {self.company} and employee is working on prgramming {self.language}")    

# Object creation
ali = Programmer("Ali", "Skype") 
ahmed = Programmer("Ahmed", "Ms Office")

# Calling getInfo() method
ali.getInfo()
ahmed.getInfo()
