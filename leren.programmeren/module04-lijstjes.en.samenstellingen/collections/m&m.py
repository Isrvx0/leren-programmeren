import random 

lege_zak= []
zak_MMs= 0

print (f'Het zit nu {zak_MMs} M&Ms er in de zak')
kleuren_lijst= ('oranje','blauw','groen','bruin')
hoeveelheid= int (input ("Hoeveel M&M's er aan de zak toegevoegd moeten worden?  "))

for i in range (3):
    random_number = random.randint(0,hoeveelheid)
    lege_zak.append(random_number)
    zak_MMs += random_number
    hoeveelheid-=random_number

lege_zak.append(hoeveelheid)
zipped = zip (kleuren_lijst,lege_zak)

print (list(zipped))
print (f'Het zit nu {zak_MMs} M&Ms er in de zak')
