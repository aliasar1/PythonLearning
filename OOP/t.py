import os
import re

class Test:
    def ReadAccountNumber(self, file):
        with open(file, 'r') as f:
            line = 0
            for line in f:
                pass
            if line == 0:
                return 0
            else:
                line = line.split('-')
                return line[0]   

    def openAccount(self, file):
        if os.path.exists(file) == False:
            with open(file, 'w')as f:
                pass
            
        print("\nTo open a new account please enter the following details:\n")
        while True:
            self.name = input("Please enter your full name: ")
            if not re.match("^[a-zA-Z ]*$", self.name):
                print ("Error! Make sure you only use letters in your name")
            else: break
        while True:
            self.accType = input("Enter your account type(S = Saving Account/ C = Current Account): ").upper()
            if self.accType == "S":
                self.accType = "Saving"
                break
            elif self.accType == "C":
                self.accType = "Current"    
                break
        while True:
            self.dob = input("Please enter your date of birth(DD/MM/YYYY): ")
            if not re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", self.dob):
                print ("Error! Make sure you only use / and numbers in your Date of Birth.")
            else: break
        while True:    
            self.gender = input("Please enter your gender(male, female): ").lower()
            if self.gender == "male" or self.gender == "female":
                break
        self.address = input("Please enter your address: ")
        while True:
            self.contact = input("Please enter your contact number: ")
            if not re.match("^[0][\d]{3}[\d]{7}$", self.contact):
                print ("Error! Make sure you only numbers.")
            else: break    
        while True:
            try:
                while True:
                    self.ammount = int(input("Please enter your initial ammount to depsoit for opening account(Atlest Rs 500 for saving account and Atleat 1000 for current account): "))
                    if self.accType == "Saving" and self.ammount >=500 or self.accType == "Current" and self.ammount >= 1000:
                        break
                break
            except Exception:
                print ("Error: Use only numbers.")

        self.accNum = self.ReadAccountNumber()
        if self.accNum == 0:
            self.accNum = 101
        else:
            self.accNum = int(self.accNum)
            self.accNum = self.accNum + 1  

        with open(file, 'a')as f:
            print(f"Your account number is {self.accNum}")
            data = f"{self.accNum}-{self.name}-{self.dob}-{self.gender}-{self.address}-{self.contact}-{self.ammount}-{self.accType}\n"
            f.write(data)
        print("Account is created.")    

if __name__ == '__main__':
    t = Test()

    file = r"C://Users//aliar//Desktop//Python Learning//OOP//testt.txt"
    t.openAccount(file)



