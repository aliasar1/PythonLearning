from t1 import *

class T2(T1):
    def __init__(self):
        print("I am from T2")

    def say(self):
        super(T2, self).say()
        print("My name is Khan2")    