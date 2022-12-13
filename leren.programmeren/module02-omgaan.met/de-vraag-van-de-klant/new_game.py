from game_function import lockerCode
from game_function import skeletons
from game_function import zombie

def introScene():
    directions = ["left","right","forward" , "backward"]
    print("You are at a crossroads, and you can choose to go down any of the four hallways. \nWhere would you like to go?")
    direction = ""
    while direction not in directions:
        print("options: left / rechts / backward / forward")
        direction = input()
        if direction == "left":
            lockerCode()
        elif direction == "right":
            skeletons()
        elif direction == "forward":
            zombie()
        elif direction == "backward":
            print("You find that this door opens into a wall.")
        else: 
            print("Please enter a valid option.")

introScene()