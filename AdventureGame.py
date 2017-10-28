import sys
import os
import random
import time

charxy = [1,1]
width = 9
hight = 9


wall = "X"
air = "-"
def menu():
    print("                 _                          _                          ")
    print("     /\         | |                        | |                         ")
    print("    /  \      __| | __   __   ___   _ __   | |_   _   _   _ __    ___  ")
    print("   / /\ \    / _` | \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \ ")
    print("  / ____ \  | (_| |  \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ ")
    print(" /_/    \_\  \__,_|   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___| ")


def player_input():
    playerInput = input("hello: ")
    if playerInput == "q":
        exit()

    
    
def map_gen():
    for i in range(width):
        print(wall + " ", end="")
    print(wall)
    print(wall, end="")
    for i in range(width - 1):
        print(air + " ", end="") 


os.system('clear')
menu()



#Game Loop
while True:
    map_gen()
    print(charxy)
    player_input()



    
                                                     
                                                                                                              