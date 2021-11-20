# This program check and compare highscores from file and write it if beaten


def game():
    return 786

def FileWriting(score):
    with open("Filings\highScore.txt", "w") as f:
        f.write(str(score))    

with open("Filings\highScore.txt", "r") as f:
    highScore = f.read()

score = game()

if highScore == "":
    FileWriting(score)
elif score > int(highScore):  
    FileWriting(score)