name = input ('Wat is jouw naam? ') 
print ('Hallo', name )

import random
num1 = random.randint(1,10)
num2 = random.randint(5,15)


try: 
    number =  int ( input (f'En weet jij wat {num1} + {num2} ,is? ') )
    if int (number == (num1+num2) ):
        print('Dat is juist')
    else:
            print('Nee dat klopt niet {}'.format(name))
except:
    print('Dat is geen nummer!')

