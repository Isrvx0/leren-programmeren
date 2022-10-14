lege_zak= []

print (f'Het zit nu 0 M&Ms er in de zak')
kleuren_lijst= ('oranje','blauw','groen','bruin')
hoeveelheid= int (input ("Hoeveel M&M's er aan de zak toegevoegd moeten worden?  "))
delen= 4

integer   = hoeveelheid/delen
remainder = hoeveelheid%delen

for i in range(delen):
   lege_zak.append(integer)
for i in range(remainder):
   lege_zak[i]+=1
zipped = zip (kleuren_lijst,lege_zak)

print (list(zipped))
print (f'Het zit nu {hoeveelheid} M&Ms er in de zak')
