import random

# voor aantal delnemers:
VRAAG = 'wat is de aantal van de deelnemers? '
aantal = int(input(VRAAG))
while aantal < 3:
    print('Aantal deelnemers moet 3 of meer zijn.')
    aantal = int(input(VRAAG))

# voor namen van de delnemers:
namen_list= []
newList = []

teller = 1 #teller begint altijd met 0 
while teller <= aantal:
    naam= input(f'wat is de naam van deelnemers {teller}?   ')
    if naam.lower() in namen_list:
        print('mag allen unieke namen! probeer nog een keer')
    else:
        namen_list.append(naam.lower())
        newList.append(naam.lower())
        teller +=1


random.shuffle(namen_list)

for deelnemer in namen_list:
    random_choice= random.choice(newList)
    if len(newList) == 1 and random_choice == deelnemer:
        newList.clear()
        for namen in namen_list:
            newList.append(namen)
            for deelnemer in namen_list:
                random_choice= random.choice(newList)
            while deelnemer == random_choice:
                random_choice = random.choice(newList)
    else:
        while deelnemer == random_choice:
           random_choice = random.choice(newList)
    print ('(',deelnemer, ':', random_choice,')')
    newList.remove(random_choice)

