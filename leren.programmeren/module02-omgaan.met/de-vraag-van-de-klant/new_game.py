answer_yes = ["yes", "y"]
answer_no = ["no", "n"]
import random

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


def lockerCode():
    score =0 
    directions = ["right","backward"]
    locker= input("You see a locked house, do you want to try to unlock the house? Then you have to find the locker code")
    if locker.lower() in answer_yes:
        for num in range (1,6):
            number1 = random.randint (0,4)
            number2 = random.randint (0,4)
            answer  = number1 + number2
            lock_code = int(input((f"fNumber {num} of the lock is: \nwat is {number1} + {number2} ?")))
        if lock_code == answer:
                score +=1
        if score >= 5:
            print(f"Good job! the house is open now. \n Your power lever is increased!")
    else:
        print(f"You didn't find the five numbers of the lock, that means you cant open the house.")
    print (' \nWhere would you like to go now?")')
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            deadDeer()
        elif userInput == "left":
            print("You find that this door opens into a wall.")
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")

def deadDeer():
    directions = ["forward","backward"]
    print("You see a dead deer with traces of fangs.. You'd better get away from here. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "backward":
            lockerCode()
        else:
            print("Please enter a valid option.")

def zombie():
    directions = ["right","left","backward"]
    global weapon
    zombie= input('There are zombie watching you , do you want to fight or run?')
    if zombie.lower() == 'fight':
        if weapon:
            ('Good job! The zombie is dead')
        else:
            print('The zombie has killed you!.')
            exit()
    else:
        print('The zombie has killed you!.')
        exit()
    print("Where would you like to go now?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("Multiple beasts start emerging as you enter the room. You are killed.")
            quit()
        elif userInput == "left":
            print("You made it! You've found an exit.")
            quit()
        elif userInput == "backward":
            introScene()
        else:
            print("Please enter a valid option.")

weapon = False
def skeletons():
    directions = ["backward","forward"]
    global weapon
    print("You see a big hole with skeletons inside. Someone is watching you. Where do you want to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
            weapons = True
        elif userInput == "backward":
            introScene()
        elif userInput == "forward":
            beasts()
        else:
            print("Please enter a valid option.")

def beasts():
    actions = ["fight","flee"]
    global weapon
    print("A strange beasts has appeared. You can either run or fight it. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
    
        if userInput == "fight":
            if weapon:
                print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("The goul-like creature has killed you.")
                quit()
        elif userInput == "flee":
            skeletons()
        else:
            print("Please enter a valid option.")