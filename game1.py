import random
from Lockpick import Lockpick
global player
global picks
picks = []


def intro():
    global player
    player = input("Hello, who are you?")
    picks.append(Lockpick(player))
    pickss.append(Lockpick(player))
    doors()

def doors():
    global player
    print("You enter a room. 3 doors...")
    door = input(player + "Which door do you choose? ")
    if(door == '1'):
        door1()
    elif(door == '2'):
        door2()
    else:
        door3()

def door1():
    print("Door 1, great")

def door2():
    print("Door 2, good")

def door3():
    print("Door 3, bad")


