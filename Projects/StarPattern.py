rows = int(input("Enter number of rows of star pattern: "))
flag = int(input("If you want to make star pattern inverted press [1] or else press [0]: "))

def isReverse(flag):
    if flag == 1:
        return True
    elif flag == 0:
        return False

def printStarPattern(rows, flag):
    if isReverse(flag) == False:
        for i in range(rows+1):
            for j in range(i):
                print("*", end="")
            print()
    else:
        for i in range(rows, 0 , -1):
            for j in range(i):
                print("*", end="")
            print()
    

printStarPattern(rows, flag)            



