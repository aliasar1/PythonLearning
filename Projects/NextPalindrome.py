def check(number):
    while True:
        number = str(number)
        if number == number[::-1]:
            print(f"The next palindrome is {number}")
            break  
        number = int(number) + 1  

if __name__ == "__main__":
    total = int(input("Enter how many numbers you want to add: "))

    for i in range(total):
        userInput = (input("Please enter any number to finds its next palindrome: "))
        check(userInput)