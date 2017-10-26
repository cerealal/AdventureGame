import sys
import os
import random
import time


wall = "X"
air = " "


def menu():
    print("                 _                          _                          ")
    print("     /\         | |                        | |                         ")
    print("    /  \      __| | __   __   ___   _ __   | |_   _   _   _ __    ___  ")
    print("   / /\ \    / _` | \ \ / /  / _ \ | '_ \  | __| | | | | | '__|  / _ \ ")
    print("  / ____ \  | (_| |  \ V /  |  __/ | | | | | |_  | |_| | | |    |  __/ ")
    print(" /_/    \_\  \__,_|   \_/    \___| |_| |_|  \__|  \__,_| |_|     \___| ")

map = [wall,wall,wall,wall,wall,wall,wall,
       wall,air,air,air,air,air,wall,
       wall,wall,air,air,air,wall,wall,
       wall,wall,wall,wall,wall,wall,wall]
def layer1():
    print (map[0] + map[1] + map[2] + map[3] + map[4] + map[5] + map[6])


#Game Loop
while True:
    os.system('clear')
    menu()
    layer1()
    usrInput = input("Do you want to quit?: ")
    if usrInput == "q":
        sys.exit()

                                                     
                                                                                                              