import random

def aboutGame():
    print("**** WELCOME TO GUESS THE NUMBER GAME ****")
    print("Guess the correct random number between the range of 1 to 100.")
    print("Good Luck!")

def userGuess():
    while True:
        try:
            num = int(input("Enter any number from 1 to 100: "))
            return num
        except ValueError:
            print("Error: Please enter any integer from 1 to 100!")

def generateRandom():
    randomNum = random.randint(1,100)
    return randomNum    

def checkGuess(userNum, randomNum):
    if userNum > randomNum:
        print("Please enter lesser number!")
        return False
    elif userNum < randomNum:
        print("Please enter greater number!")
        return False
    else:
        print(f"Random number was {randomNum}")
        print("Number matched! You won.")  
        return True

# This funstion can be used when we want to restrict user to 10 chances to guess.
# def countTurns(turns):
#     if turns > 9:
#         print("Out of turns! Better luck next time.")
#         return True
#     else:
#         return False  

def readScoreFormFile():
    with open("Projects/Games/highScore.txt", "r") as f:
        highScore = f.read()
        return highScore

def FileWriting(turns):
    highScore = readScoreFormFile()
    with open("Projects/Games/highScore.txt", "w") as f:
        if highScore == "":
            f.write(str(turns))
        elif turns < int(highScore):  
            print("You have beat the high score! Congrats.")
            f.write(str(turns))
        else:
            f.write(str(highScore))           

rNum = generateRandom()
aboutGame()
turns = 1

while True:
    print(rNum)
    userNum = userGuess()
    if (checkGuess(userNum, rNum)) == True:
        FileWriting(turns)
        break
    turns += 1

