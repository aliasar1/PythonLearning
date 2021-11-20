import random

def generate_random(lb ,up):
    return random.randint(lb, up)

def checkNumber(rNum, num):
    if num > rNum:
        print("Please enter lesser number.")
        return False
    elif num < rNum:
        print("Please enter greater number.")
        return False
    elif num == rNum:
        print("Number Matched!")
        return True          

def validate(rNum):
    counter = 0
    while True:
        try:
            counter += 1
            num = int(input(f"Enter a number between {lb} and {up}: "))
            if num >= lb and num <= up:
                isCorrect = checkNumber(rNum, num)
                if isCorrect == True:
                    print("Total turns taken: " + str(counter))
                    return counter
            else:
                print(f"Please enter number from {lb} to {up} only.")
                counter -=1
        except Exception as e:
            counter -= 1
            print(f"Error Founds: {str(e)}")                

def decalreWinner(c1, c2):
    if c1 < c2:
        print("Winner is Player 1. Congratulations!")
    elif c1 > c2:
        print("Winner is Player 2. Congratulations!")
    else:
        print("Its a draw!")        

if __name__ == '__main__':
    try:
        lb = int(input("Enter the lower bound of the range: "))
        up = int(input("Enter the upper bound of the range: "))
        rNum = generate_random(lb, up)    
        print("\nPlayer 1 Best of Luck!")
        counter1 = validate(rNum)

        rNum = generate_random(lb, up)
        print("\nPlayer 2 Best of Luck!")
        counter2 = validate(rNum)

        decalreWinner(counter1, counter2)
    except Exception as e:
        print(f"Error Found: {str(e)}")
