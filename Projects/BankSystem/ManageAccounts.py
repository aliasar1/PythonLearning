import os
import re
from ManageBankFiles import *

class ManageAccounts(ManageBankFiles):

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

        self.accNum = self.ReadAccountNumber(file)
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

    def SearchAccount(self, file):
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return
        self.accNum = input("Please enter your account number: ")
        with open(file, 'r') as f:   
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[0] == self.accNum:
                    print("-----------------------------------------------------------------------")
                    print(f"\nAccount Number: {account[0]}\nName: {account[1]}\nDate of Birth: {account[2]}\nGender: {account[3]}\nAddress: {account[4]}\nContact Number: {account[5]}\nAccount Balance: {account[6]}\nAccount Type: {account[7]}\n")
                    print("-----------------------------------------------------------------------")
                    return
            print("\nSorry, no account found!")

    def viewAllAccount(self, file):
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return
        with open(file, 'r') as f:
            print("\n-----------------------------------------------------------------------")
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                print(f"Account Number: {account[0]}\nName: {account[1]}\nDate of Birth: {account[2]}\nGender: {account[3]}\nAddress: {account[4]}\nContact Number: {account[5]}\nAccount Balance: {account[6]}\nAccount Type: {account[7]}\n")
                print("-----------------------------------------------------------------------")

    def deleteAccount(self, file, file2):
        if super().extractAccount(file, file2) == False:
            return
        self.accNum = input("Please enter your account number to delete account: ")    
        self.flag = False
        with open(file, 'r') as f:
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[0] == self.accNum:
                    self.flag = True
                    continue
                else:
                    with open(file2, 'a') as f2:
                        data = '-'.join([str(info) for info in account])
                        f2.write(data)
        if os.path.exists(file2) == False:
            print("No account exists.")
            return                
        if super().manageFiles(self.flag, file, file2) == True:                
            print("\n-----------------------------------")
            print("Account has been deleted!")
            print("\n-----------------------------------")


    def modifyDetails(self, file, file2):
        if super().extractAccount(file, file2) == False:
            return
        self.accNum = input("Please enter your account number to modify the account data: ")
        self.flag = False
        with open(file, 'r') as f:
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[0] == self.accNum:
                    print("Your account info: \n")
                    print(f"Account Number: {account[0]}\nName: {account[1]}\nDate of Birth: {account[2]}\nGender: {account[3]}\nAddress: {account[4]}\nContact Number: {account[5]}\nAccount Type: {account[7]}\n")
                    while True:
                        try: 
                            self.md = int(input("What is the data you want to modify: \n1. Name\n2. Date Of Birth\n3. Gender\n4. Address\n5. Contact Number\n6. Account Type\n"))
                            if self.md == 1:
                                while True:
                                    self.newName = input("Enter your new name: ")
                                    if not re.match("^[a-zA-Z ]*$", self.newName):
                                        print ("Error! Make sure you only use letters in your name")
                                    else: 
                                        account[1] = self.newName
                                        break
                            elif self.md == 2:
                                while True:
                                    self.newDOB = input("Enter your new date of birth(DD/MM/YYYY): ")
                                    if not re.match("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$", self.newDOB):
                                        print ("Error! Make sure you only use / and numbers in your Date of Birth.")
                                    else: 
                                        account[2] = self.newDOB
                                        break
                            elif self.md == 3:
                                while True:
                                    self.newGender = input("Enter your new gender(male/female): ").lower()
                                    if self.newGender == "male" or self.newGender == "female":
                                        account[3] = self.newGender
                                        break
                            elif self.md == 4:
                                self.newAddress = input("Enter your new address: ")
                                account[4] = self.newAddress  
                            elif self.md == 5:
                                while True:
                                    self.newContact = input("Please enter your new contact number: ")
                                    if not re.match("^[0][\d]{3}[\d]{7}$", self.newContact):
                                        print ("Error! Make sure you only numbers.")
                                    else: 
                                        account[5] = self.newContact
                                        break    
                            elif self.md == 6:
                                while True:
                                    self.accType = input("Enter your new account type(S = Saving Account/ C = Current Account): ").upper()
                                    if self.accType == "S":
                                        account[7] = "Saving\n"
                                        break
                                    elif self.accType == "C":
                                        account[7] = "Current\n"
                                        break
                            else:
                                print ("Error: Invalid number entered.")
                                continue
                            break
                        except Exception:
                            print("Error: Please enter valid numbers as instructed.")
                            continue
                    with open(file2, 'a') as f2:
                        data = f"{account[0]}-{account[1]}-{account[2]}-{account[3]}-{account[4]}-{account[5]}-{account[6]}-{account[7]}"
                        f2.write(data)               
                    self.flag = True
                    continue
                else:
                    with open(file2, 'a') as f2:
                        data = '-'.join([str(info) for info in account])
                        f2.write(data)
        if os.path.exists(file2) == False:
            print("No account exists.")
            return 
        if super().manageFiles(self.flag, file, file2) == True:                
            print("\n-----------------------------------------------------------------------")
            print("Account has been modified!")
            print("-----------------------------------------------------------------------")  
