import random

print("Welcome to Snake, Water and Gun game! ")

def menu():
    a = random.randint(1,3)
    choice = int(input("\n1 = Snake " + "\n2 = Water" + "\n3 = Gun" + "\n4 = Exit Game" + "\nEnter your choice: "))
    if choice == 4:
        print("Exiting game...")
        exit(0)
    return a, choice   

def objectPicked(a, choice):
    if a == 1:
        comp = "Snake"
    elif a == 2:
        comp = "Water"
    elif a == 3:
        comp = "Gun" 

    if choice == 1:
        ch = "Snake"
    elif choice == 2:
        ch = "Water"
    elif choice == 3:
        ch = "Gun" 
    print("Player have choosen " + ch + " and Computer have choosen " + comp)


def checkWinner(a, choice):
    if (choice == 2 and a == 3) or (choice == 3 and a == 1) or (choice == 1 and a == 2):   
        print("Congratulations! You win.") 
    elif (choice == 1 and a == 1) or (choice == 2 and a == 2) or (choice == 3 and a == 3):
        print("Its a DRAW!")
    else:
        print("Better luck next time, Comouter Wins.")         


while True:
    a , choice = menu()
    objectPicked(a, choice)
    checkWinner(a, choice)


