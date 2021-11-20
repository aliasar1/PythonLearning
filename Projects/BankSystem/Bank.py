from Summary import *
from ManageAccounts import *
from Transaction import *

class Bank:

    def __init__(self):
        print()
        print ("-----------------------")
        print ("|                     |")
        print ("| Welcome To YES Bank |")
        print ("|                     |")
        print ("-----------------------")
        print()

    def validateAdmin(self):
        self.turns = 0
        while True:
            self.userName = input("\nPlease enter admin username to access: ")
            self.userPassword = input("Please enter admin password to access: ")
            if self.userName == "admin123" and self.userPassword == "password786":
                return True
            else:
                print("\nIncorrect username or password.")   
            self.turns = self.turns + 1
            if self.turns == 3:
                return False 

if __name__ == "__main__":
    #username = admin123      password = password786
    
    acc = Bank()  
    ma = ManageAccounts()
    summary = Summary()
    tr = Transaction()

    file = r"Projects//BankSystem//accounts.txt"
    file2 = r"Projects//BankSystem//temp.txt"

    if acc.validateAdmin() == False:
        print("System locked since you failed to type correct username or password. Please contact to IT deparement.")
        exit()

    while True:
        try:
            print("\nPress 1: Manage Accounts\nPress 2: Perform Transactions\nPress 3: Bank Summary\nPress 0: Exit")
            lgn = int(input("Enter your choice: "))
            if lgn == 1:
                while True:
                    try:
                        print("\nPress 1: Open New Account\nPress 2: Search Account\nPress 3: View All Accounts\nPress 4: Remove Account\nPress 5: Modify Account Details\nPress 0: Go to Main Menu")
                        choice = int(input("Enter key: "))
                        if choice == 1:
                            ma.openAccount(file)
                        elif choice == 2:
                            ma.SearchAccount(file)
                        elif choice ==3:
                            ma.viewAllAccount(file)    
                        elif choice == 4:
                            ma.deleteAccount(file, file2)
                        elif choice == 5:
                            ma.modifyDetails(file, file2)
                        elif choice == 0:
                            print("\nGoing to main menu...")
                            break   
                        else:
                            print("Invalid choice!")
                            continue
                    except:
                        print("Enter only numbers that are instructed.")    
            elif lgn == 2:
                tr.transaction(file, file2)  
            elif lgn == 3:
                while True:
                    print("\nPress 1: Make a pdf file of all accounts in bank.\nPress 2: Calculate total money present in bank of account holders.\nPress 3. Print all Savings accounts.\nPress 4. Print all Current Accounts.\nPress 0: Exit")
                    opt = int(input("Press key: "))
                    if opt == 1:
                        file3 = r"Projects//BankSystem//BankAccounts.pdf"
                        summary.printData(file, file2, file3)
                    elif opt == 2:
                        summary.totalAmount(file)    
                    elif opt == 3:
                        summary.printSavingAccounts(file)
                    elif opt == 4:
                        summary.printCurrentAccounts(file)
                    elif opt == 0:
                        print("Going to previous menu...")
                        break
                    else:
                        print("Invalid options chosen!")
                        continue  
            elif lgn == 0:
                print("\nExiting from Banking System..")
                break    
            else:
                print("Invalid choice!")
            continue   
        except:
            print("Enter only numbers that are instructed.")