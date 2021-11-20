import random

def findTables(num):
    rIndex = random.randint(2, 9)
    rNum = random.randint(1, num-1)
    tableLst = []
    for i in range(1, 11):
        mult = num * i
        tableLst.append(mult)
    tableLst.pop(rIndex)    
    tableLst.insert(rIndex, (num*rIndex)+rNum)    
    return tableLst

def isCorrect(num, lst):
    myLst = []
    for i in range(1, 11):
        mult = num * i
        myLst.append(mult)
    for i in range(1, 11):
        if myLst[i] != lst[i]:
            return i+1
    return None
            

if __name__ == '__main__':
    num = int(input("Enter a number to find its multiplication table: "))
    lst = findTables(num)
    print("Faulty Table: " + str(lst))

    index = isCorrect(num, lst)
    print("Incorrect at index: " +str(index))