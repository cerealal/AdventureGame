import sys
import os
import random
import time

charxy = [1,1]

wall = "X"
air = "-"
def menu():
    print("                 _                          _                          ")
    print("     /\         | |                        | |                         ")
    print("    /  \      __| | __   __   ___   _ __   | |_   _   _   _ __    ___  ")
    print("   / /\ \    / _` | \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \ ")
    print("  / ____ \  | (_| |  \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ ")
    print(" /_/    \_\  \__,_|   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___| ")


def player_input(width,hight):
    move = input("What do you want to do?: ")
    if move == "north" and charxy[1] > int(hight) - 1:
        charxy[1] + 1
    else:
        if move == "south" and charxy[1] > int(hight) + 1:
            charxy[0] - 1
        else:
            if move == "east" and charxy[0] < int(width) - 1:
                charxy[1] - 1
            else:
                if move == "west" and charxy[0] < int(width) + 1:
                    charxy[0] + 1
                else:
                    if move == "q":
                        exit()
                    else:
                        print("I dont understand.")
    
    
def map_gen(width,hight):
    for i in range(int(width) + 1):
        print(wall, end="")
    print(wall)
    for i in range(int(hight) - 2):
        print(wall, end="")
        for i in range(int(width)):
            print(air, end="")
        print(wall)
    for i in range(int(width) + 1):
        print(wall, end="")
    print(wall)

os.system('clear')
menu()
width = input("what is the width you want the map to be?: ")
hight = input("what is the hight you want the map to be?: ")
hight = int(hight) + 1


#Game Loop
while True:
    map_gen(width,hight)
    player_input(width,hight)
    print(charxy)



    
                                                     
                                                                                                              