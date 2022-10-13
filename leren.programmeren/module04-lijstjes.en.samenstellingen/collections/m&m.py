lege_zak= []
kleuren_lijst= ('oranje','blauw','groen','bruin')

aantal= int (input ("Hoevee M&M's er aan de zak toegevoegd moeten worden?  "))
lege_zak.append(aantal)
zipped = zip (kleuren_lijst,lege_zak)
print(list(zipped))