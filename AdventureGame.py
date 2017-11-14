import sys
import os
import random
import time

location = "room1"
charxy = [1,1]

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

def map_gen(location):
    x = 0
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

os.system('clear')
menu()


#Game Loop
while True:
    map_gen(location)
    #print(charxy)
    print("")
    player_input()



    
                                                     
                                                                                                              