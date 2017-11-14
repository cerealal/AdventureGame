import sys
import os
import random
import time

location = "room1"
charxy = [1,1]
width = 10
hight = 9
wall = "X"
air = "-"
room1 = [wall,wall,wall,wall,wall,wall,wall,wall,wall,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,air,air,air,air,air,air,air,air,air,
         wall,wall,wall,wall,wall,wall,wall,wall,wall,
        
]

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
        for room in room1:
            print(room + " ", end="")
            x = x + 1
            if x == 9 or x == 18 or x == 27 or x == 36 or x == 45 or x == 54 or x == 63 or x == 72 or x == 81 or x == 90:
                print(wall)
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
    player_input()



    
                                                     
                                                                                                              