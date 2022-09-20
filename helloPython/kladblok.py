
x = input ('what is your name')
print ('hello,' + x ) 

print ( 10 < 11 )
#_______________
b = min ( 6 , 9 , 10)
y = max ( 6 , 7, 10 )
print ( b )
print ( y )
#_______________ 
a = 33
n = 200
if n > a:
  print ("b is greater than a") 
#_______________
 
import random
favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = random.randint(0,1)

if trueOrFalse == True:
    print('Ik vind dat ook een mooie kleur!')
else:
     not False
     print(f'TBH, ik hou niet zo van {favoriteColor}...')
#_______________
name = input ('what is ur name')
if name == 'israa':
    raise NameError ('you are not welcome, israa')
#________________
# printen van character
text = 'PYTHIN IS COOL'
for character in text :
  print (character)
#_______________
# tafel van 6 laten zien.
  for i in range (1,11):
    print ( i*6)
#_______________

# de cijfers latten zien van 0 t/m 100 twee bij twee (dus 2,4,6,8,10,12,etc..)
for x in range (0,100,2):
  print (x)