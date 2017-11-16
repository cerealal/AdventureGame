import sys
import os
import random
import time

location = "room1"
charxy = [1,1]
prvcharxy = [0,0]
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

def player_input(charxy,prvcharxy):
    playerInput = input("What to do?: ")
    if playerInput == "q":
        exit()
    if playerInput == "s":
        if charxy[1] != 7:
            
            charxy[1] = charxy[1] + 1   
        else:
            print("You cant move that way")
    if playerInput == "w":
        if charxy[1] != 1:
            
            charxy[1] = charxy[1] - 1
        else:
            print("You cant move that way")
    if playerInput == "d":
        if charxy[0] != 9:
            
            charxy[0] = charxy[0] + 1   
        else:
            print("You cant move that way")
    if playerInput == "a":
        if charxy[0] != 1:
            
            charxy[0] = charxy[0] - 1
        else:
            print("You cant move that way")
    

        


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

def get_location(charxy,prvcharxy):
    print("CurrentPos: " + str(charxy))
    print("PreviousPos: " + str(prvcharxy))

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

    if prvcharxy[0] == 1:
        if prvcharxy[1] == 1:
            room1layer2[1] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[1] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[1] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[1] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[1] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[1] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[1] = "-"

    if charxy[0] == 2:
        if charxy[1] == 1:
            room1layer2[2] = "@"
        elif charxy[1] == 2:
            room1layer3[2] = "@"
        elif charxy[1] == 3:
            room1layer4[2] = "@"
        elif charxy[1] == 4:
            room1layer5[2] = "@"
        elif charxy[1] == 5:
            room1layer6[1] = "@"
        elif charxy[1] == 6:
            room1layer7[1] = "@"
        elif charxy[1] == 7:
            room1layer8[1] = "@"
        else:
            print("Invalid location")

    if prvcharxy[0] == 2:
        if prvcharxy[1] == 1:
            room1layer2[2] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[2] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[2] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[2] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[2] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[2] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[2] = "-"

    if charxy[0] == 3:
        if charxy[1] == 1:
            room1layer2[3] = "@"
        elif charxy[1] == 2:
            room1layer3[3] = "@"
        elif charxy[1] == 3:
            room1layer4[3] = "@"
        elif charxy[1] == 4:
            room1layer5[3] = "@"
        elif charxy[1] == 5:
            room1layer6[3] = "@"
        elif charxy[1] == 6:
            room1layer7[3] = "@"
        elif charxy[1] == 7:
            room1layer8[3] = "@"
        else:
            print("Invalid location")

    if prvcharxy[0] == 3:
        if prvcharxy[1] == 1:
            room1layer2[3] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[3] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[3] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[3] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[3] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[3] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[3] = "-"

    if charxy[0] == 4:
        if charxy[1] == 1:
            room1layer2[4] = "@"
        elif charxy[1] == 2:
            room1layer3[4] = "@"
        elif charxy[1] == 3:
            room1layer4[4] = "@"
        elif charxy[1] == 4:
            room1layer5[4] = "@"
        elif charxy[1] == 5:
            room1layer6[4] = "@"
        elif charxy[1] == 6:
            room1layer7[4] = "@"
        elif charxy[1] == 7:
            room1layer8[4] = "@"
        else:
            print("Invalid location")

    if prvcharxy[0] == 4:
        if prvcharxy[1] == 1:
            room1layer2[4] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[4] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[4] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[4] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[4] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[4] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[4] = "-"
    
    if charxy[0] == 5:
        if charxy[1] == 1:
            room1layer2[5] = "@"
        elif charxy[1] == 2:
            room1layer3[5] = "@"
        elif charxy[1] == 3:
            room1layer4[5] = "@"
        elif charxy[1] == 4:
            room1layer5[5] = "@"
        elif charxy[1] == 5:
            room1layer6[5] = "@"
        elif charxy[1] == 6:
            room1layer7[5] = "@"
        elif charxy[1] == 7:
            room1layer8[5] = "@"
        else:
            print("Invalid location")
            
    if prvcharxy[0] == 5:
        if prvcharxy[1] == 1:
            room1layer2[5] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[5] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[5] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[5] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[5] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[5] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[5] = "-"

    if charxy[0] == 6:
        if charxy[1] == 1:
            room1layer2[6] = "@"
        elif charxy[1] == 2:
            room1layer3[6] = "@"
        elif charxy[1] == 3:
            room1layer4[6] = "@"
        elif charxy[1] == 4:
            room1layer5[6] = "@"
        elif charxy[1] == 5:
            room1layer6[6] = "@"
        elif charxy[1] == 6:
            room1layer7[6] = "@"
        elif charxy[1] == 7:
            room1layer8[6] = "@"
        else:
            print("Invalid location")
            
    if prvcharxy[0] == 6:
        if prvcharxy[1] == 1:
            room1layer2[6] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[6] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[6] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[6] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[6] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[6] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[6] = "-"

    if charxy[0] == 7:
        if charxy[1] == 1:
            room1layer2[7] = "@"
        elif charxy[1] == 2:
            room1layer3[7] = "@"
        elif charxy[1] == 3:
            room1layer4[7] = "@"
        elif charxy[1] == 4:
            room1layer5[7] = "@"
        elif charxy[1] == 5:
            room1layer6[7] = "@"
        elif charxy[1] == 6:
            room1layer7[7] = "@"
        elif charxy[1] == 7:
            room1layer8[7] = "@"
        else:
            print("Invalid location")
            
    if prvcharxy[0] == 7:
        if prvcharxy[1] == 1:
            room1layer2[7] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[7] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[7] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[7] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[7] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[7] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[7] = "-"

    if charxy[0] == 8:
        if charxy[1] == 1:
            room1layer2[8] = "@"
        elif charxy[1] == 2:
            room1layer3[8] = "@"
        elif charxy[1] == 3:
            room1layer4[8] = "@"
        elif charxy[1] == 4:
            room1layer5[8] = "@"
        elif charxy[1] == 5:
            room1layer6[8] = "@"
        elif charxy[1] == 6:
            room1layer7[8] = "@"
        elif charxy[1] == 7:
            room1layer8[8] = "@"
        else:
            print("Invalid location")
            
    if prvcharxy[0] == 8:
        if prvcharxy[1] == 1:
            room1layer2[8] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[8] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[8] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[8] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[8] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[8] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[8] = "-"
    
    if charxy[0] == 9:
        if charxy[1] == 1:
            room1layer2[9] = "@"
        elif charxy[1] == 2:
            room1layer3[9] = "@"
        elif charxy[1] == 3:
            room1layer4[9] = "@"
        elif charxy[1] == 4:
            room1layer5[9] = "@"
        elif charxy[1] == 5:
            room1layer6[9] = "@"
        elif charxy[1] == 6:
            room1layer7[9] = "@"
        elif charxy[1] == 7:
            room1layer8[9] = "@"
        else:
            print("Invalid location")
            
    if prvcharxy[0] == 9:
        if prvcharxy[1] == 1:
            room1layer2[9] = "-"
        elif prvcharxy[1] == 2:
            room1layer3[9] = "-"
        elif prvcharxy[1] == 3:
            room1layer4[9] = "-"
        elif prvcharxy[1] == 4:
            room1layer5[9] = "-"
        elif prvcharxy[1] == 5:
            room1layer6[9] = "-"
        elif prvcharxy[1] == 6:
            room1layer7[9] = "-"
        elif prvcharxy[1] == 7:
            room1layer8[9] = "-"
    
    return prvcharxy
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
get_location(charxy,prvcharxy)
#Game Loop
while True:
#makes sure character doesn't have a tail

#gets location of character
    get_location(charxy,prvcharxy)
#generates map with character
    map_gen(location)
#print is for python being wierd and printing line by line
    print("")
#Player inputs action
    
    prvcharxy[0] = charxy[0]
    prvcharxy[1] = charxy[1]
    player_input(charxy,prvcharxy)
#gets location of character
#clears the screen
    os.system('clear')
    



    
                                                     
                                                                                                              