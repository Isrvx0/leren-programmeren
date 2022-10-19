import random

kleuren_lijst=  ['rood','blauw','groen','geel','bruin'] #keys
aantal_MMs= int (input ("Hoeveel M&M's er aan de zak toegevoegd moeten worden?  ")) #values
zak_MMs= {} 

#list met values
values= [] #voor het random delen van values
for i in range (4):
    random_number = random.randint(0,aantal_MMs)
    values.append(random_number)
    aantal_MMs-=random_number
values.append(aantal_MMs)

#keys verdelen aan values:
for key in kleuren_lijst:
    for value in values:
        zak_MMs[key] = value
        values.remove(value)
        break

# verwijderen van de key als de waarde 0 is:   
for key in list(zak_MMs.keys()): # voor elke key in Dictionary 
    if zak_MMs[key] ==0:  # als de waarde van de key gelijk aan 0
        del zak_MMs[key] #wordt verwijdert uit de Dictionary

print (zak_MMs)
