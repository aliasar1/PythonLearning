import random

def changeNames(f, s):
    for i in range(len(fLst)):
        if i%2==0:
            r=random.randint(0,len(s)-1)
            if r == len(s)-1:
                print(f"{f[i]} {s[r-r]}")
            else:
                print(f"{f[i]} {s[r+1]}")
        else:
            continue

if __name__ == "__main__":
    totalNames = int(input("Please enter number of names you want to enter: "))
    fLst = []
    lLst = []

    for i in range(totalNames):
        fname, lname = input(f"Please enter name {i+1}: ").split()
        fLst.append(fname)
        fLst.append(lname)
        lLst.append(lname)

    changeNames(fLst, lLst)

