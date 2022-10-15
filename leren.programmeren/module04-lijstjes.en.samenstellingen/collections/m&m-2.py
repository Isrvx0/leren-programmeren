# # ()Maak een List waar de volgende kleuren in zitten: rood, blauw, groen, geel en bruin.
# # ()Het programma vraagt met een input hoeveel M&M’s er aan de zak toegevoegd moeten worden.
# # Maak functionaliteit die een lege Dictionairy datatype (zak met M&M’s) vult aan de hand van het gekozen aantal, de kleuren moeten willekeurig gekozen worden uit de beschikbare kleuren in de List aangemaakt in punt 1.
# # Het programma print als laatste de zak met M&M’s.
 
# # Let op: Elke kleur komt maar 1x voor als key in de dictionary. De value is een nummer van de hoeveelheid M&M’s van de betreffende kleur die zich in de zak bevinden! en een kleur die niet in de zak voorkomt (value 0) mag ook niet in de dictionary voorkomen.

import random

zak_MMs = {}
kleuren = ('rood','blauw','groen','geel','bruin') #keys
aantal_MMs= int (input ("Hoeveel M&M's er aan de zak toegevoegd moeten worden?  ")) #values
