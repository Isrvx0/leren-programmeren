import random 

zak_MMs= []

print (f'Het zit nu {zak_MMs} M&Ms er in de zak')
kleuren_lijst= ('oranje','blauw','groen','bruin')
hoeveelheid= int (input ("Hoeveel M&M's er aan de zak toegevoegd moeten worden?  "))

for i in range (hoeveelheid):
    zak_MMs.append(random.choices(kleuren_lijst))

print (zak_MMs)

