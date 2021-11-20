from pygame import mixer
from datetime import datetime
from time import time

def playMusic(file, stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        print("Is the reminder task done? Enter yes!")
        a = input()
        if a == stop:
            mixer.music.stop()
            break

def log(msg):
    with open('Projects/log.txt', 'a') as f:
        f.write(f"{msg} {datetime.now()}\n")        

if __name__ == "__main__":     
    init_water = time()
    init_eyes = time()
    init_move = time()
    water_secs = 10
    eyes_secs = 30
    move_secs = 60

    while True:
        if time() - init_water > water_secs:
            print("Reminder to drink water!!")
            playMusic('Projects/water.mp3',"yes") 
            init_water = time()
            log("Drank water at ")
        elif time() - init_eyes > eyes_secs:   
            print("Reminder to do eye exercises!!")
            playMusic('Projects/eye.mp3',"yes")   
            init_eyes = time()
            log("Done eyes exercise at ")
        elif time() - init_move > move_secs:
            print("Reminder to do take a walk around!!")
            playMusic('Projects/move.mp3',"yes")
            init_move = time()
            log("Took a short round at ")

