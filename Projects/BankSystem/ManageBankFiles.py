import os

class ManageBankFiles():

    def extractAccount(self, file, file2):
        if os.path.exists(file) == False:
            print("There are no records of any accounts.")
            return False
        if os.path.exists(file2) == True:
            os.remove(file2) 


    def manageFiles(self, flag, file, file2):
        if flag == True:
            os.remove(file)
            os.rename(file2, file)
            return True
        else:    
            os.remove(file2)
            print("No account found!")