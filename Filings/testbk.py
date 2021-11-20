file = r"Filings//bktest.txt"

with open(file, 'r') as f:
    accounts = f.readlines()
    accNum = input("Enter your account Number: ")
    for account in accounts:
        account = account.split("-")
        if accNum == account[0]:
            if ((account[6] == "500" and account[7] == "S\n") or (account[6] == "1000" and account[7] == "C\n")):
                print("Sorry, insufficient balace in your account. Please deposit some money first.")
            else:
                money = input("Enter how much money you want to withdraw from your account: ")
                bal = int(account[6]) - int(money)
                if int(money) > int(account[6]):
                    print ("Sorry, cannot be negative.")
                elif ((bal > 500 and account[7] == "S") or (bal > 100 and account[7] == "C")):
                    account[6] = bal
                    account[6] = str(account[6])
                else:    
                    print("Invalid!")