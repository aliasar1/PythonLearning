def isPalindrome(number):
    while True:
        number = str(number)
        if number == number[::-1]:
            return number
        number = int(number) + 1    

def listing(lst):
    for num in lst:
        if num > 9:
            n = isPalindrome(num)
            myList.append(int(n))
        elif num <=9:
            myList.append(int(num))

if __name__ == "__main__":
    lst = [3, 4, 44, 55, 9, 291, 65, 10, 1]
    myList = []
    listing(lst)
    print(myList)
