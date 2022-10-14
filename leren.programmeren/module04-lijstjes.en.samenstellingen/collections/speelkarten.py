import random

kleuren = ['hart','klaver','schoppen','ruitem'] #kleuren van de kaarten
nummers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A"] #nummers van de kaarten
joker1 = ['joker']
joker2 = ['joker']
kaarten = [] #lege kaart (om kleuren en nummers met elkaar te verbinden)

kaarten.append(joker1) #toevoegen aan de lijst van de kaarten
kaarten.append(joker2) #lees regel 9

for kleur in kleuren: #voor elke kleur in list kleuren
    for nummer in nummers: #voor elke nummer in list nummers
        kaarten.append((kleur, nummer)) #bind het samen en toevoegen aan de lijst van de kaarten

for random_kaart in range(1,8): #voor de zeven random kaarten
    random_item = random.choice(kaarten) #kiest een random kaart
    print(f'kaart {random_kaart} : {random_item}') 
    kaarten.remove(random_item) #verwijdert de kaart van de list

print (f'\n deck {len(kaarten)} kaarten: ' , kaarten)
