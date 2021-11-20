import os
from fpdf import FPDF 

class Summary:
    def printData(self, file, file2, file3):
        if os.path.exists(file2) == True:
            os.remove(file2)  
        if os.path.exists(file3) == True:
            os.remove(file3)  
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return    
        with open(file, 'r') as f:
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                with open(file2, 'a') as f2:
                    f2.write(f"Account Number: {account[0]}\nName: {account[1]}\nDate of Birth: {account[2]}\nGender: {account[3]}\nAddress: {account[4]}\nContact Number: {account[5]}\nAccount Balance: {account[6]}\nAccount Type: {account[7]}\n")
                    f2.write("---------------------------------------------------------------\n")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        with open(file2, 'r') as f:
            for x in f:
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        if os.path.exists(file2) == True:
            os.remove(file2) 
        pdf.output(file3)   
        print("\n----------------------------------------------------------------")            
        print("All accounts data file as pdf is been created in same directory.")
        print("-----------------------------------------------------------------")        

    def totalAmount(self, file):
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return
        with open(file, 'r') as f:
            self.totalCash = 0
            self.totalSaving = 0
            self.totalCurrent = 0
            accounts = f.readlines()
            for account in accounts:
                account = account.split("-")
                if account[7] == "Saving\n":
                    self.totalSaving = self.totalSaving + int(account[6])
                elif account[7] == "Current\n":
                    self.totalCurrent = self.totalCurrent + int(account[6])    
            self.totalCash = self.totalSaving + self.totalCurrent
        print("\n----------------------------------------------------------------")      
        print(f"Total Amount in Saving accounts is Rs {self.totalSaving}")     
        print(f"Total Amount in Current accounts is Rs {self.totalCurrent}")     
        print(f"Total Amount present in bank in total is Rs {self.totalCash}")        
        print("-----------------------------------------------------------------\n")    

    def printSavingAccounts(self, file):
        self.flag = False 
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return
        with open(file, 'r') as f:
            accounts = f.readlines()
            print(accounts)
            print("\nAll Saving Accounts present in Bank: ")
            print("----------------------------------------------------------------") 
            for account in accounts:
                account = account.split("-")
                if account[7] == "Saving\n":
                    print(f"Account Number: {account[0]}\nAccount Holder: {account[1]}")
                    print("----------------------------------------------------------------") 
                    self.flag = True
            if self.flag == False:
                print("No saving accounts present in our bank rightnow.")


    def printCurrentAccounts(self, file):
        self.flag = False
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return
        with open(file, 'r') as f:
            accounts = f.readlines()
            if accounts == None:
                print("\nNo current accounts present in our bank rightnow.")
                return
            print("\nAll Current Accounts present in Bank: ")
            print("----------------------------------------------------------------") 
            for account in accounts:
                account = account.split("-")
                if account[7] == "Current\n":
                    print(f"Account Number: {account[0]}\nAccount Holder: {account[1]}")
                    print("----------------------------------------------------------------") 
                    self.flag = True
            if self.flag == False:
                print("No current accounts present in our bank rightnow.")