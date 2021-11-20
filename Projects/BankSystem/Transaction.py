import os
from ManageBankFiles import *

class Transaction(ManageBankFiles):

    def checkBalance(self, file):
            if os.path.exists(file) == False:
                print("There are no records of any accounts.")
                return
            self.accNum = input("Please enter your account number to check its balance: ")    
            with open(file, 'r') as f:
                accounts = f.readlines()
                for account in accounts:
                    account = account.split("-")
                    if account[0] == self.accNum:
                        print("-----------------------------------------------------------------------")
                        print(f"Account balance of {self.accNum} is Rs {account[6]}")
                        print("-----------------------------------------------------------------------")
                        return
                print("No account found.")
    
    def depositAccount(self, file, file2):
        if super().extractAccount(file, file2) == False:
            return
        self.accNum = input("Please enter your account number to deposit money in your account: ")
        self.flag = False
        with open(file, 'r') as f:
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[0] == self.accNum:
                    while True:
                        while True:
                            try:
                                self.money = int(input("Enter how much money you want to depsoit in your account: "))
                                break
                            except Exception:
                                print ("Error: Use only numbers.")
                                continue
                        if self.money > 0:
                            with open(file2, 'a') as f2:
                                account[6] = int(account[6]) + self.money
                                account[6] = str(account[6])
                                data = f"{account[0]}-{account[1]}-{account[2]}-{account[3]}-{account[4]}-{account[5]}-{account[6]}-{account[7]}"
                                f2.write(data)
                                print()
                                print(f"Your new balance is Rs {account[6]}")
                                break
                        else:
                            print("Invalid: Please enter money greater then zero.")          
                            continue             
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
            print("-----------------------------------------------------------------------")
            print("Money successfully deposit in account.")
            print("-----------------------------------------------------------------------")


    def withdrawAccount(self, file, file2):
        if super().extractAccount(file, file2) == False:
            return 
        self.accNum = input("Please enter your account number to withdraw money from your account: ")
        self.flag = False
        with open(file, 'r') as f:
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[0] == self.accNum:
                    if (account[7] == "Saving\n" and account[6] == "500") or (account[7] == "Current\n" and account[6] == "1000"):
                        print("You cannot withdraw money as you have insufficient balance. Please depsoit some money first.")
                        os.remove(file2)
                        return
                    while True:
                        while True:
                            try:
                                self.money = int(input("Enter how much money you want to withdraw in your account: "))
                                self.bal = int(account[6]) - self.money
                                if (account[7] == "Saving\n" and self.bal >=500) or (account[7] == "Current\n" and self.bal >=1000):
                                    break
                                else:
                                    if (account[7] == "Saving\n"):
                                        self.validAmmount = int(account[6]) - 500
                                    elif (account[7] == "Current\n"):
                                        self.validAmmount = int(account[6]) - 1000
                                    print("-----------------------------------------------------------------------")
                                    print("Insufficient balance in your account. Please enter lesser money to withdraw.")
                                    print("Atlest Rs 500 for saving account and atleat 1000 for current account must remain as current balance.")
                                    print(f"Your current balance now is only Rs {account[6]} which means you can only withdraw Rs {self.validAmmount} or less.")
                                    print("-----------------------------------------------------------------------")
                                    print()       
                            except Exception:
                                print ("Error: Use only numbers.")
                        with open(file2, 'a') as f2:
                            account[6] = int(account[6]) - self.money
                            account[6] = str(account[6])
                            data = f"{account[0]}-{account[1]}-{account[2]}-{account[3]}-{account[4]}-{account[5]}-{account[6]}-{account[7]}"
                            f2.write(data)
                            print(f"Your new balance is Rs {account[6]}") 
                            break           
                    self.flag = True
                else:
                    with open(file2, 'a') as f2:
                        data = '-'.join([str(info) for info in account])
                        f2.write(data)
        if os.path.exists(file2) == False:
            print("No account exists.")
            return 
        if super().manageFiles(self.flag, file, file2) == True:
                print("-----------------------------------------------------------------------")
                print("Money successfully withdraw from account.")
                print("-----------------------------------------------------------------------")


    def transaction(self, file, file2):
        while True:
            try:
                print("\nWhat do you want to do: \n1. Check Balance\n2. Deposit in Bank Account\n3. Withdraw from Account\n0. Exit")
                self.choice = int(input("Press key: "))
                if self.choice == 1:
                    self.checkBalance(file)
                elif self.choice == 2:
                    self.depositAccount(file, file2)
                elif self.choice == 3:
                    self.withdrawAccount(file, file2)
                elif self.choice == 0:
                    print("Returning to back menu...")
                    return
                else:
                    print("Error: Please enter only the numbes that are instructed.")      
            except Exception:
                print("Error: Please enter only numbers.")  