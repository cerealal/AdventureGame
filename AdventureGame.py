import sys
import os
import random
import time

location = "room1"
charxy = [1,1]
prvcharxy = [1,1]
#width = 10
#hight = 9
wall = "X"
air = "-"
#Room 1 layers
room1layer1 = [wall,wall,wall,wall,wall,wall,wall,wall,wall,wall]
room1layer2 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer3 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer4 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer5 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer6 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer7 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer8 = [wall,air,air,air,air,air,air,air,air,wall]
room1layer9 = [wall,wall,wall,wall,wall,wall,wall,wall,wall,wall]
        

def menu():
    print("                 _                          _                          ")
    print("     /\         | |                        | |                         ")
    print("    /  \      __| | __   __   ___   _ __   | |_   _   _   _ __    ___  ")
    print("   / /\ \    / _` | \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \ ")
    print("  / ____ \  | (_| |  \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ ")
    print(" /_/    \_\  \__,_|   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___| ")

def player_input():
    playerInput = input("What to do?: ")
    if playerInput == "q":
        exit()
    if playerInput == "south":
        charxy[1] = charxy[1] + 1

def map_gen(location):
    if location == "room1":
        for room in room1layer1:
            print(room + " ", end="")
        print(" ")
        for room in room1layer2:
            print(room + " ", end="")
        print(" ")
        for room in room1layer3:
            print(room + " ", end="")
        print(" ")
        for room in room1layer4:
            print(room + " ", end="")
        print(" ")
        for room in room1layer5:
            print(room + " ", end="")
        print(" ")
        for room in room1layer6:
            print(room + " ", end="")
        print(" ")
        for room in room1layer7:
            print(room + " ", end="")
        print(" ")
        for room in room1layer8:
            print(room + " ", end="")
        print(" ")
        for room in room1layer9:
            print(room + " ", end="")
        print(" ")

def get_location(charxy):
    print(charxy)
    if charxy[0] == 1:
        if charxy[1] == 1:
            room1layer2[1] = "@"
        elif charxy[1] == 2:
            room1layer3[1] = "@"
        elif charxy[1] == 3:
            room1layer4[1] = "@"
        elif charxy[1] == 4:
            room1layer5[1] = "@"
        elif charxy[1] == 5:
            room1layer6[1] = "@"
        elif charxy[1] == 6:
            room1layer7[1] = "@"
        elif charxy[1] == 7:
            room1layer8[1] = "@"
        else:
            print("Invalid location")
    return charxy
#Old map_gen() system
"""  
def map_gen():
    for i in range(width):
        print(wall + " ", end="")
    print(wall)
    for i in range(hight - 1):
        print(wall + " ", end="")
        for i in range(width - 1):
            print(air + " ", end="")
        print(wall)
    for i in range(width):
        print(wall + " ", end="")
        print(wall)
"""


#Setting stuff up for game loop
os.system('clear')
menu()
#Game Loop
while True:
    map_gen(location)
    print("")
    get_location(charxy)
    player_input()
    os.system('clear')
    



    
                                                     
                                                                                                              