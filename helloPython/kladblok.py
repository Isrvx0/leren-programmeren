
import random
num1 = random.randint(1,10)
num2 = random.randint(5,15)

while True:
    try:
        number = int ( input (f' Do you know what {num1} + {num2} ,is? ') )
        break
    except ValueError:
        print("that is not a number! Please try again")

if number == num1 + num2 : 
        print('that is right , you opened the door and got out of the house')
else:
            print('no, that is not right , you lose the game')
            print ('GAME OVER')
#______________________________

# printing slowely in Python
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint("this this writen slowly in my terminal")

#___________________________
