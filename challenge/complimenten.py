import random
from random import randint

# # complimenten= ['je bent geweldig' , 'je bent mooi' , 'je bent leuk' , 'je bent lief' , 'je bent perfect']
# # naam= input('wat is je naam?  ')

# # hoeveel= int(input('Hoeveel complimenten wil je?  '))

# # for comp in range (hoeveel):
# #     random_choice= random.choice(complimenten)
# #     print(random_choice , naam)

# #------uitbereiden

naam= input('wat is je naam?  ')
hoeveel= int(input('Hoeveel complimenten wil je?  '))
complimenten= ['je bent geweldig' , 'je ziet mooi eruit' , 'je bent leuk' , 'je bent lief' , 'je bent special']
oude_random= 0

for compliment in range (hoeveel):
    random_choice= random.choice(complimenten)
    while random_choice == oude_random:
         random_choice= random.choice(complimenten)
    print (random_choice , naam)
    oude_random = random_choice