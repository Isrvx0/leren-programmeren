import random
import sys
import time

# function :
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def end_the_game():
    return sys.exit()

#Collection:
magicword = ['p','y','t','h','o','n']
#game start (intro) :
naam= input ('please enter your name  ')
print (f'Hello {naam} and welcome in the forest full of puzzles.')
print("\nIf you want to survive, you have to choose the right option and solve some puzzles.")
ready= input ('Are you ready? (yes,no)  ')

if ready.lower() == 'yes':
    print ('\nYou are now in a house in this forest, you have to open the door by solving the next puzzel')
else:
    print ('that is too bad, see you next time')

num1 = random.randint(1,10)
num2 = random.randint(5,15)

while True:
    try: 
        number = int ( input (f'Do you know what {num1} + {num2} ,is?  ') )
        break 
    except ValueError:
        print ("thats not a number , pleaser try again!")

if number == num1 + num2 : 
    print(f'that is right {naam}, you opened the door and got out of the house')
else:
    print(f'no, that is not right {naam} , you lose the game')
    print ('GAME OVER')
    end_the_game()

print ('\n---- level 2 ----')
choice = input ('You find a crossroads, do you want to go left or right? \n Please type (L) for left and (R) for right:  ')

if choice.lower() == 'l':
    choice= input (f' thers is a monster looking at you {naam}, do you want to attack or run?  ')
elif choice.lower() =='r': 
    print (f'you fall into deep hole {naam}, you lose!')
    print ('GAME OVER')
    end_the_game()

if choice.lower() == 'attack':
    print (f'wrong choice {naam}, you are not a hero. you lose!')
    print ('GAME OVER')
    end_the_game()
elif choice.lower() == 'run':
    print('\nyou survive, there is a box under the tree and there is a hint inside, you can only open it by solving the puzzel')

choice= input (f'are you ready to solve the puzzel {naam} ?\n type (yes) or (no):  ')
if choice == 'no':
    print (f'thats too bad {naam}, see you next time! \nGAME OVER')
    end_the_game()
elif choice == 'yes':
    print ('---- level 3 ----')
    print (f'AWESOME {naam}! The puzzel is: for what to use (int)? choose the right letter  ')

choice= input ('a) integer , b) float, c) complex   ')
if choice.lower() == 'a':
    print(f"you are genius {naam}! the box is open now")
else:
    print (f"wrong choice {naam}! You lose! \nGAME OVER")
    end_the_game()
    
print ('\n The hint in the box is a message. the message is:')
print (f'Hello {naam} , if you want to get out this forest and win, You have to collect the 6 hidden letters.\nThen make the right word from it. In this box, you will find the first hidden letter and it is {magicword[0]}')
choice= input ('Do you want to stay and find the other 5 leteters? choose between (yes) or (no).  ')
if choice == 'yes':
    print ('---- level 4 ----')
    print (f'NICE {naam}! if you want to find the next hidden letter, you need to solve the next puzzel ..')
elif choice == 'no':
    print (f"So bad {naam} , maybe next time! \nGAME OVER")
    end_the_game()

choice = input ("\nThe puzzel is: i see what you cant see and the color is 'green'. \nChoose the right letter: a)house b) box c)tree  ")
if choice == 'c':
    print (f'That is correct {naam}! you find the second hidden letter.\nThe hidden letter is {magicword[2]} ')
    print ('---- level 5 ----')
else:
    print (f'{naam} , thats not the right choice, you Lose! \nGAME OVER')
    end_the_game()
    
choice = input ('The next hidden letter is in the lake near to you.\nif you want to stay and find it,\ntype (yes). and if you want to leave, type (no).  ')

if choice == 'yes':
    print ('Great, solve the next puzzel and get the hidden letter ..')
elif choice == 'no':
    print (f'That is too bad, see you next time {naam}. \nGAME OVER')
    end_the_game()

print ()
choice= input ('what is a (string)? \nChoose the right choice: a) number . b) word or phrase . c decimal number  ')
if choice.lower() == 'b':
    print (f'How can you be so smart! You find the 3e hidden letter! and that is {magicword[4]}')
    print ('---- level 6 ----')
else:
    print (f'thats not correct {naam} , see you next time! \nGAME OVER')
    end_the_game()

print (f'You are doing great job {naam}. Dont give up! you are so close to the end! \nThis time you will find 2 hidden letters, but the 2 puzzels will be difficult! So stay awake and focus! ')
hint = input ('first puzzel, which of the following is data-type?  a) Text type . b) programming type . c)puzzel type  ') 
if hint.lower() == 'a':
    print ('correct! be ready for the next puzzel!')
else:
    print (f"that's not the right answer {naam}. you lose! \nGAME OVER")
    end_the_game()

print ('the second puzzel is: Which type of Programming does Python support?')
choice = input (" a) object-oriented programming . b)structured programming . c)all of the mentioned  ")
if choice == "c":
    print (f"without a doubt, you are Einstein's grandson, GREAT JOB {naam} !")
    print ('---- level 7 ----')
elif choice == 'a' or choice == 'b':
    print (f'that was close {naam}, maybe next time \nGAME OVER')
    end_the_game()

print (f"you find the 2 hidden letter: its {magicword[1]} and {magicword[5]}. one letter left! I'll give you a hint to find it. It's on something in this forest, you use is to make fire!" )
print ('.\n.\n.\n.')
print ('I can help you with the answer, but you need to solve this puzzel!')
print ("the puzzel is: Which of the following is the correct extension of the Python file? ")
hint = input ('chose the right letter: a) .python b) .py c) .pl  ')
if hint == 'b':
    print (f"that's right {naam} , the answer for the past question is wood ")
elif hint == 'a' or hint == 'c':
    print ("that's not right! you lose the hint!")

choice = input ('what do you think the thing that is in the forest and it can be used to make fire?  ')
if choice in ('wood' , 'Wood'):
    print ('that was good! you find the LAST LETTER, GOOD JOB')
    print ('---- level 8 ----')
else:
    print (f"that was not the right answer {naam}! you lose the game! \nGAME OVER")
    end_the_game()

random.shuffle(magicword)
print (f"you are so close for the win! THE LAST HIDEN LETTER IS {magicword[3]} ! You collect all the hidden letter and now your last job is to make from them the magic word that will help you to get out this forest")
print(f"the letters are {magicword}")
magicword= input ('what is the magic word?   ')
if magicword in ('PYTHON' , 'python' , 'Python'):
    print (f'YOU ARE A REAL HERO {naam} ! YOU MADE IT AND YOU GET OUT THE FOREST! GREAT JOB ')
    print ('YOU WIN THE GAME')
else:
    print (f"OOi that was not the right answer {naam} , you lose the game! \nGAME OVER")
    end_the_game()
print ("                          _,.-'') ,....")
print ("                      .-'      /'     ")
print ("                    /        /       /")
print ("                  _:.   `. ,:.   _.-'")
print ("                  /   `...'`  /.-'''.")
print ("     ,       __../       \::,'     /    _.-.")
print ("    /.\   .-'.--'\     ,' `'\     ,.  .'   _")
print ("   | | |,'.'`     ;---'      ..--'  `/ ,-'' ''")
print ("   \ | /,'      .'    \    ,'         `.   _.._")
print ("   '|'/.-''-. ,'      `'''  _---_     ',-'")
print ("     /// _.' / |                .        / ")
print ("    /./.'  .'  |               _/ ,'      |")
print ("   '/-'--'`    |           _.:.''`        |")
print ("  .'           |         .'''\-'''`      .'")
print ("  |'           \        /.//'/            /")
print ("  ||          ,--    ._: ||_/           _/.-`")
print ("  ||         |         |  '/     ._``:.`_..-'")
print ("  ||         `.        `-''     //.:/.:-..-'" )
print ("  ||          \       . /.''\  |||///'")
print ("  ||        ,-'``\    \/|`'. : :_`/`")
print ("  |'      ,'          | |/  \|  '/")
print ("  '|     /  ,-'    _,-,\_\   '   ;")
print ("   \\,_.' ,'   _,``  _/`-..__..-'")
print ("    \[_`;.--''   _..'")
print ("    / ='....----''\  _      YOU ARE")
print ("    `-|'         '|/' |    MY Hero")
print ("     || \         /_./")
print (f"    |'  -----------          {naam}!!!")
print ("------------------------------------------------")