import random

# voor aantal delnemers:
aantal = int(input('wat is de aantal van de delnemers? '))
while aantal < 3:
    print('Aantal delnemers moet 3 of meer zijn.')
    aantal = int(input('wat is de aantal van de delnemers? '))

# voor namen van de delnemers:
namen_list= []
newList = []

teller = 1 #teller begint altijd met 0 
while teller <= aantal:
    naam= input(f'wat is de naam van delnemer {teller}?   ')
    if naam.lower() in namen_list:
        print('mag allen unieke namen! probeer nog een keer')
    else:
        namen_list.append(naam.lower())
        newList.append(naam.lower())
        teller +=1

# voor lootje trekker:
random.shuffle(namen_list)
for i in range (0,aantal):
    deelnemer= namen_list[i]
    random_choice= random.choice(newList)
    while deelnemer == random_choice:
        random_choice = random.choice(newList)
    print ('(',deelnemer, ':', random_choice,')')
    newList.remove(random_choice)
